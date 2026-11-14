---
title: "control-ctl(5)"
name: "control-ctl"
section: "5"
letter: "c"
url: "/docs/linux/man/5-control-ctl/"
description: "control.ctl – Specify handling of Usenet control messages"
---

<p>control.ctl &#8211; Specify handling of Usenet control messages</p>
<h2>Description</h2>
<p>The file <i>pathetc</i>/control.ctl is used to determine what action is taken when a control message is received. It is read by <code>controlchan</code>, which is normally invoked as a channel program by <code>innd</code>. When <i>control.ctl</i> is modified, <code>controlchan</code> notices this automatically and reloads it. </p>
<p> If a <i>control.ctl.local</i> file exists in <i>pathetc</i>, it is read by <code>controlchan</code> after <i>control.ctl</i> (the resulting behaviour is as though the contents of <i>control.ctl.local</i> were at the end of <i>control.ctl</i>). This local file is formatted like <i>control.ctl</i> and is intended to contain local customization. It is also automatically reloaded when modified. </p>
<p> Blank lines and lines beginning with a number sign (<tt>&quot;#&quot;</tt>) are ignored. All other lines should consist of four fields separated by colons: </p>
<pre> &lt;type&gt;:&lt;from&gt;:&lt;newsgroups&gt;:&lt;action&gt;</pre>
<p>Lines are matched in order and the last matching line in the file will be used, except for checkgroups messages which are handled differently (every matching line is used). </p>
<p> The first field, &lt;type&gt;, is the type of control message for which this line is valid. It should either be the name of a control message or the word <tt>&quot;all&quot;</tt> to indicate that it applies to all control messages. Besides, the following special types are understood:</p>
<dl>
<dt><code>/encoding/</code></p>
<dd>This type specifies the encoding of newgroup and checkgroups control messages so that new descriptions could be decoded the right way. </p>
<pre> /encoding/:*:cn.*:gb18030</pre>
<p>means that a description for a newsgroup in the Chinese cn.* hierarchy will be decoded as though it were encoded in <font SIZE="-1">GB18030</font>, unless a charset is specified in the control message (in such a case, the charset mentioned in the message is used). However, it is possible to override the mentioned charset if <tt>&quot;=force&quot;</tt> is appended after the encoding. For instance, </p>
<pre> /encoding/:*:scout.forum.chinese:big5=force</pre>
<p>means that the description for scout.forum.chinese will always be decoded as though it were encoded in Big5, no matter the charset of the corresponding control message. </p>
<p> The default value when no encoding is mentioned (or when the specified encoding is unknown) is <tt>&quot;CP1252&quot;</tt>. </p>
<p> The last matching line for a given newsgroup name in <i>control.ctl</i> will be used.</p>
<dt><code>/localencoding/</code></p>
<dd>When this type is used, the line consist of only two fields. The default value when this type does not appear in <i>control.ctl</i> (or when the specified charset is unknown) is equivalent to: </p>
<pre> /localencoding/:utf-8</pre>
<p>It means that new descriptions in the <i>newsgroups</i> file will be written using <font SIZE="-1">UTF-8</font>. And <code>controlchan</code> will try to read existing descriptions, so as to see whether they should be updated, as though they were encoded in <font SIZE="-1">UTF-8</font>. </p>
<p> The last matching line in <i>control.ctl</i> will be used.</p>
<dt><code>/maxdocheckgroups/</code></p>
<dd>This type specifies the maximum number of changes that could be made at one time by a checkgroups before bailing and mailing the changes to the admin if no log file was specified. The default value is <tt>10</tt>. </p>
<pre> /maxdocheckgroups/:*:*:10
 /maxdocheckgroups/:*:fr.*:20</pre>
<p>Such a configuration means that a checkgroups containing 15 changes for the French fr.* hierarchy (newgroups to add, remove or change the status) will be automatically honoured whereas a checkgroups containing 15 changes for france.* will only have the required changes mailed or logged. </p>
<p> The last matching line for a given newsgroup name in <i>control.ctl</i> will be used.</dl>
<p> The second field, &lt;from&gt;, is a shell-style pattern that matches the e-mail address of the person posting the message (with the address first converted to lowercase). The matching is done with rules equivalent to those of the shell&#8217;s <i>case</i> statement; see <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1) for more details. </p>
<p> If the control message is a newgroup or rmgroup, the third field, &lt;newsgroups&gt;, is a shell-style pattern matching the newsgroup affected by the control message (especially <tt>&quot;?&quot;</tt> matches exactly one character, <tt>&quot;*&quot;</tt> matches zero or more characters and <tt>&quot;|&quot;</tt> permits to match several patterns on the same line &#8212; for instance <tt>&quot;comp.*|humanities.*&quot;</tt> matches every newsgroup whose name begins with <tt>&quot;comp.&quot;</tt> or <tt>&quot;humanities.&quot;</tt>). If the control message is a checkgroups, the third field is a shell-style pattern matching the newsgroups that should be processed for checking. If the control message is of any other type, the third field is ignored. </p>
<p> The fourth field, &lt;action&gt;, specifies what action to take with control messages that match this line. The following actions are understood:</p>
<dl>
<dt><code>doit</code></p>
<dd>The action requested by the control message should be performed. It means that the change will be silently performed. For checkgroups messages, depending on the value of <code>/maxdocheckgroups/</code>, the shell commands that should be run may be mailed to the news administrator (the argument to <code>&#8211;with-news-master</code> given at configure time, <tt>&quot;usenet&quot;</tt> by default) instead of being performed. </p>
<p> If you always want notification of actions taken, use <tt>&quot;doit=mail&quot;</tt> instead (see below).</p>
<dt><code>doifarg</code></p>
<dd>If the control message has an argument, this is equivalent to <code>doit</code>. If it does not have an argument, this is equivalent to <code>mail</code>. This is only useful for entries for sendsys control messages, allowing a site to request its own <i>newsfeeds</i> entry by posting a <tt>&quot;sendsys mysite&quot;</tt> control message, but not allowing the entire <i>newsfeeds</i> file to be sent. This was intended to partially counter so-called &#8220;sendsys bombs&#8221;, where forged sendsys control messages were used to mailbomb people. </p>
<p> Processing sendsys control messages is not recommended even with this work-around unless they are authenticated in some fashion. The risk of having news servers turned into anonymous mail bombing services is too high.</p>
<dt><code>doit</code>=<i>file</i></p>
<dd>The action is performed as in <code>doit</code>, and additionally a log entry is written to the specified log file <i>file</i>. If <i>file</i> is the word <tt>&quot;mail&quot;</tt>, the log entry is mailed to the news administrator instead. An empty string is equivalent to <i>/dev/null</i> and says to log nothing. </p>
<p> If <i>file</i> starts with a slash, it is taken as the absolute filename to use for the log file. Otherwise, the filename is formed by prepending <i>pathlog</i> and a slash, and appending <tt>&quot;.log&quot;</tt>. In other words, an action of <tt>&quot;doit=newgroup&quot;</tt> will log to <i>pathlog</i>/newgroup.log.</p>
<dt><code>drop</code></p>
<dd>No action is taken and the message is ignored. For checkgroups messages, it means that the newsgroups mentioned will be considered as not existent in the checkgroups for its subsequent process. </p>
<pre> checkgroups:*:comp.*:doit
 checkgroups:*:*binaries*:drop</pre>
<p>will for instance remove every newsgroup whose name contains <tt>&quot;binaries&quot;</tt> in the comp.* hierarchy, even though such groups are mentioned in the checkgroups. (In that example, the removal is performed by the <code>doit</code> action because <code>drop</code> does nothing by itself.)</p>
<dt><code>verify-*</code></p>
<dd>If the action starts with the string <tt>&quot;verify-&quot;</tt>, as in: </p>
<pre> verify-news.announce.newgroups</pre>
<p>then <font SIZE="-1">PGP</font> verification of the control message will be done and the user <font SIZE="-1">ID</font> of the key of the authenticated signer will be checked against the expected identity defined by the rest of the string (<tt>&quot;news.announce.newgroups&quot;</tt> in the above example). This verification is done via <code>pgpverify</code>; see <i><a href="/docs/linux/man/8-pgpverify/">pgpverify</a></i>(8) for more details. </p>
<p> If no logging is specified (with =<i>file</i> as mentioned below), logging will be done the same as with <code>doit</code> as described above.</p>
<dt><code>verify-*</code>=<code>mail</code></p>
<dd><font SIZE="-1">PGP</font> verification is done as for the <code>verify-*</code> action described above, and notification of successful newgroup and rmgroup control messages and the output of checkgroups messages will be mailed to the news administrator. (In the case of checkgroups messages, this means that the shell script that should be run will be mailed to the administrator. The subject of the mail will contain information on whether the script has already been run, depending on the value of <code>/maxdocheckgroups/</code>.)</p>
<dt><code>verify-*</code>=<i>file</i></p>
<dd><font SIZE="-1">PGP</font> verification is done as for the <code>verify-*</code> action described above, and a log entry is written to the specified file as described in <code>doit</code>=<i>file</i> above. (In the case of checkgroups messages, this means that the shell script output of the checkgroups message will be written to that file. The initial line of the log will contain information on whether the script has already been run, depending on the value of <code>/maxdocheckgroups/</code>.)</p>
<dt><code>log</code></p>
<dd>A one-line log message is sent to standard error. <code>innd</code> normally directs this to <i>pathlog</i>/errlog.</p>
<dt><code>log</code>=<i>file</i></p>
<dd>A log entry is written to the specified log file, which is interpreted as in <code>doit</code>=<i>file</i> described above.</p>
<dt><code>mail</code></p>
<dd>A mail message is sent to the news administrator without taking any other action.</dl>
<p> One of the difference between a <code>doit</code> or <code>verify</code> action and a <code>mail</code> action for a checkgroups control message lies in what e-mail is sent; <code>doit</code> or <code>verify</code> will mail the news administrator a shell script (which may have already been run) to create, delete, or modify newsgroups to match the checkgroups message, whereas <code>mail</code> will just mail relevant lines of the checkgroups for manual processing by the news administrator. </p>
<p> Use of the <code>verify</code> action for processing newgroup, rmgroup and checkgroups messages is <font SIZE="-1">STRONGLY</font> recommended. Abuse of control messages is rampant, and authentication via <font SIZE="-1">PGP</font> signature is currently the only reliable way to be sure that a control message comes from who it claims to be from. Most major hierarchies are now issuing PGP-authenticated control messages. </p>
<p> In order to use <code>verify</code> actions, the <font SIZE="-1">PGP</font> key ring of the news user must be populated with the <font SIZE="-1">PGP</font> keys of the hierarchy maintainers whose control messages you want to honour. For more details on PGP-authenticated control messages and the <font SIZE="-1">URL</font> for downloading the <font SIZE="-1">PGP</font> keys of major hierarchies, see <i><a href="/docs/linux/man/8-pgpverify/">pgpverify</a></i>(8). </p>
<p> Control messages of type cancel are handled internally by <code>innd</code> and cannot be affected by any of the mechanisms described here.</p>
<h2>Examples</h2>
<p>With the following three lines in <i>control.ctl</i>: </p>
<pre> newgroup:*:*:drop
 newgroup:group-admin [at] isc.org:comp.*:verify-news.announce.newgroups
 newgroup:kre [at] munnari.oz.au:aus.*:mail</pre>
<p>a newgroup coming from <tt>&quot;group-admin [at] isc.org&quot;</tt> will be honoured if it is for a newsgroup in the comp.* hierarchy and if it has a valid signature corresponding to the <font SIZE="-1">PGP</font> key with a user <font SIZE="-1">ID</font> of <tt>&quot;news.announce.newgroups&quot;</tt>. If any newgroup claiming to be from <tt>&quot;kre [at] munnari.oz.au&quot;</tt> for a newsgroup in the aus.* hierarchy is received, it too will be honoured. All other newgroup messages will be ignored. </p>
<p> Besides, if a <i>control.ctl.local</i> file exists and contains: </p>
<pre> newgroup:*:comp.lang.*:drop</pre>
<p>then a newgroup control article for comp.lang.awk will not be honoured even though it comes from <tt>&quot;group-admin [at] isc.org&quot;</tt> with a valid signature. </p>
<p> As for checkgroups, suppose your news server contains these groups for foo.*, all of them being unmoderated (<tt>&quot;y&quot;</tt> status in the <i>active</i> file): </p>
<pre> foo.bar1
 foo.bar2.first
 foo.bar2.second
 foo.bar2.third
 foo.bar3
 foo.bar3.first
 foo.bar3.second
 foo.bar5</pre>
<p>and you receive the following checkgroups by &lt;foo [at] bar.com&gt; for foo.*: </p>
<pre> foo.bar1 A valid newsgroup.
 foo.bar3.first Only one newsgroup in foo.bar3.*.
 foo.bar4 A newsgroup you want.
 foo.bar5 A newsgroup you do not want.
 foo.bar5.first Another newsgroup you do not want.</pre>
<p>with the following <i>control.ctl</i> entries: </p>
<pre> /maxdocheckgroups/:*:foo.*:2
 checkgroups:foo [at] bar.com:foo.*:verify-key-foo
 checkgroups:foo [at] bar.com:foo.bar2.*:doit
 checkgroups:foo [at] bar.com:foo.bar3.*:mail
 checkgroups:foo [at] bar.com:foo.bar4|foo.bar4.*:doit
 checkgroups:foo [at] bar.com:foo.bar5|foo.bar5.*:drop</pre>
<p>Then, as <i>control.ctl</i> is processed from bottom, here is what happens:</p>
<dl>
<dt>1.</p>
<dd>The newsgroups foo.bar5 and foo.bar5.first are marked as unwanted. But nothing is done yet: other <i>control.ctl</i> entries have to be processed with a real action and a set of newsgroups containing foo.bar5 and foo.bar5.first.</p>
<dt>2.</p>
<dd>The newsgroup foo.bar4 is silently created on the news server, with the description &#8220;A newsgroup you want.&#8221; added to the <i>newsgroups</i> file. In the absence of encoding values (either in the checkgroups message or in <code>/encoding/</code> and <code>/localencoding</code>), the default is to decode the sentence as <font SIZE="-1">CP1242</font> and reencode it as <font SIZE="-1">UTF-8</font>. </p>
<p> If <tt>&quot;doit=mail&quot;</tt> was used, a mail would be sent to the news administrator to inform him that foo.bar4 was successfully created.</p>
<dt>3.</p>
<dd>The newsgroup foo.bar3.second is no longer present. A mail is sent to the news administrator with a shell script to execute. When it is manually executed, foo.bar3.second will be removed. </p>
<p> Note that the descriptions are handled differently and have already been updated without any manual intervention (foo.bar3.first now has the description &#8220;Only one newsgroup in foo.bar3.*.&#8221; and foo.bar3.second no longer has a description).</p>
<dt>4.</p>
<dd>The newsgroups foo.bar2.first, foo.bar2.second and foo.bar2.third are no longer present. However, as the maximum number of changes that could be made at one time by a checkgroups before bailing and mailing the changes to the news administrator is 2, these newsgroups are not removed. A mail is sent with a shell script to manually execute in order to remove these groups from the news server. </p>
<p> Note that their descriptions are removed from the <i>newsgroups</i> file, as well as any other possible descriptions for obsolete newsgroups in foo.bar2.*.</p>
<dt>5.</p>
<dd>The remaining entry is executed if the <font SIZE="-1">PGP</font> verification of the checkgroups message is successful. Otherwise, nothing is done (especially, foo.bar5 remains on the news server). </p>
<p> In case the <font SIZE="-1">PGP</font> signature is verified, foo.bar3 and foo.bar5 are removed from the news server. This entry acts upon newsgroups marked as dropped in its scope and newsgroups not already dealt with by previous <i>control.ctl</i> entries (like foo.bar3 because only foo.bar3.* was previously checked). </p>
<p> Note that if you had wanted to keep foo.bar3 or foo.bar5, you could have added them to the <i>localgroups</i> file in <i>pathetc</i>.</dl>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> control.ctl.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-controlchan/">controlchan</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/5-newsgroups/">newsgroups</a></i>(5), <i><a href="/docs/linux/man/8-pgpverify/">pgpverify</a></i>(8), <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1). </p>
