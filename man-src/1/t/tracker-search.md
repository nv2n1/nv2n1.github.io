---

title: "tracker-search(1)"
name: "tracker-search"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-search/"
description: "tracker-search – Search for content by type or across all types"
---

<p> <code>tracker search</code> [<i>options</i>&#8230;] [[<i>expression1</i>] &#8230;] </p>
<p> <code>tracker search</code> searches all indexed content for <i>expression</i>. The resource in which <i>expression</i> matches must exist (see <code>&#8211;all</code> for more information). All results are returned in ascending order. In all cases, if no <i>expression</i> is given for an argument (like <code>&#8211;folders</code> for example) then ALL items in that category are returned instead.</p>
<dl>
<dt><i>expression</i></dt>
<dd> One or more terms to search. The default operation is a logical AND. For logical OR operations, see -r. </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f, &#8211;files</code></dt>
<dd> Search for files of any type matching <i>expression</i> (optional).</dd>
<dt><code>-s, &#8211;folders</code></dt>
<dd> Search for folders matching <i>expression</i> (optional).</dd>
<dt><code>-m, &#8211;music</code></dt>
<dd> Search for music files matching <i>expression</i> (optional).</dd>
<dt><code>&#8211;music-albums</code></dt>
<dd> Search for music albums matching <i>expression</i> (optional).</dd>
<dt><code>&#8211;music-artists</code></dt>
<dd> Search for music artists matching <i>expression</i> (optional).</dd>
<dt><code>-i, &#8211;images</code></dt>
<dd> Search for images matching <i>expression</i> (optional).</dd>
<dt><code>-v, &#8211;videos</code></dt>
<dd> Search for videos matching <i>expression</i> (optional).</dd>
<dt><code>-t, &#8211;documents</code></dt>
<dd> Search for documents matching <i>expression</i> (optional).</dd>
<dt><code>-e, &#8211;emails</code></dt>
<dd> Search for emails matching <i>expression</i> (optional). Returns a list of subjects for emails found.</dd>
<dt><code>-c, &#8211;contacts</code></dt>
<dd> Search for contacts matching <i>expression</i> (optional). Returns a list of names and email addresses found.</dd>
<dt><code>&#8211;software</code></dt>
<dd> Search for software installed matching <i>expression</i> (optional). Returns a list of desktop files and application titles found.</dd>
<dt><code>&#8211;software-categories</code></dt>
<dd> Search for software categories matching <i>expression</i> (optional). Returns a list of urns and their categories (e.g. Settings, Video, Utility, etc).</dd>
<dt><code>&#8211;feeds</code></dt>
<dd> Search through RSS feed information matching <i>expression</i> (optional). Returns a list of those found.</dd>
<dt><code>-b, &#8211;bookmarks</code></dt>
<dd> Search through bookmarks matching <i>expression</i> (optional). Returns a list titles and links for each bookmark found.</dd>
<dt><code>-l, &#8211;limit</code>=&lt;<i>limit</i>&gt;</dt>
<dd> Limit search to <i>limit</i> results. The default is 10 or 512 with &#8211;disable-snippets.</dd>
<dt><code>-o, &#8211;offset</code>=&lt;<i>offset</i>&gt;</dt>
<dd> Offset the search results by <i>offset</i>. For example, start at item number 10 in the results. The default is 0.</dd>
<dt><code>-r, &#8211;or-operator</code></dt>
<dd> Use OR for search terms instead of AND (the default)</dd>
<dt><code>-d, &#8211;detailed</code></dt>
<dd> Show the unique URN associated with each search result. This does not apply to &#8211;music-albums and &#8211;music-artists.</dd>
<dt><code>-a, &#8211;all</code></dt>
<dd> Show results which might not be available. This might bebecause a removable media is not mounted for example. Without this option, resources are only shown if they exist. This option applies to all command line switches except</dd>
<dt><code>&#8211;disable-snippets</code></dt>
<dd> Results are shown with snippets. Snippets are context around the word that was searched for in the first place. This gives some idea of if the resource found is the right one. Snippets require Full Text Search to be compile time enabled AND to not be disabled with &#8211;disable-fts. Using &#8211;disable-snippets only shows the resources which matched, no context is provided about where the match occurred.</dd>
<dt><code>&#8211;disable-fts</code></dt>
<dd> If Full Text Search (FTS) is available, this option allows it to be disabled for one off searches. This returns results slightly using particular properties to match the search terms (like &quot;nie:title&quot;) instead of looking for the search terms amongst ALL properties. It is more limiting to do this, but sometimes searching without FTS can yield better results if the FTS ranking is off.</dd>
<dt><code>&#8211;disable-color</code></dt>
<dd> This disables any ANSI color use on the command line. By default this is enabled to make it easier to see results. </dd>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TRACKER_SPARQL_BACKEND</code></dt>
<dd> This option allows you to choose which backend you use for connecting to the database. This choice can limit your functionality. There are three settings. </dd>
<p> With &quot;<code>direct</code>&quot; the connection to the database is made directly to the file itself on the disk, there is no intermediary daemon or process. The &quot;<code>direct</code>&quot; approach is purely <i>read-only</i>. </p>
<p> With &quot;<code>bus</code>&quot; the <code>tracker-store</code> process is used to liase with the database queuing all requests and managing the connections via an IPC / D-Bus. This adds a small overhead <i>BUT</i> this is the only approach you can use if you want to <i>write</i> to the database. </p>
<p> With &quot;<code>auto</code>&quot; the backend is decided for you, much like it would be if this environment variable was undefined. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1), <code><a href="/docs/linux/man/1-tracker-stats/">tracker-stats</a></code>(1), <code><a href="/docs/linux/man/1-tracker-tag/">tracker-tag</a></code>(1), <code><a href="/docs/linux/man/1-tracker-info/">tracker-info</a></code>(1). </p>
