---
title: "anacrontab(5)"
name: "anacrontab"
section: "5"
letter: "a"
url: "/docs/linux/man/5-anacrontab/"
description: "/etc/anacrontab – configuration file for anacron"
---

<p>/etc/anacrontab &#8211; configuration file for anacron</p>
<h2>Description</h2>
<p>The file <i>/etc/anacrontab</i> describes the jobs controlled by <code><a href="/docs/linux/man/8-anacron/">anacron</a>(8)</code>. Its lines can be of three kinds: job-description lines, environment assignments, or empty lines. Job-description lines are of one of these two forms:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;period&nbsp;<wbr>&nbsp;delay&nbsp;<wbr>&nbsp;job-identifier&nbsp;<wbr>&nbsp;command<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;@period_name delay job-identify command The <i>period</i> is specified in days, the <i>delay</i> in minutes. The <i>job-identifier</i> can contain any non-blank character, except slashes. It is used to identify the job in Anacron messages, and as the name for the job&#8217;s timestamp file. The <i>command</i> can be any shell command. The fields can be separated by blank spaces or tabs. The <i>period_name</i> can only be set to monthly at the present time. This will ensure jobs are only run once a month, no matter the number of days in this month, or the previous month. Environment assignment lines are of the form: </p>
<pre><code>VAR = VALUE</code></pre>
<p> Spaces around <i>VAR</i> are removed. No spaces around <i>VALUE</i> are allowed (unless you want them to be part of the value). The assignment takes effect from the next line to the end of the file, or to the next assignment of the same variable. Empty lines are either blank lines, line containing white-space only, or lines with white-space followed by a &#8216;#&#8217; followed by an arbitrary comment. You can continue a line onto the next line by ending it with a &#8216;\&#8217;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-anacron/">anacron</a>(8)</code> </p>
<p> The Anacron <i>README</i> file.</p>
<h2>Author</h2>
<p>Itai Tzur &lt;itzur [at] actcom.co.il&gt; </p>
<p> Currently maintained by Pascal Hakim &lt;pasc@(debian.org|redellipse.net)&gt;.</p>
