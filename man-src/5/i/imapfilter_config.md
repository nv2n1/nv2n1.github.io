---
title: "imapfilter_config(5)"
name: "imapfilter_config"
section: "5"
letter: "i"
url: "/docs/linux/man/5-imapfilter_config/"
description: "imapfilter_config – imapfilter configuration file"
---

<p><code>imapfilter_config</code> &#8211; imapfilter configuration file</p>
<h2>Synopsis</h2>
<p>$HOME/.imapfilter/config.lua</p>
<h2>Description</h2>
<p><a href="/docs/linux/man/1-imapfilter/">imapfilter</a>(1) uses the Lua programming language as a configuration and extension language, therefore the configuration file is a Lua script. </p>
<p> Although knowledge of Lua is not required to use <a href="/docs/linux/man/1-imapfilter/">imapfilter</a>(1), it is nonetheless recommended, especially if one wants to extend it.</p>
<h2>Conventions</h2>
<p>A brief description of the Lua values and types mentioned hereafter in the manual page follows:</p>
<dl>
<dt><code>The</code></p>
<dd>Vt nil is the type of the value &#8220;nil&#8221; whose main property is to be different from any other value; usually it represents the absence of a useful value.</p>
<dt><code>The</code></p>
<dd>Vt boolean is the type of the values &#8220;true&#8221; and &#8220;false&#8221; Both &#8220;nil&#8221; and &#8220;false&#8221; make a condition false; any other value makes it true.</p>
<dt><code>The type</code></p>
<dd>Vt number represents real numbers.</p>
<dt><code>The type</code></p>
<dd>Vt string represents a sequence of characters and can be defined using single quotes, double quotes or double square brackets.</p>
<dt><code>The type</code></p>
<dd>Vt table implements associative arrays, that is, arrays that can be indexed not only with numbers, but with any value.</p>
<dt><code>A</code></p>
<dd>Vt function is a first-class value; it can be stored in variables, passed as argument to other functions, and returned as a result.</dl>
<h2>Options</h2>
<p>Program&#8217;s options are set using an already initialised Vt table named &#8220;options&#8221; in the following manner: </p>
<pre>options.timeout = 120
options.namespace = false
options.charset = 'ISO-8859-1'</pre>
<p>Available options are:</p>
<dl>
<dt><i>cache</i></p>
<dd>When this option is enabled, parts of messages are cached locally in memory to avoid being downloaded more than once. The cache is preserved for the current session only. This variable takes a Vt boolean as a value. Default is &#8220;true&#8221;</p>
<dt><i>certificates</i></p>
<dd>When this option is enabled, the server certificate can be accepted and stored, in order to validate the authenticity of the server in future connections. This variable takes a Vt boolean as a value. Default is &#8220;true&#8221;</p>
<dt><i>charset</i></p>
<dd>Indicates to the server the character set of the strings for the searching methods. This variable takes a Vt string as a value. By default no character set is set, and thus plain ASCII should be assumed by the server.</p>
<dt><i>create</i></p>
<dd>According to the IMAP specification, when trying to write a message to a non-existent mailbox, the server must send a hint to the client, whether it should create the mailbox and try again or not. However some IMAP servers don&#8217;t follow the specification and don&#8217;t send the correct response code to the client. By enabling this option the client tries to create the mailbox, despite of the server&#8217;s response. This variable takes a Vt boolean as a value. Default is &#8220;false&#8221;</p>
<dt><i>close</i></p>
<dd>This option controls whether the currently selected mailbox is implicitly closed at the end of each performed operation, thus removing all messages that are marked deleted. This variable takes a Vt boolean as a value. Default is &#8220;false&#8221;</p>
<dt><i>crammd5</i></p>
<dd>When this option is enabled and the server supports the Challenge-Response Authentication Mechanism (specifically CRAM-MD5), this method will be used for user authentication instead of a plaintext password LOGIN. This variable takes a Vt boolean as a value. Default is &#8220;true&#8221;</p>
<dt><i>expunge</i></p>
<dd>Normally, messages are marked for deletion and are actually deleted when the mailbox is closed. When this option is enabled, messages are expunged immediately after being marked deleted. This variable takes a Vt boolean as a value. Default is &#8220;true&#8221;</p>
<dt><i>info</i></p>
<dd>When this options is enabled, a summary of the program&#8217;s actions is printed, while processing mailboxes. This variable takes a Vt boolean as a value. Default is &#8220;true&#8221;</p>
<dt><i>keepalive</i></p>
<dd>The time in minutes before terminating and re-issuing the IDLE command, in order to keep alive the connection, by resetting the inactivity timeout of the server. A standards compliant server must have an inactivity timeout of at least 30 minutes. But it may happen that some IMAP servers don&#8217;t respect that, or some intermediary network device has a shorter timeout. By setting this option the above problem can be worked around. This variable takes a Vt number as a value. Default is &#8220;29&#8221; minutes.</p>
<dt><i>namespace</i></p>
<dd>When enabled, the program gets the namespace of the user&#8217;s personal mailboxes, and applies automatically the prefix and hierarchy delimiter to any mailboxes residing on the mail server; the user must use the `/&#8217; character as the delimiter and &#8220;(ie. nothing) as the prefix, regardless of the folder&#8221; format of the mail server. This must be disabled, if the user wants to manually specify mailbox names (eg. because they are not part of the user&#8217;s personal namespace mailboxes). This variable takes Vt boolean as a value. Default is &#8220;true&#8221;</p>
<dt><i>recover</i></p>
<dd>With this option it is possible to control the recovery functionality, which restores a session (the connection to the server and the IMAP state at the time), after some unexpected event takes place. Currently there are two types of events that can end abnormally a session, and finally cause the program to terminate: network errors, and the IMAP BYE response which a server can send anytime. When this option is set to &#8220;all&#8221; the recovery function is triggered by both types of events, when set to &#8220;errors&#8221; only in the case of network errors, and when set to &#8220;none&#8221; the mechanism is completely disabled. Default is &#8220;all&#8221;</p>
<dt><i>starttls</i></p>
<dd>When this option is enabled and the server supports the IMAP STARTTLS extension, a TLS connection will be negotiated with the mail server in the beginning of the session. This variable takes a Vt boolean as value. Default is &#8220;true&#8221;</p>
<dt><i>subscribe</i></p>
<dd>By enabling this option new mailboxes that were automatically created, get also subscribed; they are set active in order for IMAP clients to recognize them. This variable takes a Vt boolean as a value. Default is &#8220;false&#8221;</p>
<dt><i>timeout</i></p>
<dd>The time in seconds for the program to wait for a mail server&#8217;s response. If not set, the client will block indefinitely. This variable takes a Vt number as a value. Default is &#8220;60&#8221; seconds.</dl>
<h2>Accounts</h2>
<p>Accounts are initialized using the Fn IMAP function, and the details of the connection are defined using an account Vt table : </p>
<pre>myaccount = IMAP {
 server = 'imap.mail.server',
 username = 'me',
 password = 'secret',
 ssl = 'ssl23'
}</pre>
<p>An account Vt table must have the following elements:</p>
<dl>
<dt><i>server</i></p>
<dd>The hostname of the IMAP server to connect to. It takes a Vt string as a value.</p>
<dt><i>username</i></p>
<dd>User&#8217;s name. It takes a Vt string as a value.</dl>
<p> An account Vt table can also have the following optional elements:</p>
<dl>
<dt><i>password</i></p>
<dd>User&#8217;s secret keyword. If a password wasn&#8217;t supplied the user will be asked to enter one interactively the first time it will be needed. It takes a Vt string as a value.</p>
<dt><i>port</i></p>
<dd>The port to connect to. It takes a Vt number as a value. Default is &#8220;143&#8221; for imap and &#8220;993&#8221; for imaps.</p>
<dt><i>ssl</i></p>
<dd>Forces an imaps connection and specifies the SSL/TLS protocol/version to be used. It takes a Vt string as a value, specifically one of: &#8220;ssl3&#8221; &#8220;ssl23&#8221; &#8220;tls1&#8221; &#8220;tls1.1&#8221; &#8220;tls1.2&#8221;</dl>
<h3>Listing</h3>
<p>The following methods can be used on an account to list mailboxes in a folder of an account: </p>
<dl>
<dt><code>Fn </code>list_all folder</p>
<dd>Lists all the available mailboxes in the Fa folder (Vt string ) and returns a Vt table that contains Vt strings , the available mailboxes, and a Vt table that contains Vt strings , the available folders. </p>
<dt><code>Fn </code>list_subscribed folder</p>
<dd>Lists all the subscribed mailboxes in the Fa folder (Vt string ) and returns a Vt table that contains Vt strings , the subscribed mailboxes, and a Vt table that contains Vt strings , the subscribed folders.</dl>
<p> The following methods can be used on an account to list mailboxes, using wildcards, in a folder of an account. The `*&#8217; wildcard, matches any character and the `%&#8217; matches any character except the folder delimiter, ie. non-recursively: </p>
<dl>
<dt><code>Fn </code>list_all folder mailbox</p>
<dd>Lists all the available mailboxes in the Fa folder (Vt string ) with the name Fa mailbox (Vt string , ) and returns a Vt table that contains Vt strings , the available mailboxes, and a Vt table that contains Vt strings , the available folders. Wildcards may only be used in the Fa mailbox argument. </p>
<dt><code>Fn </code>list_subscribed folder mailbox</p>
<dd>Lists all the subscribed mailboxes in the Fa folder (Vt string ) with the name Fa mailbox (Vt string ) and returns a Vt table that contains Vt strings , the subscribed mailboxes, and a Vt table that contains Vt strings , the subscribed folders. Wildcards may only be used in the Fa mailbox argument.</dl>
<p> Examples: </p>
<pre>mailboxes, folders = myaccount:list_subscribed('myfolder')
mailboxes, folders = myaccount:list_all('myfolder/mysubfolder', '*')</pre>
<h3>Manipulating</h3>
<p>The following methods can be used to manipulate mailboxes in an account: </p>
<dl>
<dt><code>Fn </code>create_mailbox name</p>
<dd>Creates the Fa name (Vt string ) mailbox. </p>
<dt><code>Fn </code>delete_mailbox name</p>
<dd>Deletes the Fa name (Vt string ) mailbox. </p>
<dt><code>Fn </code>rename_mailbox oldname newname</p>
<dd>Renames the Fa oldname (Vt string ) mailbox to Fa newname (Vt string ) </p>
<dt><code>Fn </code>subscribe_mailbox name</p>
<dd>Subscribes the Fa name (Vt string ) mailbox. </p>
<dt><code>Fn </code>unsubscribe_mailbox name</p>
<dd>Unsubscribes the Fa name (Vt string ) mailbox.</dl>
<p> Examples: </p>
<pre>myaccount:create_mailbox('mymailbox')
myaccount:subscribe_mailbox('mymailbox')
myaccount:unsubscribe_mailbox('myfolder/mymailbox')
myaccount:delete_mailbox('myfolder/mymailbox')</pre>
<h2>Mailboxes</h2>
<p>After an IMAP account has been initialized, mailboxes residing in that account can be accessed simply as elements of the account Vt table : </p>
<pre>myaccount.mymailbox</pre>
<p>If mailbox names don&#8217;t only include letters, digits and underscores, or begin with a digit, an alternative form must be used: </p>
<pre>myaccount['mymailbox']</pre>
<p>A mailbox inside a folder can be only accessed by using the alternative form: </p>
<pre>myaccount['myfolder/mymailbox']</pre>
<p>The methods that are available for an account (eg. Fn list_all , Fn create_mailbox , etc.) , are considered keywords and must not be used as mailbox names, and the same also applies for any string starting with an underscore, as they are considered reserved.</p>
<h3>Checking</h3>
<p>The following methods can be used to check the status of a mailbox: </p>
<dl>
<dt><code>Fn </code>check_status</p>
<dd>The Fn check_status method gets the current status of a mailbox, and returns four values of Vt number type: the total number of messages, the number of recent messages, the number of unseen messages in the mailbox, and the next UID to be assigned to a new message in the mailbox. </p>
<dt><code>Fn </code>enter_idle</p>
<dd>The Fn enter_idle method implements the IMAP IDLE (RFC 2177) extension. By using this extension it&#8217;s not necessary to poll the server for changes to the selected mailbox (ie. using the Fn check_status method), but instead the server sends an update when there is a change in the mailbox (eg. in case of new mail). When the Fn enter_idle method has been called no more commands in the configuration file are executed until an update is received, at which point the Fn enter_idle method returns. For the Fn enter_idle to work, the IDLE extension has to be supported by the IMAP server. The Fn enter_idle method returns one value of type Vt boolean : &#8220;true&#8221; if the IDLE extension is supported and there was a update in the mailbox, and &#8220;false&#8221; if the IDLE extension is not supported, in which case the method returns immediately.</dl>
<p> Examples: </p>
<pre>exist, unread, unseen, uidnext = myaccount.mymailbox:check_status()
update = myaccount.mymailbox:enter_idle()</pre>
<h3>Searching</h3>
<p>The searching methods in this subsection can be applied to any mailbox. They return a special form of Vt table , that contains the messages that match the searching method. This Vt table can be combined with other Vt tables using logic theory. There are three available operations, that implement logical &#8220;or&#8221; logical &#8220;and&#8221; and logical &#8220;not&#8221; </p>
<p> The logical &#8220;or&#8221; is implemented using the `+&#8217; operator: </p>
<pre>results = myaccount.mymailbox:is_unseen() +
 myaccount.mymailbox:is_larger(100000)</pre>
