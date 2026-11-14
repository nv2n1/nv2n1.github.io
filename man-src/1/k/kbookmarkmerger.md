---
title: "kbookmarkmerger(1)"
name: "kbookmarkmerger"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kbookmarkmerger/"
description: "kbookmarkmerger – A program for merging a given set of bookmarks into the user’s list of bookmarks."
---

<h2 class="name">NAME</h2>
<p> kbookmarkmerger &#8211; A program for merging a given set of bookmarks into the user&#8217;s list of bookmarks. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kbookmarkmerger</code> [Qt Options&#8230;] [KDE Options&#8230;] {directory}</dl>
<h2>DESCRIPTION</h2>
<p> <code>kbookmarkmerger</code></p>
<dd>is a program for merging a given set of bookmarks into the user&#8217;s set of bookmarks; if the user doesn&#8217;t have any bookmarks created yet, a new bookmark list is created and the given bookmarks are inserted into it. While doing this, <code>kbookmarkmerger</code> keeps track of which files were merged in a previous run already, so no bookmark will get installed to the user&#8217;s bookmarks more than once. In case KDE is running while <code>kbookmarkmerger</code> is executed, the KDE bookmark subsystem will be informed of any changes to the user&#8217;s bookmarks, so that all applications accessing that information (i.e.Konqueror) will pick the changes up instantly. </p>
<p> The traditionally used approach to achieve something like this was to use carefully crafted skeleton home directories when creating a new user account, to provide the user with a standard set of bookmarks. The problem with this approach is that after the user account has been created, no new bookmarks can be propagated. </p>
<p> This mechanism is useful for system administrators who want to propagate a bookmark pointing to a certain document (for instance, important notes about the system) to all users. Distributors might find it useful as well, for instance by augmenting the software packages they supply with bookmark files which <code>kbookmarkmerger</code> merges into the user&#8217;s bookmark list when the package is installed. That way, documentation shipped with a software package is easily and visibly accessible right after the package has been installed. </p>
<p> The only parameter required by <code>kbookmarkmerger</code> is the name of a directory which shall be scanned for bookmark files. All files in the given directory will be considered for being merged into the user&#8217;s setup. The files in the given directory should be valid XBEL files.</p>
<h2>SEE ALSO</h2>
<p> m[blue]<code>Konqueror manual</code>m[]<font SIZE="-2">[1]</font></p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
joe [at] hal9000:~&gt; <code>kbookmarkmerger </code><code>/usr/local/extra-bookmarks</code>
</pre>
</dl>
<p> Merges all bookmark files stored in /usr/local/extra-bookmarks into joe&#8217;s list of bookmarks.</p>
<h2>STANDARDS</h2>
<dl>
<dt>
<dd> m[blue]<code>XBEL specification</code>m[]<font SIZE="-2">[2]</font></dl>
<h2>RESTRICTIONS</h2>
<p> When determining whether a given bookmark file has been merged into the user&#8217;s bookmarks already or not, <code>kbookmarkmerger</code> merely looks at the filename of the bookmark file &#8211; the contents are not checked at all. This means that changing a bookmark file which was already merged into a user&#8217;s bookmarks will not trigger merging it once again. </p>
<p> Also note that in case a user modifies a bookmark which was merged into his setup, the original bookmark file will be left unmodified.</p>
<h2>AUTHOR</h2>
<p> Frerich Raabe&lt;raabe [at] kde.org&gt;</p>
<h2>AUTHOR</h2>
<p> <code>Frerich Raabe</code> &lt;raabe [at] kde.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Konqueror manual</p>
<dl>
<dt>
<dd> help:/konqueror/index.html</dl>
<dt> 2.</p>
<dd> XBEL specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://pyxml.sourceforge.net/topics/xbel/">http://pyxml.sourceforge.net/topics/xbel/</a></dl>
</dl>
<h2>Index</h2>
