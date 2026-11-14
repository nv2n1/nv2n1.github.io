---
title: "centerim(1)"
name: "centerim"
section: "1"
letter: "c"
url: "/docs/linux/man/1-centerim/"
description: "centerim – a text mode based IM client for Linux, *BSD, Sun Solaris, MacOS X and possibly, other Unices. ICQ2000, Yahoo!, AIM TOC, IRC, MSN, Gadu-Gadu and Jabber protocols are now supported. Intern..."
---

<h2 class="name">NAME</h2>
<p> <code>centerim</code> &#8211; a text mode based IM client for Linux, *BSD, Sun Solaris, MacOS X and possibly, other Unices. ICQ2000, Yahoo!, AIM TOC, IRC, MSN, Gadu-Gadu and Jabber protocols are now supported. Internal LiveJournal client and RSS reader are also provided.</p>
<h2>SYNOPSIS</h2>
<p> <code>centerim </code> [ <code>option</code> ] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>centerim</code> command. </p>
<p> <code>centerim</code> is a text mode menu- and window-driven IM interface. Currently ICQ2000, Yahoo!, AIM, IRC, MSN, Gadu-Gadu and Jabber protocols are supported. It allows you to send, receive, and forward messages, URLs, SMSes and, contacts, mass message send, search for users (including extended &quot;whitepages search&quot;), view users&#8217; details, maintain your contact list directly from the program (including non-icq contacts), view the messages history, register a new UIN and update your details, be informed on receiving email messages, automatically set away after the defined period of inactivity (on any console), and have your own ignore, visible and invisible lists. It can also associate events with sounds, add events to the outgoing queue from command line, define external event processing actions (like events auto-forwarding or elizatalk), has support for Hebrew and Arabic languages and allows to arrange contacts into groups. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;ascii</code></p>
<dd> use ascii characters to draw lines and boxes</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display command line usage</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> show the program version info</p>
<dt><code>-b</code>, <code>&#8211;basedir</code> &lt;directory&gt;</p>
<dd> specify another base directory; useful for having several IM identities under the same UNIX account</p>
<dt><code>-B</code>, <code>&#8211;bind</code> &lt;hostname/ip&gt;</p>
<dd> tells centerim to use the specified IP address for outgoing connections</p>
<dt><code>-B</code>, <code>&#8211;no-xtitles</code></p>
<dd> disable title changing in xterm or screen</p>
<dt><code>-o</code>, <code>&#8211;offline</code></p>
<dd> start with all protocols set offline </p>
</dl>
<p> The following commands are used to put events to the outgoing queue from the command line. If centerim is already running they&#8217;re to be sent immediately, otherwise they will be sent as soon as you go on-line. </p>
<dl>
<dt><code>-s</code>, <code>&#8211;send</code> &lt;event type&gt;</p>
<dd> This parameter specifies the type of event you want to send. Currently only &quot;msg&quot;, &quot;url&quot; and &quot;sms&quot; are supported.</p>
<dt><code>-p</code>, <code>&#8211;proto</code> &lt;protocol type&gt;</p>
<dd> This one specifies to which IM network the destination contact belongs. Can be &quot;icq&quot;, &quot;yahoo&quot;, &quot;aim&quot;, &quot;irc&quot;, &quot;jab&quot;, &quot;msn&quot;, &quot;gg&quot; or &quot;lj&quot;.</p>
<dt><code>-t</code>, <code>&#8211;to</code> &lt;nickname or UIN&gt;</p>
<dd> With this one you specify nickname or UIN of the destination contact. For icq it&#8217;s possible to specify 0 to send events to yourself. Only SMSes are known to be possible to be sent to oneself though.</p>
<dt><code>-n</code>, <code>&#8211;number</code> &lt;phone number&gt;</p>
<dd> Using this parameter you can send SMSes to any mobile numbers through the ICQ network. </p>
</dl>
<p> The message text is read from the standard input, so use pipes in shell to pass it. For example, you can say &quot;hi&quot; to me through the ICQ network with the following command: </p>
<p>&nbsp;<wbr><code>$&nbsp;<wbr>echo&nbsp;<wbr>&quot;hi&quot;&nbsp;<wbr>| centerim -s msg -p icq -t 17502151</code> </p>
<p> In case you want to send an URL, the URL itself and its description are separated with a newline character the following way: </p>
<p>&nbsp;<wbr><code>$&nbsp;<wbr>echo -e&nbsp;<wbr>&quot;<a rel="nofollow" href="http://thekonst.net/
My">http://thekonst.net/
My</a>&nbsp;<wbr>modest homepage.&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| centerim -s url -p icq -t 17502151</code> </p>
<p> Please note, that all three parameters are required in order to queue an event. </p>
<p> Finally, a small example of sending SMSes: </p>
<p>&nbsp;<wbr><code>$&nbsp;<wbr>echo&nbsp;<wbr>&quot;sms test&quot;&nbsp;<wbr>| centerim -s sms -n 1234567890</code> </p>
<p> It&#8217;s also possible to change your current status on a particular IM network with the following command line option. </p>
<dl>
<dt><code>-S</code>, <code>&#8211;status</code> &lt;status letter&gt;</p>
<dd> The argument parameter is a letter which indicates which status is to be set: o (Online), _ (Offline), a (Away), d (Don&#8217;t disturb), n (N/A), c (Occupied), f (Free for chat), i (Invisible)</p>
<dt><code>-p</code> or <code>&#8211;proto</code> &lt;protocol name&gt;</p>
<dd> Exactly the same like it was described for the previous command. </p>
</dl>
<p> Examples: </p>
<p>&nbsp;<wbr><code>$&nbsp;<wbr>centerim -S&nbsp;<wbr>_&nbsp;<wbr>-p icq</code> </p>
<p> This will set the icq status to offline. In other words, it&#8217;ll be disconnected immediately. </p>
<p>&nbsp;<wbr><code>$&nbsp;<wbr>centerim -S a -p yahoo</code> </p>
<p> And this command will switch your yahoo status to away. </p>
<h2>VERSION</h2>
<p> centerim 4.22.1 </p>
<h2>BUG REPORT</h2>
<p> Report any bugs at our Bugzilla site at <a rel="nofollow" href="http://bugzilla.centerim.org/">http://bugzilla.centerim.org/</a> </p>
<h2>AUTHOR</h2>
<p> This page and centerim was originally written by Konstantin Klyagin. Currently, several people are maintaining this software project. </p>
<h2>WEB</h2>
<p> <a rel="nofollow" href="http://www.centerim.org/">http://www.centerim.org/</a> </p>
<h2>Index</h2>
