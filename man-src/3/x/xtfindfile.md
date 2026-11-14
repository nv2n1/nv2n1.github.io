---
title: "xtfindfile(3)"
name: "xtfindfile"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtfindfile/"
description: "XtFindFile – search for a file using substitutions in the path list"
---

<p>XtFindFile &#8211; search for a file using substitutions in the path list </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>char * XtFindFile(const char *<i>path</i>, Substitution <i>substitutions</i>, Cardinal <i>num_substitutions</i>, XtFilePredicate <i>predicate</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>path</i></p>
<dd>Specifies a path of file names, including substitution characters.</p>
<dt><i>substitutions</i></p>
<dd>Specifies a list of substitutions to make into a path.</p>
<dt><i>num_substitutions</i></p>
<dd>Specifies the number of substitutions passed in.</p>
<dt><i>predicate</i></p>
<dd>Specifies a procedure to call to judge a potential file name, or NULL.</dl>
<h2>Description</h2>
<p>The <i>path</i> parameter specifies a string that consists of a series of potential file names delimited by colons. Within each name, the percent character specifies a string substitution selected by the following character. The character sequence &#8220;%:&#8221; specifies an embedded colon that is not a delimiter; the sequence is replaced by a single colon. The character sequence &#8220;%%&#8221; specifies a percent character that does not introduce a substitution; the sequence is replaced by a single percent character. If a percent character is followed by any other character, <code>XtFindFile</code> looks through the specified <i>substitutions</i> for that character in the <i>match</i> field and if found replaces the percent and match characters with the string in the corresponding <i>substitution</i> field. A <i>substitution</i> field entry of NULL is equivalent to a pointer to an empty string. If the operating system does not interpret multiple embedded name separators in the path (i.e., &#8220;/&#8221; in POSIX) the same way as a single separator, <code>XtFindFile</code> will collapse multiple separators into a single one after performing all string substitutions. Except for collapsing embedded separators, the contents of the string substitutions are not interpreted by <code>XtFindFile</code> and may therefore contain any operating-system-dependent characters, including additional name separators. Each resulting string is passed to the predicate procedure until a string is found for which the procedure returns <code>True</code>; this string is the return value for <code>XtFindFile</code>. If no string yields a <code>True</code> return from the predicate, <code>XtFindFile</code> returns NULL. </p>
<p> If the <i>predicate</i> parameter is NULL, an internal procedure that checks if the file exists, is readable, and is not a directory will be used. </p>
<p> It is the responsibility of the caller to free the returned string using <code>XtFree</code> when it is no longer needed.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
