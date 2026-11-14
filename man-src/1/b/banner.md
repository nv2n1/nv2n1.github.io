---
title: "banner(1)"
name: "banner"
section: "1"
letter: "b"
url: "/docs/linux/man/1-banner/"
description: "banner – prints a short string to the console in very large letters"
---

<h2>NAME</h2>
<p> banner &#8211; prints a short string to the console in very large letters</p>
<h2>SYNOPSIS</h2>
<p> <code>banner</code> <i>string</i></p>
<h2>DESCRIPTION</h2>
<p> This is a classic-style banner program similar to the one found in Solaris or AIX in the late 1990s. It prints a short string to the console in very large letters. </p>
<p> Banners that do not fit in the terminal will be truncated. If $COLUMNS is exported in the environment, it is taken to be the width of the terminal. If $COLUMNS is not exported, and TIOCGWINSZ is available on the platform, then its idea of the terminal size is used. Otherwise, a terminal width of 80 characters is assumed. </p>
<p> Usage is straightforward. For instance, a single word is printed like this: </p>
<p>&gt;&nbsp;<wbr>banner ken </p>
<p>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#######&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#<br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#<br />
#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#<br />
###&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#####&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#<br />
#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>#<br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>##<br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#######&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr># </p>
<p> Multiple arguments are printed on separate lines: </p>
<p>&gt;&nbsp;<wbr>banner one two&nbsp;<wbr>&nbsp;<wbr> </p>
<p>#######&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#######&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#####&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
#######&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#######&nbsp;<wbr>&nbsp;<wbr> </p>
<p>#######&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#######&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>##&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#######&nbsp;<wbr> </p>
<p> To get a single long line containing whitespace, you must quote the string: </p>
<p>&gt;&nbsp;<wbr>banner&nbsp;<wbr>&quot;one two&quot; </p>
<p>#######&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#######&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#######&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#######&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#####&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr><br />
#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr><br />
#######&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>#######&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>##&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#######&nbsp;<wbr>&nbsp;<wbr> </p>
<h2>COMPATIBILITY</h2>
<p> From time to time, people assert that this program is buggy because it doesn&#8217;t do something that some other banner implementation does. The behavior of the program is based on what I saw on Solaris and AIX systems at the time I wrote it in the late 1990s. I make no claims that the behavior is identical to that of any other contemporary system, especially any non-free system that I may or may not have access to. </p>
<p> If you don&#8217;t like the behavior, you can either submit a patch, or you can use an alternative program such as figlet. I am always happy to accept patches, and I promise to integrate patches promptly if provided. So far, no one who&#8217;s complained has bothered to provide any patches, so the behavior remains the same.</p>
<h2>BUGS</h2>
<p> Report bugs to &lt;support [at] cedar-solutions.com&gt;.</p>
<h2>AUTHOR</h2>
<p> Written by Kenneth J. Pronovici &lt;pronovic [at] ieee.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2004.2007,2013,2014 Kenneth J. Pronovici.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
