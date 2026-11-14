---
title: "lintianspelling(3)"
name: "lintianspelling"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianspelling/"
description: "Lintian::Spelling — Lintian spell checks shared between multiple scripts"
---

<p>Lintian::Spelling &#8212; Lintian spell checks shared between multiple scripts </p>
<h2>Synopsis</h2>
<pre> use Lintian::Spelling qw(check_spelling);</pre>
<h2>Description</h2>
<p>This module provides functions to do some Lintian checks that need to be done in multiple places. There are certain low-level checks, such as validating a maintainer name and e-mail address or checking spelling, which apply in multiple situations and should be done in multiple checks scripts or in checks scripts and the Lintian front-end. </p>
<p> The functions provided by this module issue tags directly, usually either taking the tag name to issue as an argument or dynamically constructing the tag name based on function parameters. The caller is responsible for ensuring that all tags are declared in the relevant *.desc file with proper descriptions and other metadata. The possible tags issued by each function are described in the documentation for that function.</p>
<h2>Functions</h2>
<dl COMPACT>
<dt>check_spelling(<font SIZE="-1">TEXT</font>,[ <font SIZE="-1">EXCEPTIONS,</font>] <font SIZE="-1">CODEREF</font>)</p>
<dd>Performs a spelling check of <font SIZE="-1">TEXT.</font> Call <font SIZE="-1">CODEREF</font> once for each unique misspelling with the following arguments:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>The misspelled word/phrase</p>
<dd>
<dt>The correct word/phrase</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd>If <font SIZE="-1">EXCEPTIONS</font> is given, it will be used as a hash ref of exceptions. Any lowercase word appearing as a key of this hash ref will never be considered a spelling mistake (exception being if it is a part of a multiword misspelling). </p>
<p> Returns the number of spelling mistakes found in <font SIZE="-1">TEXT.</font></dl>
<dt>check_spelling_picky(<font SIZE="-1">TEXT, CODEREF</font>)</p>
<dd>Performs a spelling check of <font SIZE="-1">TEXT.</font> Call <font SIZE="-1">CODEREF</font> once for each unique misspelling with the following arguments:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>The misspelled word/phrase</p>
<dd>
<dt>The correct word/phrase</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd>This method performs some pickier corrections &#8211; such as checking for common capitalization mistakes &#8211; which would are not included in check_spelling as they are not appropriate for some files, such as changelogs. </p>
<p> Returns the number of spelling mistakes found in <font SIZE="-1">TEXT.</font></dl>
</dl>
<h2>Variables</h2>
<dl COMPACT>
<dt>$known_shells_regex</p>
<dd>Regular expression that matches names of any known shell.</dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian. Based on code from checks scripts by Marc Brockschmidt and Richard Braakman.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
