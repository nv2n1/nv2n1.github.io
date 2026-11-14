---
title: "autojump(1)"
name: "autojump"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autojump/"
---

<h3>NAME</h3>

 

 autojump - a faster way to navigate your filesystem

<h3>DESCRIPTION</h3>

 

 autojump is a faster way to navigate your filesystem. It works by maintaining a database of the directories you use the most from the command line. 

 Directories must be visited first before they can be jumped to.

<h3>USAGE</h3>

 

 j is a convenience wrapper function around autojump. Any option that can be used with autojump can be used with j and vice versa.
<dl>
<dt>&bull;
<dd> Jump To A Directory That Contains foo:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
j foo
</pre></dl>
</dl>

<dt>&bull;
<dd> Jump To A Child Directory:
<dl>
<dt>
<dd> 

 Sometimes it's convenient to jump to a child directory (sub-directory of current directory) rather than typing out the full name.
<dl>
<dt>
<dd> <pre>
jc bar
</pre></dl>
</dl>

<dt>&bull;
<dd> Open File Manager To Directories (instead of jumping):
<dl>
<dt>
<dd> 

 Instead of jumping to a directory, you can open a file explorer window (Mac Finder, Windows Explorer, GNOME Nautilus, etc.) to the directory instead.
<dl>
<dt>
<dd> <pre>
jo music
</pre></dl>
 

 Opening a file manager to a child directory is also supported:
<dl>
<dt>
<dd> <pre>
jco images
</pre></dl>
</dl>

<dt>&bull;
<dd> Using Multiple Arguments:
<dl>
<dt>
<dd> 

 Let's assume the following database:
<dl>
<dt>
<dd> <pre><code>
30 &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
/ home / user / mail / inbox 10 &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
/ home / user / work / inbox
</code></pre></dl>
 

 j in would jump into /home/user/mail/inbox as the higher weighted entry. However you can pass multiple arguments to autojump to prefer a different entry. In the above example, j w in would then change directory to /home/user/work/inbox.</dl>
</dl>
 

 For more options refer to help:
<dl>
<dt>
<dd> <pre>
autojump --help
</pre></dl>

<h3>KNOWN ISSUES</h3>

<dl>
<dt>&bull;
<dd> autojump does not support directories that begin with -.
<dt>&bull;
<dd> For bash users, autojump keeps track of directories by modifying $PROMPT_COMMAND. Do not overwrite $PROMPT_COMMAND:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
export PROMPT_COMMAND=&quot;history -a&quot;
</pre></dl>
 

 Instead append to the end of the existing $PROMPT_COMMAND:
<dl>
<dt>
<dd> <pre><code>
export PROMPT_COMMAND = "${PROMPT_COMMAND:+$PROMPT_COMMAND&amp;nbsp;;}&amp;nbsp;history -a"
</code></pre></dl>
</dl>
</dl>

<h3>REPORTING BUGS</h3>

 

 For any questions or issues please visit:
<dl>
<dt>
<dd> <pre>
<a rel="nofollow" HREF="https://github.com/joelthelion/autojump/issues">https://github.com/joelthelion/autojump/issues</a>
</pre></dl>

<h3>AUTHORS</h3>

 

 autojump was originally written by Joël Schaerer, and currently maintained by William Ting. More contributors can be found in AUTHORS.

<h3>COPYRIGHT</h3>

 

 Copyright © 2012 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" HREF="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. 

<h2>Index</h2>

<dl>

</dl>
