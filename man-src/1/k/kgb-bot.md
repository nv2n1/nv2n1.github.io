---
title: "kgb-bot(1)"
name: "kgb-bot"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kgb-bot/"
description: "kgb-bot – an IRC bot helping collaborative work"
---

<h2>SYNOPSIS</h2>
<p> kgb-bot [&#8211;config <i>file</i>] [&#8211;foreground] [&#8211;simulate <i>file</i>]</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;config <i>file</i></dt>
<dd> Specify configuration file to load. Default is <i>/etc/kgb-bot/kgb.conf</i>.</dd>
<dt>&#8211;config-dir <i>directory</i></dt>
<dd> Specify directory with configuration files to load. All files like <i>*.conf</i> are loaded, in alphabetical order. Default is <i>/etc/kgb-bot/kgb.conf.d</i>.</dd>
<dt>&#8211;foreground</dt>
<dd> Do not detach from console, print log messages to <font SIZE="-1">STDERR</font> and do not become a daemon, useful for debugging.</dd>
<dt>&#8211;simulate <i>file</i></dt>
<dd> Do not connect to <font SIZE="-1">IRC.</font> Instead, output each notification line to the given <i>file</i>, like: </dd>
<pre>
    #chan repo user branch revision module changed-paths
    #chan repo commit message line 1
    #chan repo commit message line 2
</pre>
<p> There are no colour codes in the output, unless <code>&#8211;simulate-color</code> is also given.</p>
<dt>&#8211;simulate-color</dt>
<dd> Include color codes in the file used by <code>&#8211;simulate</code>.</dd>
<dt>&#8211;debug</dt>
<dd> Log additional debugging information </dd>
</dl>
