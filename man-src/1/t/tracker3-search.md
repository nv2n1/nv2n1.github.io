---
title: "tracker3-search(1)"
name: "tracker3-search"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker3-search/"
description: "tracker3-search – Search for content by type or across all types"
---

<h2 class="name">NAME</h2>
<p> tracker3-search &#8211; Search for content by type or across all types </p>
<h2>SYNOPSIS</h2>
<p> <code>tracker3 search</code> [<i>options</i>&#8230;] [[<i>expression1</i>] &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>tracker3 search</code> searches all indexed content for <i>expression</i>. The resource in which <i>expression</i> matches must exist (see <code>&#8211;all</code> for more information). All results are returned in ascending order. In all cases, if no <i>expression</i> is given for an argument (like <code>&#8211;folders</code> for example) then ALL items in that category are returned instead. </p>
<p> <i>expression</i></p>
<dl>
<dt>
<dd> One or more terms to search. The default operation is a logical AND. For logical OR operations, see -r.</dl>
<h2>OPTIONS</h2>
<p> <code>-f, &#8211;files</code></p>
<dl>
<dt>
<dd> Search for files of any type matching <i>expression</i> (optional).</dl>
<p> <code>-s, &#8211;folders</code></p>
<dl>
<dt>
<dd> Search for folders matching <i>expression</i> (optional).</dl>
<p> <code>-m, &#8211;music</code></p>
<dl>
<dt>
<dd> Search for music files matching <i>expression</i> (optional).</dl>
<p> <code>&#8211;music-albums</code></p>
<dl>
<dt>
<dd> Search for music albums matching <i>expression</i> (optional).</dl>
<p> <code>&#8211;music-artists</code></p>
<dl>
<dt>
<dd> Search for music artists matching <i>expression</i> (optional).</dl>
<p> <code>-i, &#8211;images</code></p>
<dl>
<dt>
<dd> Search for images matching <i>expression</i> (optional).</dl>
<p> <code>-v, &#8211;videos</code></p>
<dl>
<dt>
<dd> Search for videos matching <i>expression</i> (optional).</dl>
<p> <code>-t, &#8211;documents</code></p>
<dl>
<dt>
<dd> Search for documents matching <i>expression</i> (optional).</dl>
<p> <code>-e, &#8211;emails</code></p>
<dl>
<dt>
<dd> Search for emails matching <i>expression</i> (optional). Returns a list of subjects for emails found.</dl>
<p> <code>-c, &#8211;contacts</code></p>
<dl>
<dt>
<dd> Search for contacts matching <i>expression</i> (optional). Returns a list of names and email addresses found.</dl>
<p> <code>&#8211;software</code></p>
<dl>
<dt>
<dd> Search for software installed matching <i>expression</i> (optional). Returns a list of desktop files and application titles found.</dl>
<p> <code>&#8211;software-categories</code></p>
<dl>
<dt>
<dd> Search for software categories matching <i>expression</i> (optional). Returns a list of urns and their categories (e.g. Settings, Video, Utility, etc).</dl>
<p> <code>&#8211;feeds</code></p>
<dl>
<dt>
<dd> Search through RSS feed information matching <i>expression</i> (optional). Returns a list of those found.</dl>
<p> <code>-b, &#8211;bookmarks</code></p>
<dl>
<dt>
<dd> Search through bookmarks matching <i>expression</i> (optional). Returns a list titles and links for each bookmark found.</dl>
<p> <code>-l, &#8211;limit=&lt;</code><i>limit</i><code>&gt;</code></p>
<dl>
<dt>
<dd> Limit search to <i>limit</i> results. The default is 10 or 512 with &#8211;disable-snippets.</dl>
<p> <code>-o, &#8211;offset=&lt;</code><i>offset</i><code>&gt;</code></p>
<dl>
<dt>
<dd> Offset the search results by <i>offset</i>. For example, start at item number 10 in the results. The default is 0.</dl>
<p> <code>-r, &#8211;or-operator</code></p>
<dl>
<dt>
<dd> Use OR for search terms instead of AND (the default)</dl>
<p> <code>-d, &#8211;detailed</code></p>
<dl>
<dt>
<dd> Show the unique URN associated with each search result. This does not apply to &#8211;music-albums and &#8211;music-artists.</dl>
<p> <code>-a, &#8211;all</code></p>
<dl>
<dt>
<dd> Show results which might not be available. This might bebecause a removable media is not mounted for example. Without this option, resources are only shown if they exist. This option applies to all command line switches except</dl>
<p> <code>&#8211;disable-snippets</code></p>
<dl>
<dt>
<dd> Results are shown with snippets. Snippets are context around the word that was searched for in the first place. This gives some idea of if the resource found is the right one. Snippets require Full Text Search to be compile time enabled AND to not be disabled with &#8211;disable-fts. Using &#8211;disable-snippets only shows the resources which matched, no context is provided about where the match occurred.</dl>
<p> <code>&#8211;disable-fts</code></p>
<dl>
<dt>
<dd> If Full Text Search (FTS) is available, this option allows it to be disabled for one off searches. This returns results slightly using particular properties to match the search terms (like &quot;nie:title&quot;) instead of looking for the search terms amongst ALL properties. It is more limiting to do this, but sometimes searching without FTS can yield better results if the FTS ranking is off.</dl>
<p> <code>&#8211;disable-color</code></p>
<dl>
<dt>
<dd> This disables any ANSI color use on the command line. By default this is enabled to make it easier to see results.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker3-status/">tracker3-status</a></code>(1), <code><a href="/docs/linux/man/1-tracker3-tag/">tracker3-tag</a></code>(1), <code><a href="/docs/linux/man/1-tracker3-info/">tracker3-info</a></code>(1). </p>
<h2>Index</h2>
