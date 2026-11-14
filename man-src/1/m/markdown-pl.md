---
title: "markdown-pl(1)"
name: "markdown-pl"
section: "1"
letter: "m"
url: "/docs/linux/man/1-markdown-pl/"
---

Markdown.pl - Convert Markdown syntax to (X)HTML 

<h2>Description</h2>This program is distributed as part of Perl's Text::Markdown module, illustrating sample usage. 

 Markdown can be invoked on any file containing Markdown-syntax, and will produce the corresponding (X)HTML on <font SIZE="-1">STDOUT:</font> 

 <pre> $ cat file.txt
 This is a *test*.
 Absolutely _nothing_ to see here. _Just a **test**_!
 * test
 * Yup, test.
 $ Markdown.pl file.txt
 &lt;p&gt;This is a &lt;em&gt;test&lt;/em&gt;.&lt;/p&gt;
 &lt;p&gt;Absolutely &lt;em&gt;nothing&lt;/em&gt; to see here. &lt;em&gt;Just a &lt;strong&gt;test&lt;/strong&gt;&lt;/em&gt;!&lt;/p&gt;
 &lt;ul&gt;
 &lt;li&gt;test&lt;/li&gt;
 &lt;li&gt;Yup, test.&lt;/li&gt;
 &lt;/ul&gt;</pre>If no file is specified, it will expect its input from <font SIZE="-1">STDIN:</font> 

 <pre> $ echo &quot;A **simple** test&quot; | markdown
 &lt;p&gt;A &lt;strong&gt;simple&lt;/strong&gt; test&lt;/p&gt;</pre><h2>Options</h2><dl><dt>version
<dd>Shows the full information for this version
<dt>shortversion
<dd>Shows only the version number
<dt>html4tags
<dd>Produce <font SIZE="-1">HTML</font> 4-style tags instead of <font SIZE="-1">XHTML - XHTML</font> requires elements that do not wrap a block (i.e. the <tt>&quot;hr&quot;</tt> tag) to state they will not be closed, by closing with <tt>&quot;/&gt;&quot;</tt>. <font SIZE="-1">HTML</font> 4-style will plainly output the tag as it comes: 

 <pre> $ echo '---' | markdown
 &lt;hr /&gt;
 $ echo '---' | markdown --html4tags
 &lt;hr&gt;</pre><dt>help
<dd>Shows this documentation</dl><h2>Author</h2>Copyright 2004 John Gruber 

 Copyright 2008 Tomas Doran 

 The manpage was written by Gunnar Wolf &lt;gwolf [at] debian.org&gt; for its use in Debian systems, but can be freely used elsewhere. 

 For full licensing information, please refer to Text::Markdown.pm's full documentation.
<h2>See Also</h2>Text::Markdown, &lt;<a rel="nofollow" HREF="http://daringfireball.net/projects/markdown/">http://daringfireball.net/projects/markdown/</a>&gt;
