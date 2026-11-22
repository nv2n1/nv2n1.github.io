---

title: "txt2regex(1)"
name: "txt2regex"
section: "1"
letter: "t"
url: "/docs/linux/man/1-txt2regex/"
description: "txt2regex – a Regular Expression Wizard, written with bash2 builtins"
---

<p> txt2regex &#8211; a Regular Expression Wizard, written with bash2 builtins</p>
<h2>SYNOPSIS</h2>
<p> <code>txt2regex</code> </p>
<p> <code>txt2regex</code> &#8211;nocolor|&#8211;whitebg </p>
<p> <code>txt2regex</code> &#8211;all|&#8211;prog &lt;p1,p2,&#8230;,pN&gt; </p>
<p> <code>txt2regex</code> &#8211;showmeta|&#8211;showinfo &lt;program&gt; </p>
<p> <code>txt2regex</code> &#8211;make &lt;target&gt; </p>
<p> <code>txt2regex</code> &#8211;history &lt;value&gt; </p>
<h2>DESCRIPTION</h2>
<p> <code>txt2regex</code> is a Regular Expression &quot;wizard&quot;, all written with bash2 builtins, that converts human sentences to regexes. </p>
<p> With a simple interactive interface, you just answer to questions and build your own regex for a large variety of programs, like awk, emacs, grep, perl, php, procmail, python, sed and vim. There are more than 20 supported programs. </p>
<p> It&#8217;s bash so download and run, no compilation needed. </p>
<p> Please visit the program homepage at <i><a rel="nofollow" href="http://txt2regex.sf.net">http://txt2regex.sf.net</a></i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;all</code></dt>
<dd> works with all registered programs </dd>
<dt><code>&#8211;help</code></dt>
<dd> prints the help message and quit </dd>
<dt><code>&#8211;history &lt;value&gt;</code></dt>
<dd> prints to STDOUT a regex from a history data </dd>
<dt><code>&#8211;make &lt;target&gt;</code></dt>
<dd> prints a ready regex for a common pattern </dd>
<dt><code>&#8211;nocolor</code></dt>
<dd> self-explanatory </dd>
<dt><code>&#8211;prog &lt;p1,p2,&#8230;&gt;</code></dt>
<dd> choose which programs to use (separated by commas) </dd>
<dt><code>&#8211;showinfo &lt;program&gt;</code></dt>
<dd> prints regex info about the program </dd>
<dt><code>&#8211;showmeta</code></dt>
<dd> prints a complete metachar table for all programs </dd>
<dt><code>&#8211;version</code></dt>
<dd> prints the program version and quit </dd>
<dt><code>&#8211;whitebg</code></dt>
<dd> colors adjusted to white background terminals </dd>
</dl>
<p> By default, all options are turned OFF. Just call it with no options to launch the default interactive interface. </p>
<h2>DETAILS</h2>
<p> <code>&#8211;all</code> is cool but requires lots of lines (~35) </p>
<p> <code>&#8211;nocolor</code> is strong, so it kills &#8211;whitebg </p>
<p> <code>&#8211;showmeta</code> rules, try it </p>
<p> <code>&#8211;showinfo</code> uses reverse video output, &#8211;nocolor turns it off </p>
<p> <code>&#8211;history</code> is getting useful, stay tunned </p>
<p> <code>&#8211;make</code> is a remedy for headaches </p>
<p> <code>&#8211;prog</code> is nice to use your favorite programs, mix it with &#8211;make and &#8211;history </p>
<h2>EXAMPLES</h2>
<dl>
<dt>Calling the program on the default interactive interface</dt>
<dd>
<pre>
  $ txt2regex
</pre>
</dd><dt>Calling the program on a white terminal</dt>
<dd>
<pre>
  $ xterm -fg black -bg white ; txt2regex --whitebg
</pre>
</dd><dt>Getting information</dt>
<dd>
<pre>
  $ txt2regex --showmeta
</pre>
</dd><dt>Getting specific information</dt>
<dd>
<pre>
  $ txt2regex --showinfo sed
</pre>
</dd><dt>Calling it for specific programs</dt>
<dd>
<pre>
  $ txt2regex --prog vim,sed,grep,python
</pre>
</dd><dt>Applying a history data</dt>
<dd>
<pre>
  $ txt2regex --history '16421¤:01¤:'
</pre>
</dd><dt>Getting ready regexes!</dt>
<dd>
<pre><code>
$ txt2regex-- make hour
    $ txt2regex-- make number3-- prog perl
        $ txt2regex-- make date2-- all
</code></pre>
</dd></dl>
<h2>INTERFACE</h2>
<p> The program interface is simple and easy to use. This is its contents: </p>
<pre><code>
+ -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -+ |-&gt;Top menu |
    |-&gt;Group menu |
    | |
    |-&gt;Regexes of the programs selected |
    | ... |
    | ... |
    | |
    |-&gt;History |
    |-&gt;Your prompt |
    | |
    |-&gt;The question |
    |-&gt;The answers |
    | ... |
    | ... |
    +-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -+
</code></pre>
<p> All the basic commands can be used on the numeric pad on the keyboard, but remember to turn ON the NumLock key. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center>
&nbsp;<wbr><code>Command</code>^<code>Description</code></td>
<td ALIGN=right ROWSPAN=2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code><br/>
&nbsp;<wbr><code>.</code>^Quit the program&nbsp;<wbr>(with confirmation)</code></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><br/>
&nbsp;<wbr><code>0</code>^Reset the Regular Expression</code></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><br/>
&nbsp;<wbr><code>1-9</code>^Answers the questions</code></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><br/>
&nbsp;<wbr><code>*</code>^Toggles color ON/OFF</code></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><br/>
&nbsp;<wbr><code>/</code>^Add/remove programs on/from the list</code></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><br/>
&nbsp;<wbr><code>|</code>^Insert an alternation&nbsp;<wbr>(where allowed)</code></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><br/>
&nbsp;<wbr><code>(</code>^Open a new group&nbsp;<wbr>(where allowed)</code></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><br/>
&nbsp;<wbr><code>)</code>^Close the opened group&nbsp;<wbr>(if any)</code></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
</table>
<h2>BUGS</h2>
<p> Bug reports and contributions are VERY welcome! Please send them to the author. </p>
<h2>AUTHOR</h2>
<p> Written and maintained by Aurelio Marinho Jargas &lt;verde [at] aurelio.net&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright © 2000, 2001, 2002, 2003, 2004 Aurelio Marinho Jargas </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
