---
title: "gajim-remote(1)"
name: "gajim-remote"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gajim-remote/"
description: "gajim-remote – a remote control utility for"
---

<h2 class="name">NAME</h2>
<p> <code>gajim-remote</code> &#8211; a remote control utility for </p>
<p><a href="/docs/linux/man/1-gajim/">gajim</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> is a script to control and communicate with a running instance of <a href="/docs/linux/man/1-gajim/">gajim</a>(1) by D-Bus.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>Available commands</code></p>
<dd></dl>
<h3>account_info Aq account</h3>
<p> Gets detailed info on a account</p>
<h3>add_contact Ao jid Ac Bq account</h3>
<p> Adds contact to roster</p>
<h3>change_avatar Ao picture Ac Bq account</h3>
<p> Change the avatar</p>
<h3>change_status Bo status Bc Bo message Bc Bq account</h3>
<p> Changes the status of account or accounts</p>
<h3>check_gajim_running</h3>
<p> Check if Gajim is running</p>
<h3>contact_info Aq jid</h3>
<p> Gets detailed info on a contact</p>
<h3>get_status Bq account</h3>
<p> Returns current status (the global one unless account is specified)</p>
<h3>get_status_message Bq account</h3>
<p> Returns current status message (the global one unless account is specified)</p>
<h3>get_unread_msgs_number</h3>
<p> Returns number of unread messages</p>
<h3>handle_uri Ao uri Ac Bo account Bc Bq message</h3>
<p> Handle a xmpp:/ uri</p>
<h3>help Bq command</h3>
<p> Shows a help on specific command</p>
<h3>join_room Ao room Ac Bo nick Bc Bo password Bc Bq account</h3>
<p> Join a MUC room</p>
<h3>list_accounts</h3>
<p> Prints a list of registered accounts</p>
<h3>list_contacts Bq account</h3>
<p> Prints a list of all contacts in the roster. Each contact appears on a separate line</p>
<h3>open_chat Ao jid Ac Bo account Bc Bq message</h3>
<p> Shows the chat dialog so that you can send messages to a contact</p>
<h3>prefs_del Aq key</h3>
<p> Deletes a preference item</p>
<h3>prefs_list</h3>
<p> Lists all preferences and their values</p>
<h3>prefs_put Aq key=value</h3>
<p> Sets value of &#8216;key&#8217; to &#8216;value&#8217;.</p>
<h3>prefs_store</h3>
<p> Writes the current state of Gajim preferences to the .config file</p>
<h3>remove_contact Ao jid Ac Bq account</h3>
<p> Removes contact from roster</p>
<h3>send_chat_message Ao jid Ac Ao message Ac Bo pgp key Bc Bq account</h3>
<p> Sends new chat message to a contact in the roster. Both OpenPGP key and account are optional. If you want to set only &#8216;account&#8217;, without &#8216;OpenPGP key&#8217;, just set &#8216;OpenPGP key&#8217; to &#8221;.</p>
<h3>send_file Ao file Ac Ao jid Ac Bq account</h3>
<p> Sends file to a contact</p>
<h3>send_groupchat_message Ao room_jid Ac Ao message Ac Bq account</h3>
<p> Sends new message to a groupchat you&#8217;ve joined.</p>
<h3>send_single_message Ao jid subject Ac Ao message Ac Bo pgp key Bc Bq account</h3>
<p> Sends new single message to a contact in the roster. Both OpenPGP key and account are optional. If you want to set only &#8216;account&#8217;, without &#8216;OpenPGP key&#8217;, just set &#8216;OpenPGP key&#8217; to &#8221;.</p>
<h3>send_xml Ao xml Ac Bq account</h3>
<p> Sends custom XML</p>
<h3>set_priority Ao priority Ac Bq account</h3>
<p> Changes the priority of account or accounts</p>
<h3>show_next_pending_event</h3>
<p> Pops up a window with the next pending event</p>
<h3>start_chat Aq account</h3>
<p> Opens &#8216;Start Chat&#8217; dialog</p>
<h3>toggle_ipython</h3>
<p> Shows or hides the ipython window</p>
<h3>toggle_roster_appearance</h3>
<p> Shows or hides the roster window</p>
<h2>EXAMPLES</h2>
<p> Open a URI of group chat gajim </p>
<blockquote><p><tt>$ gajim-remote handle_uri xmpp:gajim [at] conferenc.gajim.org?join</tt></p></blockquote>
<p> Send custom XML </p>
<blockquote><p><tt>$ gajim-remote send_xml $(cat filename.xml ) Qq </tt>your [at] jabber.id </p></blockquote>
<h2>AUTHORS</h2>
<p> An -nosplit is written and maintained by An Yann Leboulanger , and An Denis Fomin , with contributions and patches merged from many individuals around the world. See files AUTHORS and THANKS for a complete list.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003-2015 Gajim Team </p>
<p> is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; version 3 only. </p>
<p> is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with <code>.</code> If not, see &lt;<a rel="nofollow" href="https://www.gnu.org/licenses/">https://www.gnu.org/licenses/</a>&gt;.</p>
<h2>FEEDBACK</h2>
<p> You can report bugs or feature requests in our bug tracker at <i>trac.gajim.org</i> or in the <i>gajim-devel</i> mailing list; if you want to send us a patch, please do so in our bug tracker. You can also find us in our chat room.</p>
<h2>WWW</h2>
<p> <a rel="nofollow" href="https://www.gajim.org/">https://www.gajim.org/</a></p>
<h2>XMPP</h2>
<p> You are welcome to join us at gajim [at] conference.gajim.org</p>
<h2>MAILING LIST</h2>
<p> Below are public mailing lists on lists.gajim.org </p>
<blockquote>
<pre>
<a rel="nofollow" href="https://lists.gajim.org/cgi-bin/listinfo/gajim-devel">https://lists.gajim.org/cgi-bin/listinfo/gajim-devel</a>
<a rel="nofollow" href="https://lists.gajim.org/cgi-bin/listinfo/translators">https://lists.gajim.org/cgi-bin/listinfo/translators</a>
</pre>
</blockquote>
<p> More mailing lists at </p>
<blockquote>
<pre>
<a rel="nofollow" href="https://lists.gajim.org/cgi-bin/listinfo">https://lists.gajim.org/cgi-bin/listinfo</a>
</pre>
</blockquote>
<h2>BUGS</h2>
<p> Please submit bugs at <a rel="nofollow" href="https://trac.gajim.org/">https://trac.gajim.org/</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gajim/">gajim</a>(1) gajim-history-manager1 </p>
<h2>Index</h2>
