---
title: "sandbox(8)"
name: "sandbox"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sandbox/"
description: "sandbox – Run cmd under an SELinux sandbox"
---

<p>sandbox &#8211; Run cmd under an SELinux sandbox</p>
<h2>Synopsis</h2>
<p><code>sandbox</code> [-C] [-s] [ -d DPI ] [-l level ] [[-M | -X] -H homedir -T tempdir ] [-I includefile ] [ -W windowmanager ] [ -w windowsize ] [[-i file ]&#8230;] [ -t type ] cmd </p>
<p> <code>sandbox</code> [-C] [-s] [ -d DPI ] [-l level ] [[-M | -X] -H homedir -T tempdir ] [-I includefile ] [ -W windowmanager ] [ -w windowsize ] [[-i file ]&#8230;] [ -t type ] -S</p>
<h2>Description</h2>
<p>Run the <i>cmd </i> application within a tightly confined SELinux domain. The default sandbox domain only allows applications the ability to read and write stdin, stdout and any other file descriptors handed to it. It is not allowed to open any other files. The -M option will mount an alternate homedir and tmpdir to be used by the sandbox. If you have the <i>policycoreutils-sandbox </i> package installed, you can use the -X option and the -M option. <code>sandbox -X</code> allows you to run X applications within a sandbox. These applications will start up their own X Server and create a temporary home directory and /tmp. The default SELinux policy does not allow any capabilities or network access. It also prevents all access to the users other processes and files. Files specified on the command that are in the home directory or /tmp will be copied into the sandbox directories. If directories are specified with -H or -T the directory will have its context modified with <a href="/docs/linux/man/1-chcon/">chcon</a>(1) unless a level is specified with -l. If the MLS/MCS security level is specified, the user is responsible to set the correct labels.</p>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd>display usage message</p>
<dt><code>-H &#8211;homedir</code></p>
<dd>Use alternate homedir to mount over your home directory. Defaults to temporary. Requires -X or -M.</p>
<dt><code>-i</code> <code>&#8211;include</code></p>
<dd>Copy this file into the appropriate temporary sandbox directory. Command can be repeated.</p>
<dt><code>-I</code> <code>&#8211;includefile</code></p>
<dd>Copy all files listed in inputfile into the appropriate temporary sandbox directories.</p>
<dt><code>-l</code> <code>&#8211;level</code></p>
<dd>Specify the MLS/MCS Security Level to run the sandbox with. Defaults to random.</p>
<dt><code>-M</code> <code>&#8211;mount</code></p>
<dd>Create a Sandbox with temporary files for $HOME and /tmp.</p>
<dt><code>-s</code> <code>&#8211;shred</code></p>
<dd>Shred temporary files created in $HOME and /tmp, before deleting.</p>
<dt><code>-t</code> <code>&#8211;type</code></p>
<dd>Use alternate sandbox type, defaults to sandbox_t or sandbox_x_t for -X. <code>Examples:</code><br />
 sandbox_t<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>No X, No Network Access, No Open, read/write on passed in file descriptors.</p>
<p> sandbox_min_t<tt>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>No Network Access</p>
<p> sandbox_x_t<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Ports for X applications to run locally</p>
<p> sandbox_web_t<tt>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Ports required for web browsing</p>
<p> sandbox_net_t<tt>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Network ports (for server software)</p>
<p> sandbox_net_client_t<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>All network ports</p>
<dt><code>-T</code> <code>&#8211;tmpdir</code></p>
<dd>Use alternate temporary directory to mount on /tmp. Defaults to tmpfs. Requires -X or -M.</p>
<dt><code>-S</code> <code>&#8211;session</code></p>
<dd>Run a full desktop session, Requires level, and home and tmpdir.</p>
<dt><code>-w</code> <code>&#8211;windowsize</code></p>
<dd>Specifies the windowsize when creating an X based Sandbox. The default windowsize is 1000&#215;700.</p>
<dt><code>-W</code> <code>&#8211;windowmanager</code></p>
<dd>Select alternative window manager to run within <code>sandbox -X.</code> Default to /usr/bin/matchbox-window-manager.</p>
<dt><code>-X</code></p>
<dd>Create an X based Sandbox for gui apps, temporary files for $HOME and /tmp, secondary Xserver, defaults to sandbox_x_t</p>
<dt><code>-d</code> <code>&#8211;dpi</code></p>
<dd>Set the DPI value for the sandbox X Server. Defaults to the current X Sever DPI.</p>
<dt><code>-C</code> <code>&#8211;capabilities</code> Use capabilities within the</p>
<dd>sandbox. By default applications executed within the sandbox will not be allowed to use capabilities (setuid apps), with the -C flag, you can use programs requiring capabilities.</dl>
<h2>See Also</h2>
<dl>
<dt><a href="/docs/linux/man/1-runcon/">runcon</a>(1), <a href="/docs/linux/man/8-seunshare/">seunshare</a>(8), <a href="/docs/linux/man/8-selinux/">selinux</a>(8)</p>
<dd></dl>
<h2>Author</h2>
<p>This manual page was written by <i>Dan Walsh &lt;dwalsh [at] redhat.com&gt;</i> and <i>Thomas Liu &lt;tliu [at] fedoraproject.org&gt;</i></p>
