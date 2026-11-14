---
title: "mod-active(8)"
name: "mod-active"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mod-active/"
description: "mod-active – Batch processing of newsgroups creation and removal commands"
---

<p>mod-active &#8211; Batch processing of newsgroups creation and removal commands</p>
<h2>Synopsis</h2>
<p><code>mod-active</code> [<i>ctlinnd-command-file</i> &#8230;]</p>
<h2>Description</h2>
<p><code>mod-active</code> is a Perl script that updates the <i>active</i> file based on its input lines of <code>ctlinnd</code> <tt>&quot;newgroup&quot;</tt>, <tt>&quot;rmgroup&quot;</tt> and <tt>&quot;changegroup&quot;</tt> commands. It pauses the server briefly while the existing <i>active</i> file is read and rewritten, which not only keeps <code>innd</code> from updating the <i>active</i> file but also locks against other instances of <code>mod-active</code>. </p>
<p> The script must be run as the news user. </p>
<p> The input to <code>mod-active</code> can come either from one or more <i>ctlinnd-command-file</i> files named on the command line, or from the standard input. Typically its input is the output from the <code>docheckgroups</code> or <code>actsync</code> commands. Every line which contains the string <tt>&quot;ctlinnd newgroup&quot;</tt>, <tt>&quot;ctlinnd rmgroup&quot;</tt>, or <tt>&quot;ctlinnd changegroup&quot;</tt>, optionally preceded by whitespace and/or the path to <code>ctlinnd</code>, is noted for the update. Redundant commands, such as a newgroup directive for a group that already exists, are silently ignored. All other lines in the input are also silently ignored. After the new <i>active</i> file has been generated, the existing one is renamed to <i>active.old</i> and the new one is moved into place. The script then displays the differences between the two files. Any groups that were added to the <i>active</i> file are also added to the <i>active.times</i> file with the string <tt>&quot;checkgroups-update&quot;</tt>. </p>
<p> Please note that no syntax checking is performed on group names by <code>mod-active</code>.</p>
<h2>Bugs</h2>
<p>Though <code>innd</code> is paused while <code>mod-active</code> works, it is not inconceivable that there could be a conflict if something else tries to update the <i>active</i> file during the relatively short time that <code>mod-active</code> is working. The two most realistic ways for this to happen are either by an administrator concurrently doing a manual <code>ctlinnd</code> command, or by <code>innd</code> receiving a control message, then <code>mod-active</code> pausing the server, then the control message handler script that <code>innd</code> forked running its own <code>ctlinnd</code> command while <code>mod-active</code> is working. Note that such scenarios are <i>very</i> unlikely to happen.</p>
<h2>History</h2>
<p>Written by David C Lawrence &lt;tale [at] isc.org&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/5-active-times/">active.times</a></i>(5), <i><a href="/docs/linux/man/8-actsync/">actsync</a></i>(8), <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/8-docheckgroups/">docheckgroups</a></i>(8), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8). </p>