<p>The logical &#8220;and&#8221; is implemented using the `*&#8217; operator: </p>
<pre>results = myaccount.mymailbox:is_unseen() *
 myaccount.mymailbox:is_larger(100000)</pre>
<p>The logical &#8220;not&#8221; is implemented using the `-&#8216; operator: </p>
<pre>results = myaccount.mymailbox:is_unseen() -
 myaccount.mymailbox:is_larger(100000)</pre>
<p>The three logical operators can be combined in the same expression. The logical &#8220;and&#8221; has higher precedence than the logical &#8220;or&#8221; and the logical &#8220;not&#8221; with the latter two having the same precedence, and parentheses may be used to change this behaviour: </p>
<pre>results = myaccount.mymailbox:is_unseen() +
 myaccount.mymailbox:is_larger(100000) *
 myaccount.mymailbox:contain_subject('test')
results = ( myaccount.mymailbox:is_unseen() +
 myaccount.mymailbox:is_larger(100000) ) *
 myaccount.mymailbox:contain_subject('test')</pre>
<p>The returned Vt tables of the searching methods can also be stored in variables and then further processed: </p>
<pre>unseen = myaccount.myaccount:is_unseen()
larger = myaccount.mymailbox:is_larger(100000)
subject = myaccount.mymailbox:contain_subject('test')
results = unseen + larger * subject</pre>
<p>A composite filter that includes one or more simple rules can be defined: </p>
<pre>myfilter = function ()
 return myaccount.mymailbox:is_unseen() +
 myaccount.mymailbox:is_larger(100000) *
 myaccount.mymailbox:contain_subject('test')
 end
