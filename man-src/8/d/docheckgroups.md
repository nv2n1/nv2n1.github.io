---
title: "docheckgroups(8)"
name: "docheckgroups"
section: "8"
letter: "d"
url: "/docs/linux/man/8-docheckgroups/"
description: "docheckgroups – Process checkgroups and output a list of changes"
---

<p>docheckgroups &#8211; Process checkgroups and output a list of changes</p>
<h2>Synopsis</h2>
<p><code>docheckgroups</code> [<code>-u</code>] [<i>include-pattern</i> [<i>exclude-pattern</i>]]</p>
<h2>Description</h2>
<p><code>docheckgroups</code> is usually run by <code>controlchan</code> in order to process checkgroups control messages. It reads a list of newsgroups along with their descriptions on its standard input. That list should be formatted like the <i><a href="/docs/linux/man/5-newsgroups/">newsgroups</a></i>(5) file: each line contains the name of a newsgroup followed by one or more tabulations and its description. </p>
<p> <code>docheckgroups</code> will only check the presence of newsgroups which match <i>include-pattern</i> (an <code>egrep</code> expression like <tt>&quot;^comp\..*$&quot;</tt> for newsgroups starting with <tt>&quot;comp.&quot;</tt>) and which do not match <i>exclude-pattern</i> (also an <code>egrep</code> expression) except for newsgroups mentioned in the <i>pathetc</i>/localgroups file. This file is also formatted like the <i><a href="/docs/linux/man/5-newsgroups/">newsgroups</a></i>(5) file and should contain local newsgroups which would otherwise be mentioned for removal. There is no need to put local newsgroups of hierarchies for which no checkgroups control messages are sent, unless you manually process checkgroups texts for them. Lines beginning with a hash sign (<tt>&quot;#&quot;</tt>) are not taken into account in this file. All the newsgroups and descriptions mentioned in <i>pathetc</i>/localgroups are appended to the processed checkgroups. </p>
<p> If <i>exclude-pattern</i> is given, <i>include-pattern</i> should also be given before (you can use an empty string (&quot;&quot;) if you want to include all the newsgroups). Be that as it may, <code>docheckgroups</code> will only check newsgroups in the top-level hierarchies which are present in the checkgroups. </p>
<p> Then, <code>docheckgroups</code> checks the <i>active</i> and <i>newsgroups</i> files and displays on its standard output a list of changes, if any. It does not change anything by default; it only points out what should be changed:</p>
<dl>
<dt>&bull;</p>
<dd>Newsgroups which should be removed (they are in the <i>active</i> file but not in the checkgroups) and the relevant <code>ctlinnd</code> commands to achieve that;</p>
<dt>&bull;</p>
<dd>Newsgroups which should be added (they are not in the <i>active</i> file but in the checkgroups) and the relevant <code>ctlinnd</code> commands to achieve that;</p>
<dt>&bull;</p>
<dd>Newsgroups which are incorrectly marked as moderated or unmoderated (they are both in the <i>active</i> file and the checkgroups but their status differs) and the relevant <code>ctlinnd</code> commands to fix that;</p>
<dt>&bull;</p>
<dd>Descriptions which should be removed (they are in the <i>newsgroups</i> file but not in the checkgroups);</p>
<dt>&bull;</p>
<dd>Descriptions which should be added (they are not in the <i>newsgroups</i> file but in the checkgroups).</dl>
<p> The output of <code>docheckgroups</code> can be fed into <code>mod-active</code> (it will pause the news server, update the <i>active</i> file accordingly, reload it and resume the work of the news server) or into the shell (commands for <code>ctlinnd</code> will be processed one by one). In order to update the <i>newsgroups</i> file, the <code>-u</code> flag must be given to <code>docheckgroups</code>. </p>
<p> When processing a checkgroups manually, it is always advisable to first check the raw output of <code>docheckgroups</code>. Then, if everything looks fine, use <code>mod-active</code> and the <code>-u</code> flag.</p>
<h2>Options</h2>
<dl>
<dt><code>-u</code></p>
<dd>If this flag is given, <code>docheckgroups</code> will update the <i>newsgroups</i> file: it removes obsolete descriptions and adds new ones. It also sorts this file alphabetically and improves its general format (see <i><a href="/docs/linux/man/5-newsgroups/">newsgroups</a></i>(5) for an explanation of the preferred number of tabulations).</dl>
<h2>Examples</h2>
<p>So as to better understand how <code>docheckgroups</code> works, here are examples with the following <i>active</i> file: </p>
<pre> a.first 0000000000 0000000001 y
 a.second.announce 0000000000 0000000001 y
 a.second.group 0000000000 0000000001 y
 b.additional 0000000000 0000000001 y
 b.third 0000000000 0000000001 y
 c.fourth 0000000000 0000000001 y</pre>
<p>the following <i>newsgroups</i> file (using tabulations): </p>
<pre> a.first First group.
 a.second.announce Announce group.
 a.second.group Second group.
 b.third Third group.
 c.fourth Fourth group.</pre>
<p>and the following <i>localgroups</i> file (using tabulations): </p>
<pre> b.additional A local newsgroup I want to keep.</pre>
<p>The checkgroups we process is in the file <i>test</i> which contains: </p>
<pre> a.first First group.
 a.second.announce Announce group. (Moderated)
 a.second.group Second group.
 b.third Third group.
 c.fourth Fourth group.</pre>
<p>If we run: </p>
<pre> cat test | docheckgroups</pre>
<p><code>docheckgroups</code> will output that a.second.announce is incorrectly marked as unmoderated and that its description is obsolete. Besides, two new descriptions will be mentioned for addition (the new one for a.second.announce and the missing description for b.additional &#8212; it should indeed be in the <i>newsgroups</i> file and not only in <i>localgroups</i>). Now that we have checked the output of <code>docheckgroups</code> and that we agree with the changes, we run it with the <code>-u</code> flag to update the <i>newsgroups</i> file and we redirect the standard output to <code>mod-active</code> to update the <i>active</i> file: </p>
<pre> cat test | docheckgroups -u | mod-active</pre>
<p>That&#8217;s all! </p>
<p> Now, suppose we run: </p>
<pre> cat test | docheckgroups &quot;^c\..*$&quot;</pre>
<p>Nothing is output (indeed, everything is fine for the c.* hierarchy). It would have been similar if the <i>test</i> file had only contained the checkgroups for the c.* hierarchy (<code>docheckgroups</code> would not have checked a.* and b.*, even if they had been in <i>include-pattern</i>). </p>
<p> In order to check both a.* and c.*, you can run: </p>
<pre> cat test | docheckgroups &quot;^a\..*$|^c\..*$&quot;</pre>
<p>And if you want to check a.* but not a.second.*, you can run: </p>
<pre> cat test | docheckgroups &quot;^a\..*$&quot; &quot;^a\.second\..*$&quot;</pre>
<p>In our example, <code>docheckgroups</code> will then mention a.second.announce and a.second.group for removal since they are in the <i>active</i> file (the same goes for their descriptions). Notwithstanding, if you do want to keep a.second.announce, just add this group to <i>localgroups</i> and <code>docheckgroups</code> will no longer mention it for removal.</p>
<h2>Files</h2>
<dl>
<dt><i>pathbin</i>/docheckgroups</p>
<dd>The Shell script itself used to process checkgroups.</p>
<dt><i>pathetc</i>/localgroups</p>
<dd>The list of local newsgroups along with their descriptions.</dl>
<h2>History</h2>
<p>Documentation written by Julien Elie for InterNetNews. </p>
<p> <tt>$Id:</tt> docheckgroups.pod 8357 2009-02-27 17:56:00Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/8-controlchan/">controlchan</a></i>(8), <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/8-mod-active/">mod-active</a></i>(8), <i><a href="/docs/linux/man/5-newsgroups/">newsgroups</a></i>(5). </p>
