---
title: "expect_autoexpect(1)"
name: "expect_autoexpect"
section: "1"
letter: "e"
url: "/docs/linux/man/1-expect_autoexpect/"
description: "autoexpect – generate an Expect script from watching a session"
---

<h2 class="name">NAME</h2>
<p> autoexpect &#8211; generate an Expect script from watching a session </p>
<h2>SYNOPSIS</h2>
<p> <code>autoexpect</code> [ <i>args</i> ] [ <i>program args&#8230;</i> ] </p>
<h2>INTRODUCTION</h2>
<p> autoexpect watches you interacting with another program and creates an Expect script that reproduces your interactions. For straightline scripts, autoexpect saves substantial time over writing scripts by hand. Even if you are an Expect expert, you will find it convenient to use autoexpect to automate the more mindless parts of interactions. It is much easier to cut/paste hunks of autoexpect scripts together than to write them from scratch. And if you are a beginner, you may be able to get away with learning nothing more about Expect than how to call autoexpect. </p>
<p> The simplest way to use autoexpect is to call it from the command line with no arguments. For example: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>% autoexpect</p>
<p> By default, autoexpect spawns a shell for you. Given a program name and arguments, autoexpect spawns that program. For example: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>% autoexpect ftp <a href="ftp://ftp.cme.nist.gov">ftp.cme.nist.gov</a></p>
<p> Once your spawned program is running, interact normally. When you have exited the shell (or program that you specified), autoexpect will create a new script for you. By default, autoexpect writes the new script to &quot;script.exp&quot;. You can override this with the -f flag followed by a new script name. </p>
<p> The following example runs &quot;ftp <a href="ftp://ftp.cme.nist.gov">ftp.cme.nist.gov</a>&quot; and stores the resulting Expect script in the file &quot;nist&quot;. </p>
<pre>
        % autoexpect -f nist ftp <a href="ftp://ftp.cme.nist.gov">ftp.cme.nist.gov</a>
</pre>
<p> It is important to understand that autoexpect does not guarantee a working script because it necessarily has to guess about certain things &#8211; and occasionally it guesses wrong. However, it is usually very easy to identify and fix these problems. The typical problems are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Timing. A surprisingly large number of programs (rn, ksh, zsh, telnet, etc.) and devices (e.g., modems) ignore keystrokes that arrive &quot;too quickly&quot; after prompts. If you find your new script hanging up at one spot, try adding a short sleep just before the previous send. </p>
<p> You can force this behavior throughout by overriding the variable &quot;force_conservative&quot; near the beginning of the generated script. This &quot;conservative&quot; mode makes autoexpect automatically pause briefly (one tenth of a second) before sending each character. This pacifies every program I know of. </p>
<p> This conservative mode is useful if you just want to quickly reassure yourself that the problem is a timing one (or if you really don&#8217;t care about how fast the script runs). This same mode can be forced before script generation by using the -c flag. </p>
<p> Fortunately, these timing spots are rare. For example, telnet ignores characters only after entering its escape sequence. Modems only ignore characters immediately after connecting to them for the first time. A few programs exhibit this behavior all the time but typically have a switch to disable it. For example, rn&#8217;s -T flag disables this behavior. </p>
<p> The following example starts autoexpect in conservative mode. </p>
<pre>
        autoexpect -c
</pre>
<p> The -C flag defines a key to toggle conservative mode. The following example starts autoexpect (in non-conservative mode) with ^L as the toggle. (Note that the ^L is entered literally &#8211; i.e., enter a real control-L). </p>
<pre>
        autoexpect -C ^L
</pre>
<p> The following example starts autoexpect in conservative mode with ^L as the toggle. </p>
<pre>
        autoexpect -c -C ^L
</pre>
<dt>&bull;</p>
<dd> Echoing. Many program echo characters. For example, if you type &quot;more&quot; to a shell, what autoexpect actually sees is: </p>
<pre>
        you typed 'm',
        computer typed 'm',
        you typed 'o',
        computer typed 'o',
        you typed 'r',
        computer typed 'r',
        ...
</pre>
<p> Without specific knowledge of the program, it is impossible to know if you are waiting to see each character echoed before typing the next. If autoexpect sees characters being echoed, it assumes that it can send them all as a group rather than interleaving them the way they originally appeared. This makes the script more pleasant to read. However, it could conceivably be incorrect if you really had to wait to see each character echoed. </p>
<dt>&bull;</p>
<dd> Change. Autoexpect records every character from the interaction in the script. This is desirable because it gives you the ability to make judgements about what is important and what can be replaced with a pattern match. </p>
<p> On the other hand, if you use commands whose output differs from run to run, the generated scripts are not going to be correct. For example, the &quot;date&quot; command always produces different output. So using the date command while running autoexpect is a sure way to produce a script that will require editing in order for it to work. </p>
<p> The -p flag puts autoexpect into &quot;prompt mode&quot;. In this mode, autoexpect will only look for the the last line of program output &#8211; which is usually the prompt. This handles the date problem (see above) and most others. </p>
<p> The following example starts autoexpect in prompt mode. </p>
<pre>
        autoexpect -p
</pre>
<p> The -P flag defines a key to toggle prompt mode. The following example starts autoexpect (in non-prompt mode) with ^P as the toggle. Note that the ^P is entered literally &#8211; i.e., enter a real control-P. </p>
<pre>
        autoexpect -P ^P
</pre>
<p> The following example starts autoexpect in prompt mode with ^P as the toggle. </p>
<pre>
        autoexpect -p -P ^P
</pre>
</dl>
</dl>
<h2>OTHER FLAGS</h2>
<p> The <code>-quiet</code> flag disables informational messages produced by autoexpect. </p>
<p> The <code>-Q</code> flag names a quote character which can be used to enter characters that autoexpect would otherwise consume because they are used as toggles. </p>
<p> The following example shows a number of flags with quote used to provide a way of entering the toggles literally. </p>
<pre>
        autoexpect -P ^P -C ^L -Q ^Q
</pre>
<h2>STYLE</h2>
<p> I don&#8217;t know if there is a &quot;style&quot; for Expect programs but autoexpect should definitely not be held up as any model of style. For example, autoexpect uses features of Expect that are intended specifically for computer-generated scripting. So don&#8217;t try to faithfully write scripts that appear as if they were generated by autoexpect. This is not useful. </p>
<p> On the other hand, autoexpect scripts do show some worthwhile things. For example, you can see how any string must be quoted in order to use it in a Tcl script simply by running the strings through autoexpect. </p>
<h2>SEE ALSO</h2>
<p> <i>&quot;Exploring Expect: A Tcl-Based Toolkit for Automating Interactive Programs&quot;</i> by Don Libes, O&#8217;Reilly and Associates, January 1995.</p>
<h2>AUTHOR</h2>
<p> Don Libes, National Institute of Standards and Technology </p>
<p> <code>expect</code> and <code>autoexpect</code> are in the public domain. NIST and I would appreciate credit if these programs or parts of them are used. </p>
<h2>Index</h2>
