---
title: "sortm(1)"
name: "sortm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sortm/"
description: "sortm – sort messages"
---

<h2 class="name">NAME</h2>
<p> sortm &#8211; sort messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>sortm</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-all</code> | <code>-noall</code>] [<code>-datefield</code> <i>field</i>] [<code>-textfield</code> <i>field</i>] [<code>-notextfield</code>] [<code>-limit</code> <i>days</i>] [<code>-nolimit</code>] [<code>-check</code> | <code>-nocheck</code>] [<code>-verbose</code> | <code>-noverbose</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Sortm</code></p>
<dd>sorts the specified messages in the named folder according to the chronological order of the &#8220;Date:&#8221; field of each message. </p>
<p> If no messages are specified, the default is all messages in the folder. However, if no messages are specified and the <code>-noall</code> switch is enabled, then <code>sortm</code> reports that as an error and exits with non-zero status. <code>-noall</code> is most useful in the user&#8217;s profile, to avoid inadvertant sorting of an entire folder. The <code>-all</code> switch can then be used on the command line to disable it. Of course, a message specification of <i>all</i> can be used in any case. </p>
<p> The <code>-verbose</code> switch directs <code>sortm</code> to tell the user the general actions that it is taking to place the folder in sorted order. </p>
<p> The <code>-datefield</code> <i>field</i> switch tells <code>sortm</code> the name of the field to use when making the date comparison. If the user has a special field in each message, such as &#8220;BB-Posted:&#8221; or &#8220;Delivery-Date:&#8221;, then the <code>-datefield</code> switch can be used to direct <code>sortm</code> which field to examine. </p>
<p> The <code>-textfield</code> <i>field</i> switch causes <code>sortm</code> to sort messages by the specified text field. All characters except letters and numbers are stripped and the resulting strings are sorted datefield-major, textfield-minor, using a case insensitive comparison. If this field is &#8220;subject&#8221;, any leading &quot;re:&quot; is stripped off. </p>
<p> With <code>-textfield</code> <i>field</i>, if <code>-limit</code> <i>days</i> is specified, messages with the same textfields that are dated within `days&#8217; of each other appear together. Specifying <code>-nolimit</code> makes the limit infinity. With <code>-limit</code> <i>0</i>, the sort is instead simply textfield-major. </p>
<p> For example, to order a folder by date-major, grouping messages with the same subject on the same date together, use: </p>
<dl>
<dt>
<dd> sortm -textfield subject +folder</dl>
<p> <code>sortm</code> always issues a warning for each message that is missing a &#8220;Date:&#8221; field, has a &#8220;Date:&#8221; field that cannot be parsed, or has a format error in any header field. With the <code>-check</code> switch, <code>sortm</code> inhibits all modifications to the folder if there are any such messages, and exits with non-zero status. With the default of <code>-nocheck</code>, <code>sortm</code> sorts messages with a missing or invalid &#8220;Date:&#8221; field using their file modification times. </p>
<p> When ordering messages based on their dates, if they have the same dates, their original message order is preserved.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-folder/">folder</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msgs' defaults to all without -noall, no default with -noall</code>
`<code>-all</code>'
`<code>-datefield</code>' defaults to date
`<code>-notextfield</code>'
`<code>-noverbose</code>'
`<code>-nolimit</code>'
`<code>-nocheck</code>'
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder. If the current message is moved, <code>sortm</code> will preserve its status as current.</p>
<h2>HISTORY</h2>
<p> Timezones used to be ignored when comparing dates: they aren&#8217;t any more. </p>
<p> Messages which were in the folder, but not specified by `msgs&#8217;, used to be moved to the end of the folder; now such messages are left untouched. </p>
<p> <code>Sortm</code> sometimes did not preserve the message numbering in a folder (e.g., messages 1, 3, and 5, might have been renumbered to 1, 2, 3 after sorting). This was a bug, and has been fixed. To compress the message numbering in a folder, use &#8220;<code>folder -pack</code>&#8221; as always.</p>
<h2>BUGS</h2>
<p> When <code>sortm</code> complains about a message which it can&#8217;t temporally order, it complains about the message number <code>prior</code> to sorting. It should indicate what the message number will be <code>after</code> sorting. </p>
<h2>Index</h2>
