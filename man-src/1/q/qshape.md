---
title: "qshape(1)"
name: "qshape"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qshape/"
description: "qshape – Print Postfix queue domain and age distribution"
---

<h2 class="name">NAME</h2>
<p> qshape &#8211; Print Postfix queue domain and age distribution </p>
<h2>SYNOPSIS</h2>
<p> <code>qshape</code> [<code>-s</code>] [<code>-p</code>] [<code>-m </code><i>min_subdomains</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-b&nbsp;</code><i>bucket_count</i>]&nbsp;[<code>-t&nbsp;</code><i>bucket_time</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-l</code>]&nbsp;[<code>-w&nbsp;</code><i>terminal_width</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-N&nbsp;</code><i>batch_msg_count</i>]&nbsp;[<code>-n&nbsp;</code><i>batch_top_domains</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-c&nbsp;</code><i>config_directory</i>]&nbsp;[<i>queue_name</i>&nbsp;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>qshape</code> program helps the administrator understand the Postfix queue message distribution in time and by sender domain or recipient domain. The program needs read access to the queue directories and queue files, so it must run as the superuser or the <code>mail_owner</code> specified in <code>main.cf</code> (typically <code>postfix</code>). </p>
<p> Options:</p>
<dl>
<dt><code>-s</code></p>
<dd> Display the sender domain distribution instead of the recipient domain distribution. By default the recipient distribution is displayed. There can be more recipients than messages, but as each message has only one sender, the sender distribution is a message distribution.</p>
<dt><code>-p</code></p>
<dd> Generate aggregate statistics for parent domains. Top level domains are not shown, nor are domains with fewer than <i>min_subdomains</i> subdomains. The names of parent domains are shown with a leading dot, (e.g. <i>.example.com</i>).</p>
<dt><code>-m </code><i>min_subdomains</i></p>
<dd> When used with the <code>-p</code> option, sets the minimum subdomain count needed to show a separate line for a parent domain. The default is 5.</p>
<dt><code>-b </code><i>bucket_count</i></p>
<dd> The age distribution is broken up into a sequence of geometrically increasing intervals. This option sets the number of intervals or &quot;buckets&quot;. Each bucket has a maximum queue age that is twice as large as that of the previous bucket. The last bucket has no age limit.</p>
<dt><code>-t </code><i>bucket_time</i></p>
<dd> The age limit in minutes for the first time bucket. The default value is 5, meaning that the first bucket counts messages between 0 and 5 minutes old.</p>
<dt><code>-l</code></p>
<dd> Instead of using a geometric age sequence, use a linear age sequence, in other words simple multiples of <code>bucket_time</code>. </p>
<p> This feature is available in Postfix 2.2 and later.</p>
<dt><code>-w </code><i>terminal_width</i></p>
<dd> The output is right justified, with the counts for the last bucket shown on the 80th column, the <i>terminal_width</i> can be adjusted for wider screens allowing more buckets to be displayed without truncating the domain names on the left. When a row for a full domain name and its counters does not fit in the specified number of columns, only the last 17 bytes of the domain name are shown with the prefix replaced by a &#8216;+&#8217; character. Truncated parent domain rows are shown as &#8216;.+&#8217; followed by the last 16 bytes of the domain name. If this is still too narrow to show the domain name and all the counters, the terminal_width limit is violated.</p>
<dt><code>-N </code><i>batch_msg_count</i></p>
<dd> When the output device is a terminal, intermediate results are shown each &quot;batch_msg_count&quot; messages. This produces usable results in a reasonable time even when the deferred queue is large. The default is to show intermediate results every 1000 messages.</p>
<dt><code>-n </code><i>batch_top_domains</i></p>
<dd> When reporting intermediate or final results to a termainal, report only the top &quot;batch_top_domains&quot; domains. The default limit is 20 domains.</p>
<dt><code>-c </code><i>config_directory</i></p>
<dd> The <code>main.cf</code> configuration file is in the named directory instead of the default configuration directory.</dl>
<p> Arguments:</p>
<dl>
<dt><i>queue_name</i></p>
<dd> By default <code>qshape</code> displays the combined distribution of the incoming and active queues. To display a different set of queues, just list their directory names on the command line. Absolute paths are used as is, other paths are taken relative to the <code>main.cf</code> <code>queue_directory</code> parameter setting. While <code>main.cf</code> supports the use of <i>$variable</i> expansion in the definition of the <code>queue_directory</code> parameter, the <code>qshape</code> program does not. If you must use variable expansions in the <code>queue_directory</code> setting, you must specify an explicit absolute path for each queue subdirectory even if you want the default incoming and active queue distribution.</dl>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-mailq/">mailq</a>(1), List all messages in the queue.
QSHAPE_README Examples and background material.
</pre>
<h2>FILES</h2>
<pre>
$config_directory/main.cf, Postfix installation parameters.
$queue_directory/maildrop/, local submission directory.
$queue_directory/incoming/, new message queue.
$queue_directory/hold/, messages waiting for tech support.
$queue_directory/active/, messages scheduled for delivery.
$queue_directory/deferred/, messages postponed for later delivery.
</pre>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>AUTHOR(S)</h2>
<pre>
Victor Duchovni
Morgan Stanley
</pre>
<h2>Index</h2>
