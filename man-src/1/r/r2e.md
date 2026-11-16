---
title: "r2e(1)"
name: "r2e"
section: "1"
letter: "r"
url: "/docs/linux/man/1-r2e/"
description: "r2e – receive RSS feeds by email"
---

<h2>NAME</h2>
<p> r2e &#8211; receive RSS feeds by email</p>
<h2>SYNOPSIS</h2>
<p> <code>r2e action [options]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>r2e</code> is a simple program which you can run in your crontab. It watches RSS feeds and sends you a nicely formatted email message for each new item. </p>
<p> The program is configured by ~/.rss2email/config.py </p>
<p> For a quick start with r2e, try these steps: </p>
<dl>
<dt>
</dt><dd>
<pre>
<code>r2e new </code><i>your [at] address</i>
<code>r2e add </code><i><a rel="nofollow" href="http://feed.url/somewhere.rss">http://feed.url/somewhere.rss</a></i>
<code>r2e run </code>
</dd></dl>
The last command should eventually be put into your crontab, if you
want things be sent you automatically.
It is possible to use authenticated feeds using the following syntax:
<dl><dt></dt><dd><code>r2e add </code><i><a rel="nofollow" href="http://user:password@example.com/feed">http://user:password@example.com/feed</a></i>
</dd></dl>
</pre>
<h2>ACTIONS</h2>
<dl>
<dt><code>new [youremail]</code></dt>
<dd> Create a new feedfile. If the second option is specified, it sets the default email address that mails are sent to.</dd>
<dt><code>add url [youremail]</code></dt>
<dd> Subscribe to a feed. The first option is the URL of the feed. The optional second option is the email address to send new items to. Repeat for each feed you want to subscribe to.</dd>
<dt><code>run [&#8211;no-send] [num]</code></dt>
<dd> Scan the feeds and send emails for new items. This can be run in a cron job.</dd></dl>
<p> The &#8211;no-send option stops r2e from sending any email. This can be useful the first time you run it, as otherwise it would send every available story. </p>
<p> If a number is specified, r2e will only download that feed. The list command lists the feed numbers.</p>
<dl>
<dt><code>email yournewemail</code></dt>
<dd> Change the default email address.</dd>
<dt><code>list</code></dt>
<dd> List all your currently subscribed feeds.</dd>
<dt><code>delete n</code></dt>
<dd> Delete a feed, using its number from the list command.</dd>
<dt><code>pause n</code></dt>
<dd> Temporarily ignore a feed. A paused feed won&#8217;t be updated at all.</dd>
<dt><code>unpause n</code></dt>
<dd> Re-enable updates from a feed.</dd>
<dt><code>opmlimport url</code></dt>
<dd> Import feeds from an OPML file.</dd>
<dt><code>opmlexport</code></dt>
<dd> Export feeds to standard output, as an OPML file.</dd></dl>
<h2>CONFIGURATION</h2>
<p> The program&#8217;s behavior can be controlled via the ~/.rss2email/config.py config file. The file is a python file, so variables are set using a syntax like this: VARIABLE = &quot;value&quot; </p>
<p> If the value is a number, the quotes may be omitted. Most configuration variables in the file are boolean values, where a 1 indicates the option is set, and a 0 disables it. </p>
<p> See the example config.py file for a full list of available configuration variables.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.rss2email/feeds.dat</code></dt>
<dd> The database of feeds. Use r2e to add, remove, or modify feeds, do not edit it directly.</dd>
<dt><code>~/.rss2email/config.py</code></dt>
<dd> If this file exists, it is read to configure the program.</dd></dl>
<h2>AUTHOR</h2>
<p> Aaron Swartz &lt;rss2email [at] aaronsw.com&gt; </p>
<h2>Index</h2>
