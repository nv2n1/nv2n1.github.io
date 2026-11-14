---
title: "telegram-cli(8)"
name: "telegram-cli"
section: "8"
letter: "t"
url: "/docs/linux/man/8-telegram-cli/"
description: "telegram-cli – Command-line interface for Telegram messenger"
---

<p><code>telegram-cli</code> &#8211; Command-line interface for Telegram messenger</p>
<h2>Description</h2>
<p><code>telegram-cli</code> -k <i>&lt;public-server-key&gt;</i> By default, the public key is stored in <i>/etc/telegram-cli/server.pub</i><br />
 Remember to put your international area code before the phone number: </p>
<pre><code>{areacode}{cellphonenumber}</code></pre>
<p> e.g. for Italy: +391234567890<br />
&nbsp;<wbr>Telegram messenger is a cloud-based instant messaging designed for<br />
&nbsp;<wbr>smart phones and similar to Whatsapp but more flexible, and<br />
&nbsp;<wbr>powerful. You can send messages, photos, videos and documents to<br />
&nbsp;<wbr>people who are in your phone contacts&nbsp;<wbr>(and have Telegram). Telegram<br />
&nbsp;<wbr>also supports secret chats whose provide a private&nbsp;<wbr>(encrypted)&nbsp;<wbr>way of<br />
&nbsp;<wbr>communication. This package contains a command-line based client for Telegram with the following features:<br />
&nbsp;<wbr>*&nbsp;<wbr>Colored terminal messages.<br />
&nbsp;<wbr>*&nbsp;<wbr>Message management: history, stats, etc.<br />
&nbsp;<wbr>*&nbsp;<wbr>Group chat: create and manage groups.<br />
&nbsp;<wbr>*&nbsp;<wbr>Secret chat: secured and encrypted conversations.<br />
&nbsp;<wbr>*&nbsp;<wbr>Contact management: add/edit/remove contacts.<br />
&nbsp;<wbr>*&nbsp;<wbr>Multimedia support: send/load photos and videos. <code>Supported commands</code></p>
<dl>
<dd><code>* Messaging</code> <code>msg </code><i>&lt;peer&gt;</i> Text &#8211; Sends message to this peer<br />
 <code>fwd </code><i>&lt;user&gt;</i> <i>&lt;msg-seqno&gt;</i> &#8211; Forward message to user. You can see message numbers starting client with -N<br />
 <code>chat_with_peer </code><i>&lt;peer&gt;</i> &#8211; Starts one on one chat session with this peer. <i>/exit</i> or <i>/quit</i> to end this mode<br />
 <code>add_contact </code><i>&lt;phone-number&gt;</i> <i>&lt;first-name&gt;</i> <i>&lt;last-name&gt;</i> &#8211; Tries to add contact to contact-list by phone<br />
 <code>rename_contact</code> <i>&lt;user&gt;</i> <i>&lt;first-name&gt;</i> <i>&lt;last-name&gt;</i> &#8211; Tries to rename contact. If you have another device it will be a fight<br />
 <code>mark_read</code> <i>&lt;peer&gt;</i> &#8211; Mark read all received messages with peer<br />
 <code>delete_msg</code> <i>&lt;msg-seqno&gt;</i> &#8211; Deletes message (not completly, though)<br />
 <code>restore_msg</code> <i>&lt;msg-seqno&gt;</i> &#8211; Restores delete message. Impossible for secret chats. Only possible short time (one hour, I think) after deletion <code>* Multimedia</code> <code>send_photo</code> <i>&lt;peer&gt;</i> <i>&lt;photo-file-name&gt;</i> &#8211; Sends photo to peer<br />
 <code>send_video</code> <i>&lt;peer&gt;</i> <i>&lt;video-file-name&gt;</i> &#8211; Sends video to peer<br />
 <code>send_text</code> <i>&lt;peer&gt;</i> <i>&lt;text-file-name&gt;</i> &#8211; Sends text file as plain messages<br />
 <code>load_photo</code>/<code>load_video</code>/<code>load_video_thumb</code>/<code>load_audio</code>/<code>load_document</code>/<code>load_document_thumb</code> <i>&lt;msg-seqno&gt;</i> &#8211; Loads photo/video/audio/document to download dir<br />
 <code>view_photo</code>/<code>view_video</code>/<code>view_video_thumb</code>/<code>view_audio</code>/<code>view_document</code>/<code>view_document_thumb</code> <i>&lt;msg-seqno&gt;</i> &#8211; Loads photo/video to download dir and starts system default viewer<br />
 <code>fwd_media</code> <i>&lt;msg-seqno&gt;</i> &#8211; Send media in your message. Use this to prevent sharing info about author of media (though, it is possible to determine user_id from media itself, it is not possible get access_hash of this user)<br />
 <code>set_profile_photo</code> <i>&lt;photo-file-name&gt;</i> &#8211; Sets userpic. Photo should be square, or server will cut biggest central square part <code>* Group chat options</code> <code>chat_info</code> <i>&lt;chat&gt;</i> &#8211; Prints info about chat<br />
 <code>chat_add_user</code> <i>&lt;chat&gt;</i> <i>&lt;user&gt;</i> &#8211; Add user to chat<br />
 <code>chat_del_user</code> <i>&lt;chat&gt;</i> <i>&lt;user&gt;</i> &#8211; Remove user from chat<br />
 <code>rename_chat</code> <i>&lt;chat&gt;</i> <i>&lt;new-name&gt;</i><br />
 <code>create_group_chat</code> <i>&lt;chat topic&gt;</i> <i>&lt;user1&gt;</i> <i>&lt;user2&gt;</i> <i>&lt;user3&gt;</i> &#8230; &#8211; Creates a groupchat with users, use chat_add_user to add more users<br />
 <code>chat_set_photo</code> <i>&lt;chat&gt;</i> <i>&lt;photo-file-name&gt;</i> &#8211; Sets group chat photo. Same limits as for profile photos. <code>* Search</code> <code>search</code> <i>&lt;peer&gt;</i> pattern &#8211; Searches pattern in messages with peer<br />
 <code>global_search</code> pattern &#8211; Searches pattern in all messages <code>* Secret chat</code> <code>create_secret_chat</code> <i>&lt;user&gt;</i> &#8211; Creates secret chat with this user<br />
 <code>visualize_key</code> <i>&lt;secret_chat&gt;</i> &#8211; Prints visualization of encryption key. You should compare it to your partner&#8217;s one<br />
 <code>set_ttl</code> <i>&lt;secret_chat&gt;</i> <i>&lt;ttl&gt;</i> &#8211; Sets ttl to secret chat. Though client does ignore it, client on other end can make use of it<br />
 <code>accept_secret_chat</code> <i>&lt;secret_chat&gt;</i> &#8211; Manually accept secret chat (only useful when starting with -E key) <code>* Stats and various info</code> <code>user_info</code> <i>&lt;user&gt;</i> &#8211; Prints info about user<br />
 <code>history</code> <i>&lt;peer&gt;</i> [limit] &#8211; Prints history (and marks it as read). Default limit = 40<br />
 <code>dialog_list </code> &#8211; Prints info about your dialogs<br />
 <code>contact_list</code> &#8211; Prints info about users in your contact list<br />
 <code>suggested_contacts</code> &#8211; Print info about contacts, you have max common friends<br />
 <code>stats</code> &#8211; Just for debugging<br />
 <code>show_license</code> &#8211; Prints contents of GPLv2<br />
 <code>help</code> &#8211; Prints this help <code>get_self</code> &#8211; Get our user info <code>* Card</code> <code>export_card</code> &#8211; Print your &#8216;card&#8217; that anyone can later use to import your contact<br />
 <code>import_card</code> <i>&lt;card&gt;</i> &#8211; Gets user by card. You can write messages to him after that <code>* Other</code> <code>quit</code> &#8211; Quit<br />
 <code>safe_quit</code> &#8211; Wait for all queries to end then quit</dl>
