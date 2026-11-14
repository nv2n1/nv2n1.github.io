---
title: "glob(7)"
name: "glob"
section: "7"
letter: "g"
url: "/docs/linux/man/7-glob/"
description: "glob – globbing pathnames"
---

<p>glob &#8211; globbing pathnames</p>
<h2>Description</h2>
<p>Long ago, in UNIX V6, there was a program <i>/etc/glob</i> that would expand wildcard patterns. Soon afterward this became a shell built-in. </p>
<p> These days there is also a library routine <code><a href="/docs/linux/man/3-glob/">glob</a></code>(3) that will perform this function for a user program. </p>
<p> The rules are as follows (POSIX.2, 3.13).</p>
<h3>Wildcard matching</h3>
<p>A string is a wildcard pattern if it contains one of the characters &#8216;?&#8217;, &#8216;*&#8217; or &#8216;[&#8216;. Globbing is the operation that expands a wildcard pattern into the list of pathnames matching the pattern. Matching is defined by: </p>
<p> A &#8216;?&#8217; (not between brackets) matches any single character. </p>
<p> A &#8216;*&#8217; (not between brackets) matches any string, including the empty string. </p>
<p> <code>Character classes</code> </p>
<p> An expression &quot;<i>[&#8230;]</i>&quot; where the first character after the leading &#8216;[&#8216; is not an &#8216;!&#8217; matches a single character, namely any of the characters enclosed by the brackets. The string enclosed by the brackets cannot be empty; therefore &#8216;]&#8217; can be allowed between the brackets, provided that it is the first character. (Thus, &quot;<i>[][!]</i>&quot; matches the three characters &#8216;[&#8216;, &#8216;]&#8217; and &#8216;!&#8217;.) </p>
<p> <code>Ranges</code> </p>
<p> There is one special convention: two characters separated by &#8216;-&#8216; denote a range. (Thus, &quot;<i>[A-Fa-f0-9]</i>&quot; is equivalent to &quot;<i>[ABCDEFabcdef0123456789]</i>&quot;.) One may include &#8216;-&#8216; in its literal meaning by making it the first or last character between the brackets. (Thus, &quot;<i>[]-]</i>&quot; matches just the two characters &#8216;]&#8217; and &#8216;-&#8216;, and &quot;<i>[&#8211;0]</i>&quot; matches the three characters &#8216;-&#8216;, &#8216;.&#8217;, &#8216;0&#8217;, since &#8216;/&#8217; cannot be matched.) </p>
<p> <code>Complementation</code> </p>
<p> An expression &quot;<i>[!&#8230;]</i>&quot; matches a single character, namely any character that is not matched by the expression obtained by removing the first &#8216;!&#8217; from it. (Thus, &quot;<i>[!]a-]</i>&quot; matches any single character except &#8216;]&#8217;, &#8216;a&#8217; and &#8216;-&#8216;.) </p>
<p> One can remove the special meaning of &#8216;?&#8217;, &#8216;*&#8217; and &#8216;[&#8216; by preceding them by a backslash, or, in case this is part of a shell command line, enclosing them in quotes. Between brackets these characters stand for themselves. Thus, &quot;<i>[[?*\]</i>&quot; matches the four characters &#8216;[&#8216;, &#8216;?&#8217;, &#8216;*&#8217; and &#8216;\&#8217;.</p>
<h3>Pathnames</h3>
<p>Globbing is applied on each of the components of a pathname separately. A &#8216;/&#8217; in a pathname cannot be matched by a &#8216;?&#8217; or &#8216;*&#8217; wildcard, or by a range like &quot;<i>[.-0]</i>&quot;. A range containing an explicit &#8216;/&#8217; character is syntactically incorrect. (POSIX requires that syntactically incorrect patterns are left unchanged.) </p>
<p> If a filename starts with a &#8216;.&#8217;, this character must be matched explicitly. (Thus, <i>rm&nbsp;*</i> will not remove .profile, and <i>tar c&nbsp;*</i> will not archive all your files; <i>tar c .</i> is better.)</p>
<h3>Empty lists</h3>
<p>The nice and simple rule given above: &quot;expand a wildcard pattern into the list of matching pathnames&quot; was the original UNIX definition. It allowed one to have patterns that expand into an empty list, as in </p>
<pre> xv -wait 0 *.gif *.jpg</pre>
<p>where perhaps no *.gif files are present (and this is not an error). However, POSIX requires that a wildcard pattern is left unchanged when it is syntactically incorrect, or the list of matching pathnames is empty. With <i>bash</i> one can force the classical behavior using this command: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shopt -s nullglob </p>
<p> (Similar problems occur elsewhere. For example, where old scripts have </p>
<pre> rm `find . -name &quot;*~&quot;`</pre>
<p>new scripts require </p>
<pre> rm -f nosuchfile `find . -name &quot;*~&quot;`</pre>
<p>to avoid error messages from <i>rm</i> called with an empty argument list.)</p>
<h2>Notes</h2>
<h3>Regular expressions</h3>
<p>Note that wildcard patterns are not regular expressions, although they are a bit similar. First of all, they match filenames, rather than text, and secondly, the conventions are not the same: for example, in a regular expression &#8216;*&#8217; means zero or more copies of the preceding thing. </p>
<p> Now that regular expressions have bracket expressions where the negation is indicated by a &#8216;ha&#8217;, POSIX has declared the effect of a wildcard pattern &quot;<i>[ha&#8230;]</i>&quot; to be undefined.</p>
<h3>Character classes and internationalization</h3>
<p>Of course ranges were originally meant to be ASCII ranges, so that &quot;<i>[&nbsp;-%]</i>&quot; stands for &quot;<i>[&nbsp;!&quot;#$%]</i>&quot; and &quot;<i>[a-z]</i>&quot; stands for &quot;any lowercase letter&quot;. Some UNIX implementations generalized this so that a range X-Y stands for the set of characters with code between the codes for X and for Y. However, this requires the user to know the character coding in use on the local system, and moreover, is not convenient if the collating sequence for the local alphabet differs from the ordering of the character codes. Therefore, POSIX extended the bracket notation greatly, both for wildcard patterns and for regular expressions. In the above we saw three types of items that can occur in a bracket expression: namely (i) the negation, (ii) explicit single characters, and (iii) ranges. POSIX specifies ranges in an internationally more useful way and adds three more types: </p>
<p> (iii) Ranges X-Y comprise all characters that fall between X and Y (inclusive) in the current collating sequence as defined by the <code>LC_COLLATE</code> category in the current locale. </p>
<p> (iv) Named character classes, like </p>
<pre>[:alnum:] [:alpha:] [:blank:] [:cntrl:]
[:digit:] [:graph:] [:lower:] [:print:]
[:punct:] [:space:] [:upper:] [:xdigit:]</pre>
<p>so that one can say &quot;<i>[[:lower:]]</i>&quot; instead of &quot;<i>[a-z]</i>&quot;, and have things work in Denmark, too, where there are three letters past &#8216;z&#8217; in the alphabet. These character classes are defined by the <code>LC_CTYPE</code> category in the current locale. </p>
<p> (v) Collating symbols, like &quot;<i>[.ch.]</i>&quot; or &quot;<i>[.a-acute.]</i>&quot;, where the string between &quot;<i>[.</i>&quot; and &quot;<i>.]</i>&quot; is a collating element defined for the current locale. Note that this may be a multicharacter element. </p>
<p> (vi) Equivalence class expressions, like &quot;<i>[=a=]</i>&quot;, where the string between &quot;<i>[=</i>&quot; and &quot;<i>=]</i>&quot; is any collating element from its equivalence class, as defined for the current locale. For example, &quot;<i>[[=a=]]</i>&quot; might be equivalent to &quot;<i>[a&aacute;\`a&auml;&acirc;]</i>&quot;, that is, to &quot;<i>[a[.a-acute.][.a-grave.][.a-umlaut.][.a-circumflex.]]</i>&quot;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3), <code><a href="/docs/linux/man/3-glob/">glob</a></code>(3), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
