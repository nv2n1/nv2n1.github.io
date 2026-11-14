---
title: "yum-shell(8)"
name: "yum-shell"
section: "8"
letter: "y"
url: "/docs/linux/man/8-yum-shell/"
description: "yum – Yellowdog Updater Modified shell"
---

<p>yum &#8211; Yellowdog Updater Modified shell</p>
<h2>Synopsis</h2>
<p><code>yum shell</code> [filename]</p>
<h2>Description</h2>
<p><code>yum</code> includes an interactive shell for conducting multiple commands or sets of commands during a single execution of yum. These commands can be issued manually or passed to yum from a file. The commands are much the same as the normal yum command line options. See here <i><a href="/docs/linux/man/8-yum/">yum</a>(8)</i> for that information. There are a few additional commands documented below.</p>
<dl>
<dt><code>config</code></p>
<dd>[argument]&nbsp;<wbr>[value]&nbsp;<wbr><br />
args: debuglevel, errorlevel, obsoletes, gpgcheck, assumeyes, exclude<br />
&nbsp;<wbr>&nbsp;<wbr>If no value is given it prints the current value.&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>If value is given it sets that value.</p>
<dd>
<dt><code>repo</code></p>
<dd>[argument]&nbsp;<wbr>[option]<br />
&nbsp;<wbr>&nbsp;<wbr>list: lists repositories and their status<br />
&nbsp;<wbr>&nbsp;<wbr>enable: enable repositories. option&nbsp;<wbr>=&nbsp;<wbr>repository id&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>disable: disable repositories. option&nbsp;<wbr>=&nbsp;<wbr>repository id&nbsp;<wbr></p>
<dd>
<dt><code>transaction</code></p>
<dd>[argument]<br />
&nbsp;<wbr>&nbsp;<wbr>list: lists the contents of the transaction&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>reset: reset&nbsp;<wbr>(zero-out)&nbsp;<wbr>the transaction&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>solve: run the dependency solver on the transaction<br />
&nbsp;<wbr>&nbsp;<wbr>run: run the transaction&nbsp;<wbr> </p>
<h2>Examples</h2>
<p>The following are examples of using the yum shell.</p>
<dl>
<dd>&nbsp;<wbr>list available packagename*<br />
&nbsp;<wbr>groupinfo&nbsp;<wbr>&#8216;Some Group&#8217;<br />
&nbsp;<wbr>install foo<br />
&nbsp;<wbr>remove bar<br />
&nbsp;<wbr>update baz<br />
&nbsp;<wbr>run That will list available packages matching the glob &#8216;packagename*&#8217;. It will return information on the group &#8216;Some Group&#8217; It will then queue the following commands into the transaction: install foo, remove bar, update baz. Then the &#8216;run&#8217; command will resolve dependencies for the transaction commands and run the transaction.</dl>
<h2>See Also</h2>
<pre><i>yum (8)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a></pre>
<h2>Authors</h2>
<pre>See the Authors file included with this program.</pre>
<h2>Bugs</h2>
<p>There of course aren&#8217;t any bugs, but if you find any, they should be sent to the mailing list: yum [at] lists.baseurl.org or filed in bugzilla. </p>
