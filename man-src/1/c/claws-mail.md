---
title: "claws-mail(1)"
name: "claws-mail"
section: "1"
letter: "c"
url: "/docs/linux/man/1-claws-mail/"
description: "Claws Mail – a GTK+ based fast email and news client"
---

<h2 class="name">NAME</h2>
<p> Claws Mail &#8211; a GTK+ based fast email and news client</p>
<h2>SYNOPSIS</h2>
<p> <code>claws-mail</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<dl>
<dt>Claws Mail is an email client (and news reader) based on GTK+, running on the X Window System, and aiming for:</p>
<dd>
 &bull; Quick response<br />
 &bull; Graceful, and sophisticated interface<br />
 &bull; Easy configuration, intuitive operation<br />
 &bull; Abundant features</p>
<dt>Currently implemented features include:</p>
<dd> &bull; POP3 support<br />
 &bull; IMAP4rev1 support<br />
 &bull; integrated NetNews client<br />
 &bull; unlimited multiple account handling<br />
 &bull; thread display<br />
 &bull; filtering<br />
 &bull; MIME (attachments)<br />
 &bull; built-in image view<br />
 &bull; X-Face and (colour) Face support<br />
 &bull; multiple MH folder support<br />
 &bull; mbox importing / exporting<br />
 &bull; external editor support<br />
 &bull; message queueing<br />
 &bull; automatic mail checking<br />
 &bull; draft message function<br />
 &bull; template function<br />
 &bull; line-wrapping<br />
 &bull; clickable URI<br />
 &bull; XML-based address book<br />
 &bull; LDAP, vCard, and JPilot support<br />
 &bull; newly arrived and unread message management<br />
 &bull; Mew/Wanderlust-like key bind<br />
 &bull; printing<br />
 &bull; APOP authentication support<br />
 &bull; SMTP AUTH support<br />
 &bull; SSL support (POP3, SMTP, IMAP4rev1)<br />
 &bull; IPv6 support<br />
 &bull; drag &amp; drop (partially implemented)<br />
 &bull; GnuPG support<br />
 &bull; automake + autoconf support<br />
 &bull; internationalization of UI messages by gettext<br />
 &bull; support of many code sets, including UTF-8 (Unicode) (when using libjconv)<br />
 &bull; support for plugins</dl>
<p> This list is not complete. </p>
<h2>OPTIONS</h2>
<p> <code> &#8211;compose</code> [address]<br />
 <code> &#8211;compose-from-file</code> file<br />
 <code> &#8211;subscribe</code> [uri]<br />
 <code> &#8211;attach file1 [file2]&#8230;</code><br />
 <code> &#8211;receive</code><br />
 <code> &#8211;receive-all</code><br />
 <code> &#8211;cancel-receiving</code><br />
 <code> &#8211;cancel-sending</code><br />
 <code> &#8211;send</code><br />
 <code> &#8211;status</code><br />
 <code> &#8211;status folder[/subfolder]</code><br />
 <code> &#8211;status-full</code><br />
 <code> &#8211;statistics</code><br />
 <code> &#8211;reset-statistics</code><br />
 <code> &#8211;select [#mh/mailbox/]folder[/msg|/msgid]</code><br />
 <code> &#8211;online</code><br />
 <code> &#8211;offline</code><br />
 <code> &#8211;exit</code><br />
 <code> &#8211;debug</code><br />
 <code> &#8211;toggle-debug</code><br />
 <code> &#8211;help</code><br />
 <code> &#8211;version</code><br />
 <code> &#8211;version-full</code><br />
 <code> &#8211;config-dir</code><br />
 <code> &#8211;alternate-config-dir [dir]</code> </p>
