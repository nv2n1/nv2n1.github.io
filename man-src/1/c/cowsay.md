---
title: "cowsay(1)"
name: "cowsay"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cowsay/"
description: "cowsay/cowthink – configurable speaking/thinking cow (and a bit more)"
---

<h2>NAME</h2>
<p> cowsay/cowthink &#8211; configurable speaking/thinking cow (and a bit more)</p>
<h2>SYNOPSIS</h2>
<p> cowsay [<code>-e</code> <i>eye_string</i>] [<code>-f</code> <i>cowfile</i>] [<code>-h</code>] [<code>-l</code>] [<code>-n</code>] [<code>-T</code> <i>tongue_string</i>] [<code>-W</code> <i>column</i>] [<code>-bdgpstwy</code>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Cowsay</i> generates an ASCII picture of a cow saying something provided by the user. If run with no arguments, it accepts standard input, word-wraps the message given at about 40 columns, and prints the cow saying the given message on standard output. </p>
<p> To aid in the use of arbitrary messages with arbitrary whitespace, use the <code>-n</code> option. If it is specified, the given message will not be word-wrapped. This is possibly useful if you want to make the cow think or speak in <a href="/docs/linux/man/6-figlet/">figlet</a>(6). If <code>-n</code> is specified, there must not be any command-line arguments left after all the switches have been processed. </p>
<p> The <code>-W</code> specifies roughly (where the message should be wrapped. The default is equivalent to <code>-W 40</code> i.e. wrap words at or before the 40th column. </p>
<p> If any command-line arguments are left over after all switches have been processed, they become the cow&#8217;s message. The program will not accept standard input for a message in this case. </p>
<p> There are several provided modes which change the appearance of the cow depending on its particular emotional/physical state. The <code>-b</code> option initiates Borg mode; <code>-d</code> causes the cow to appear dead; <code>-g</code> invokes greedy mode; <code>-p</code> causes a state of paranoia to come over the cow; <code>-s</code> makes the cow appear thoroughly stoned; <code>-t</code> yields a tired cow; <code>-w</code> is somewhat the opposite of <code>-t</code>, and initiates wired mode; <code>-y</code> brings on the cow&#8217;s youthful appearance. </p>
<p> The user may specify the <code>-e</code> option to select the appearance of the cow&#8217;s eyes, in which case the first two characters of the argument string <i>eye_string</i> will be used. The default eyes are &#8216;oo&#8217;. The tongue is similarly configurable through <code>-T</code> and <i>tongue_string</i>; it must be two characters and does not appear by default. However, it does appear in the &#8216;dead&#8217; and &#8216;stoned&#8217; modes. Any configuration done by <code>-e</code> and <code>-T</code> will be lost if one of the provided modes is used. </p>
<p> The <code>-f</code> option specifies a particular cow picture file (&#8220;cowfile&#8221;) to use. If the cowfile spec contains &#8216;/&#8217; then it will be interpreted as a path relative to the current directory. Otherwise, cowsay will search the path specified in the <code>COWPATH </code> environment variable. To list all cowfiles on the current <code>COWPATH</code>, invoke <code>cowsay</code> with the <code>-l</code> switch. </p>
<p> If the program is invoked as <code>cowthink </code> then the cow will think its message instead of saying it. </p>
<h2>COWFILE FORMAT</h2>
<p> A cowfile is made up of a simple block of <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1) code, which assigns a picture of a cow to the variable <code>$the_cow</code>. Should you wish to customize the eyes or the tongue of the cow, then the variables <code>$eyes </code> and <code>$tongue</code> may be used. The trail leading up to the cow&#8217;s message balloon is composed of the character(s) in the <code>$thoughts</code> variable. Any backslashes must be reduplicated to prevent interpolation. The name of a cowfile should end with <code>.cow</code>, otherwise it is assumed not to be a cowfile. Also, at-signs (&#8220;@&#8221;) must be backslashed because that is what Perl 5 expects. </p>
<h2>COMPATIBILITY WITH OLDER VERSIONS</h2>
<p> What older versions? :-) </p>
<p> Version 3.x is fully backward-compatible with 2.x versions. If you&#8217;re still using a 1.x version, consider upgrading. And tell me where you got the older versions, since I didn&#8217;t exactly put them up for world-wide access. </p>
<p> Oh, just so you know, this manual page documents version 3.02 of cowsay.</p>
<h2>ENVIRONMENT</h2>
<p> The COWPATH environment variable, if present, will be used to search for cowfiles. It contains a colon-separated list of directories, much like <code>PATH or</code> <code>MANPATH</code>. It should always contain the <code>/usr/share/cowsay</code> directory, or at least a directory with a file called <code>default.cow</code> in it.</p>
<h2>FILES</h2>
<p> <code>/usr/share/cowsay</code> holds a sample set of cowfiles. If your <code>COWPATH</code> is not explicitly set, it automatically contains this directory.</p>
<h2>BUGS</h2>
<p> If there are any, please notify the author at the address below.</p>
<h2>AUTHOR</h2>
<p> Tony Monroe (tony [at] nog.net), with suggestions from Shannon Appel (appel [at] CSUA.Berkeley.EDU) and contributions from Anthony Polito (aspolito [at] CSUA.Berkeley.EDU).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-perl/">perl</a>(1), <a href="/docs/linux/man/1-wall/">wall</a>(1), <a href="/docs/linux/man/1-nwrite/">nwrite</a>(1), <a href="/docs/linux/man/6-figlet/">figlet</a>(6) </p>
<h2>Index</h2>
