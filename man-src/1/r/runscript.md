---

title: "runscript(1)"
name: "runscript"
section: "1"
letter: "r"
url: "/docs/linux/man/1-runscript/"
description: "runscript – script interpreter for minicom"
---

<p> runscript - script interpreter for minicom  </p>
<h2>SYNOPSIS</h2>
<p> <code>runscript</code> scriptname [logfile [homedir]]  </p>
<h2>DESCRIPTION</h2>
<p> <code>runscript</code> is a simple script interpreter that can be called from within the minicom communications program to automate tasks like logging in to a Unix system or your favorite BBS.  </p>
<h2>INVOCATION</h2>
<p> The program expects a script name and optionally a filename and the user&#8217;s home directory as arguments, and it expects that it&#8217;s input and output are connected to the &quot;remote end&quot;, the system you are connecting to. All messages from <code>runscript</code> meant for the local screen are directed to the <code>stderr</code> output. All this is automatically taken care of if you run it from <code>minicom</code>. The logfile and home directory parameters are only used to tell the log command the name of the logfile and where to write it. If the homedir is omitted, runscript uses the directory found in the $HOME environment variable. If also the logfile name is omitted, the log commands are ignored.  </p>
<h2>KEYWORDS</h2>
<dl>
<dt>Runscript recognizes the following commands:</dt>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dd> <pre><code>expect send goto gosub return !
exit print set inc dec if
timeout verbose sleep break call log
</code></pre>
 </dd></dl>
</dl>
<h2>OVERVIEW OF KEYWORDS</h2>
<dl>
<dt><code>send &lt;string&gt;</code></dt>
<dd> <p> &lt;string&gt; is sent to the modem. It is followed by a &#8216;\r&#8217;. &lt;string&gt; can be: <br />
&nbsp;<wbr>&nbsp;<wbr>- regular text, e.g.&nbsp;<wbr>&#8216;send hello&#8217; <br />
&nbsp;<wbr>&nbsp;<wbr>- text enclosed in quotes, e.g.&nbsp;<wbr>&#8216;send&nbsp;<wbr>&quot;hello world&quot;&#8216; </p>
 </dd>
<dt><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Within&nbsp;<wbr>&lt;string&gt;&nbsp;<wbr>the following sequences are recognized:</dt>
<dd> <p> <br />
&nbsp;<wbr>\n - newline <br />
&nbsp;<wbr>\r - carriage return <br />
&nbsp;<wbr>\a - bell <br />
&nbsp;<wbr>\b - backspace <br />
&nbsp;<wbr>\c - don&#8217;t send the default&nbsp;<wbr>&#8216;\r&#8217;. <br />
&nbsp;<wbr>\f - formfeed <br />
&nbsp;<wbr>\^&nbsp;<wbr>- the&nbsp;<wbr>^&nbsp;<wbr>character <br />
&nbsp;<wbr>\o - send character&nbsp;<wbr><code>o</code>&nbsp;<wbr>(<code>o</code>&nbsp;<wbr>is an octal number) </p>
<p> <br />
 Control characters can be used in the string with the ^ prefix (^A to ^Z, ^[, ^, ^], ^^ and ^_). If you need to send the ^ character, you must prefix it with the \ escape character. <br />
 Also $(environment_variable) can be used, for example $(TERM). Minicom passes three special environment variables: $(LOGIN), which is the username, $(PASS), which is the password, as defined in the proper entry of the dialing directory, and $(TERMLIN) which is the number of actual terminal lines on your screen (that is, the statusline excluded). </p>
 </dd>
<dt><code>print &lt;string&gt;</code></dt>
<dd> <p> Prints &lt;string&gt; to the local screen. Default followed by &#8216;\r\n&#8217;. See the description of &#8216;send&#8217; above. </p>
 </dd>
