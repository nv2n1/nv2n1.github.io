---
title: "setup(1)"
name: "setup"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setup/"
description: "setup – A text mode system configuration tool"
---

<h2>NAME</h2>
<p> setup &#8211; A text mode system configuration tool</p>
<h2>SYNOPSIS</h2>
<p> <code>setup</code></p>
<h2>DESCRIPTION</h2>
<p> The setuptool program (<code>setup</code>) is a front-end menu program for a group of other tools, mostly <code>system-config-*-tui</code> tools. The list of options which it presents is assembled by scanning /etc/setuptool.d and /usr/share/setuptool/setuptool.d for files. </p>
<p> Each file in the directory should contain one or more lines of text. Each line contains from one to four fields which are separated by &quot;|&quot; characters. In order, they are:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; the path to the binary to invoke&nbsp;<wbr>(mandatory)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; the untranslated name of the application which should be displayed<br />
&nbsp;<wbr>(If unset, defaults to the path of the binary, but don&#8217;t depend on that.)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; the gettext textdomain in which a translation of the name of the application can be found<br />
&nbsp;<wbr>(If unset, defaults to&nbsp;<wbr>&quot;setup&quot;.)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; the directory in which translations for the textdomain can be found<br />
&nbsp;<wbr>(If unset, defaults to&nbsp;<wbr>&quot;/usr/share/locale&quot;.) </p>
<p> If multiple entries with the same untranslated name exist, the one which was read FIRST takes precedence. Files are read in name collation order.</p>
<h2>EXAMPLE</h2>
<p> A contrived example would create /etc/setuptool.d/00bogus with these contents: </p>
<pre>
  /bin/ls --color; /bin/sleep 5|Example &quot;ls&quot; invocation.
</pre>
<p> or </p>
<pre>
  /bin/ls --color; /bin/sleep 5|Give this help list|libc
</pre>
<p> to use one of libc&#8217;s (not meaningful here, but) translatable messages. </p>
<h2>Index</h2>
