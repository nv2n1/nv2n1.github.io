---
title: "openvt(1)"
name: "openvt"
section: "1"
letter: "o"
url: "/docs/linux/man/1-openvt/"
description: "openvt – start a program on a new virtual terminal (VT)."
---

<h2 class="name">NAME</h2>
<p> openvt &#8211; start a program on a new virtual terminal (VT). </p>
<h2>SYNOPSIS</h2>
<p> <code>openvt</code> [-c vtnumber] [OPTIONS] [&#8211;] command</p>
<h2>DESCRIPTION</h2>
<p> <code>openvt</code> will find the first available VT, and run on it the given <code>command</code> with the given <code>command options,</code> standard input, output and error are directed to that terminal. The current search path ($PATH) is used to find the requested command. If no command is specified then the environment variable $SHELL is used.</p>
<h3>OPTIONS</h3>
<dl>
<dt><i>-c, &#8211;console=VTNUMBER</i></dt>
<dd> Use the given VT number and not the first available. Note you must have write access to the supplied VT for this to work.</dd>
<dt><i>-f, &#8211;force</i></dt>
<dd> Force opening a VT without checking whether it is already in use.</dd>
<dt><i>-e, &#8211;exec</i></dt>
<dd> Directly execute the given command, without forking. This option is meant for use in <i>/etc/inittab</i>. If you want to use this feature in another context, be aware that <code>openvt</code> has to be a session leader in order for -e to work. See <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2) or <code><a href="/docs/linux/man/1-setsid/">setsid</a></code>(1) on how to achieve this.</dd>
<dt><i>-s, &#8211;switch</i></dt>
<dd> Switch to the new VT when starting the command. The VT of the new command will be made the new current VT.</dd>
<dt><i>-u, &#8211;user</i></dt>
<dd> Figure out the owner of the current VT, and run login as that user. Suitable to be called by init. Shouldn&#8217;t be used with <i>-c</i> or <i>-l</i>.</dd>
<dt><i>-l, &#8211;login</i></dt>
<dd> Make the command a login shell. A &#8211; is prepended to the name of the command to be executed.</dd>
<dt><i>-v, &#8211;verbose</i></dt>
<dd> Be a bit more verbose.</dd>
<dt><i>-w, &#8211;wait</i></dt>
<dd> wait for command to complete. If -w and -s are used together then <code>openvt</code> will switch back to the controlling terminal when the command completes.</dd>
<dt><i>-V, &#8211;version</i></dt>
<dd> print program version and exit.</dd>
<dt><i>-h, &#8211;help</i></dt>
<dd> show this text and exit.</dd>
<dt><i>&#8212;</i></dt>
<dd> end of options to <code>openvt</code>.</dd></dl>
<h2>NOTE</h2>
<p> If <code>openvt</code> is compiled with a getopt_long() and you wish to set options to the command to be run, then you must supply the end of options &#8212; flag before the command.</p>
<h2>EXAMPLES</h2>
<p> <code>openvt</code> can be used to start a shell on the next free VT, by using the command:</p>
<dl>
<dt><i>openvt bash</i></dt>
<dd>
</dd><dt>
</dt><dd> To start the shell as a login shell, use:</dd>
<dt><i>openvt -l bash</i></dt>
<dd>
</dd><dt>
</dt><dd> To get a long listing you must supply the &#8212; separator:</dd>
<dt><i>openvt &#8212; ls -l</i></dt>
<dd></dd></dl>
<h2>HISTORY</h2>
<p> Earlier, <code>openvt</code> was called <code>open</code>. It was written by Jon Tombs &lt;jon [at] gtex02.us.es&gt; or &lt;jon [at] robots.ox.ac.uk&gt;. The <i>-w</i> idea is from &quot;sam&quot;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chvt/">chvt</a></code>(1), <code>doshell</code>(8), <code><a href="/docs/linux/man/1-login/">login</a></code>(1) </p>
<h2>Index</h2>
