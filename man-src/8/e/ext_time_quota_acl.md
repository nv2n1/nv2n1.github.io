---
title: "ext_time_quota_acl(8)"
name: "ext_time_quota_acl"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ext_time_quota_acl/"
description: "ext_time_quota_acl – Squid time quota external acl helper."
---

<p>ext_time_quota_acl &#8211; Squid time quota external acl helper. </p>
<p> Version 1.0</p>
<h2>Synopsis</h2>
<p><code>ext_time_quota_acl</code> <code>[-b database] [-l logfile] [-d] [-p pauselen] [-h] configfile</code></p>
<h2>Description</h2>
<p><code>ext_time_quota_acl</code> allows an administrator to define time budgets for the users of squid to limit the time using squid. </p>
<p> This is useful for corporate lunch time allocations, wifi portal pay-per-minute installations or for parental control of children. The administrator can define a time budget (e.g. 1 hour per day) which is enforced through this helper.</p>
<h2>Options</h2>
<dl>
<dt><code>-b database</code></p>
<dd><code>Filename</code> of persistent database. This defaults to ext_time_quota.db in Squids state directory.</p>
<dt><code>-p pauselen</code></p>
<dd><code>Pauselen</code> is given in seconds and defines the period between two requests to be treated as part of the same session. Pauses shorter than this value will be counted against the quota, longer ones ignored. Default is 300 seconds (5 minutes).</p>
<dt><code>-l logfile</code></p>
<dd><code>Filename</code> where all logging and debugging information will be written. If none is given, then stderr will be used and the logging will go to Squids main cache.log.</p>
<dt><code>-d</code></p>
<dd>Enables debug logging in the logfile.</p>
<dt><code>-h</code></p>
<dd>show a short command line help.</p>
<dt><code>configfile</code></p>
<dd>This file contains the definition of the time budgets for the users.</dl>
<h2>Configuration</h2>
<p>The time quotas of the users are defined in a text file typically residing in /etc/squid/time_quota. Any line starting with &quot;#&quot; contains a comment and is ignored. Every line must start with a user followed by a time budget and a corresponding time period separated by &quot;/&quot;. Here is an example file: </p>
<dl>
<dd># user budget / period<br />
 <code>john 8h / 1d</code><br />
 <code>littlejoe 1h / 1d</code><br />
 <code>babymary 30m / 1w</code>
</dl>
<p> John has a time budget of 8 hours every day, littlejoe is only allowed 1 hour and the poor babymary only 30 minutes a week. </p>
<p> You can use &quot;s&quot; for seconds, &quot;m&quot; for minutes, &quot;h&quot; for hours, &quot;d&quot; for days and &quot;w&quot; for weeks. Numerical values can be given as integer values or with a fraction. E.g. &quot;0.5h&quot; means 30 minutes. </p>
<p> This helper is configured in <code>squid.conf </code> using the <code>external_acl_type </code> directive then access controls which use it to allow or deny. </p>
<p> Here is an example. </p>
<dl>
<dd># Ensure that users have a valid login. We need their username. </p>
<p> <code>acl users proxy_auth REQUIRED</code><br />
 <code>http_access deny !users</code><br />
 # Define program and quota file<br />
 <code>external_acl_type time_quota ttl=60 children-max=1 %LOGIN /usr/libexec/ext_time_quota_acl /etc/squid/time_quota</code> </p>
<p> <code>acl noquota src all</code><br />
 <code>acl time_quota external time_quota</code><br />
 <code>deny_info ERR_ACL_TIME_QUOTA_EXCEEDED noquota</code><br />
 <code>http_access deny !time_quota noquota</code></dl>
<p> In this example, after restarting Squid it should allow access only for users as long as they have time budget left. If the budget is exceeded the user will be presented with an error page informing them. </p>
<p> In this example we use separate <code>users </code> access control and <code>noquota </code> ACL in order to keep the username and password prompt and the quota-exceeded messages separated. </p>
<p> User is just a unique key value. The above example uses %LOGIN and the username but any of the <code>external_acl_type </code> format tags can be substituted in its place. <code>%EXT_TAG</code> , <code>%LOGIN</code> , <code>%IDENT</code> , <code>%EXT_USER</code> , <code>%SRC </code> , <code>%SRCEUI48</code> , and <code>%SRCEUI64</code> are all likely candidates for client identification. The Squid wiki has more examples at <a rel="nofollow" href="http://wiki.squid-cache.org/ConfigExamples.">http://wiki.squid-cache.org/ConfigExamples.</a></p>
<h2>Limitations</h2>
<p>This helper only controls access to the Internet through HTTP. It does not control other protocols, like VOIP, ICQ, IRC, FTP, IMAP, SMTP or SSH. </p>
<p> Desktop browsers are typically able to deal with authentication to HTTP proxies like <code>squid . </code> But more and more different programs and devices (smartphones, games on mobile devices, &#8230;) are using the Internet over HTTP. These devices are often not able to work through an authenticating proxy. Means other than %LOGIN authentication are required to authorize these devices and software. </p>
<p> A more general control to Internet access could be a captive portal approach (such as pfSense or ChilliSpot) using %SRC, %SRCEUI48 and %SRCEUI64 as keys or maybe a 802.11X solution. But the latter is often not supported by mobile devices.</p>
<h2>Implementation</h2>
<p>When the helper is called it will be asked if the current user is allowed to access squid. The helper will reduce the remaining time budget of this user and return <code>OK </code> if there is budget left. Otherwise it will return <code>ERR .</code> </p>
<p> The <code>ttl=N </code> parameter in <code>squid.conf </code> determines how often the helper will be called, the example config uses a 1 minute TTL. The interaction is that Squid will only call the helper on new requests <code>if</code> there has been more than TTL seconds passed since last check. This handling creates an amount of slippage outside the quota by whatever amount is configured. TTL can be set as short as desired, down to and including zero. Though values of 1 or more are recommended due to a quota resolution of one second. </p>
<p> If the configured time period (e.g. &quot;1w&quot; for babymary) is over, the time budget will be restored to the configured value thus allowing the user to access squid with a fresh budget. </p>
<p> If the time between the current request and the previous request is greater than <code>pauselen</code> (default 5 minutes and adjustable with command line parameter <code>-p</code> ), the current request will be considered as a new request and the time budget will not be decreased. If the time is less than <code>pauselen </code> , then both requests will be considered as part of the same active time period and the time budget will be decreased by the time difference. This allows the user to take arbitrary breaks during Internet access without losing their time budget.</p>
<h2>Further Ideas</h2>
<p>The following ideas could further improve this helper. Maybe someone wants to help? Any support or feedback is welcome!</p>
<dl>
<dt>There should be a way for a user to see their configured and remaining</p>
<dd>time budget. This could be realized by implementing a web page accessing the database of the helper showing the corresponding data. One of the problems to be solved is user authentication.</p>
<dt>We could always return &quot;OK&quot; and use the module simply as an Internet</p>
<dd>usage tracker showing who has stayed how long in the WWW.</dl>
<h2>Author</h2>
<p>This program and documentation was written by <i>Dr. Tilmann Bubeck &lt;t.bubeck [at] reinform.de&gt;</i></p>
<h2>Copyright</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br />
&nbsp;<wbr>*<br />
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br />
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br />
&nbsp;<wbr>*&nbsp;<wbr>Please see the COPYING and CONTRIBUTORS files for details. </p>
<p> This program and documentation is copyright to the authors named above. </p>
<p> Distributed under the GNU General Public License (GNU GPL) version 2 or later (GPLv2+).</p>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list</i> &lt;squid-users [at] squid-cache.org&gt;</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