<h2>FILES</h2>
<dl>
<dt>$HOME/Mail</p>
<dd> Default directory for mail storage</p>
<dt>$PREFIX/share/claws-mail</p>
<dd> Global program directory</p>
<dt>$PREFIX/share/claws-mail/manual</p>
<dd> Manual files in HTML, PDF, PostScript and plain text format</p>
<dt>$PREFIX/share/claws-mail/themes</p>
<dd> Global themes directory</p>
<dt>$PREFIX/lib/claws-mail/plugins</p>
<dd> Directory for plugins</p>
<dt>$PREFIX/include/claws-mail</p>
<dd> Directory for header files</p>
<dt>$HOME/.claws-mail</p>
<dd> Default directory for user&#8217;s configuration files directory</p>
<dt>$HOME/.claws-mail/addrbook/*</p>
<dd> Addressbook files</p>
<dt>$HOME/.claws-mail/autofaces/*</p>
<dd> Automatic Faces and X-Faces files for accounts</p>
<dt>$HOME/.claws-mail/certs/*</p>
<dd> SSL certificates received from mail servers</p>
<dt>$HOME/.claws-mail/templates</p>
<dd> User-defined templates directory</p>
<dt>$HOME/.claws-mail/themes</p>
<dd> User&#8217;s themes directory</p>
<dt>$HOME/.claws-mail/accountrc</p>
<dd> Configuration for account(s)</p>
<dt>$HOME/.claws-mail/actionsrc</p>
<dd> User-defined custom actions</p>
<dt>$HOME/.claws-mail/addressbookcustomattributerc</p>
<dd> User-defined address book custom attributes</p>
<dt>$HOME/.claws-mail/claws.log</p>
<dd> Claws Mail logfile</p>
<dt>$HOME/.claws-mail/claws-win32.log</p>
<dd> Claws Mail output file (Windows only)</p>
<dt>$HOME/.claws-mail/clawsrc</p>
<dd> Main configuration file</p>
<dt>$HOME/.claws-mail/command_history</p>
<dd> User-specified commands</p>
<dt>$HOME/.claws-mail/customheaderrc</p>
<dd> Configuration for custom headers for sending mail</p>
<dt>$HOME/.claws-mail/dispheaderrc</p>
<dd> Configuration for custom display of headers in message view</p>
<dt>$HOME/.claws-mail/extraheaderrc</p>
<dd> Editable extra headers to be added to compose window combobox</p>
<dt>$HOME/.claws-mail/folderitemrc</p>
<dd> All folders&#8217; attributes</p>
<dt>$HOME/.claws-mail/folderlist.xml</p>
<dd> Folder hierarchy listing</p>
<dt>$HOME/.claws-mail/matcherrc</p>
<dd> Filtering and Processing function configuration</p>
<dt>$HOME/.claws-mail/menurc</p>
<dd> Menu shortcut-key configuration</p>
<dt>$HOME/.claws-mail/messagesearch_history</p>
<dd> User-specified searches in message bodies</p>
<dt>$HOME/.claws-mail/quicksearch_history</p>
<dd> User-specified quick-search list</p>
<dt>$HOME/.claws-mail/messagesearch_history</p>
<dd> User-specified searches in message bodies</p>
<dt>$HOME/.claws-mail/summary*_history</p>
<dd> User-specified searches in message list</p>
<dt>$HOME/.claws-mail/tagsrc</p>
<dd> User-specified tag list</p>
<dt>$HOME/.claws-mail/toolbar*.xml</p>
<dd> User-defined custom toolbars </p>
</dl>
<h2>EXAMPLES</h2>
<p> To run this program the standard way type: </p>
<p> claws-mail </p>
<p> Alternatively you can run it with the following options:</p>
<dl>
<dt><code>&#8211;compose [address]</code></p>
<dd> to open a Compose window</p>
<dt><code>&#8211;compose-from-file file</p>
<dd> open composition window with data from given file. Use &#8211; as file name for reading from standard input. Content format: headers first (To: header required) until an empty line is found, then mail body until end of file.</p>
<dt>&#8211;subscribe [uri]</code></p>
<dd> subscribe to the given URI if possible</p>
<dt><code>&#8211;attach file1 [file2]&#8230;</code></p>
<dd> open composition window with specified files attached</p>
<dt><code>&#8211;compose</code> &quot;mailto:<i>%t</i>?subject=<i>%s</i>&amp;cc=<i>%c</i>&amp;body=<i>%b</i>&quot;</p>
<dd> this syntax can be used in web-browsers and CLI to open a pre-populated Compose window. Possible fields after the destination recipient are: subject, from, cc, bcc, in-reply-to, body, insert (insert a file in body part, needs an absolute path), attach (attach a file, needs an absolute path, see also: &#8211;attach)</p>
<dt><code>&#8211;receive</code></p>
<dd> receive new messages</p>
<dt><code>&#8211;receive-all</code></p>
<dd> receive new messages from all accounts</p>
<dt><code>&#8211;cancel-receiving</code></p>
<dd> cancel receiving of messages</p>
<dt><code>&#8211;cancel-sending</code></p>
<dd> cancel sending of messages</p>
<dt><code>&#8211;send</code></p>
<dd>
 send all queued messages</p>
<dt><code>&#8211;status</code></p>
<dd> show the total number of messages<br />
 [new][unread][unread answers to marked][total]</p>
<dt><code>&#8211;status folder[/subfolder]</code></p>
<dd> show the total number of messages in specified folder<br />
 [new][unread][unread answers to marked][total]</p>
<dt><code>&#8211;status-full</code></p>
<dd> show the total number of messages per folder<br />
 [new][unread][unread answers to marked][total]</p>
<dt><code>&#8211;statistics</code></p>
<dd>
 show session statistics</p>
<dt><code>&#8211;reset-statistics</code></p>
<dd>
 reset session statistics</p>
<dt><code>&#8211;select [#mh/mailbox/]folder[/msg|/msgid]</code></p>
<dd> on startup, jumps to the specified folder/message</p>
<dt><code>&#8211;online</code></p>
<dd> start Claws Mail in (or switch to, if already running) online mode</p>
<dt><code>&#8211;offline</code></p>
<dd> start Claws Mail in (or switch to, if already running) offline mode</p>
<dt><code>&#8211;help</code></p>
<dd> display the help message and exit</p>
<dt><code>&#8211;exit</code></p>
<dd> exit Claws Mail</p>
<dt><code>&#8211;debug</code></p>
<dd> for debug mode</p>
<dt><code>&#8211;toggle-debug</code></p>
<dd> toggle debug mode of a running Claws Mail instance</p>
<dt><code>&#8211;version</code></p>
<dd> display version number and exit</p>
<dt><code>&#8211;version-full</code></p>
<dd> display version number and compiled-in features then exit</p>
<dt><code>&#8211;config-dir</code></p>
<dd> display the CONFIG-DIR and exit</p>
<dt><code>&#8211;alternate-config-dir [dir]</code></p>
<dd> start Claws Mail with the configuration stored in [dir] directory </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>CLAWS_NO_CRASH</code></p>
<dd> if defined disables crash dialog (only if Claws Mail has been built with crash dialog feature enabled)</p>
<dt><code>DISPLAY</code></p>
<dd> default host and display number to use</p>
<dt><code>GPG_AGENT_INFO</code></p>
<dd> the information to access the GPG agent if using GPG agent is enabled in GPG plugin preferences (this is usually set by the agent when launched, otherwise it likely means the GPG agent is not running)</p>
<dt><code>G_BROKEN_FILENAMES</code></p>
<dd> assumes that filenames are in the locale encoding rather than in UTF-8</p>
<dt><code>HOME</code></p>
<dd> full path of the user&#8217;s home directory</p>
<dt><code>LC_ALL</code>, <code>LC_CTYPE</code>, <code>LANG</code></p>
<dd> locale to use for non-win32 systems (the first one not empty is used)</p>
<dt><code>PILOT_CHARSET</code></p>
<dd> if defined overrides default J-Pilot charset (CP1252)</p>
<dt><code>POSIXLY_CORRECT</code></p>
<dd> if defined regular expressions matching follows POSIX standards</p>
<dt><code>SESSION_MANAGER</code></p>
<dd> if defined tries to use the Session Manager (only if Claws Mail has been built with libSM feature enabled)</p>
<dt><code>SHELL</code></p>
<dd> if defined overrides default shell &quot;sh&quot; used by Spamassassin plugin to launch spamc wrappers</p>
<dt><code>SSL_CERT_DIR</code></p>
<dd> use this CA certificates directory instead known system directories</p>
<dt><code>SSL_CERT_FILE</code></p>
<dd> use this CA certificates file instead of searching known system files</p>
<dt><code>USER</code></p>
<dd> used to initialize default &quot;user_id&quot; preference in newly created accounts </p>
</dl>
<h2>BUGS</h2>
<dl>
<dt>You can search for existing bugs and report new ones on Claws Mail bugzilla:</p>
<dd>
 &lt;<a rel="nofollow" href="http://www.thewildbeast.co.uk/claws-mail/bugzilla/">http://www.thewildbeast.co.uk/claws-mail/bugzilla/</a>&gt; </p>
</dl>
<h2>COPYRIGHT</h2>
<dl>
<dt>1999-2014 Hiroyuki Yamamoto and the Claws Mail team</p>
<dd></dl>
<p> Portions are also Copyright:<br />
 (C) 2007-2009 g10 Code GmbH<br />
 (C) 1999-2005 Nullsoft, Inc.<br />
 (C) 1991-1993, 1996-2000, 2001 Free Software Foundation, Inc.<br />
 (C) 2001 Thomas Link, Hiroyuki Yamamoto<br />
 (C) 1995-1997 Peter Mattis and Spencer Kimball<br />
 (C) 1995-1997 Peter Mattis, Spencer Kimball, Josh MacDonald<br />
 (C) 1997-1998 Jay Painter &lt;jpaint [at] serv.net&gt;&lt;jpaint [at] gimp.org&gt;<br />
 (C) 1999-2003 Michael Natterer &lt;mitch [at] gimp.org&gt;<br />
 (C) 2000 Evan Martin<br />
 (C) 1998 Lars Hamann and Stefan Jeske<br />
 (C) 2005, 2006, 2007, 2009 GNOME Foundation<br />
 (C) 2004-2006 Christian Hammond<br />
 (C) 2003-2004 Pawel Salek<br />
 (C) 2001, 2002 &#8211; DINH Viet Hoa<br />
 (C) 1999-2000, Gael Roualland &lt;gael.roualland [at] iname.com&gt;<br />
 (C) 1998-2002 Sendmail, Inc.<br />
 (C) 2007-2008 Juha Kautto (juha at xfce.org)<br />
 (C) 1994-2002 World Wide Web Consortium<br />
 (C) 1999 Graham Davison<br />
 (C) 1999 Eric Busboom<br />
 (C) 2000, Eric Busboom, <a rel="nofollow" href="http://www.softwarestudio.org">http://www.softwarestudio.org</a><br />
 (C) 2002-2007 Randall Hand &lt;yerase [at] yerot.com&gt;<br />
 (C) 2001 by Werner Koch &lt;dd9jn [at] gnu.org&gt;<br />
 (C) 2004 Apache Software Foundation<br />
 (C) 2008 Mikkel Kamstrup Erlandsen<br />
 (C) 2002 Red Hat, Inc.; Copyright 1998, 2001 Tim Janik<br />
 (C) 2008-2009 Christian Hammond, David Trowbridge<br />
 (C) 2003-2005 Lars Lindner &lt;lars.lindner [at] gmx.net&gt;<br />
 (C) 2004,2005 Nathan J. Conrad &lt;t98502 [at] users.sourceforge.net&gt;<br />
 (C) 2004 Karl Soderstrom &lt;ks [at] xanadunet.net&gt;<br />
 (C) 2000 Helix Code, Inc. (<a rel="nofollow" href="http://www.helixcode.com">www.helixcode.com</a>) </p>
<h2>LICENSE</h2>
<dl>
<dt>This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.</p>
<dd>
<dt>See COPYING file on toplevel distribution directory for more license details.</p>
<dd>
</dl>
<h2>AUTHORS</h2>
<dl>
<dt><i>The Claws Mail Team</i></p>
<dd></dl>
<dl>
<dt>
<dd> Holger Berndt <tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;berndth [at] users.sf.net&gt;</p>
<p> Tristan Chabredier<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;wwp [at] claws-mail.org&gt;</p>
<p> Andrej Kacian<tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;andrej [at] kacian.sk&gt;</p>
<p> Darko Koruga <tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;darko [at] users.sf.net&gt;</p>
<p> Ricardo Mones Lastra <tt>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;ricardo [at] mones.org&gt;</p>
<p> Colin Leroy <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;colin [at] colino.net&gt;</p>
<p> Paul Mangan <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;paul [at] claws-mail.org&gt;</p>
<p> Salvatore De Paolis <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;iwkse [at] claws-mail.org&gt;</p>
<p> Pawel Pekala<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;cOrn [at] o2.pl&gt;</p>
<p> Michael Rasmussen<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;mir [at] datanom.net&gt;
</dl>
<dl>
<dt><i>Previous team members</i></p>
<dd></dl>
<dl>
<dt>
<dd> Ho&agrave; Vi&ecirc;t Dinh, Keith Edmunds, Match Grun, Melvin Hadasht, Oliver Haertel, Christoph Hohmann, Alfons Hoogervorst, Werner Koch, Thorsten Maerz, Leandro A. F. Pereira, Luke Plant, Martin Schaaf, Carsten Schurig, Fabien Vantard, Sergey Vlasov, Hiroyuki Yamamoto</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>Claws Mail Homepage</p>
<dd> &lt;<a rel="nofollow" href="http://www.claws-mail.org">http://www.claws-mail.org</a>&gt;</p>
<dt>Claws Mail online manual</p>
<dd> &lt;<a rel="nofollow" href="http://www.claws-mail.org/manual">http://www.claws-mail.org/manual</a>&gt;</p>
<dt>Claws Mail plugins</p>
<dd> &lt;<a rel="nofollow" href="http://www.claws-mail.org/plugins.php">http://www.claws-mail.org/plugins.php</a>&gt; </p>
</dl>
<h2>Index</h2>
