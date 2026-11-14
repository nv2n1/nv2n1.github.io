---
title: "irexec(1)"
name: "irexec"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irexec/"
description: "irexec – run programs with one button press"
---

<h2>NAME</h2>
<p> irexec &#8211; run programs with one button press</p>
<h2>SYNOPSIS</h2>
<p> <code>irexec</code> [<i>options</i>] [<i>config_file</i>]</p>
<h2>DESCRIPTION</h2>
<p> This program lets you execute arbitrary commands on an IR signal decoded by lircd, the LIRC daemon. You can give irexec a command line parameter which has to be a name of a valid config file. If no command line parameters are given irexec reads the default config file which is usually ~/.config/lircrc. </p>
<p> If irexec executes a program it will wait until this program terminates. So append a &#8216;&amp;&#8217; to the command string if you don&#8217;t want that. </p>
<p> The config string consists of the command to be run. Potential uses are shutting down the computer, starting a dial-up connection etc.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display usage summary</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display version</p>
<dt><code>-d, &#8211;daemon</code></p>
<dd> Make irexec fork to background. That way you can easily start irexec from an init script. In this case you should specify a config file on the command line as irexec won&#8217;t be able to find your home directory.</p>
<dt><code>-n, &#8211;name &lt;name&gt;</code></p>
<dd> Use this program name instead of the default &#8216;irexec&#8217; as identifier in the lircd.conf file.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>LIRC_SOCKET_PATH</p>
<dd> Path to the lircd socket irexec reads from, defaults to /var/run/lirc/lircd. </p>
</dl>
<h2>NOTE</h2>
<p> If you start irexec, it reads your ~/.config/lircrc and reacts only on prog= entries that point to irexec. If you have included more than one program in your .lircrc, then start all these programs, they react itself only to their according entries in .lircrc. </p>
<p> irexec should run as a service. The contrib directory contains a .desktop file which could be dropped in ~/.local/autostart. Doing so creates a service which can be handled by regular desktop tools on all major desktops. If you need to run run restricted commands such as powering off the machine, you can use sudo to allow regular users to run specific commands. See the Configuration Guide in the html documentation.</p>
<h2>SEE ALSO</h2>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
<h2>Index</h2>
