---
title: "rifle(1)"
name: "rifle"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rifle/"
description: "rifle – ranger’s file opener"
---

<h2 class="name">NAME</h2>
<p> rifle &#8211; ranger&#8217;s file opener </p>
<h2>SYNOPSIS</h2>
<p> <code>rifle</code> [<code>&#8211;help</code>] [<code>-f</code> <i></i><font SIZE="-1"><i>FLAGS</i></font><i></i>] [<code>-l</code>] [<code>-p</code> <i></i><font SIZE="-1"><i>KEYWORD</i></font><i></i>] [<code>-w</code> <i></i><font SIZE="-1"><i>PROGRAM</i></font><i></i>] [<code>-c</code> <i></i><font SIZE="-1"><i>CONFIG_FILE</i></font><i></i>] <i>files</i></p>
<h2>DESCRIPTION</h2>
<p> rifle is a powerful file executor that allows for complex file type checking, written to meet the needs of the file manager <i>ranger</i>. rifle&#8217;s strength lies in automatically determining file types, depending on which programs are installed on the system, even without any user interaction.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code> <i></i><font SIZE="-1"><i>FLAGS</i></font><i></i></p>
<dd> Specify flags for opening the files. Flags are letters that changes how the program is executed. Any combination of flags will work. Writing uppercase flags will negate the effect of all previously used lowercase flags of the same letter. </p>
<p> Table of all flags:<br />
&nbsp;f&nbsp;<wbr>&nbsp;<wbr>&nbsp;fork program to background<br />
&nbsp;r&nbsp;<wbr>&nbsp;<wbr>&nbsp;run program as root, using sudo<br />
&nbsp;t&nbsp;<wbr>&nbsp;<wbr>&nbsp;run program in a separate terminal, as specified by&nbsp;<tt>$TERMCMD</tt></p>
<dt><code>-l</code></p>
<dd> List all possible ways to open the specified files. Each line will contain information in the format of <i>id:label:flags:command</i>. <i>id</i> is the identification number. <i>label</i> is an arbitrary string that was specified for this command, <i>flags</i> are the flags that are used by default, and <i>command</i> is the command that is going to be executed.</p>
<dt><code>-p</code> <i></i><font SIZE="-1"><i>KEYWORD</i></font><i></i></p>
<dd> Pick a method to open the files. </p>
<p> <i></i><font SIZE="-1"><i>KEYWORD</i></font><i></i> is either the <font SIZE="-1">ID</font> number listed by <tt>&quot;rifle -l&quot;</tt> or a string that matches a label in the configuration file.</p>
<dt><code>-w</code> <i></i><font SIZE="-1"><i>PROGRAM</i></font><i></i></p>
<dd> Open the files with the program <i></i><font SIZE="-1"><i>PROGRAM</i></font><i></i></p>
<dt><code>-c</code> <i></i><font SIZE="-1"><i>CONFIG_FILE</i></font><i></i></p>
<dd> Read configuration from <i></i><font SIZE="-1"><i>CONFIG_FILE</i></font><i></i>, instead of the default.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a list of options and exit.</dl>
<h2>FILES</h2>
<p> rifle shares configuration files with ranger, though ranger is not required in order to use rifle. The default configuration file <i>rifle.conf</i> is expected to be at <i>~/.config/ranger/rifle.conf</i>. However, this can be overridden with the <code>-c</code> option. </p>
<p> This file specifies patterns for determining the commands to open files with. The syntax is described in the comments of the default <i>rifle.conf</i> that ships with ranger. To obtain it, you need to run: <tt>&quot;ranger --copy-config=rifle&quot;</tt></p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1">VISUAL</font></p>
<dd> Determines which editor to use for editing files.</p>
<dt><font SIZE="-1">EDITOR</font></p>
<dd> Determines which editor to use for editing files if <font SIZE="-1">VISUAL</font> is undefined or empty (in the default <i>rifle.conf</i>). If both are undefined or empty, &#8220;vim&#8221; is used instead.</p>
<dt><font SIZE="-1">PAGER</font></p>
<dd> Determines which pager to use for displaying files (in the default <i>rifle.conf</i>).</p>
<dt><font SIZE="-1">TERMCMD</font></p>
<dd> Determines the terminal emulator command for use with the <i>t</i> flag. It is required that the value is the path to an executable file which accepts the &#8220;-e <font SIZE="-1">COMMAND&#8221;</font> argument.</p>
<dt><font SIZE="-1">XDG_CONFIG_HOME</font></p>
<dd> Specifies the directory for configuration files. Defaults to <i></i>$HOME<i>/.config</i>.</dl>
<h2>EXAMPLES</h2>
<p> List all the different methods: </p>
<pre>
 $ rifle -l helloworld.py
 0:editor::&quot;$EDITOR&quot; -- &quot;$@&quot;
 1:pager::&quot;$PAGER&quot; -- &quot;$@&quot;
 2:::python -- &quot;$1&quot;
</pre>
<p> Display its content by opening it with &#8220;cat&#8221;: </p>
<pre>
 $ rifle -w cat helloworld.py
 print(&quot;Hello World!&quot;)
</pre>
<p> Run it by picking the method 2, which calls &#8216;python &#8212; &#8220;$1&#8221;&#8217;: </p>
<pre>
 $ rifle -p 2 helloworld.py
 Hello World!
</pre>
<p> Display the file in a pager inside a new terminal, run as root: </p>
<pre>
 $ rifle -p 1 -f tr helloworld.py
</pre>
<h2>Index</h2>