<dt><code>label:</code></dt>
<dd> <p> Declares a label (with the name &#8216;label&#8217;) to use with goto or gosub. </p>
 </dd>
<dt><code>goto &lt;label&gt;</code></dt>
<dd> <p> Jump to another place in the program. </p>
 </dd>
<dt><code>gosub &lt;label&gt;</code></dt>
<dd> <p> Jumps to another place in the program. When the statement &#8216;return&#8217; is encountered, control returns to the statement after the gosub. Gosub&#8217;s can be nested. </p>
 </dd>
<dt><code>return</code></dt>
<dd> <p> Return from a gosub. </p>
 </dd>
<dt><code>! &lt;command&gt;</code></dt>
<dd> <p> Runs a shell for you in which &#8216;command&#8217; is executed. On return, the variable &#8216;$?&#8216; is set to the exit status of this command, so you can subsequently test it using &#8216;if&#8217;. </p>
 </dd>
<dt><code>exit [value]</code></dt>
<dd> <p> Exit from &quot;runscript&quot; with an optional exit status. (default 1) </p>
 </dd>
<dt><code>set &lt;variable&gt; &lt;value&gt;</code></dt>
<dd> <p> Sets the value of &lt;variable&gt; (which is a single letter a-z) to the value &lt;value&gt;. If &lt;variable&gt; does not exist, it will be created. &lt;value&gt; can be a integer value or another variable. </p>
 </dd>
<dt><code>inc &lt;variable&gt;</code></dt>
<dd> <p> Increments the value of &lt;variable&gt; by one. </p>
 </dd>
<dt><code>dec &lt;variable&gt;</code></dt>
<dd> <p> Decrements the value of &lt;variable&gt; by one. </p>
 </dd>
<dt><code>if &lt;value&gt; &lt;operator&gt; &lt;value&gt; &lt;statement&gt;</code></dt>
<dd> <p> Conditional execution of &lt;statement&gt;. &lt;operator&gt; can be &lt;, &gt;, != or =. Eg, &#8216;if a &gt; 3 goto exitlabel&#8217;. </p>
 </dd>
<dt><code>timeout &lt;value&gt;</code></dt>
<dd> <p> Sets the global timeout. By default, &#8216;runscript&#8217; will exit after 120 seconds. This can be changed with this command. Warning: this command acts differently within an &#8216;expect&#8217; statement, but more about that later. </p>
 </dd>
<dt><code>verbose &lt;on|off&gt;</code></dt>
<dd> <p> By default, this is &#8216;on&#8217;. That means that anything that is being read from the modem by &#8216;runscript&#8217;, gets echoed to the screen. This is so that you can see what &#8216;runscript&#8217; is doing. </p>
 </dd>
<dt><code>sleep &lt;value&gt;</code></dt>
<dd> <p> Suspend execution for &lt;value&gt; seconds. </p>
 </dd>
<dt><code>expect</code></dt>
<dd> <pre><code>  expect {
    pattern [statement]
    pattern [statement]
    [timeout &lt;value&gt; [statement] ]
    ....
  }
</code></pre>
<p> The most important command of all. Expect keeps reading from the input until it reads a pattern that matches one of the specified ones. If expect encounters an optional statement after that pattern, it will execute it. Otherwise the default is to just break out of the expect. &#8216;pattern&#8217; is a string, just as in &#8216;send&#8217; (see above). Normally, expect will timeout in 60 seconds and just exit, but this can be changed with the timeout command. </p>
 </dd>
<dt><code>break</code></dt>
<dd> <p> Break out of an &#8216;expect&#8217; statement. This is normally only useful as argument to &#8216;timeout&#8217; within an expect, because the default action of timeout is to exit immediately. </p>
 </dd>
<dt><code>call &lt;scriptname&gt;</code></dt>
<dd> <p> Transfers control to another scriptfile. When that scriptfile finishes without errors, the original script will continue. </p>
 </dd>
<dt><code>log &lt;text&gt;</code></dt>
<dd> <p> Write text to the logfile. </p>
 </dd></dl>
<h2>NOTES</h2>
<p> If you want to make your script to exit minicom (for example when you use minicom to dial up your ISP, and then start a PPP or SLIP session from a script), try the command &quot;! killall -9 minicom&quot; as the last script command. The -9 option should prevent minicom from hanging up the line and resetting the modem before exiting. <br />
 <br />
 Well, I don&#8217;t think this is enough information to make you an experienced &#8216;programmer&#8217; in &#8216;runscript&#8217;, but together with the examples it shouldn&#8217;t be too hard to write some useful script files. Things will be easier if you have experience with BASIC. The <code>minicom</code> source code comes together with two example scripts, <code>scriptdemo</code> and <code>unixlogin</code>. Especially the last one is a good base to build on for your own scripts.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-minicom/">minicom</a></code>(1)  </p>
<h2>BUGS</h2>
<p> Runscript should be built in to minicom.  </p>
<h2>AUTHOR</h2>
<p> Miquel van Smoorenburg, &lt;miquels [at] drinkel.ow.org&gt; Jukka Lahtinen, &lt;walker [at] netsonic.fi&gt; </p>
