---
title: "tracker-search(1)"
name: "tracker-search"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-search/"
description: "tracker-search – Search for content by type or across all types"
---

<h2 class="name">NAME</h2>
<p> tracker-search &#8211; Search for content by type or across all types</p>
<h2>SYNOPSIS</h2>
<p> <code>tracker search</code> [<i>options</i>&#8230;] [[<i>expression1</i>] &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>tracker search</code> searches all indexed content for <i>expression</i>. The resource in which <i>expression</i> matches must exist (see <code>&#8211;all</code> for more information). All results are returned in ascending order. In all cases, if no <i>expression</i> is given for an argument (like <code>&#8211;folders</code> for example) then ALL items in that category are returned instead.</p>
<dl>
<dt><i>expression</i></p>
<dd> One or more terms to search. The default operation is a logical AND. For logical OR operations, see -r. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f, &#8211;files</code></p>
<dd> Search for files of any type matching <i>expression</i> (optional).</p>
<dt><code>-s, &#8211;folders</code></p>
<dd> Search for folders matching <i>expression</i> (optional).</p>
<dt><code>-m, &#8211;music</code></p>
<dd> Search for music files matching <i>expression</i> (optional).</p>
<dt><code>&#8211;music-albums</code></p>
<dd> Search for music albums matching <i>expression</i> (optional).</p>
<dt><code>&#8211;music-artists</code></p>
<dd> Search for music artists matching <i>expression</i> (optional).</p>
<dt><code>-i, &#8211;images</code></p>
<dd> Search for images matching <i>expression</i> (optional).</p>
<dt><code>-v, &#8211;videos</code></p>
<dd> Search for videos matching <i>expression</i> (optional).</p>
<dt><code>-t, &#8211;documents</code></p>
<dd> Search for documents matching <i>expression</i> (optional).</p>
<dt><code>-e, &#8211;emails</code></p>
<dd> Search for emails matching <i>expression</i> (optional). Returns a list of subjects for emails found.</p>
<dt><code>-c, &#8211;contacts</code></p>
<dd> Search for contacts matching <i>expression</i> (optional). Returns a list of names and email addresses found.</p>
<dt><code>&#8211;software</code></p>
<dd> Search for software installed matching <i>expression</i> (optional). Returns a list of desktop files and application titles found.</p>
<dt><code>&#8211;software-categories</code></p>
<dd> Search for software categories matching <i>expression</i> (optional). Returns a list of urns and their categories (e.g. Settings, Video, Utility, etc).</p>
<dt><code>&#8211;feeds</code></p>
<dd> Search through RSS feed information matching <i>expression</i> (optional). Returns a list of those found.</p>
<dt><code>-b, &#8211;bookmarks</code></p>
<dd> Search through bookmarks matching <i>expression</i> (optional). Returns a list titles and links for each bookmark found.</p>
<dt><code>-l, &#8211;limit</code>=&lt;<i>limit</i>&gt;</p>
<dd> Limit search to <i>limit</i> results. The default is 10 or 512 with &#8211;disable-snippets.</p>
<dt><code>-o, &#8211;offset</code>=&lt;<i>offset</i>&gt;</p>
<dd> Offset the search results by <i>offset</i>. For example, start at item number 10 in the results. The default is 0.</p>
<dt><code>-r, &#8211;or-operator</code></p>
<dd> Use OR for search terms instead of AND (the default)</p>
<dt><code>-d, &#8211;detailed</code></p>
<dd> Show the unique URN associated with each search result. This does not apply to &#8211;music-albums and &#8211;music-artists.</p>
<dt><code>-a, &#8211;all</code></p>
<dd> Show results which might not be available. This might bebecause a removable media is not mounted for example. Without this option, resources are only shown if they exist. This option applies to all command line switches except</p>
<dt><code>&#8211;disable-snippets</code></p>
<dd> Results are shown with snippets. Snippets are context around the word that was searched for in the first place. This gives some idea of if the resource found is the right one. Snippets require Full Text Search to be compile time enabled AND to not be disabled with &#8211;disable-fts. Using &#8211;disable-snippets only shows the resources which matched, no context is provided about where the match occurred.</p>
<dt><code>&#8211;disable-fts</code></p>
<dd> If Full Text Search (FTS) is available, this option allows it to be disabled for one off searches. This returns results slightly using particular properties to match the search terms (like &quot;nie:title&quot;) instead of looking for the search terms amongst ALL properties. It is more limiting to do this, but sometimes searching without FTS can yield better results if the FTS ranking is off.</p>
<dt><code>&#8211;disable-color</code></p>
<dd> This disables any ANSI color use on the command line. By default this is enabled to make it easier to see results. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TRACKER_SPARQL_BACKEND</code></p>
<dd> This option allows you to choose which backend you use for connecting to the database. This choice can limit your functionality. There are three settings. </p>
<p> With &quot;<code>direct</code>&quot; the connection to the database is made directly to the file itself on the disk, there is no intermediary daemon or process. The &quot;<code>direct</code>&quot; approach is purely <i>read-only</i>. </p>
<p> With &quot;<code>bus</code>&quot; the <code>tracker-store</code> process is used to liase with the database queuing all requests and managing the connections via an IPC / D-Bus. This adds a small overhead <i>BUT</i> this is the only approach you can use if you want to <i>write</i> to the database. </p>
<p> With &quot;<code>auto</code>&quot; the backend is decided for you, much like it would be if this environment variable was undefined. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1), <code><a href="/docs/linux/man/1-tracker-stats/">tracker-stats</a></code>(1), <code><a href="/docs/linux/man/1-tracker-tag/">tracker-tag</a></code>(1), <code><a href="/docs/linux/man/1-tracker-info/">tracker-info</a></code>(1). </p>
<h2>Index</h2>
