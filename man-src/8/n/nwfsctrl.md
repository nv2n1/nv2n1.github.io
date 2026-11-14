---
title: "nwfsctrl(8)"
name: "nwfsctrl"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nwfsctrl/"
description: "nwfsctrl – Perform server command"
---

<p>nwfsctrl &#8211; Perform server command</p>
<h2>Synopsis</h2>
<p><code>nwfsctrl</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-p</code> <i>ncpfs path</i> ] <code>-c</code> | <code>-o</code> | <code>&#8211;</code>[<code>f</code>]<code>d</code> <code>nwfsctrl [ -h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-p</code> <i>ncpfs path</i> ] <i>server command</i> </p>
<h2>Description</h2>
<p><code>nwfsctrl</code> performs command on server. </p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>With -h nwfsctrl prints a little help text.</dl>
<p> <code>-S</code> <i>server</i></p>
<dl>
<dd>is the name of the server you want to use.</dl>
<p> <code>-U</code> <i>user</i></p>
<dl>
<dd><code>user</code> is the user name to use for login. To set the server&#8217;s time, you need supervisor privileges.</dl>
<p> <code>-P</code> <i>password</i></p>
<dl>
<dd><code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwfstime prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dd><code>-n</code> should be given if no password is required for the login. As you need supervisor privileges for setting the date and time, this option is probably not used very often.</dl>
<p> <code>-C</code></p>
<dl>
<dd>By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<p> <code>-o</code></p>
<dl>
<dd>Open bindery.</dl>
<p> <code>-c</code></p>
<dl>
<dd>Close bindery.</dl>
<p> <code>-d</code></p>
<dl>
<dd>Down fileserver. This command will complain if there are open files on server.</dl>
<p> <code>-fd</code></p>
<dl>
<dd>Down fileserver, regardless of opened files.</dl>
<p> <code>load</code> <i>module options&#8230;</i></p>
<dl>
<dd>Load module <i>module</i> with options <i>options&#8230;</i> on server. Program will complain if <i>module</i> is already loaded.</dl>
<p> <code>unload</code> <i>module</i></p>
<dl>
<dd>Unload module <i>module</i> from server. Program will complain if <i>module</i> is not loaded.</dl>
<p> <code>mount</code> <i>volume</i></p>
<dl>
<dd>Mount volume <i>volume</i>.</dl>
<p> <code>dismount</code> <i>volume</i></p>
<dl>
<dd>Dismount volume <i>volume</i>. <code>If there are open files on volume, server displays prompt on console. You must go to the server (or telnet/xconsole) and hit </code><i>Y</i> <code>or</code> <i>N</i> <code>to get beyond this point).</code></dl>
<p> <code>set</code> <i>variable</i> <code>=</code> <i>value</i></p>
<dl>
<dd>Set server settable variable <i>variable</i> to value <i>value</i>.</dl>
<p> <code>open bindery</code></p>
<dl>
<dd>Open bindery.</dl>
<p> <code>close bindery</code></p>
<dl>
<dd>Close bindery.</dl>
<p> <code>enable login</code></p>
<dl>
<dd>Enable login to file server.</dl>
<p> <code>disable login</code></p>
<dl>
<dd>Disable login to file server.</dl>
<p> <code>disable tts</code></p>
<dl>
<dd>Disable TTS. This probably does not work on Netware 4.11.</dl>
<p> <code>enable tts</code></p>
<dl>
<dd>Enable TTS. This probably does not work on Netware 4.11.</dl>
<h2>Bugs</h2>
<p>Other commands are not written yet (<code>volume</code>, <code>clear connection</code> &#8230;) </p>
<h2>Credits</h2>
<p>This utility was created by Petr Vandrovec (vandrove [at] vc.cvut.cz) and is part of ncpfs since 2.2.0.11.</p>