<h2>Options</h2>
<p><i>telegram-cli</i> Usage </p>
<p> <code>&#8211;phone</code>/-u Specify username (would not be asked during authorization)</p>
<dl>
<dt><code>&#8211;rsa-key</code>/-k</p>
<dd>Specify location of public key (possible multiple entries)</p>
<dt><code>&#8211;verbosity</code>/-v</p>
<dd>Increase verbosity (0-ERROR 1-WARNIN 2-NOTICE 3+-DEBUG-levels)</p>
<dt><code>&#8211;enable-msg-id</code>/-N</p>
<dd>Message num mode</p>
<dt><code>&#8211;config</code>/-c</p>
<dd>Config file name</p>
<dt><code>&#8211;profile</code>/-p</p>
<dd>Use specified profile</p>
<dt><code>&#8211;log-level</code>/-l</p>
<dd>Log level</p>
<dt><code>&#8211;sync-from-start</code>/-f</p>
<dd>During authorization fetch all messages since registration</p>
<dt><code>&#8211;disable-auto-accept</code>/-E</p>
<dd>disable auto accept of encrypted chats</p>
<dt><code>&#8211;lua-script</code>/-s</p>
<dd>Lua script file</p>
<dt><code>&#8211;wait-dialog-list</code>/-W</p>
<dd>Send dialog_list query and wait for answer before reading input</p>
<dt><code>&#8211;disable-colors</code>/-C</p>
<dd>Disable color output</p>
<dt><code>&#8211;disable-readline</code>/-R</p>
<dd>Disable readline</p>
<dt><code>&#8211;alert</code>/-A</p>
<dd>Enable bell notifications</p>
<dt><code>&#8211;daemonize</code>/-d</p>
<dd>Daemon mode</p>
<dt><code>&#8211;logname</code>/-L &lt;log-name&gt;</p>
<dd>Log file name</p>
<dt><code>&#8211;username</code>/-U &lt;user-name&gt;</p>
<dd>Change uid after start</p>
<dt><code>&#8211;groupname</code>/-G &lt;group-name&gt;</p>
<dd>Change gid after start</p>
<dt><code>&#8211;disable-output</code>/-D</p>
<dd>Disable output</p>
<dt><code>&#8211;tcp-port</code>/-P &lt;port&gt;</p>
<dd>Port to listen for input commands</p>
<dt><code>&#8211;udp-socket</code>/-S &lt;socket-name&gt;</p>
<dd>Unix socket to create</p>
<dt><code>&#8211;exec</code>/-e &lt;commands&gt;</p>
<dd>Make commands end exit</p>
<dt><code>&#8211;disable-names</code>/-I</p>
<dd>Use user and chat IDs in updates instead of names</p>
<dt><code>&#8211;enable-ipv6</code>/-6</p>
<dd>Use ipv6 (may be unstable)</p>
<dt><code>&#8211;help</code>/-h</p>
<dd>Prints this help</p>
<dt><code>&#8211;accept-any-tcp</code></p>
<dd>Accepts tcp connections from any src (only loopback by default)</p>
<dt><code>&#8211;disable-link-preview</code></p>
<dd>Disables server-side previews to links</p>
<dt><code>&#8211;bot</code>/-b</p>
<dd>Bot mode</p>
<dt><code>&#8211;json</code></p>
<dd>Prints answers and values in json format</dl>
<h2>Files</h2>
<p><i>/usr/bin/generate</i><br />
 <i>/usr/bin/telegram-cli</i><br />
 <i>/usr/bin/tl-parser</i> </p>
