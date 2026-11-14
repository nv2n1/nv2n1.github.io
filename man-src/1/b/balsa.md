---
title: "balsa(1)"
name: "balsa"
section: "1"
letter: "b"
url: "/docs/linux/man/1-balsa/"
description: "Balsa – the GNOME email client."
---

<h2>NAME</h2>
<p>&nbsp;<wbr>Balsa &#8211; the GNOME email client. </p>
<h2>DESCRIPTION</h2>
<p> You can use Balsa to fetch, read, write and send e-mails. </p>
<p> It supports<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>local mailboxes in maildir, mbox and/or mh format,<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>nested mailboxes,<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>protocols POP3, IMAP and SMTP,<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>multithreaded mail retrieval,<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>GnuPG/GPG encryption, LDAP, Kerberos and SSL,<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>MIME&nbsp;<wbr>(view images, save parts),<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>multiple character sets,<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>GPE address book,<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>printing and spell-checking.&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr> Balsa is an integral part of the GNOME desktop environment, but it can<br />
&nbsp;<wbr>&nbsp;<wbr>also be used standalone though it may print some error messages then. </p>
<p> For help on using Balsa, see the documentation in its help menu using<br />
&nbsp;<wbr>&nbsp;<wbr>Yelp Gnome 2 help/documentation browser. </p>
<p> This man page tells about the options of the &#8216;<code>balsa</code>&#8216; command,<br />
&nbsp;<wbr>&nbsp;<wbr>which is used to start Balsa.</p>
<dl>
<dt>
<dd></dl>
<p> Most of these options let you tell Balsa that when it starts<br />
&nbsp;<wbr>&nbsp;<wbr>it should immediately open a mailbox, or the composer ,<br />
&nbsp;<wbr>&nbsp;<wbr>and things like that.</p>
<dl>
<dt>
<dd></dl>
<p> There is also an option to debug POP connections. </p>
<p> When you start Balsa from the command line of an (x)terminal,<br />
&nbsp;<wbr>&nbsp;<wbr>not only can you use the command line options described below,<br />
&nbsp;<wbr>&nbsp;<wbr>any error messages are printed to that terminal too<br />
&nbsp;<wbr>&nbsp;<wbr>(whether you execute that command in the background or not). </p>
<h2>SYNTAX</h2>
<p> <code>balsa </code>[ <code>&nbsp;<wbr> </code> <code>&#8211;help </code>] [ <code>&nbsp;<wbr> </code> <code>&#8211;version </code>] [ <code>-c </code>| <code>&#8211;check-mail </code>] [( <code>-m </code>| <code>&#8211;compose=</code>)<i>email-address </i>] [( <code>-a </code>| <code>&#8211;attach=</code>)<i>filename </i>] [( <code>-o </code>| <code>&#8211;open-mailbox=)</code><i>mailbox</i>[<i>:mailbox</i>]&#8230; ] [ <code>-u </code>| <code>&#8211;open-unread-mailbox </code>] [ <code>-d </code>| <code>&#8211;debug-pop </code>] [ <code>-D </code>| <code>&#8211;debug-imap </code>]</p>
<h2>OPTIONS</h2>
<p> <code>-? </code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Displays a message describing command line syntax of Balsa,<br />
&nbsp;<wbr>&nbsp;<wbr>giving many more options than are presented in this man page;<br />
&nbsp;<wbr>&nbsp;<wbr>Balsa exits immediately after that.</p>
<dl>
<dt>
<dd></dl>
<p> Some of these options work (and thus should be in this man page)<br />
&nbsp;<wbr>&nbsp;<wbr>for example &#8211;display ,<br />
&nbsp;<wbr>&nbsp;<wbr>others may not &#8211;<br />
&nbsp;<wbr>&nbsp;<wbr>for example &#8211;disable-crash-dialog which is provided by GNOME GUI Library.</p>
<dl>
<dt>
<dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Balsa prints its version and exits.</dl>
<p> <code>-c </code>, <code>&#8211;check-mail</code></p>
<dl>
<dt>
<dd> Balsa starts and checks for new mail immediately.</dl>
<p> <code>-i </code>, <code>&#8211;open-inbox</p>
<dl>
<dt>
<dd> Balsa starts and opens the Inbox.</dl>
<p> -m </code><i>email-address </i>, <code>&#8211;compose=</code><i>email-address</i></p>
<dl>
<dt>
<dd> When invoked with this option,<br />
&nbsp;<wbr>&nbsp;<wbr>Balsa will open its email-composer for a new message<br />
&nbsp;<wbr>&nbsp;<wbr>with the specified address in the To: field.</p>
<dl>
<dt>
<dd></dl>
<p> The email-address parameter can be specified<br />
&nbsp;<wbr>&nbsp;<wbr>as user [at] host, e.g.&nbsp;<wbr><code>balsa-list [at] gnome.org&nbsp;<wbr></code>,<br />
&nbsp;<wbr>&nbsp;<wbr>or in URL format, e.g.&nbsp;<wbr><code>&quot;Balsa List&nbsp;<wbr>&lt;balsa-list [at] gnome.org&gt;&quot;&nbsp;<wbr></code>.</p>
<dl>
<dt>
<dd></dl>
<p> You can use Balsa as mailto protocol handler<br />
&nbsp;<wbr>&nbsp;<wbr>by, in the URL handlers section of the GNOME control center,<br />
&nbsp;<wbr>&nbsp;<wbr>setting the mailto protocol command to :&nbsp;<wbr><code>balsa -m&nbsp;<wbr>&quot;%s&quot;</code></dl>
<p> <code>-a </code><i>FILENAME </i>, <code>&#8211;attach=</code><i>FILENAME</i></p>
<dl>
<dt>
<dd> When invoked with this option,<br />
&nbsp;<wbr>&nbsp;<wbr>Balsa will open its email-composer for a new message<br />
&nbsp;<wbr>&nbsp;<wbr>with the specified file already attached to the message.</p>
<dl>
<dt>
<dd></dl>
<p> Example : <code>balsa -a ~/balsa-new.1.gz</code></dl>
<p> <code>-o </code><i>MAILBOX</i>, <code>&#8211;open-mailbox=</code><i>MAILBOX</i>&#8230;</p>
<dl>
<dt>
<dd> This makes FIBalsaFR start and open the specified mailbox. The mailbox should be specified by its full URL.</p>
<dl>
<dt>
<dd></dl>
<p> Example : <code>balsa -o <a href="imap://user@mail.example.com/INBOX">imap://user@mail.example.com/INBOX</a></code> <code>balsa -o file:///var/mail/user</code></dl>
<p> <code>-u </code>, <code>&#8211;open-unread-mailbox</code></p>
<dl>
<dt>
<dd> Open all mailboxes that may contain unread messages.</dl>
<p> <code>-d </code>, <code>&#8211;debug-pop</code></p>
<dl>
<dt>
<dd> Makes Balsa print the POP3 communication to stderr,<br />
&nbsp;<wbr>&nbsp;<wbr>including the full text of every message.</p>
<dl>
<dt>
<dd></dl>
<p> The former can be useful for debugging POP3 connections.</dl>
<p> <code>-D </code>, <code>&#8211;debug-imap</code></p>
<dl>
<dt>
<dd> Makes Balsa print the IMAP communication to stderr.</p>
<dl>
<dt>
<dd></dl>
<p> This feature is useful for debugging IMAP problems.</dl>
</dl>
<h2>WEBSITE</h2>
<p> Balsa&#8217;s website is <i> <a rel="nofollow" href="http://balsa.gnome.org">http://balsa.gnome.org</a></i> </p>
<h2>SUGGESTIONS AND BUG REPORTS</h2>
<p> Any bugs found in Balsa can be reported through<br />
&nbsp;<wbr>&nbsp;<wbr>the Balsa Developer mailing list at&nbsp;<wbr><code>balsa-list [at] gnome.org&nbsp;<wbr></code>,<br />
&nbsp;<wbr>&nbsp;<wbr>or the online bug-tracking system at&nbsp;<wbr><code><a rel="nofollow" href="http://bugzilla.gnome.org/">http://bugzilla.gnome.org/</a>&nbsp;<wbr></code>.</p>
<dl>
<dt>
<dd></dl>
<p> See <a rel="nofollow" href="http://balsa.gnome.org/bugs.html">http://balsa.gnome.org/bugs.html</a> for more information on reporting Balsa bugs. </p>
<p> Before reporting bugs, please check to see if the bug is mentioned in the FAQ&#8217;s or the mailing list archive <i> <a rel="nofollow" href="http://mail.gnome.org/mailman/listinfo/balsa-list">http://mail.gnome.org/mailman/listinfo/balsa-list</a></i> </p>
<p> When reporting Balsa bugs, it is important to include<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>a reliable way to reproduce the bug,<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>version number of Balsa&nbsp;<wbr>(as well as GTK and GNOME),<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>OS name and version,<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>any relevant hardware specs. </p>
<p> If a bug is causing a crash, it is very useful if a stack trace can be provided.</p>
<dl>
<dt>
<dd></dl>
<p> And of course, patches to rectify the bug are even better. </p>
<h2>AUTHORS</h2>
<p> See the AUTHORS file included with Balsa, probably at <code>/usr/share/doc/balsa-2.4.1/AUTHORS </code>. </p>
<h2>FILES</h2>
<p> <code> ~/.gnome2/balsa </code>Balsa&#8217;s preferences file. <code> ~/.gnome2_private/balsa </code>Balsa&#8217;s POP and IMAP passwords file. <code> /etc/sound/events/balsa.soundlist </code>system-wide configuration file </p>
<h2>SEE ALSO</h2>
<p> Package names given in parenthesis are Debian package names. </p>
<p> <code>mailcap </code>(5) &#8211; metamail capabilities file (package: mime-support)</p>
<dl>
<dt>
<dd></dl>
<p> <code>metamail </code>(1) &#8211; infrastructure for mailcap-based multimedia mail<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(package: metamail)</p>
<dl>
<dt>
<dd></dl>
<p> <code>sendmail </code>(8) &#8211; a Mail Transfer Agent (package: exim4-daemon-light)</p>
<dl>
<dt>
<dd></dl>
<p> <code>yelp </code>(1) &#8211; browse Gnome documentation (package: yelp)</p>
<dl>
<dt>
<dd></dl>
<p> <code>GNOME </code>(1) &#8211; modern desktop environment (package: gnome-bin) </p>
<h2>COPYRIGHT</h2>
<p> (c) 1997-2003 Stuart Parmenter and others, see AUTHORS for a list of people. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
