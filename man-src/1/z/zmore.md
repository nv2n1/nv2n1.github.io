---
title: "zmore(1)"
name: "zmore"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zmore/"
description: "zmore – file perusal filter for crt viewing of compressed text"
---

<h2 class="name">NAME</h2>
<p> zmore &#8211; file perusal filter for crt viewing of compressed text </p>
<h2>SYNOPSIS</h2>
<p> <code>zmore</code> [ name &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Zmore</i> is a filter which allows examination of compressed or plain text files one screenful at a time on a soft-copy terminal. <i>zmore</i> works on files compressed with <i>compress</i>, <i>pack</i> or <i>gzip</i>, and also on uncompressed files. If a file does not exist, <i>zmore</i> looks for a file of the same name with the addition of a .gz, .z or .Z suffix. </p>
<p> <i>Zmore</i> normally pauses after each screenful, printing &#8211;More&#8211; at the bottom of the screen. If the user then types a carriage return, one more line is displayed. If the user hits a space, another screenful is displayed. Other possibilities are enumerated later. </p>
<p> <i>Zmore</i> looks in the file <i>/etc/termcap</i> to determine terminal characteristics, and to determine the default window size. On a terminal capable of displaying 24 lines, the default window size is 22 lines. To use a pager other than the default <i>more</i>, set environment variable PAGER to the name of the desired program, such as <i>less</i>. </p>
<p> Other sequences which may be typed when <i>zmore</i> pauses, and their effects, are as follows (<i>i</i> is an optional integer argument, defaulting to 1) : </p>
<dl>
<dt><i>i</i>&lt;space&gt;</p>
<dd> display <i>i</i> more lines, (or another screenful if no argument is given)</dl>
<dl>
<dt>^D</p>
<dd> display 11 more lines (a &#8220;scroll&#8221;). If <i>i</i> is given, then the scroll size is set to <i>i</i>.</dl>
<dl>
<dt>d</p>
<dd> same as ^D (control-D)</dl>
<dl>
<dt><i>i</i>z</p>
<dd> same as typing a space except that <i>i</i>, if present, becomes the new window size.</dl>
<dl>
<dt><i>i</i>s</p>
<dd> skip <i>i</i> lines and print a screenful of lines</dl>
<dl>
<dt><i>i</i>f</p>
<dd> skip <i>i</i> screenfuls and print a screenful of lines</dl>
<dl>
<dt>q or Q</p>
<dd> Quit.</dl>
<dl>
<dt>=</p>
<dd> Display the current line number.</dl>
<dl>
<dt><i>i</i>/expr</p>
<dd> search for the <i>i</i>-th occurrence of the regular expression <i>expr.</i> The user&#8217;s erase and kill characters may be used to edit the regular expression. Erasing back past the first column cancels the search command.</dl>
<dl>
<dt><i>i</i>n</p>
<dd> search for the <i>i</i>-th occurrence of the last regular expression entered.</dl>
<dl>
<dt>!command</p>
<dd> invoke a shell with <i>command</i>. The character `!&#8217; in &quot;command&quot; is replaced with the previous shell command. The sequence &quot;\!&quot; is replaced by &quot;!&quot;.</dl>
<dl>
<dt>:q or :Q</p>
<dd> Quit (same as q or Q).</dl>
<dl>
<dt>.</p>
<dd> (dot) repeat the previous command.</dl>
<p> The commands take effect immediately, i.e., it is not necessary to type a carriage return. Up to the time when the command character itself is given, the user may hit the line kill character to cancel the numerical argument being formed. In addition, the user may hit the erase character to redisplay the &#8211;More&#8211; message. </p>
<p> At any time when output is being sent to the terminal, the user can hit the quit key (normally control-\). <i>Zmore</i> will stop sending output, and will display the usual &#8211;More&#8211; prompt. The user may then enter one of the above commands in the normal manner. Unfortunately, some output is lost when this is done, due to the fact that any characters waiting in the terminal&#8217;s output queue are flushed when the quit signal occurs. </p>
<p> The terminal is set to <i>noecho</i> mode by this program so that the output can be continuous. What you type will thus not show on your terminal, except for the / and ! commands. </p>
<p> If the standard output is not a teletype, then <i>zmore</i> acts just like <i>zcat</i>, except that a header is printed before each file if there is more than one file.</p>
<h2>FILES</h2>
<dl>
<dt>/etc/termcap</p>
<dd> Terminal data base</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-more/">more</a>(1), <a href="/docs/linux/man/1-gzip/">gzip</a>(1), <a href="/docs/linux/man/1-zdiff/">zdiff</a>(1), <a href="/docs/linux/man/1-zgrep/">zgrep</a>(1), <a href="/docs/linux/man/1-znew/">znew</a>(1), <a href="/docs/linux/man/1-zforce/">zforce</a>(1), <a href="/docs/linux/man/1-gzexe/">gzexe</a>(1) </p>
<h2>Index</h2>
