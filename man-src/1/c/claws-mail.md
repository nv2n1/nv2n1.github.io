---
title: "claws-mail(1)"
name: "claws-mail"
section: "1"
letter: "c"
url: "/docs/linux/man/1-claws-mail/"
description: "Claws Mail – a GTK+ based fast email and news client"
---

<h2>SYNOPSIS</h2>
<p> <code>claws-mail</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<dl>
<dt>Claws Mail is an email client (and news reader) based on GTK+, running on the X Window System, and aiming for:</dt>
<dd>
 &bull; Quick response<br />
 &bull; Graceful, and sophisticated interface<br />
 &bull; Easy configuration, intuitive operation<br />
 &bull; Abundant features</dd>
<dt>Currently implemented features include:</dt>
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
 &bull; support for plugins</dd></dl>
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
<dt>$HOME/Mail</dt>
<dd> Default directory for mail storage</dd>
<dt>$PREFIX/share/claws-mail</dt>
<dd> Global program directory</dd>
<dt>$PREFIX/share/claws-mail/manual</dt>
<dd> Manual files in HTML, PDF, PostScript and plain text format</dd>
<dt>$PREFIX/share/claws-mail/themes</dt>
<dd> Global themes directory</dd>
<dt>$PREFIX/lib/claws-mail/plugins</dt>
<dd> Directory for plugins</dd>
<dt>$PREFIX/include/claws-mail</dt>
<dd> Directory for header files</dd>
<dt>$HOME/.claws-mail</dt>
<dd> Default directory for user&#8217;s configuration files directory</dd>
<dt>$HOME/.claws-mail/addrbook/*</dt>
<dd> Addressbook files</dd>
<dt>$HOME/.claws-mail/autofaces/*</dt>
<dd> Automatic Faces and X-Faces files for accounts</dd>
<dt>$HOME/.claws-mail/certs/*</dt>
<dd> SSL certificates received from mail servers</dd>
<dt>$HOME/.claws-mail/templates</dt>
<dd> User-defined templates directory</dd>
<dt>$HOME/.claws-mail/themes</dt>
<dd> User&#8217;s themes directory</dd>
<dt>$HOME/.claws-mail/accountrc</dt>
<dd> Configuration for account(s)</dd>
<dt>$HOME/.claws-mail/actionsrc</dt>
<dd> User-defined custom actions</dd>
<dt>$HOME/.claws-mail/addressbookcustomattributerc</dt>
<dd> User-defined address book custom attributes</dd>
<dt>$HOME/.claws-mail/claws.log</dt>
<dd> Claws Mail logfile</dd>
<dt>$HOME/.claws-mail/claws-win32.log</dt>
<dd> Claws Mail output file (Windows only)</dd>
<dt>$HOME/.claws-mail/clawsrc</dt>
<dd> Main configuration file</dd>
<dt>$HOME/.claws-mail/command_history</dt>
<dd> User-specified commands</dd>
<dt>$HOME/.claws-mail/customheaderrc</dt>
<dd> Configuration for custom headers for sending mail</dd>
<dt>$HOME/.claws-mail/dispheaderrc</dt>
<dd> Configuration for custom display of headers in message view</dd>
<dt>$HOME/.claws-mail/extraheaderrc</dt>
<dd> Editable extra headers to be added to compose window combobox</dd>
<dt>$HOME/.claws-mail/folderitemrc</dt>
<dd> All folders&#8217; attributes</dd>
<dt>$HOME/.claws-mail/folderlist.xml</dt>
<dd> Folder hierarchy listing</dd>
<dt>$HOME/.claws-mail/matcherrc</dt>
<dd> Filtering and Processing function configuration</dd>
<dt>$HOME/.claws-mail/menurc</dt>
<dd> Menu shortcut-key configuration</dd>
<dt>$HOME/.claws-mail/messagesearch_history</dt>
<dd> User-specified searches in message bodies</dd>
<dt>$HOME/.claws-mail/quicksearch_history</dt>
<dd> User-specified quick-search list</dd>
<dt>$HOME/.claws-mail/messagesearch_history</dt>
<dd> User-specified searches in message bodies</dd>
<dt>$HOME/.claws-mail/summary*_history</dt>
<dd> User-specified searches in message list</dd>
<dt>$HOME/.claws-mail/tagsrc</dt>
<dd> User-specified tag list</dd>
<dt>$HOME/.claws-mail/toolbar*.xml</dt>
<dd> User-defined custom toolbars </dd>
</dl>
<h2>EXAMPLES</h2>
<p> To run this program the standard way type: </p>
<p> claws-mail </p>
<p> Alternatively you can run it with the following options:</p>
<dl>
<dt><code>&#8211;compose [address]</code></dt>
<dd> to open a Compose window</dd>
<dt><code>&#8211;compose-from-file file</dt>
<dd> open composition window with data from given file. Use &#8211; as file name for reading from standard input. Content format: headers first (To: header required) until an empty line is found, then mail body until end of file.</dd>
<dt>&#8211;subscribe [uri]</code></dt>
<dd> subscribe to the given URI if possible</dd>
<dt><code>&#8211;attach file1 [file2]&#8230;</code></dt>
<dd> open composition window with specified files attached</dd>
<dt><code>&#8211;compose</code> &quot;mailto:<i>%t</i>?subject=<i>%s</i>&amp;cc=<i>%c</i>&amp;body=<i>%b</i>&quot;</dt>
<dd> this syntax can be used in web-browsers and CLI to open a pre-populated Compose window. Possible fields after the destination recipient are: subject, from, cc, bcc, in-reply-to, body, insert (insert a file in body part, needs an absolute path), attach (attach a file, needs an absolute path, see also: &#8211;attach)</dd>
<dt><code>&#8211;receive</code></dt>
<dd> receive new messages</dd>
<dt><code>&#8211;receive-all</code></dt>
<dd> receive new messages from all accounts</dd>
<dt><code>&#8211;cancel-receiving</code></dt>
<dd> cancel receiving of messages</dd>
<dt><code>&#8211;cancel-sending</code></dt>
<dd> cancel sending of messages</dd>
<dt><code>&#8211;send</code></dt>
<dd>
 send all queued messages</dd>
<dt><code>&#8211;status</code></dt>
<dd> show the total number of messages<br />
 [new][unread][unread answers to marked][total]</dd>
<dt><code>&#8211;status folder[/subfolder]</code></dt>
<dd> show the total number of messages in specified folder<br />
 [new][unread][unread answers to marked][total]</dd>
<dt><code>&#8211;status-full</code></dt>
<dd> show the total number of messages per folder<br />
 [new][unread][unread answers to marked][total]</dd>
<dt><code>&#8211;statistics</code></dt>
<dd>
 show session statistics</dd>
<dt><code>&#8211;reset-statistics</code></dt>
<dd>
 reset session statistics</dd>
<dt><code>&#8211;select [#mh/mailbox/]folder[/msg|/msgid]</code></dt>
<dd> on startup, jumps to the specified folder/message</dd>
<dt><code>&#8211;online</code></dt>
<dd> start Claws Mail in (or switch to, if already running) online mode</dd>
<dt><code>&#8211;offline</code></dt>
<dd> start Claws Mail in (or switch to, if already running) offline mode</dd>
<dt><code>&#8211;help</code></dt>
<dd> display the help message and exit</dd>
<dt><code>&#8211;exit</code></dt>
<dd> exit Claws Mail</dd>
<dt><code>&#8211;debug</code></dt>
<dd> for debug mode</dd>
<dt><code>&#8211;toggle-debug</code></dt>
<dd> toggle debug mode of a running Claws Mail instance</dd>
<dt><code>&#8211;version</code></dt>
<dd> display version number and exit</dd>
<dt><code>&#8211;version-full</code></dt>
<dd> display version number and compiled-in features then exit</dd>
<dt><code>&#8211;config-dir</code></dt>
<dd> display the CONFIG-DIR and exit</dd>
<dt><code>&#8211;alternate-config-dir [dir]</code></dt>
<dd> start Claws Mail with the configuration stored in [dir] directory </dd>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>CLAWS_NO_CRASH</code></dt>
<dd> if defined disables crash dialog (only if Claws Mail has been built with crash dialog feature enabled)</dd>
<dt><code>DISPLAY</code></dt>
<dd> default host and display number to use</dd>
<dt><code>GPG_AGENT_INFO</code></dt>
<dd> the information to access the GPG agent if using GPG agent is enabled in GPG plugin preferences (this is usually set by the agent when launched, otherwise it likely means the GPG agent is not running)</dd>
<dt><code>G_BROKEN_FILENAMES</code></dt>
<dd> assumes that filenames are in the locale encoding rather than in UTF-8</dd>
<dt><code>HOME</code></dt>
<dd> full path of the user&#8217;s home directory</dd>
<dt><code>LC_ALL</code>, <code>LC_CTYPE</code>, <code>LANG</code></dt>
<dd> locale to use for non-win32 systems (the first one not empty is used)</dd>
<dt><code>PILOT_CHARSET</code></dt>
<dd> if defined overrides default J-Pilot charset (CP1252)</dd>
<dt><code>POSIXLY_CORRECT</code></dt>
<dd> if defined regular expressions matching follows POSIX standards</dd>
<dt><code>SESSION_MANAGER</code></dt>
<dd> if defined tries to use the Session Manager (only if Claws Mail has been built with libSM feature enabled)</dd>
<dt><code>SHELL</code></dt>
<dd> if defined overrides default shell &quot;sh&quot; used by Spamassassin plugin to launch spamc wrappers</dd>
<dt><code>SSL_CERT_DIR</code></dt>
<dd> use this CA certificates directory instead known system directories</dd>
<dt><code>SSL_CERT_FILE</code></dt>
<dd> use this CA certificates file instead of searching known system files</dd>
<dt><code>USER</code></dt>
<dd> used to initialize default &quot;user_id&quot; preference in newly created accounts </dd>
</dl>
<h2>BUGS</h2>
<dl>
<dt>You can search for existing bugs and report new ones on Claws Mail bugzilla:</dt>
<dd>
 &lt;<a rel="nofollow" href="http://www.thewildbeast.co.uk/claws-mail/bugzilla/">http://www.thewildbeast.co.uk/claws-mail/bugzilla/</a>&gt; </dd>
</dl>
<h2>COPYRIGHT</h2>
<dl>
<dt>1999-2014 Hiroyuki Yamamoto and the Claws Mail team</dt>
<dd></dd></dl>
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
<dt>This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.</dt>
<dd>
</dd><dt>See COPYING file on toplevel distribution directory for more license details.</dt>
<dd>
</dd></dl>
<h2>AUTHORS</h2>
<dl>
<dt><i>The Claws Mail Team</i></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Holger Berndt <tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;berndth [at] users.sf.net&gt;</dd>
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
<dt><i>Previous team members</i></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Ho&agrave; Vi&ecirc;t Dinh, Keith Edmunds, Match Grun, Melvin Hadasht, Oliver Haertel, Christoph Hohmann, Alfons Hoogervorst, Werner Koch, Thorsten Maerz, Leandro A. F. Pereira, Luke Plant, Martin Schaaf, Carsten Schurig, Fabien Vantard, Sergey Vlasov, Hiroyuki Yamamoto</dd></dl>
<h2>SEE ALSO</h2>
<dl>
<dt>Claws Mail Homepage</dt>
<dd> &lt;<a rel="nofollow" href="http://www.claws-mail.org">http://www.claws-mail.org</a>&gt;</dd>
<dt>Claws Mail online manual</dt>
<dd> &lt;<a rel="nofollow" href="http://www.claws-mail.org/manual">http://www.claws-mail.org/manual</a>&gt;</dd>
<dt>Claws Mail plugins</dt>
<dd> &lt;<a rel="nofollow" href="http://www.claws-mail.org/plugins.php">http://www.claws-mail.org/plugins.php</a>&gt; </dd>
</dl>
