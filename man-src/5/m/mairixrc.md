---
title: "mairixrc(5)"
name: "mairixrc"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mairixrc/"
description: "mairixrc – configuration file for"
---

<p>mairixrc &#8211; configuration file for </p>
<p><a href="/docs/linux/man/1-mairix/">mairix</a>(1)</p>
<h2>Synopsis</h2>
<p>$HOME/.mairixrc</p>
<h2>Description</h2>
<p>The <i>mairixrc</i> file tells <code>mairix</code> where your mail folders are located. It also tells <code>mairix</code> where the results of searches are to be written. <code>mairix</code> searches for this file at <i>$HOME/.mairixrc</i> unless the <code>-f</code> option is used. The directives <code>base</code>, <code>mfolder</code>, and <code>database</code> must always appear in the file. There must also be some folder definitions (using the <code>maildir</code>, <code>mh</code>, or <code>mbox</code>) directives.</p>
<h3>Comments</h3>
<p>Any line starting with a &#8216;#&#8217; character is treated as a comment.</p>
<h3>Directives</h3>
<dl>
<dt><code>base=</code><i>base-directory</i></p>
<dd>This defines the path to the common parent directory of all your maildir folders. If the path is relative, it is treated as relative to the location of the <i>mairixrc</i> file.</p>
<dt><code>maildir=</code><i>list-of-folder-specifications</i></p>
<dd>This is a colon-separated list of the Maildir folders (relative to `base&#8217;) that you want indexed. Any entry that ends `&#8230;&#8217; is recursively scanned to find any Maildir folders underneath it. More than one line starting with `maildir&#8217; can be included. In this case, mairix joins the lines together with colons as though a single list of folders had been given on a single very long line. Each colon-separated entry may be a wildcard. See the discussion under mbox (below) for the wildcard syntax. For example</dl>
<pre><dl><dt><dd>maildir=zzz/foo*...
</dl></pre>
<dl>
<dd>will match maildir folders like these (relative to the <i>base-directory</i>)</dl>
<pre><dl><dt><dd>zzz/foobar/xyz
zzz/fooquux
zzz/foo
zzz/fooabc/u/v/w
</dl></pre>
<dl>
<dd>and</dl>
<pre><dl><dt><dd>maildir=zzz/foo[abc]*
</dl></pre>
<dl>
<dd>will match maildir folders like these (relative to the folder_base)</dl>
<pre><dl><dt><dd>zzz/fooa
zzz/fooaaaxyz
zzz/foobcd
zzz/fooccccccc
</dl></pre>
<dl>
<dd>If a folder name contains a colon, you can write this by using the sequence &#8216;\:&#8217; to escape the colon. Otherwise, the backslash character is treated normally. (If the folder name actually contains the sequence &#8216;\:&#8217;, you&#8217;re out of luck.)</p>
<dt><code>mh=</code><i>list-of-folder-specifications</i></p>
<dd>This is a colon-separated list of the MH folders (relative to recursively scanned to find any MH folders underneath it. More than one line starting with &#8216;mh&#8217; can be included. In this case, mairix joins the lines together with colons as though a single list of folders had been given on a single very long line. Each colon-separated entry may be a wildcard, see the discussion under maildir (above) and mbox (below) for the syntax and semantics of specifying wildcards. recognizes the types of MH folders created by the following email applications:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>xmh</p>
<dt>*</p>
<dd>sylpheed</p>
<dt>*</p>
<dd>evolution</p>
<dt>*</p>
<dd>NNML</p>
<dt>*</p>
<dd>Mew</dl>
</dl>
<dt><code>mbox=</code><i>list-of-folder-specifications</i></p>
<dd>This is a colon-separated list of the mbox folders (relative to Each colon-separated item in the list can be suffixed by &#8216;&#8230;&#8217;. If the item matches a regular file, that file is treated as a mbox folder and the &#8216;&#8230;&#8217; suffix is ignored. If the item matches a directory, a recursive scan of everything inside that directory is made, and all regular files are initially considered as mbox folders. (Any directories found in this scan are themselves scanned, since the scan is recursive.) Each colon-separated item may contain wildcard operators, but only in its final path component. The wildcard operators currently supported are</p>
<dt>*</p>
<dd>Match zero or more characters (each character matched is arbitrary)</p>
<dt>?</p>
<dd>Match exactly one arbitrary character</p>
<dt>[abcs-z]</p>
<dd>Character class : match a single character from the set a, b, c, s, t, u, v, w, x, y and z. To include a literal &#8216;]&#8217; in the class, place it immediately after the opening &#8216;[&#8216;. To include a literal &#8216;-&#8216; in the class, place it immediately before the closing &#8216;]&#8217;. If these metacharacters are included in non-final path components, they have no special meaning. Here are some examples</p>
<dt>mbox=foo/bar*</p>
<dd>matches &#8216;foo/bar&#8217;, &#8216;foo/bar1&#8217;, &#8216;foo/barrrr&#8217; etc</p>
<dt>mbox=foo*/bar*</p>
<dd>matches &#8216;foo*/bar&#8217;, &#8216;foo*/bar1&#8217;, &#8216;foo*/barrrr&#8217; etc</p>
<dt>mbox=foo/*</p>
<dd>matches &#8216;foo/bar&#8217;, &#8216;foo/bar1&#8217;, &#8216;foo/barrrr&#8217;, &#8216;foo/foo&#8217;, &#8216;foo/x&#8217; etc</p>
<dt>mbox=foo&#8230;</p>
<dd>matches any regular file in the tree rooted at &#8216;foo&#8217;</p>
<dt>mbox=foo/*&#8230;</p>
<dd>same as before</p>
<dt>mbox=foo/[a-z]*&#8230;</p>
<dd>matches &#8216;foo/a&#8217;, &#8216;foo/aardvark/xxx&#8217;, &#8216;foo/zzz/foobar&#8217;, &#8216;foo/w/x/y/zzz&#8217;, but not &#8216;foo/A/foobar&#8217; Regular files that are mbox folder candidates are examined internally. Only files containing standard mbox &#8216;From &#8216; separator lines will be scanned for messages. If a regular file has a name ending in &#8216;.gz&#8217;, and gzip support is compiled into the <code>mairix</code> binary, the file will be treated as a gzipped mbox. If a regular file has a name ending in &#8216;.bz2&#8217;, and bzip support is compiled into the <code>mairix</code> binary, the file will be treated as a bzip2&#8217;d mbox. More than one line starting with &#8216;mbox&#8217; can be included. In this case, <code>mairix</code> joins the lines together with colons as though a single list of folders had been given on a single very long line. <code>mairix</code> performs no locking of mbox folders when it is accessing them. If a mail delivery program is modifying the mbox at the same time, it is likely that one or messages in the mbox will never get indexed by <code>mairix</code> (until the database is removed and recreated from scratch, anyway.) The assumption is that <code>mairix</code> will be used to index archive folders rather than incoming ones, so this is unlikely to be much of a problem in reality. <code>mairix</code> can support a maximum of 65536 separate mboxes, and a maximum of 65536 messages within any one mbox.</p>
<dt><code>omit=</code><i>list-of-glob-patterns</i></p>
<dd>This is a colon-separated list of glob patterns for folders to be omitted from the indexing. This allows wide wildcards and recursive elements to be used in the <code>maildir</code>,<code>mh</code>, and<code>mbox</code> directives, with the <code>omit</code> option used to selectively remove unwanted folders from the folder lists. Within the glob patterns, a single &#8216;*&#8217; matches any sequence of characters other than &#8216;/&#8217;. However &#8216;**&#8217; matches any sequence of characters including &#8216;/&#8217;. This allows glob patterns to be constructed which have a wildcard for just one directory component, or for any number of directory components. The _omit_ option can be specified as many times as required so that the list of patterns doesn&#8217;t all have to fit on one line. As an example,</dl>
<pre><dl><dt><dd>mbox=bulk...
omit=bulk/spam*
</dl></pre>
<dl>
<dd>will index all mbox folders at any level under the &#8216;bulk&#8217; subdirectory of the base folder, except for those folders whose names start &#8216;bulk/spam&#8217;, e.g. &#8216;bulk/spam&#8217;, &#8216;bulk/spam2005&#8217; etc. In constrast,</dl>
<pre><dl><dt><dd>mbox=bulk...
omit=bulk/spam**
</dl></pre>
<dl>
<dd>will index all mbox folders at any level under the &#8216;bulk&#8217; subdirectory of the base folder, except for those folders whose names start &#8216;bulk/spam&#8217;, e.g. &#8216;bulk/spam&#8217;, &#8216;bulk/spam2005&#8217;, &#8216;bulk/spam/2005&#8217;, &#8216;bulk/spam/2005/jan&#8217; etc.</p>
<dt><code>nochecks</code></p>
<dd>This takes no arguments. If a line starting with <code>nochecks is</code> present, it is the equivalent of specifying the <code>-Q</code> flag to every indexing run.</p>
<dt><code>mfolder=</code><i>match-folder-name</i></p>
<dd>This defines the name of the folder (within the directory specified by <code>base</code>) into which the search mode writes its output. (If the <code>mformat</code> used is &#8216;raw&#8217; or &#8216;excerpt&#8217;, then this setting is not used and may be omitted.) The <code>mfolder</code> setting may be over-ridden for a particular search by using the <code>-o</code> option to <code>mairix</code>. <code>mairix</code> will refuse to output search results to a folder that appears to be amongst those that are indexed. This is to prevent accidental deletion of emails. If the first character of the mfolder value is &#8216;/&#8217; or &#8216;.&#8217;, it is taken as a pathname in its own right. This allows you to specify absolute paths and paths relative to the current directory where the mfolder should be written. Otherwise, the value of mfolder is appended to the value of base, in the same way as for the source folders.</p>
<dt><code>mformat=</code><i>format</i></p>
<dd>This defines the type of folder used for the match folder where the search results go. There are four valid settings for <i>format</i>, namely &#8216;maildir&#8217;, &#8216;mh&#8217;, &#8216;mbox&#8217;, &#8216;raw&#8217; or &#8216;excerpt&#8217;. If the &#8216;raw&#8217; setting is used then <code>mairix</code> will just print out the path names of the files that match and no match folder will be created. If the &#8216;excerpt&#8217; setting is used, <code>mairix</code> will also print out the To:, Cc:, From:, Subject: and Date: headers of the matching messages. &#8216;maildir&#8217; is the default if this option is not defined. The setting is case-insensitive.</p>
<dt><code>database=</code><i>path-to-database</i></p>
<dd>This defines the path where <code>mairix</code>&#8216;s index database is kept. You can keep this file anywhere you like. Currently, <code>mairix</code> will place a single database file at the location indicated by <i>path-to-database</i>. However, a future version of <code>mairix</code> may instead place a directory containing several files at this location. <i>path-to-database</i> should be an absolute pathname (starting with &#8216;/&#8217;). If a relative pathname is used, it will be interpreted relative to the current directory at the time <code>mairix</code> is run, (<code>not</code> relative to the location of the <i>mairixrc</i> file or anything like that.)</dl>
<h3>Expansions</h3>
<p>The part of each line in &#8216;.mairixrc&#8217; following the equals sign can contain the following types of expansion:</p>
<dl>
<dt><code>Home directory expansion</code></p>
<dd>If the sequence &#8216;~/&#8217; appears at the start of the text after the equals sign, it is expanded to the user&#8217;s home directory. Example:</dl>
<pre><dl><dt><dd>database=~/Mail/mairix_database
</dl></pre>
<dl>
<dd>
<dt><code>Environment expansion</code></p>
<dd>If a &#8216;$&#8217; is followed by a sequence of alpha-numeric characters (or &#8216;_&#8217;), the whole string is replaced by looking up the corresponding environment variable. Similarly, if &#8216;$&#8217; is followed by an open brace (&#8216;{&#8216;), everything up to the next close brace is looked up as an environment variable and the result replaces the entire sequence. Suppose in the shell we do</dl>
<pre><dl><dt><dd>export FOO=bar
</dl></pre>
<dl>
<dd>and the &#8216;.mairixrc&#8217; file contains</dl>
<pre><dl><dt><dd>maildir=xxx/$FOO
mbox=yyy/a${FOO}b
</dl></pre>
<dl>
<dd>this is equivalent to</dl>
<pre><dl><dt><dd>maildir=xxx/bar
mbox=yyy/abarb
</dl></pre>
<dl>
<dd>If the specified environment variable is not set, the replacement is the empty string. </p>
<h2>Notes</h2>
<p>An alternative path to the configuration file may be given with the <code>-f</code> option to <a href="/docs/linux/man/1-mairix/">mairix</a>(1). </p>
