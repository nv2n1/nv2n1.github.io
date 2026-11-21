---
title: "mulog(1)"
name: "mulog"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mulog/"
description: "Mulog – Chat Logging Script for Museekd"
---

<h2>NAME</h2>
<p> <code>Mulog</code> &#8211; Chat Logging Script for Museekd</p>
<h2>DESCRIPTION</h2>
<p> Mulog is command-line Python script that connects to <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) and saves chat messages into log files. Under the Log Directory, it creates room &amp; private subdirectories and a syslog file. If it loses connection with museekd, it will automatically exit. </p>
<p> Setting the interface and password on the command-line is a security risk. Since interface and password settings are saved to the config file when set, you should set them, exit mulog, and restart mulog without the options on the commandline..LP </p>
<p> Before running, you will need a working <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) and need to know your museekd interface and interface password. Configure those with <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1).</p>
<h2>SYNOPSIS</h2>
<p> <code>mulog</code> [-c &lt;<i>config-filename</i>&gt; ] [&#8211;config &lt;<i>config-filename</i>&gt;] [-i &lt;host:port | /socket.path&gt;] [&#8211;interface &lt;host:port | /socket.path&gt; [-p &lt;interface-password&gt;] [&#8211;password &lt;inteface-password&gt;] [-l &lt;<i>directory</i>&gt;] [&#8211;log &lt;<i>directory</i>&gt;] [-v] [&#8211;version] [-h] [&#8211;help]</p>
<h2>OPTIONS</h2>
<p> Mulog accepts the following options:</p>
<dl>
<dt><code>-c &lt;</code><i>filename</i>&gt;, &#8211;config &lt;<i>filename</i>&gt;</dt>
<dd> Use a different config file.</dd>
<dt><code>-l &lt;</code><i>directory</i>&gt;, &#8211;log &lt;<i>directory</i>&gt;</dt>
<dd> Use a different chat log directory.</dd>
<dt><code>-i, &#8211;interface &lt;</code><i>host:port | /socket.path</i>&gt;</dt>
<dd> Choose a different interface (saved to config file)</dd>
<dt><code>-p, &#8211;password &lt;</code><i>interface-password</i>&gt;</dt>
<dd> Choose a different password (saved to config file)</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Display Version and exit.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display Help and exit. </dd>
</dl>
<h2>EXAMPLE</h2>
<p> To run this program the standard way type: </p>
<p> mulog </p>
<p> Alternativly you use a different config file with: </p>
<p> mulog &#8211;config mulog.config </p>
<p> To set the interface password: </p>
<p> mulog &#8211;password 1234567890</p>
<h2>FILES</h2>
<dl>
<dt>
&nbsp;<wbr><i>~/.museekd/mulog.config</i></dt>
<dd> The default location for the <code>mulog</code> config file.</dd>
<dt>
&nbsp;<wbr><i>~/.museekd/logs/</i></dt>
<dd> The default log directory.</dd>
<dt>
&nbsp;<wbr><i>~/.museekd/logs/syslog</i></dt>
<dd> The museekd error/connection log file.</dd>
<dt>
&nbsp;<wbr><i>~/.museekd/logs/room/</i></dt>
<dd> The directory where chat room logs are stored.</dd>
<dt>
&nbsp;<wbr><i>~/.museekd/logs/private/</i></dt>
<dd> The directory where private chat logs are stored.</dd></dl>
<h2>AUTHORS</h2>
<p> Hyriand &lt;hyriand [at] thegraveyard.org&gt; </p>
<p> daelstorm &lt;daelstorm [at] gmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mucous/">mucous</a></i>(1) <i><a href="/docs/linux/man/1-murmur/">murmur</a></i>(1) <i><a href="/docs/linux/man/1-muscan/">muscan</a></i>(1) <i><a href="/docs/linux/man/1-muscand/">muscand</a></i>(1)<i><a href="/docs/linux/man/1-museekcontrol/">museekcontrol</a></i>(1) <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1) <i><a href="/docs/linux/man/1-musetup-gtk/">musetup-gtk</a></i>(1) <i><a href="/docs/linux/man/1-museeq/">museeq</a></i>(1) </p>