results = myfilter()</pre>
<p>Composite filters can may be more dynamic by adding arguments: </p>
<pre>myfilter = function (mailbox, size, subject)
 return mailbox:is_unseen() +
 mailbox:is_larger(size) *
 mailbox:contain_subject(subject)
 end
results = myfilter(myaccount.mailbox, 100000, 'test')</pre>
<p>It is also possible to combine the searching methods in different mailboxes, either at the same or different accounts, for example when the same actions will be executed on messages residing in different mailboxes or accounts. </p>
<pre>results = myaccount.mymailbox:is_unseen() +
 myaccount.myothermailbox:is_larger(100000) +
 myotheraccount.myothermailbox:contain_subject('test')</pre>
<p>The following method can be used to get all messages in a mailbox: </p>
<dl>
<dt><code>Fn </code>select_all</p>
<dd>All messages.</dl>
<p> The following methods can be used to search for messages that are in a specific state: </p>
<dl>
<dt><code>Fn </code>is_answered</p>
<dd>Messages that have been answered. </p>
<dt><code>Fn </code>is_deleted</p>
<dd>Messages that are marked for later removal. </p>
<dt><code>Fn </code>is_draft</p>
<dd>Messages that have not completed composition. </p>
<dt><code>Fn </code>is_flagged</p>
<dd>Messages that are flagged for urgent/special attention. </p>
<dt><code>Fn </code>is_new</p>
<dd>Messages that are recently arrived (this session is the first to have been notified about these messages) and have not been read. </p>
<dt><code>Fn </code>is_old</p>
<dd>Messages that are not recently arrived (this session is not the first to have been notified about these messages) and have not been read. </p>
<dt><code>Fn </code>is_recent</p>
<dd>Messages that are recently arrived (this session is the first to have been notified about these messages). </p>
<dt><code>Fn </code>is_seen</p>
<dd>Messages that have been read. </p>
<dt><code>Fn </code>is_unanswered</p>
<dd>Messages that have not been answered. </p>
<dt><code>Fn </code>is_undeleted</p>
<dd>Messages that are not marked for later removal. </p>
<dt><code>Fn </code>is_undraft</p>
<dd>Messages that have completed composition. </p>
<dt><code>Fn </code>is_unflagged</p>
<dd>Messages that are not flagged for urgent/special attention. </p>
<dt><code>Fn </code>is_unseen</p>
<dd>Messages that have not been read.</dl>
<p> The following method can be used to search for messages that have a specific flag set: </p>
<dl>
<dt><code>Fn </code>has_flag keyword</p>
<dd>Messages with the specified keyword flag (Vt string ) set.</dl>
<p> The following methods can be used to search for messages based on their size: </p>
<dl>
<dt><code>Fn </code>is_larger size</p>
<dd>Messages that are larger than the size (Vt number ) in octets (bytes). </p>
<dt><code>Fn </code>is_smaller size</p>
<dd>Messages that are smaller than the size (Vt number ) in octets (bytes).</dl>
<p> The following methods can be used to search for messages based on their age: </p>
<dl>
<dt><code>Fn </code>is_newer age</p>
<dd>Messages that are newer than the Fa age (Vt number ) in days. </p>
<dt><code>Fn </code>is_older age</p>
<dd>Messages that are older than the Fa age (Vt number ) in days.</dl>
<p> The following methods can be used to search for messages based on their arrival or sent date, in the &#8220;day-month-year&#8221; form, where day is the day of the month as a decimal number (01-31), month is the abbreviated month ( &#8220;Jan&#8221; &#8220;Feb&#8221; &#8220;Mar&#8221; &#8220;Apr&#8221; &#8220;May&#8221; &#8220;Jun&#8221; &#8220;Jul&#8221; &#8220;Aug&#8221; &#8220;Sep&#8221; &#8220;Oct&#8221; &#8220;Nov&#8221; &#8220;Dec&#8221; and year is the year as decimal number including the century (eg. 2007): </p>
<dl>
<dt><code>Fn </code>arrived_before date</p>
<dd>messages that have arrived before the Fa date (Vt string ) where Fa date is in the &#8220;day-month-year&#8221; form. </p>
<dt><code>Fn </code>arrived_on date</p>
<dd>Messages that have arrived on the Fa date (Vt string ) where Fa date is in the &#8220;day-month-year&#8221; form. </p>
<dt><code>Fn </code>arrived_since date</p>
<dd>Messages that have arrived after the Fa date (Vt string ) where Fa date is in the &#8220;day-month-year&#8221; form. </p>
<dt><code>Fn </code>sent_before date</p>
<dd>Messages that have been sent before the Fa date (Vt string ) where Fa date is in the &#8220;day-month-year&#8221; form. </p>
<dt><code>Fn </code>sent_on date</p>
<dd>Messages that have been sent on the Fa date (Vt string ) where Fa date is in the &#8220;day-month-year&#8221; form. </p>
<dt><code>Fn </code>sent_since date</p>
<dd>Messages that have been sent after the Fa date (Vt string ) where Fa date is in the &#8220;day-month-year&#8221; form.</dl>
<p> The following methods can be used to search for messages that contain a specific word or phrase: </p>
<dl>
<dt><code>Fn </code>contain_bcc string</p>
<dd>Messages that contain the Fa string (Vt string ) in the &#8220;Bcc&#8221; header field. </p>
<dt><code>Fn </code>contain_cc string</p>
<dd>Messages that contain the Fa string (Vt string ) in the &#8220;Cc header field. &#8221; </p>
<dt><code>Fn </code>contain_from string</p>
<dd>Messages that contain the Fa string (Vt string ) in the &#8220;From&#8221; header field. </p>
<dt><code>Fn </code>contain_subject string</p>
<dd>Messages that contain the Fa string (Vt string ) in the &#8220;Subject&#8221; header field. </p>
<dt><code>Fn </code>contain_to string</p>
<dd>Messages that contain the Fa string (Vt string ) in the &#8220;To header field. &#8221; </p>
<dt><code>Fn </code>contain_field field string</p>
<dd>Messages that contain the Fa string (Vt string ) in the Fa field (Vt string ) header field. </p>
<dt><code>Fn </code>contain_body string</p>
<dd>Messages that contain the Fa string (Vt string ) in the message body. </p>
<dt><code>Fn </code>contain_message string</p>
<dd>Messages that contain the Fa string (Vt string ) in the message.</dl>
<p> The following methods can be used to search for messages that match a specific regular expression pattern. </p>
<p> This way of searching is not supported by the IMAP protocol, and this means that what actually happens under the hood, is that the relevant parts of all the messages are downloaded and matched locally. It is therefore recommended to use these methods with meta-searching (see following section), in order to narrow down the set of messages that should be searched, and thus minimize what will be downloaded. </p>
<p> Note that due to Lua using backslash `\&#8217; as an escape character for its strings, one has to double backslashes in order to insert a single backslash inside a regular expression pattern: </p>
<dl>
<dt><code>Fn </code>match_bcc pattern</p>
<dd>Messages that match the regular expression Fa pattern (Vt string ) in the &#8220;Bcc&#8221; header field. </p>
<dt><code>Fn </code>match_cc pattern</p>
<dd>Messages that match the regular expression Fa pattern (Vt string ) in the &#8220;Cc header field. &#8221; </p>
<dt><code>Fn </code>match_from pattern</p>
<dd>Messages that match the regular expression Fa pattern (Vt string ) in the &#8220;From&#8221; header field. </p>
<dt><code>Fn </code>match_subject pattern</p>
<dd>Messages that match the regular expression Fa pattern (Vt string ) in the &#8220;Subject&#8221; header field. </p>
<dt><code>Fn </code>match_to pattern</p>
<dd>Messages that match the regular expression Fa pattern (Vt string ) in the &#8220;To header field. &#8221; </p>
<dt><code>Fn </code>match_field field pattern</p>
<dd>Messages that match the regular expression Fa pattern (Vt string ) in the Fa field (Vt string ) header field. </p>
<dt><code>Fn </code>match_header pattern</p>
<dd>Messages that match the regular expression Fa pattern (Vt string ) in the message header. </p>
<dt><code>Fn </code>match_body pattern</p>
<dd>Messages that match the regular expression Fa pattern (Vt string ) in the message body. </p>
<dt><code>Fn </code>match_message pattern</p>
<dd>Messages that match the regular expression Fa pattern (Vt string ) in the message.</dl>
<p> The following method can be used to search for messages using user queries based on the IMAP specification (RFC 3501 Section 6.4.4): </p>
<dl>
<dt><code>Fn </code>send_query criteria</p>
<dd>Searches messages by sending an IMAP search query as described in the search Fa criteria (Vt string )</dl>
<p> Examples: </p>
<pre>results = myaccount.mymailbox:select_all()
results = myaccount.mymailbox:is_new()
results = myaccount.mymailbox:is_recent()
results = myaccount.mymailbox:is_larger(100000)
results = myaccount.mymailbox:is_older(10)
results = myaccount.mymailbox:has_flag('MyFlag')
results = myaccount.mymailbox:arrived_before('01-Jan-2007')
results = myaccount.mymailbox:sent_since('01-Jan-2007')
results = myaccount.mymailbox:contain_subject('test')
results = myaccount.mymailbox:contain_field('Sender', 'user [at] host')
results = myaccount.mymailbox:contain_body('hello world')
results = myaccount.mymailbox:match_from('.*(user1|user2)@host')
results = myaccount.mymailbox:send_query('ALL')
results = myaccount['mymailbox']:is_new()
results = myaccount['myfolder/mymailbox']:is_recent()</pre>
<h2>Results</h2>
<p>After one of more searching methods have been applied to one or more mailboxes, the result contains all the necessary information, such as which messages matched in which mailboxes. Using this result these messages can be either searched further or processed in various way.</p>
<h3>Meta-Searching</h3>
<p>The results of the searching methods can be searched further on in the same way as searching is done in mailboxes. The difference is that instead of doing the search in the whole mailbox, ie. in all the messages, it is instead done only to those messages that were returned in a previous search. </p>
<p> Examples: </p>
<pre>results:match_message('^[Hh]ello world!?$')
myaccount.mymailbox:is_new():match_body('^[Ww]orld, hello!?$')</pre>
<h3>Processing</h3>
<p>The processing methods are applied to the results that searching returned. </p>
<p> The following method can be used to delete messages in a mailbox: </p>
<dl>
<dt><code>Fn </code>delete_messages</p>
<dd>Deletes the messages that matched.</dl>
<p> The following methods can be used to copy and move messages in a mailbox at the same or different accounts. If the destination mailbox is in a different account than the source mailbox, then the messages are downloaded and then uploaded to the destination: </p>
<dl>
<dt><code>Fn </code>copy_messages destination</p>
<dd>Copies the messages to the Fa destination , which is a mailbox at an account. </p>
<dt><code>Fn </code>move_messages destination</p>
<dd>Moves the messages to the Fa destination , which is a mailbox at an account.</dl>
<p> The following methods can be used to mark messages in a mailbox: </p>
<dl>
<dt><code>Fn </code>mark_answered</p>
<dd>Marks the messages as answered. </p>
<dt><code>Fn </code>mark_deleted</p>
<dd>Marks the messages for later removal. </p>
<dt><code>Fn </code>mark_draft</p>
<dd>Marks the messages as draft. </p>
<dt><code>Fn </code>mark_flagged</p>
<dd>Marks the messages for urgent/special attention. </p>
<dt><code>Fn </code>mark_seen</p>
<dd>Marks the messages as read. </p>
<dt><code>Fn </code>unmark_answered</p>
<dd>Unmarks the messages that have been marked as answered. </p>
<dt><code>Fn </code>unmark_deleted</p>
<dd>Unmarks the messages that have been marked for later removal. </p>
<dt><code>Fn </code>unmark_draft</p>
<dd>Unmarks the messages that have been marked as draft. </p>
<dt><code>Fn </code>unmark_flagged</p>
<dd>Unmarks the messages that have been marked for urgent/special attention. </p>
<dt><code>Fn </code>unmark_seen</p>
<dd>Unmarks the messages that have been marked as read. </p>
</dl>
<p> The following methods can be used to flag messages in a mailbox. The standard system flags are &#8220;\Answered&#8221; &#8220;\Deleted&#8221; &#8220;\Draft&#8221; &#8220;\Flagged&#8221; &#8220;\Seen&#8221; while if the server supports it, new user keywords may be defined: </p>
<dl>
<dt><code>Fn </code>add_flags flags</p>
<dd>Adds the Fa flags Po Vt table that contains Vt strings Pc to the messages. </p>
<dt><code>Fn </code>remove_flags flags</p>
<dd>Removes the Fa flags Po Vt table that contains Vt strings Pc from the messages. </p>
<dt><code>Fn </code>replace_flags flags</p>
<dd>Replaces the Fa flags Po Vt table that contains Vt strings Pc of the messages.</dl>
<p> Examples: </p>
<pre>results:delete_messages()
results:copy_messages(myaccount.myothermailbox)
results:move_messages(myotheraccount.mymailbox)
results:mark_seen()
results:unmark_flagged()
results:add_flags({ 'MyFlag', '\Seen' })
results:remove_flags({ '\Seen' })
results:move_messages(myotheraccount['myfolder/mymailbox'])</pre>
<h2>Messages</h2>
<p>The messages that are residing in any mailbox can be also accessed, as a whole or in parts. Messages can be accessed using their unique identifier (UID): </p>
<pre>myaccount.mymailbox[22]</pre>
<p>The UIDs of messages the user is interested in, are gained from the results of searching: </p>
<pre>results = account.INBOX:is_unseen()
for _, message in ipairs(results) do
 mailbox, uid = table.unpack(message)
 header = mailbox[uid]:fetch_header()
end</pre>
<h3>Fetching</h3>
<p>The following methods can be used to fetch parts of messages. The methods return a Vt string . The downloaded message parts are cached locally, so they can be reused inside the same program session: </p>
<dl>
<dt><code>Fn </code>fetch_message</p>
<dd>Fetches the header and body of the message. </p>
<dt><code>Fn </code>fetch_header</p>
<dd>Fetches the header of the message. </p>
<dt><code>Fn </code>fetch_body</p>
<dd>Fetches the body of the messages. </p>
<dt><code>Fn </code>fetch_field field</p>
<dd>Fetches the specified header Fa field (Vt string ) of the message. </p>
<dt><code>Fn </code>fetch_part part</p>
<dd>Fetches the specified Fa part (Vt string ) of the message.</dl>
<p> The following methods can be used to fetch details about the state of a message: </p>
<dl>
<dt><code>Fn </code>fetch_flags</p>
<dd>Fetches the flags of the message. Returns a Vt table of Vt strings . </p>
<dt><code>Fn </code>fetch_date</p>
<dd>Fetches the internal date of the message. Returns a Vt string . </p>
<dt><code>Fn </code>fetch_size</p>
<dd>Fetches the size of the message. Returns a Vt number . </p>
<dt><code>Fn </code>fetch_structure</p>
<dd>Fetches the body structure of the message. Returns a Vt table that has as keys the parts of the message, and as values a Vt table that has one mandatory element, the type (Vt string ) of the part, and two optional elements, the size (Vt number ) and name (Vt string ) of the part.</dl>
<h3>Appending</h3>
<p>The following methods can be used to append a message to a mailbox: </p>
<dl>
<dt><code>Fn </code>append_message message</p>
<dd>Appends the Fa message (Vt string ) to the mailbox. </p>
<dt><code>Fn </code>append_message message flags date</p>
<dd>Appends the Fa message (Vt string ) to the mailbox, setting the specified Fa flags Po Vt table of Vt strings Pc , as returned by Fn fetch_flags , and Fa date (Vt string ) as returned by Fn fetch_date .</dl>
<p> Examples: </p>
<pre>myaccount.mymailbox[2]:fetch_message()
myaccount.mymailbox[3]:fetch_field('subject')
myaccount.mymailbox[5]:fetch_part('1.1')
myaccount['mymailbox'][7]:fetch_message()
myaccount['myfolder/mymailbox'][11]:fetch_message()
myaccount.mymailbox:append_message(message)</pre>
<h2>Functions</h2>
<p>The following auxiliary functions are also available for convenience: </p>
<dl>
<dt><code>Fn </code>form_date days</p>
<dd>Forms a date in &#8220;day-month-year&#8221; format that the system had before the number of Fa days (Vt number ) and returns it as a Vt string . </p>
<dt><code>Fn </code>get_password prompt</p>
<dd>Displays the specified Fa prompt (Vt string ) and reads a password, while character echoing is turned off. Returns that password as a Vt string . </p>
<dt><code>Fn </code>become_daemon interval commands</p>
<dd>Detaches the program from the controlling terminal and runs it in the background as system daemon. The program will then repeatedly poll at the specified Fa interval (Vt number ) in seconds. Each time the program wakes up, the Fa commands (Vt function ) are executed. </p>
<dt><code>Fn </code>become_daemon interval commands nochdir noclose</p>
<dd>Detaches the program from the controlling terminal and runs it in the background as system daemon. The program will then repeatedly poll at the specified Fa interval (Vt number ) in seconds. Each time the program wakes up, the Fa commands (Vt function ) are executed. </p>
<p> If Fa nochdir (Vt boolean ) is &#8220;true&#8221; the current working directory is not changed to the root directory (/ ) If Fa noclose (Vt boolean ) is &#8220;true&#8221; the standard input, standard output and standard error are not redirected to /dev/null </p>
<dt><code>Fn </code>pipe_to command data</p>
<dd>Executes the system&#8217;s Fa command (Vt string ) and sends the Fa data (Vt string ) to the standard input channel of the subprocess. Returns a Vt number , the exit status of the child process. </p>
<dt><code>Fn </code>pipe_from command</p>
<dd>Executes the system&#8217;s Fa command (Vt string ) and retrieves the data from the standard output channel of the subprocess. Returns a Vt number , the exit status of the child process, and a Vt string , the output of the child process. </p>
<dt><code>Fn </code>regex_search pattern string</p>
<dd>Implements Perl-compatible regular expressions (PCRE). The Fa pattern (Vt string ) is a PCRE pattern. The Vt string (Vt string ) is the subject string in which the pattern is matched against. Returns at least a Vt boolean , that denotes if the match was successful, and any captures which are of Vt string type. Note that due to Lua using backslash `\&#8217; as an escape character for its strings, one has to double backslashes in order to insert a single backslash inside a regular expression pattern.</dl>
<p> Examples: </p>
<pre>date = form_date(14)
password = get_password('Enter password: ')
become_daemon(600, myfunction)
status = pipe_to('mycommandline', 'mydata')
status, data = pipe_from('mycommandline')
success, capture = regex_search('^[PpCcRrEe]: (\w)$', 'mystring')</pre>
<h2>Examples</h2>
<p>See samples/config.lua and samples/extend.lua in the source code distribution.</p>
<h2>Environment</h2>
<dl>
<dt><code>HOME</code></p>
<dd>User&#8217;s home directory.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-imapfilter/">imapfilter</a>(1) </p>
