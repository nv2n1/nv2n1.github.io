---
title: "pac(1)"
name: "pac"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pac/"
description: "pac – Perl Auto Connector"
---

<h2>NAME</h2>
<p> pac &#8211; Perl Auto Connector</p>
<h2>SYNOPSIS</h2>
<p> <code>pac [-start_tray]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pac</code> is a (simple?) GUI to manage/launch connections to remote machines with: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Configurable [Pre|Post]-connection local commands execution.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Configurable list of macros (commands) to send to connected client.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Configurable list of macros (commands) to execute locally when connected.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Configurable list of conditional executions on connected machine via &#8216;Expect&#8217;:</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>. forget about SSH certificates</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>. chain multiple ssh connections</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>. automate tunnels creation</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>. etc</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Ability to connect to machines through a Proxy server!</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Scripting (Perl language), just like SecureCRT, but much better! :P</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Wake On LAN capabilities</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; TABBED/WINDOWED terminals</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Possibility to *CLUSTER* terminals!!</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Local and Global variables, eg.: write down a password once, use it ANY where, centralizing its modification for faster changes! use them for:</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>. password vault</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>. reusing connection strings</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>. etc</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Seamless Gnome/Gtk integration.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Tray icon for &#8216;right button&#8217; quick launching of managed connections.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Written in Perl/Gtk (wait, *is* that a feature? Well, it is for me! ;=)</p>
<h2>OPTIONS</h2>
<dl>
<dt>-start_tray</p>
<dd> Initialise <code>pac</code> minimized to tray.</dl>
<h2>FILES</h2>
<p> <i>~/.pac/</i></p>
<dl>
<dt>
<dd> Per user configuration directory.</dl>
<h2>ENVIRONMENT</h2>
<p> Uses next Gnome&#8217;s configuration paths:</p>
<dl>
<dt>/system/http_proxy/host</p>
<dd> Takes this proxy path</p>
<dt>/system/http_proxy/port</p>
<dd> Takes this proxy port</p>
<dt>/system/http_proxy/authentication_user</p>
<dd> Takes this proxy user name</p>
<dt>/system/http_proxy/authentication_password</p>
<dd> Takes this proxy password</dl>
<h2>BUGS</h2>
<p> Well&#8230; I thinks that by this version, there should not be any known bugs but, I&#8217;m sure you &#8216;will&#8217; find some. If so, please, let me know!</p>
<h2>AUTHOR</h2>
<p> David Torrejón Vaquerizas &lt;david.tv [at] gmail.com&gt; </p>
<p> Visit: </p>
<p> <a rel="nofollow" href="http://sourceforge.net/projects/pacmanager/">http://sourceforge.net/projects/pacmanager/</a> </p>
<p> <a rel="nofollow" href="https://sites.google.com/site/davidtv/">https://sites.google.com/site/davidtv/</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code><a href="/docs/linux/man/1-sftp/">sftp</a></code>(1), <code><a href="/docs/linux/man/1-telnet/">telnet</a></code>(1) <code><a href="/docs/linux/man/1-rdesktop/">rdesktop</a></code>(1) <code><a href="/docs/linux/man/1-vncviewer/">vncviewer</a></code>(1) <code><a href="/docs/linux/man/1-remote-tty/">remote-tty</a></code>(1) <code><a href="/docs/linux/man/1-cu/">cu</a></code>(1) </p>
<h2>Index</h2>
