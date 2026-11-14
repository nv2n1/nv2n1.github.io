---
title: "smrsh(8)"
name: "smrsh"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smrsh/"
description: "smrsh – restricted shell for sendmail"
---

<p>smrsh &#8211; restricted shell for sendmail</p>
<h2>Synopsis</h2>
<p><code>smrsh</code> <code>-c</code> command</p>
<h2>Description</h2>
<p>The <i>smrsh</i> program is intended as a replacement for <i>sh</i> for use in the &#8220;prog&#8221; mailer in <i><a href="/docs/linux/man/8-sendmail/">sendmail</a></i>(8) configuration files. It sharply limits the commands that can be run using the &#8220;|program&#8221; syntax of <i>sendmail</i> in order to improve the over all security of your system. Briefly, even if a &#8220;bad guy&#8221; can get sendmail to run a program without going through an alias or forward file, <i>smrsh</i> limits the set of programs that he or she can execute. </p>
<p> Briefly, <i>smrsh</i> limits programs to be in a single directory, by default /etc/smrsh, allowing the system administrator to choose the set of acceptable commands, and to the shell builtin commands &#8220;exec&#8221;, &#8220;exit&#8221;, and &#8220;echo&#8221;. It also rejects any commands with the characters &#8220;&#8217;, `&lt;&#8216;, `&gt;&#8217;, `;&#8217;, `$&#8217;, `(&#8216;, `)&#8217;, `&#8217; (carriage return), or `
&#8217; (newline) on the command line to prevent &#8220;end run&#8221; attacks. It allows &#8220;||&#8221; and &#8220;&amp;&amp;&#8221; to enable commands like: &#8220;&quot;|exec /usr/local/bin/filter || exit 75&quot;&#8221; </p>
<p> Initial pathnames on programs are stripped, so forwarding to &#8220;/usr/ucb/vacation&#8221;, &#8220;/usr/bin/vacation&#8221;, &#8220;/home/server/mydir/bin/vacation&#8221;, and &#8220;vacation&#8221; all actually forward to &#8220;/etc/smrsh/vacation&#8221;. </p>
<p> System administrators should be conservative about populating the /etc/smrsh directory. For example, a reasonable additions is <i><a href="/docs/linux/man/1-vacation/">vacation</a></i>(1), and the like. No matter how brow-beaten you may be, never include any shell or shell-like program (such as <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1)) in the /etc/smrsh directory. Note that this does not restrict the use of shell or perl scripts in the sm.bin directory (using the &#8220;#!&#8221; syntax); it simply disallows execution of arbitrary programs. Also, including mail filtering programs such as <i><a href="/docs/linux/man/1-procmail/">procmail</a></i>(1) is a very bad idea. <i><a href="/docs/linux/man/1-procmail/">procmail</a></i>(1) allows users to run arbitrary programs in their <i><a href="/docs/linux/man/5-procmailrc/">procmailrc</a></i>(5).</p>
<h2>Files</h2>
<p>/etc/smrsh &#8211; directory for restricted programs</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sendmail/">sendmail</a>(8) </p>
