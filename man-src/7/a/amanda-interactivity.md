---
title: "amanda-interactivity(7)"
name: "amanda-interactivity"
section: "7"
letter: "a"
url: "/docs/linux/man/7-amanda-interactivity/"
description: "amanda-interactivity – Configuring Interactivity with Amanda Amanda"
---

<p>amanda-interactivity &#8211; Configuring Interactivity with Amanda Amanda</p>
<h2>Description</h2>
<p>Amanda uses interactivity to ask user to load specific volumes when they are needed. This manual page describes the interactivity modules included with Amanda. </p>
<p> This is a <i>user-level</i> description of the API, and does not address details that are only of concern to developers of new interactivity plugins. For that purpose, consult the Amanda source code, perldoc &#8216;Amanda::Interactivity&#8217; and <a rel="nofollow" href="http://wiki.zmanda.com.">http://wiki.zmanda.com.</a></p>
<h2>Defining Interactivity</h2>
<p>Interactivity is specified in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) as follows: </p>
<pre>define interactivity $interactivity_name {
 comment &quot;$comment&quot;
 plugin &quot;$pluginname&quot;
 property &quot;$PROPERTY_NAME&quot; &quot;$PROPERTY_VALUE&quot;
 ...
}</pre>
<p>and then referenced in the global section as </p>
<pre> interactivity &quot;$interactivity_name&quot;</pre>
<p>Interactivity properties, like Amanda configuration parameters, are insensitive to case, and &#8211; (dash) and _ (underscore) may be used interchangeably. </p>
<p> See the individual plugin sections, below for properties applicable to each plugin.</p>
<h2>Interactivity Modules</h2>
<p>Amanda provides three interactivity modules, <i>tty</i>, <i>email</i> and <i>tty_email</i>.</p>
<h3>Tty</h3>
<p>The <i>tty</i> interactivity module uses the tty to communicate with the user, it works only if a terminal is available, which is the case if amanda is executed from a command line. </p>
<p> When promted for a volume, the user must put the requested volume in the changer and type &lt;enter&gt;. User can type the name of another changer if the volume is available in that changer. Typing &#8216;abort&#8217; will abort the operation.</p>
<h3>Email</h3>
<p>The <i>email</i> interactivity module uses email to send requests to the user, and reads replies from the filesystem. </p>
<p> The <i>email</i> module has many properties: </p>
<p> check-file</p>
<dl>
<dd>If set, amanda will check this file for user input. The user can touch the file to tell amanda that the requested volume was inserted in the changer. If the user writes the name of a changer into the file, Amanda will use that changer. If the user writes the word &#8216;abort&#8217; into the file, the scan will be aborted.</dl>
<p> check-file-delay</p>
<dl>
<dd>Default: 10. This integer property indicates the time in seconds between each check of the check-file.</dl>
<p> mailto</p>
<dl>
<dd>Default: global value of <code>mailto</code>. The email addresses to which the email should be sent. If multiple addresses are given, they should be separated by spaces.</dl>
<p> resend-delay</p>
<dl>
<dd>Default 0. The time in seconds between emails. Amanda will resend the same email at this frequency, which can be useful if <code>mailto</code> is a pager or phone. If set to 0, only one email is sent.</dl>
<h3>Tty_Email</h3>
<p>The <i>tty_email</i> interactivity module uses the <i>tty</i> module if a terminal is available and uses the <i>email</i> module otherwise. Its properties are a combination of properties from each module.</p>
<h2>Example</h2>
<pre> define interactivity &quot;by-tty-or-email&quot; {
 comment &quot;Send email on runs from cron; use terminal on command line&quot;
 plugin &quot;tty_email&quot;
 property &quot;mailto&quot; &quot;admin1&quot; &quot;admin2&quot; &quot;me [at] home&quot;
 property &quot;resend-delay&quot; &quot;1800&quot; #every 30 minutes
 property &quot;check-file&quot; &quot;/tmp/email_input&quot;
 property &quot;check-file-delay&quot; &quot;10&quot; #every 10 seconds
 }</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
