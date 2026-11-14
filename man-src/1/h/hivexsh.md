---
title: "hivexsh(1)"
name: "hivexsh"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hivexsh/"
description: "hivexsh – Windows Registry hive shell"
---

<h2 class="name">NAME</h2>
<p> hivexsh &#8211; Windows Registry hive shell </p>
<h2>SYNOPSIS</h2>
<pre><code>
hivexsh[-options][hivefile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This program provides a simple shell for navigating Windows Registry &#8216;hive&#8217; files. It uses the hivex library for access to these binary files. </p>
<p> Firstly you will need to provide a hive file from a Windows operating system. The hive files are usually located in <tt>&quot;C:\Windows\System32\Config&quot;</tt> and have names like <tt>&quot;software&quot;</tt>, <tt>&quot;system&quot;</tt> etc (without any file extension). For more information about hive files, read <i><a href="/docs/linux/man/3-hivex/">hivex</a></i>(3). For information about downloading files from virtual machines, read <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1) and <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1). </p>
<p> You can provide the name of the hive file to examine on the command line. For example: </p>
<pre>
 hivexsh software
</pre>
<p> Or you can start <tt>&quot;hivexsh&quot;</tt> without any arguments, and immediately use the <tt>&quot;load&quot;</tt> command to load a hive: </p>
<pre>
 $ hivexsh
 Welcome to hivexsh, the hivex interactive shell for examining
 Windows Registry binary hive files.
 Type: 'help' for help with commands
       'quit' to quit the shell
 &gt; load software
 software\&gt;
</pre>
<p> Navigate through the hive&#8217;s keys using the <tt>&quot;cd&quot;</tt> command, as if it contained a filesystem, and use <tt>&quot;ls&quot;</tt> to list the subkeys of the current key. Other commands are listed below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Enable lots of debug messages. If you find a Registry file that this program cannot parse, please enable this option and post the complete output <i>and</i> the Registry hive file in your bug report.</p>
<dt><code>-f</code> filename</p>
<dd> Read commands from <tt>&quot;filename&quot;</tt> instead of stdin. To write a hivexsh script, use: </p>
<pre>
 #!/usr/bin/hivexsh -f
