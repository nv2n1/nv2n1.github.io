---
title: "weechat(1)"
name: "weechat"
section: "1"
letter: "w"
url: "/docs/linux/man/1-weechat/"
description: "weechat – the extensible chat client"
---

<h2 class="name">NAME</h2>
<p> weechat &#8211; the extensible chat client </p>
<h2>SYNOPSIS</h2>
<pre><code>
weechat[-a | --no - connect][-d | --dir&lt;path&gt;][-p | --no - plugin][-r | --run - command&lt;command&gt;][-s | --no - script][--upgrade] [plugin:option...] weechat[-c | --colors] weechat[-h | --help] weechat[-l | --license] weechat[-v | --version]
</code></pre>
<h2>DESCRIPTION</h2>
<p> WeeChat (Wee Enhanced Environment for Chat) is a free chat client, fast and light, designed for many operating systems. It is highly customizable and extensible with scripts.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;no-connect</code></p>
<dl>
<dt>
<dd> Disable auto-connect to servers when WeeChat is starting.</dl>
<p> <code>-c</code>, <code>&#8211;colors</code></p>
<dl>
<dt>
<dd> Display default colors in terminal.</dl>
<p> <code>-d</code>, <code>&#8211;dir</code> <i>&lt;path&gt;</i></p>
<dl>
<dt>
<dd> Set path as home for WeeChat (used for configuration files, logs, user plugins and scripts), default value is <i>~/.weechat</i> (note: directory is created if not found by WeeChat). If this option is not given, the environment variable WEECHAT_HOME is used (if not empty).</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help.</dl>
<p> <code>-l</code>, <code>&#8211;license</code></p>
<dl>
<dt>
<dd> Display WeeChat license.</dl>
<p> <code>-p</code>, <code>&#8211;no-plugin</code></p>
<dl>
<dt>
<dd> Disable plugins auto-load.</dl>
<p> <code>-r</code>, <code>&#8211;run-command</code> <i>&lt;command&gt;</i></p>
<dl>
<dt>
<dd> Run command(s) after startup (many commands can be separated by semicolons).</dl>
<p> <code>-s</code>, <code>&#8211;no-script</code></p>
<dl>
<dt>
<dd> Disable scripts auto-load.</dl>
<p> <code>&#8211;upgrade</code></p>
<dl>
<dt>
<dd> Upgrade WeeChat using session files generated with command /upgrade -quit.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display WeeChat version.</dl>
<p> <code>plugin:option</code></p>
<dl>
<dt>
<dd> Option for a plugin.</dl>
<h2>PLUGIN OPTIONS</h2>
<p> For complete doc on plugin options, please look at plugins documentation in WeeChat user&#8217;s guide. </p>
<p> With irc plugin, you can connect to temporary server with an URL like: </p>
<dl>
<dt>
<dd>
<pre><code>
irc[6][s]: //[[nickname][:password]@]server[:port][/#channel1[,#channel2...]]
</code></pre>
</dl>
<p> To join WeeChat IRC channel support with nick &quot;mynick&quot;: </p>
<dl>
<dt>
<dd>
<pre>
<a href="irc://mynick@chat.freenode.net/#weechat">irc://mynick@chat.freenode.net/#weechat</a>
</pre>
</dl>
<p> IPv6 address can be enclosed in brackets to add a port after address, for example: </p>
<dl>
<dt>
<dd>
<pre>
<a href="irc://mynick@[2001:db8:0:85a3::ac1f:8001]:6668/#test">irc://mynick@[2001:db8:0:85a3::ac1f:8001]:6668/#test</a>
</pre>
</dl>
<h2>FILES</h2>
<p> $HOME/.weechat/weechat.conf</p>
<dl>
<dt>
<dd> main WeeChat configuration file</dl>
<p> $HOME/.weechat/plugins.conf</p>
<dl>
<dt>
<dd> plugins configuration file</dl>
<p> $HOME/.weechat/sec.conf</p>
<dl>
<dt>
<dd> configuration file with secured data</dl>
<p> $HOME/.weechat/alias.conf</p>
<dl>
<dt>
<dd> configuration file for <i>alias</i> plugin</dl>
<p> $HOME/.weechat/aspell.conf</p>
<dl>
<dt>
<dd> configuration file for <i>aspell</i> plugin</dl>
<p> $HOME/.weechat/charset.conf</p>
<dl>
<dt>
<dd> configuration file for <i>charset</i> plugin</dl>
<p> $HOME/.weechat/exec.conf</p>
<dl>
<dt>
<dd> configuration file for <i>exec</i> plugin</dl>
<p> $HOME/.weechat/irc.conf</p>
<dl>
<dt>
<dd> configuration file for <i>irc</i> plugin</dl>
<p> $HOME/.weechat/logger.conf</p>
<dl>
<dt>
<dd> configuration file for <i>logger</i> plugin</dl>
<p> $HOME/.weechat/relay.conf</p>
<dl>
<dt>
<dd> configuration file for <i>relay</i> plugin</dl>
<p> $HOME/.weechat/script.conf</p>
<dl>
<dt>
<dd> configuration file for <i>script</i> plugin</dl>
<p> $HOME/.weechat/trigger.conf</p>
<dl>
<dt>
<dd> configuration file for <i>trigger</i> plugin</dl>
<p> $HOME/.weechat/xfer.conf</p>
<dl>
<dt>
<dd> configuration file for <i>xfer</i> plugin</dl>
<p> $HOME/.weechat/weechat.log</p>
<dl>
<dt>
<dd> WeeChat log file</dl>
<h2>AUTHORS</h2>
<p> This manpage was written by Sébastien Helleu &lt;flashcode [at] flashtux.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> WeeChat is written by Sébastien Helleu and contributors (complete list is in the AUTHORS.asciidoc file). </p>
<p> Copyright &#169; 2003-2016 Sébastien Helleu &lt;flashcode [at] flashtux.org&gt; </p>
<p> WeeChat is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> Please read the COPYING file for more information. </p>
<p> Web: <a rel="nofollow" href="https://weechat.org/">https://weechat.org/</a></p>
<h2>SUPPORT / REPORTING BUGS</h2>
<p> For help or a bug report: <a rel="nofollow" href="https://weechat.org/dev/support">https://weechat.org/dev/support</a> </p>
<h2>Index</h2>
