---
title: "openipmish(1)"
name: "openipmish"
section: "1"
letter: "o"
url: "/docs/linux/man/1-openipmish/"
description: "openipmish – Shell interface to an IPMI system"
---

<h2 class="name">NAME</h2>
<p> openipmish &#8211; Shell interface to an IPMI system</p>
<h2>SYNOPSIS</h2>
<p> <code>openipmish</code> [<i>option</i>] </p>
<h2>DESCRIPTION</h2>
<p> The <code>openipmish</code> is a command interpreter that gives the full power of the OpenIPMI library to a user-level command language. It is designed so it can easily be driven with a scripting language like TCL, it has well-formed output. </p>
<p> <code>openipmish</code> starts up with no connections or anything of that nature. You must enter commands to make connections to domains. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;dmsg</code></p>
<dd> Turn on message debugging, this will dump all messages to debug log output.</p>
<dt><code>&#8211;drawmsg</code></p>
<dd> Turn on raw message debugging, this will dump all low-level messages to debug log output. This differs from normal message debugging in that all protocol messages are also dumped, not just IPMI messages.</p>
<dt><code>&#8211;dmem</code></p>
<dd> Turn on memory debugging, this will cause memory allocation and deallocations to be checked. When the program terminates, it will dump all memory that was not properly freed (leaked).</p>
<dt><code>&#8211;dmsgerr</code></p>
<dd> Turn on printing out low-level message errors.</p>
<dt><code>&#8211;dlock</code></p>
<dd> Turn on lock debugging, this will check lock operations to make sure that locks are help in all the proper places and make sure that locks are properly nested.</p>
<dt><code>-x</code>&nbsp;<wbr>&lt;string&gt;,&nbsp;<wbr><code>&#8211;execute</code>&nbsp;<wbr>&lt;string&gt;</p>
<dd> Execute the given string at startup. This may be entered multiple times for multiple commands.</p>
<dt><code>&#8211;glib</code></p>
<dd> Use glib for the OS handler.</p>
<dt><code>&#8211;snmp</code></p>
<dd> Enable the SNMP trap handler. <code>openipmish</code> must be compiled with SNMP code enabled for this option to be available.</p>
<dt><code>&#8211;help</code></p>
<dd> Help output </p>
</dl>
<h2>COMMANDS</h2>
<p> <code>openipmish</code> follows the standard command syntax defined in <code><a href="/docs/linux/man/7-ipmi_cmdlang/">ipmi_cmdlang</a></code>(7). See that for the details on most commands. The IPMI manual that comes with OpenIPMI will also be quite handy. </p>
<p> <code>openipmish</code> defines some commands that are not in the standard command language. These are: </p>
<dl>
<dt><code>read</code></p>
<dd> Read and execute commands from the given file. </p>
<dt><code>exit</code></p>
<dd> Quit </p>
<dt><code>redisp_cmd on</code>|<code>off</code></p>
<dd> Normally, openipmish redisplays the command line when an event comes in. This is nice for interactive use, but bad for scripting. This lets you turn that function on and off. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-ipmi_cmdlang/">ipmi_cmdlang</a></code>(7), <code><a href="/docs/linux/man/1-ipmi_ui/">ipmi_ui</a></code>(1) </p>
<h2>KNOWN PROBLEMS</h2>
<p> None </p>
<h2>AUTHOR</h2>
<p> Corey Minyard &lt;cminyard [at] mvista.org&gt; </p>
<h2>Index</h2>