</pre>
<dt><code>-w</code></p>
<dd> If this option is given, then writes are allowed to the hive (see &#8220;commit&#8221; command below, and the discussion of modifying hives in &#8220;<font SIZE="-1">WRITING TO HIVE FILES&#8221;</font> in <i><a href="/docs/linux/man/3-hivex/">hivex</a></i>(3)). </p>
<p> <code>Important Note:</code> Even if you specify this option, nothing is written to a hive unless you call the &#8220;commit&#8221; command. If you exit the shell without committing, all changes will be discarded. </p>
<p> If this option is not given, then write commands are disabled.</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>add</code> name</p>
<dd> Add a subkey named <tt>&quot;name&quot;</tt> below the current node. The name may contain spaces and punctuation characters, and does not need to be quoted. </p>
<p> The new key will have no subkeys and no values (see <tt>&quot;setval&quot;</tt>). </p>
<p> There must be no existing subkey called <tt>&quot;name&quot;</tt>, or this command will fail. To replace an existing subkey, delete it first like this: </p>
<pre>
 cd name
 del
</pre>
<dt><code>cd</code> path</p>
<dd> Change to the subkey <tt>&quot;path&quot;</tt>. Use Windows-style backslashes to separate path elements, and start with a backslash in order to start from the root of the hive. For example: </p>
<pre>
 cd \Classes\*
</pre>
<p> moves from the root node, to the <tt>&quot;Classes&quot;</tt> node, to the <tt>&quot;*&quot;</tt> node. If you were already at the root node, you could do this instead: </p>
<pre>
 cd Classes\*
</pre>
<p> or even: </p>
<pre>
 cd Classes
 cd *
</pre>
<p> Path elements (node names) are matched case insensitively, and characters like space, <tt>&quot;*&quot;</tt>, and <tt>&quot;?&quot;</tt> have <i>no</i> special significance. </p>
<p> <tt>&quot;cd ..&quot;</tt> may be used to go to the parent directory. </p>
<p> <tt>&quot;cd&quot;</tt> without any arguments prints the current path. </p>
<p> Be careful with <tt>&quot;cd \&quot;</tt> since the readline library has an undocumented behaviour where it will think the final backslash is a continuation (it reads the next line of input and appends it). Put a single space after the backslash.</p>
<dt><code>close</code> | <code>unload</code></p>
<dd> Close the currently loaded hive. </p>
<p> If you modified the hive, all uncommitted writes are lost when you call this command (or if the shell exits). You have to call <tt>&quot;commit&quot;</tt> to write changes.</p>
<dt><code>commit</code> [newfile]</p>
<dd> Commit changes to the hive. If the optional <tt>&quot;newfile&quot;</tt> parameter is supplied, then the hive is written to that file, else the original file is overwritten. </p>
<p> Note that you have to specify the <tt>&quot;-w&quot;</tt> flag, otherwise no writes are allowed.</p>
<dt><code>del</code></p>
<dd> Delete the current node and everything beneath it. The current directory is moved up one level (as if you did <tt>&quot;cd ..&quot;</tt>) after this command. </p>
<p> You cannot delete the root node.</p>
<dt><code>exit</code> | <code>quit</code></p>
<dd> Exit the shell.</p>
<dt><code>load</code> hivefile</p>
<dd> Load the binary hive named <tt>&quot;hivefile&quot;</tt>. The currently loaded hive, if any, is closed. The current directory is changed back to the root node.</p>
<dt><code>ls</code></p>
<dd> List the subkeys of the current hive Registry key. Note this command does not take any arguments.</p>
<dt><code>lsval</code> [key]</p>
<dd> List the (key, value) pairs of the current hive Registry key. If no argument is given then all pairs are displayed. If <tt>&quot;key&quot;</tt> is given, then the value of the named key is displayed. If <tt>&quot;@&quot;</tt> is given, then the value of the default key is displayed.</p>
<dt><code>setval</code> nrvals</p>
<dd> This command replaces all (key, value) pairs at the current node with the values in subsequent input. <tt>&quot;nrvals&quot;</tt> is the number of values (ie. (key, value) pairs), and any existing values at this node are deleted. So <tt>&quot;setval 0&quot;</tt> just deletes any values at the current node. </p>
<p> The command reads 2 * nrvals lines of input, with each pair of lines of input corresponding to a key and a value to add. </p>
<p> For example, the following setval command replaces whatever is at the current node with two (key, value) pairs. The default key is set to the UTF16-LE-encoded string &#8220;abcd&#8221;. The other value is named &#8220;ANumber&#8221; and is a little-endian <font SIZE="-1">DWORD</font> 0x12345678. </p>
<pre>
 setval 2
 @
 string:abcd
 ANumber
 dword:12345678
</pre>
<p> The first line of each pair is the key (the special key <tt>&quot;@&quot;</tt> means the default key, but you can also use a blank line). </p>
<p> The second line of each pair is the value, which has a special format <tt>&quot;type:value&quot;</tt> with possible types summarized in the table below: </p>
<pre>
 none                 No data is stored, and the type is set to 0.
 string:abc           &quot;abc&quot; is stored as a UTF16-LE-encoded
                      string (type 1).  Note that only 7 bit
                      ASCII strings are supported as input.
 expandstring:...     Same as string but with type 2.
 dword:0x01234567     A DWORD (type 4) with the hex value
                      0x01234567.  You can also use decimal
                      or octal numbers here.
 qword:0x0123456789abcdef
                      A QWORD (type 11) with the hex value
                      0x0123456789abcdef.  You can also use
                      decimal or octal numbers here.
 hex:&lt;type&gt;:&lt;hexbytes&gt;
 hex:1:41,00,42,00,43,00,44,00,00,00
                      This is the generic way to enter any
                      value.  &lt;type&gt; is the integer value type.
                      &lt;hexbytes&gt; is a list of pairs of hex
                      digits which are treated as bytes.
                      (Any non-hex-digits here are ignored,
                      so you can separate bytes with commas
                      or spaces if you want).
</pre>
</dl>
<h2>EXAMPLE</h2>
<pre>
 $ guestfish --ro -i Windows7
 &gt;&lt;fs&gt; download win:c:\windows\system32
