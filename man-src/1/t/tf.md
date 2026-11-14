---
title: "tf(1)"
name: "tf"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tf/"
description: "tf – TinyFugue, a MUD client"
---

<h2>NAME</h2>
<p> tf &#8211; TinyFugue, a MUD client</p>
<h2>SYNOPSIS</h2>
<p> <code>tf [-f</code><i>file</i><code>] [-lnq] [</code><i>world</i><code>]</code><br />
 <code>tf [-f</code><i>file</i><code>] </code><i>host</i><i>port</i></p>
<h2>DESCRIPTION</h2>
<p> <i>TinyFugue</i> (also known as &quot;Fugue&quot; or &quot;TF&quot;) is a line-based client designed for connecting to MUD servers (note: LP, DIKU, and other servers which use prompts require &quot;/lp on&quot;; see /help prompts). </p>
<p> Most of the <i>TF</i> documentation is in the help file, which may be read online with the &quot;/help&quot; command. This manual page may be obsolete in certain areas; however, the helpfile will always be up to date. </p>
<p> <i>TinyFugue</i> is larger than most MUD clients, but has many more features and is much more flexible. The goal is to provide the most functionality in a client that still maintains the user-friendliness of <i>Tinytalk</i>. Clients with extension languages such as <i>Tcltt</i> or <i>VaporTalk</i> can do a little more in certain areas, but are considerably harder to use and learn. <i>TF</i> provides most of these abilities in such a manner that learning to use any one function is relatively easy. </p>
<p> Because I am continually adding new features and changing the code, <i>TF</i> sometimes becomes less stable in a new release. Versions labled &quot;alpha&quot; are generally not as well tested as &quot;beta&quot; versions, so they have the potential for more bugs. For this reason, I leave some older versions at the site where I distribute <i>TF</i>, which do not have all the current features but may have fewer bugs than the most recent release. </p>
<h2>COMMAND LINE ARGUMENTS</h2>
<p> With no arguments, <i>TF</i> will try to connect to the first world defined in the configuration file(s). </p>
<p> With a <code>world</code> argument, <i>TF</i> will try to connect to <code>world</code>, as defined in the configuration file. If <code>world</code> is omitted, it will try to connect to the first world defined in your configuration files. </p>
<p> With <code>host</code> and <code>port</code> arguments, <i>TF</i> will define a temporary world and try to connect to it. The <code>host</code> may be an IP number or regular name format. </p>
<p> OPTIONS</p>
<dl>
<dt>-f<i>file</i></p>
<dd> Load <i>file</i> instead of $HOME/.tfrc at startup.</p>
<dt>-f</p>
<dd> Do not load any personal configuration file. The library will still be loaded.</p>
<dt>-l</p>
<dd> Disable automatic login.</p>
<dt>-n</p>
<dd> Do not connect to any world at startup.</p>
<dt>-q</p>
<dd> Quiet login (overrides %{quiet} flag). </p>
</dl>
<h2>FEATURES</h2>
<p> Among other things, <i>TF</i> allows you to: </p>
<p> Divide the screen into two parts, for input and output, with flexible handling of input (/visual mode). </p>
<p> Connect to multiple worlds and switch between them. </p>
<p> Wrap MUD output at the edge of the screen. </p>
<p> Edit text in the input buffer. </p>
<p> Recall previous commands. </p>
<p> Modify key sequences used to perform editing functions. </p>
<p> Bind commands to key sequences. </p>
<p> Define complex macros to perform MUD tasks easily. </p>
<p> Create triggers which automatically perform certain tasks when certain output is received from the MUD. </p>
<p> Modify existing macros using either a command format or interactive editing. </p>
<p> Support &quot;portals&quot; that automatically switch from world to world. </p>
<p> Hilite or color all or part of a line that matches a certain pattern. </p>
<p> Gag lines that match certain patterns. </p>
<p> Suppress frequently repeated text (&quot;spamming&quot;). </p>
<p> Automatically log into a character on a world. </p>
<p> Send a text file to the MUD in flexible ways, or echo it locally. </p>
<p> Send the output of a system command to the MUD, or echo it locally. </p>
<p> Send text previously received from the MUD to the MUD, or echo it locally. </p>
<p> Repeat a MUD or <i>TF</i> command a number of times. </p>
<p> Do the above four things at varying intervals, or at a rapid-fire rate. </p>
<p> Log a session to a file. </p>
<p> Separate LP and Diku style prompts from normal output. </p>
<p> Page output using a &#8211;More&#8211; prompt. </p>
<p> Recall previously received text. </p>
<h2>CONFIGURATION FILES</h2>
<p> <i>TF</i> will attempt to read two files when starting. The first is a public configuration file &quot;stdlib.tf&quot;, located in TFLIBDIR. TFLIBDIR is defined when <i>TF</i> is installed, and is often /usr/local/lib/tf.lib, or under the home directory of the installer. This library contains many macros and definitions essential to the correct operation of <i>TF.</i> </p>
<p> Next, <i>TF</i> will attempt to read your personal configuration file, $HOME/.tfrc, in which you can put any <i>TF</i> commands you want executed automatically at startup. Two of the most useful commands to use in a <i>TF</i> configuration file are /addworld and /load. </p>
<p> For backward compatability, <i>TF</i> will also try to read the <i>TinyTalk</i> configuration file. Its name defautls to $HOME/.tinytalk, or can be defined by the TINYTALK environment variable. This file may start with a list of worlds that will be defined as if with /addworld. </p>
<h2>HISTORY</h2>
<p> Anton Rang (Tarrant) in February of 1990 released <i>Tinytalk</i>, the first Tinyclient with any great number of features, including hiliting and suppression of text, simple triggers, and separating input and output on the screen. Leo Plotkin (Grod) made rather extensive modifications to <i>Tinytalk</i> to produce <i>Tinywar,</i> which was plagued with some serious bugs and was never officially released (the phrase &quot;Tinywar doesn&#8217;t exist&quot; is often quoted), and is now an unsupported client. <i>TF</i> began when Greg Hudson (Explorer_Bob) merged many of the new features of <i>Tinywar</i> back into <i>TinyTalk,</i> and added many new features of his own, most notably the split screen. Some of the code in Greg&#8217;s releases was contributed by Leo Plotkin. After Greg moved on to <i>VaporTalk,</i> Ken Keys (Hawkeye) took over design and maintenance of <i>TF</i> in July 1991, and continues to make improvements in features and performance. </p>
<p> The code size of <i>TF</i> has surpassed 300K (unstripped), and is signifigantly larger than <i>Tinytalk.</i> It is, in fact, more than three times the size of a number of existing servers. As of version 3.0, it has 66 builtin commands and 57 library commands, each documented in the helpfile. </p>
<p> It has been stated that <i>TF</i> is the most-used client in MUDdom at the current time. I haven&#8217;t taken a poll, but I wouldn&#8217;t be surprised. </p>
<h2>REVIEWS</h2>
<p> <i>TF</i> has significantly changed the tinyclient world. It has a number of merits and a number of flaws, and has frequently been criticized (mostly out of boredom; nobody takes this business too seriously) as having too many features and being too damn big. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&quot;Tinywar doesn&#8217;t exist; TinyFugue merely shouldn&#8217;t.&quot;<br />
 &#8212; Coined by Woodlock, I believe. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&quot;TinyFugue is a work of art.&quot;<br />
 &#8212; Binder, obviously after having too much to drink. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&quot;TinyFugue is the biggest hack since the platform it was built on.&quot;<br />
 &#8212; Explorer_Bob, in one of his lucid moments. </p>
<p> The New York Times, the Christian Science Monitor and the Washington Post all refused to comment. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2002, 2006-2007 Ken Keys </p>
<p> <i>TinyFugue</i> (aka &quot;<i>tf</i>&quot;) is protected under the terms of the GNU General Public License. See the file &quot;COPYING&quot; for details. </p>
<p> <i>TF</i> is currently supported by Ken Keys, who may be contacted by e-mail at kenkeys [at] users.sourceforge.net or kkeys [at] ucsd.edu. </p>
<h2>BACKWARD INCOMPATIBILTIES</h2>
<p> VERSION 3.2 </p>
<p> /rand has been replaced with rand(). Color names can no longer be user defined (but color codes still can). The &quot;=&quot; operator does comparison, not assignment. </p>
<p> VERSION 3.1 </p>
<p> Added type argument to WORLD and LOGIN hooks. </p>
<p> VERSION 3.0 </p>
<p> Backslashes in macros are interpreted slightly differently than in previous versions. Turning on the &quot;backslash&quot; flag will enable the old behavior. </p>
<p> VERSION 2.1 </p>
<p> The CONNECT hook is now called before the LOGIN hook. In 2.0, CONNECT was called after autologin. </p>
<p> VERSION 2.0 </p>
<p> In versions prior to 2.0, &lt;space&gt; was used to scroll the pager; 2.0 uses &lt;tab&gt; as the default, to allow the pager to be nonblocking. </p>
<p> <i>Tinytalk</i> style name gags and hilites are no longer supported. You must use the &#8216;*&#8217; wildcard explicitly, as in &#8216;/hilite hawkeye*&#8217;. </p>
<p> <i>Tinytalk</i> style page and whisper hilites are no longer supported. However, /hilite_page and /hilite_whisper macros are provided in the default macro library. </p>
<p> The .tinytalk file may not be supported in the future; use .tfrc instead. </p>
<p> The &#8216;-&#8216; command line option in versions prior to 2.0 is no longer supported, and has been replaced with &#8216;-l&#8217;. </p>
<h2>BUGS</h2>
<p> When unterbamfing, the old connection should not be closed until the new connection succeeds. </p>
<p> If a shell quote (/quote !) reads a partial line from the pipe, the read will block until the rest of the line is read. </p>
<h2>WARNINGS</h2>
<p> The Surgeon General has determined that MUDding can be detrimental to your GPA. </p>
<h2>Index</h2>