<p> * <code>Python2 bindings</code> </p>
<p> <i>/usr/bin/generate-2</i> -&gt; <i>/usr/bin/python2.7-generate</i><br />
 <i>/usr/bin/generate-2.7</i> -&gt; <i>/usr/bin/python2.7-generate</i><br />
 <i>/usr/bin/telegram-cli-2.7</i> -&gt; <i>/usr/bin/python2.7-telegram-cli</i><br />
 <i>/usr/bin/telegram-cli-2</i> -&gt; <i>/usr/bin/python2.7-telegram-cli</i><br />
 <i>/usr/bin/tl-parser-2</i> -&gt; <i>/usr/bin/python2.7-tl-parser</i><br />
 <i>/usr/bin/tl-parser-2.7</i> -&gt; <i>/usr/bin/python2.7-tl-parser</i><br />
 <i>/usr/bin/python2.7-tl-parser</i><br />
 <i>/usr/bin/python2.7-telegram-cli</i><br />
 <i>/usr/bin/python2.7-generate</i> </p>
<p> * <code>Python3 bindings</code> </p>
<p> <i>/usr/bin/generate-3</i> -&gt; <i>/usr/bin/python3.x-generate</i><br />
 <i>/usr/bin/generate-3.x</i> -&gt; <i>/usr/bin/python3.x-generate</i><br />
 <i>/usr/bin/telegram-cli-3.x</i> -&gt; <i>/usr/bin/python3.x-telegram-cli</i><br />
 <i>/usr/bin/telegram-cli-3</i> -&gt; <i>/usr/bin/python3.x-telegram-cli</i><br />
 <i>/usr/bin/tl-parser-3</i> -&gt; <i>/usr/bin/python3.x-tl-parser</i><br />
 <i>/usr/bin/tl-parser-3.x</i> -&gt; <i>/usr/bin/python3.x-tl-parser</i><br />
 <i>/usr/bin/python3.x-tl-parser</i><br />
 <i>/usr/bin/python3.x-telegram-cli</i><br />
 <i>/usr/bin/python3.x-generate</i></p>
<h2>Version</h2>
<p>1.3.3</p>
<h2>See Also</h2>
<p>How to contact maintainers: <i><a rel="nofollow" href="https://github.com/vysheng/tg#contacts">https://github.com/vysheng/tg#contacts</a></i></p>
<h2>Bugs</h2>
<p>Bug tracker: <i><a rel="nofollow" href="https://github.com/vysheng/tg/issues">https://github.com/vysheng/tg/issues</a></i></p>
<h2>Author</h2>
<p>Vitaliy Vatman (-@-)</p>
