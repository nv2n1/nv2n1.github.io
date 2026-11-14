---
title: "markdown(7)"
name: "markdown"
section: "7"
letter: "m"
url: "/docs/linux/man/7-markdown/"
description: "Markdown – The Markdown text formatting syntax"
---

<p><code>Markdown</code> &#8211; The Markdown text formatting syntax</p>
<h2>Description</h2>
<h3>Philosophy</h3>
<p><code>Markdown</code> is intended to be as easy-to-read and easy-to-write as is feasible. </p>
<p> Readability, however, is emphasized above all else. A Markdown-formatted document should be publishable as-is, as plain text, without looking like it&#8217;s been marked up with tags or formatting instructions. While Markdown&#8217;s syntax has been influenced by several existing text-to-HTML filters &#8212; including <i>Setext</i> <i>atx</i> <i>Textile</i> <i>reStructuredText</i> <i>Grutatext</i> and <i>EtText</i> &#8212; the single biggest source of inspiration for Markdown&#8217;s syntax is the format of plain text email. </p>
<p> To this end, Markdown&#8217;s syntax is comprised entirely of punctuation characters, which punctuation characters have been carefully chosen so as to look like what they mean. E.g., asterisks around a word actually look like *emphasis*. Markdown lists look like, well, lists. Even blockquotes look like quoted passages of text, assuming you&#8217;ve ever used email.</p>
<h3>Inline HTML</h3>
<p>Markdown&#8217;s syntax is intended for one purpose: to be used as a format for <i>writing</i> for the web. </p>
<p> is not a replacement for HTML, or even close to it. Its syntax is very small, corresponding only to a very small subset of HTML tags. The idea is <i>not</i> to create a syntax that makes it easier to insert HTML tags. In my opinion, HTML tags are already easy to insert. The idea for Markdown is to make it easy to read, write, and edit prose. HTML is a <i>publishing</i> format; Markdown is a <i>writing</i> format. Thus, Markdown&#8217;s formatting syntax only addresses issues that can be conveyed in plain text. </p>
<p> For any markup that is not covered by Markdown&#8217;s syntax, you simply use HTML itself. There&#8217;s no need to preface it or delimit it to indicate that you&#8217;re switching from Markdown to HTML; you just use the tags. </p>
<p> The only restrictions are that block-level HTML elements &#8212; e.g. <code>&lt;div&gt;</code> <code>&lt;table&gt;</code> <code>&lt;pre&gt;</code> <code>&lt;p&gt;</code> etc. &#8212; must be separated from surrounding content by blank lines, and the start and end tags of the block should not be indented with tabs or spaces. Markdown is smart enough not to add extra (unwanted) <code>&lt;p&gt;</code> tags around HTML block-level tags. </p>
<p> For example, to add an HTML table to a Markdown article: </p>
<blockquote>
<pre> This is a regular paragraph.
 &lt;table&gt;
 &lt;tr&gt;
 &lt;td&gt;Foo&lt;/td&gt;
 &lt;/tr&gt;
 &lt;/table&gt;
 This is another regular paragraph.</pre>
</blockquote>
<p> Note that Markdown formatting syntax is not processed within block-level HTML tags. E.g., you can&#8217;t use Markdown-style <code>*emphasis*</code> inside an HTML block. </p>
<p> Span-level HTML tags &#8212; e.g. <code>&lt;span&gt;</code> <code>&lt;cite&gt;</code> or <code>&lt;del&gt;</code> &#8212; can be used anywhere in a Markdown paragraph, list item, or header. If you want, you can even use HTML tags instead of Markdown formatting; e.g. if you&#8217;d prefer to use HTML <code>&lt;a&gt;</code> or <code>&lt;img&gt;</code> tags instead of Markdown&#8217;s link or image syntax, go right ahead. </p>
<p> Unlike block-level HTML tags, Markdown syntax *is* processed within span-level tags.</p>
<h3>Automatic Escaping for Special Characters</h3>
<p>In HTML, there are two characters that demand special treatment: `&lt;` and `&amp;`. Left angle brackets are used to start tags; ampersands are used to denote HTML entities. If you want to use them as literal characters, you must escape them as entities, e.g. `&amp;lt;`, and `&amp;amp;`. </p>
<p> Ampersands in particular are bedeviling for web writers. If you want to write about &#8216;AT&amp;T&#8217;, you need to write &#8216;`AT&amp;amp;T`&#8217;. You even need to escape ampersands within URLs. Thus, if you want to link to: </p>
<blockquote>
<pre> <a rel="nofollow" href="http://images.google.com/images?num=30">http://images.google.com/images?num=30</a>&amp;q=larry+bird</pre>
</blockquote>
<p> you need to encode the URL as: </p>
<blockquote>
<pre> <a rel="nofollow" href="http://images.google.com/images?num=30">http://images.google.com/images?num=30</a>&amp;amp;q=larry+bird</pre>
</blockquote>
<p> in your anchor tag `href` attribute. Needless to say, this is easy to forget, and is probably the single most common source of HTML validation errors in otherwise well-marked-up web sites. </p>
<p> allows you to use these characters naturally, taking care of all the necessary escaping for you. If you use an ampersand as part of an HTML entity, it remains unchanged; otherwise it will be translated into `&amp;amp;`. </p>
<p> So, if you want to include a copyright symbol in your article, you can write: </p>
<blockquote>
<pre> &amp;copy;</pre>
</blockquote>
<p> and Markdown will leave it alone. But if you write: </p>
<blockquote>
<pre> AT&amp;T</pre>
</blockquote>
<p> will translate it to: </p>
<blockquote>
<pre> AT&amp;amp;T</pre>
</blockquote>
<p> Similarly, because Markdown supports inline HTML, if you use angle brackets as delimiters for HTML tags, Markdown will treat them as such. But if you write: </p>
<blockquote>
<pre> 4 &lt; 5</pre>
</blockquote>
<p> will translate it to: </p>
<blockquote>
<pre> 4 &amp;lt; 5</pre>
</blockquote>
<p> However, inside Markdown code spans and blocks, angle brackets and ampersands are *always* encoded automatically. This makes it easy to use Markdown to write about HTML code. (As opposed to raw HTML, which is a terrible format for writing about HTML syntax, because every single `&lt;` and `&amp;` in your example code needs to be escaped.)</p>
<h2>Block Elements</h2>
<h3>Paragraphs and Line Breaks</h3>
<p>A paragraph is simply one or more consecutive lines of text, separated by one or more blank lines. (A blank line is any line that looks like a blank line &#8212; a line containing nothing but spaces or tabs is considered blank.) Normal paragraphs should not be indented with spaces or tabs. </p>
<p> The implication of the Qq one or more consecutive lines of text rule is that Markdown supports Qq hard-wrapped Dtext paragraphs. This differs significantly from most other text-to-HTML formatters (including Movable Type&#8217;s Qq Convert Line Breaks option) which translate every line break character in a paragraph into a `&lt;br /&gt;` tag. </p>
<p> When you *do* want to insert a `&lt;br /&gt;` break tag using Markdown, you end a line with two or more spaces, then type return. </p>
<p> Yes, this takes a tad more effort to create a `&lt;br /&gt;`, but a simplistic &quot;every line break is a `&lt;br /&gt;`&quot; rule wouldn&#8217;t work for Markdown. Markdown&#8217;s email-style Sx blockquoting<br />
&nbsp;<wbr>and multi-paragraph Sx list items work best &#8212; and look better &#8212; when you format them with hard breaks.</p>
<h3>Headers</h3>
<p>supports two styles of headers, <i>Setext</i> and <i>atx</i> </p>
<p> Setext-style headers are `underlined&#8217; using equal signs (for first-level headers) and dashes (for second-level headers). For example: </p>
<blockquote>
<pre> This is an H1
 =============
 This is an H2
 -------------</pre>
</blockquote>
<p> Any number of underlining `=`&#8217;s or `-`&#8217;s will work. </p>
<p> Atx-style headers use 1-6 hash characters at the start of the line, corresponding to header levels 1-6. For example: </p>
<blockquote>
<pre> # This is an H1
 ## This is an H2
 ###### This is an H6</pre>
</blockquote>
<p> Optionally, you may Qq close atx-style headers. This is purely cosmetic &#8212; you can use this if you think it looks better. The closing hashes don&#8217;t even need to match the number of hashes used to open the header. (The number of opening hashes determines the header level.) : </p>
<blockquote>
<pre> # This is an H1 #
 ## This is an H2 ##
 ### This is an H3 ######</pre>
</blockquote>
<h3>Blockquotes</h3>
<p>uses email-style `&gt;` characters for blockquoting. If you&#8217;re familiar with quoting passages of text in an email message, then you know how to create a blockquote in Markdown. It looks best if you hard wrap the text and put a `&gt;` before every line: </p>
<blockquote>
<pre> &gt; This is a blockquote with two paragraphs. Lorem ipsum
 &gt; dolor sit amet, consectetuer adipiscing elit. Aliquam
 &gt; hendrerit mi posuere lectus. Vestibulum enim wisi,
 &gt; viverra nec, fringilla in, laoreet vitae, risus.
 &gt; 
 &gt; Donec sit amet nisl. Aliquam semper ipsum sit amet
 &gt; velit. Suspendisse id sem consectetuer libero luctus
 &gt; adipiscing.</pre>
</blockquote>
<p> allows you to be lazy and only put the `&gt;` before the first line of a hard-wrapped paragraph: </p>
<blockquote>
<pre> &gt; This is a blockquote with two paragraphs. Lorem ipsum
 dolor sit amet, consectetuer adipiscing elit. Aliquam
 hendrerit mi posuere lectus. Vestibulum enim wisi,
 viverra nec, fringilla in, laoreet vitae, risus.
 &gt; Donec sit amet nisl. Aliquam semper ipsum sit amet
 velit. Suspendisse id sem consectetuer libero luctus
 adipiscing.</pre>
</blockquote>
<p> Blockquotes can be nested (i.e. a blockquote-in-a-blockquote) by adding additional levels of `&gt;`: </p>
<blockquote>
<pre> &gt; This is the first level of quoting.
 &gt;
 &gt; &gt; This is nested blockquote.
 &gt;
 &gt; Back to the first level.</pre>
</blockquote>
<p> Blockquotes can contain other Markdown elements, including headers, lists, and code blocks: </p>
<blockquote>
<pre> &gt; ## This is a header.
 &gt; 
 &gt; 1. This is the first list item.
 &gt; 2. This is the second list item.
 &gt; 
 &gt; Here's some example code:
 &gt; 
 &gt; return shell_exec(&quot;echo $input | $markdown_script&quot;);</pre>
</blockquote>
<p> Any decent text editor should make email-style quoting easy. For example, with BBEdit, you can make a selection and choose Increase Quote Level from the Text menu.</p>
<h3>Lists</h3>
<p>supports ordered (numbered) and unordered (bulleted) lists. </p>
<p> Unordered lists use asterisks, pluses, and hyphens &#8212; interchangably &#8212; as list markers: </p>
<blockquote>
<pre> * Red
 * Green
 * Blue</pre>
</blockquote>
<p> is equivalent to: </p>
<blockquote>
<pre> + Red
 + Green
 + Blue</pre>
</blockquote>
<p> and: </p>
<blockquote>
<pre> - Red
 - Green
 - Blue</pre>
</blockquote>
<p> Ordered lists use numbers followed by periods: </p>
<blockquote>
<pre> 1. Bird
 2. McHale
 3. Parish</pre>
</blockquote>
<p> It&#8217;s important to note that the actual numbers you use to mark the list have no effect on the HTML output Markdown produces. The HTML Markdown produces from the above list is: </p>
<blockquote>
<pre> &lt;ol&gt;
 &lt;li&gt;Bird&lt;/li&gt;
 &lt;li&gt;McHale&lt;/li&gt;
 &lt;li&gt;Parish&lt;/li&gt;
 &lt;/ol&gt;</pre>
</blockquote>
<p> If you instead wrote the list in Markdown like this: </p>
<blockquote>
<pre> 1. Bird
 1. McHale
 1. Parish</pre>
</blockquote>
<p> or even: </p>
<blockquote>
<pre> 3. Bird
 1. McHale
 8. Parish</pre>
</blockquote>
<p> you&#8217;d get the exact same HTML output. The point is, if you want to, you can use ordinal numbers in your ordered Markdown lists, so that the numbers in your source match the numbers in your published HTML. But if you want to be lazy, you don&#8217;t have to. </p>
<p> If you do use lazy list numbering, however, you should still start the list with the number 1. At some point in the future, Markdown may support starting ordered lists at an arbitrary number. </p>
<p> List markers typically start at the left margin, but may be indented by up to three spaces. List markers must be followed by one or more spaces or a tab. </p>
<p> To make lists look nice, you can wrap items with hanging indents: </p>
<blockquote>
<pre> * Lorem ipsum dolor sit amet, consectetuer adipiscing
 elit. Aliquam hendrerit mi posuere lectus. Vestibulum
 enim wisi, viverra nec, fringilla in, laoreet vitae,
 risus.
 * Donec sit amet nisl. Aliquam semper ipsum sit amet
 velit. Suspendisse id sem consectetuer libero luctus
 adipiscing.</pre>
</blockquote>
<p> But if you want to be lazy, you don&#8217;t have to: </p>
<blockquote>
<pre> * Lorem ipsum dolor sit amet, consectetuer adipiscing
 elit. Aliquam hendrerit mi posuere lectus. Vestibulum
 enim wisi, viverra nec, fringilla in, laoreet vitae,
 risus.
 * Donec sit amet nisl. Aliquam semper ipsum sit amet
 velit. Suspendisse id sem consectetuer libero luctus
 adipiscing.</pre>
</blockquote>
<p> If list items are separated by blank lines, Markdown will wrap the items in `&lt;p&gt;` tags in the HTML output. For example, this input: </p>
<blockquote>
<pre> * Bird
 * Magic</pre>
</blockquote>
<p> will turn into: </p>
<blockquote>
<pre> &lt;ul&gt;
 &lt;li&gt;Bird&lt;/li&gt;
 &lt;li&gt;Magic&lt;/li&gt;
 &lt;/ul&gt;</pre>
</blockquote>
<p> But this: </p>
<blockquote>
<pre> * Bird
 * Magic</pre>
</blockquote>
<p> will turn into: </p>
<blockquote>
<pre> &lt;ul&gt;
 &lt;li&gt;&lt;p&gt;Bird&lt;/p&gt;&lt;/li&gt;
 &lt;li&gt;&lt;p&gt;Magic&lt;/p&gt;&lt;/li&gt;
 &lt;/ul&gt;</pre>
</blockquote>
<p> List items may consist of multiple paragraphs. Each subsequent paragraph in a list item must be intended by either 4 spaces or one tab: </p>
<blockquote>
<pre> 1. This is a list item with two paragraphs. Lorem ipsum
 dolor sit amet, consectetuer adipiscing elit. Aliquam
 hendrerit mi posuere lectus.
 Vestibulum enim wisi, viverra nec, fringilla in,
 laoreet vitae, risus. Donec sit amet nisl. Aliquam
 semper ipsum sit amet velit.
 2. Suspendisse id sem consectetuer libero luctus
 adipiscing.</pre>
</blockquote>
<p> It looks nice if you indent every line of the subsequent paragraphs, but here again, Markdown will allow you to be lazy: </p>
<blockquote>
<pre> * This is a list item with two paragraphs.
 This is the second paragraph in the list item.
 You're only required to indent the first line. Lorem
 ipsum dolor sit amet, consectetuer adipiscing elit.
 * Another item in the same list.</pre>
</blockquote>
<p> To put a blockquote within a list item, the blockquote&#8217;s `&gt;` delimiters need to be indented: </p>
<blockquote>
<pre> * A list item with a blockquote:
 &gt; This is a blockquote
 &gt; inside a list item.</pre>
</blockquote>
<p> To put a code block within a list item, the code block needs to be indented *twice* &#8212; 8 spaces or two tabs: </p>
<blockquote>
<pre> * A list item with a code block:
 &lt;code goes here&gt;</pre>
</blockquote>
<p> It&#8217;s worth noting that it&#8217;s possible to trigger an ordered list by accident, by writing something like this: </p>
<blockquote>
<pre> 1986. What a great season.</pre>
</blockquote>
<p> In other words, a *number-period-space* sequence at the beginning of a line. To avoid this, you can backslash-escape the period: </p>
<blockquote>
<pre> 1986\. What a great season.</pre>
</blockquote>
<h3>Code Blocks</h3>
<p>Pre-formatted code blocks are used for writing about programming or markup source code. Rather than forming normal paragraphs, the lines of a code block are interpreted literally. Markdown wraps a code block in both `&lt;pre&gt;` and `&lt;code&gt;` tags. </p>
<p> To produce a code block in Markdown, simply indent every line of the block by at least 4 spaces or 1 tab. For example, given this input: </p>
<blockquote>
<pre> This is a normal paragraph:
 This is a code block.</pre>
</blockquote>
<p> will generate: </p>
<blockquote>
<pre> &lt;p&gt;This is a normal paragraph:&lt;/p&gt;
 &lt;pre&gt;&lt;code&gt;This is a code block.
 &lt;/code&gt;&lt;/pre&gt;</pre>
</blockquote>
<p> One level of indentation &#8212; 4 spaces or 1 tab &#8212; is removed from each line of the code block. For example, this: </p>
<blockquote>
<pre> Here is an example of AppleScript:
 tell application &quot;Foo&quot;
 beep
 end tell</pre>
</blockquote>
<p> will turn into: </p>
<blockquote>
<pre> &lt;p&gt;Here is an example of AppleScript:&lt;/p&gt;
 &lt;pre&gt;&lt;code&gt;tell application &quot;Foo&quot;
 beep
 end tell
 &lt;/code&gt;&lt;/pre&gt;</pre>
</blockquote>
<p> A code block continues until it reaches a line that is not indented (or the end of the article). </p>
<p> Within a code block, ampersands (`&amp;`) and angle brackets (`&lt;` and `&gt;`) are automatically converted into HTML entities. This makes it very easy to include example HTML source code using Markdown &#8212; just paste it and indent it, and Markdown will handle the hassle of encoding the ampersands and angle brackets. For example, this: </p>
<blockquote>
<pre> &lt;div class=&quot;footer&quot;&gt;
 &amp;copy; 2004 Foo Corporation
 &lt;/div&gt;</pre>
</blockquote>
<p> will turn into: </p>
<blockquote>
<pre> &lt;pre&gt;&lt;code&gt;&amp;lt;div class=&quot;footer&quot;&amp;gt;
 &amp;amp;copy; 2004 Foo Corporation
 &amp;lt;/div&amp;gt;
 &lt;/code&gt;&lt;/pre&gt;</pre>
</blockquote>
<p> Regular Markdown syntax is not processed within code blocks. E.g., asterisks are just literal asterisks within a code block. This means it&#8217;s also easy to use Markdown to write about Markdown&#8217;s own syntax.</p>
<h3>Horizontal Rules</h3>
<p>You can produce a horizontal rule tag (`&lt;hr /&gt;`) by placing three or more hyphens, asterisks, or underscores on a line by themselves. If you wish, you may use spaces between the hyphens or asterisks. Each of the following lines will produce a horizontal rule: </p>
<blockquote>
<pre> * * *
 ***
 *****
 - - -
 ---------------------------------------</pre>
</blockquote>
<h2>Span Elements</h2>
<h3>Links</h3>
<p>supports two style of links: <i>inline</i> and <i>reference</i> </p>
<p> In both styles, the link text is delimited by [square brackets]. </p>
<p> To create an inline link, use a set of regular parentheses immediately after the link text&#8217;s closing square bracket. Inside the parentheses, put the URL where you want the link to point, along with an *optional* title for the link, surrounded in quotes. For example: </p>
<blockquote>
<pre> This is [an example](<a rel="nofollow" href="http://example.com/">http://example.com/</a> &quot;Title&quot;) inline link.
 [This link](<a rel="nofollow" href="http://example.net/)">http://example.net/)</a> has no title attribute.</pre>
</blockquote>
<p> Will produce: </p>
<blockquote>
<pre> &lt;p&gt;This is &lt;a href=&quot;<a rel="nofollow" href="http://example.com/">http://example.com/</a>&quot; title=&quot;Title&quot;&gt;
 an example&lt;/a&gt; inline link.&lt;/p&gt;
 &lt;p&gt;&lt;a href=&quot;<a rel="nofollow" href="http://example.net/">http://example.net/</a>&quot;&gt;This link&lt;/a&gt; has no
 title attribute.&lt;/p&gt;</pre>
</blockquote>
<p> If you&#8217;re referring to a local resource on the same server, you can use relative paths: </p>
<blockquote>
<pre> See my [About](/about/) page for details. </pre>
</blockquote>
<p> Reference-style links use a second set of square brackets, inside which you place a label of your choosing to identify the link: </p>
<blockquote>
<pre> This is [an example][id] reference-style link.</pre>
</blockquote>
<p> You can optionally use a space to separate the sets of brackets: </p>
<blockquote>
<pre> This is [an example] [id] reference-style link.</pre>
</blockquote>
<p> Then, anywhere in the document, you define your link label like this, on a line by itself: </p>
<blockquote>
<pre> [id]: <a rel="nofollow" href="http://example.com/">http://example.com/</a> &quot;Optional Title Here&quot;</pre>
</blockquote>
<p> That is: </p>
<ul>
<li> Square brackets containing the link identifier (optionally indented from the left margin using up to three spaces);
<li> followed by a colon;
<li> followed by one or more spaces (or tabs);
<li> followed by the URL for the link;
<li> optionally followed by a title attribute for the link, enclosed in double or single quotes, or enclosed in parentheses. </ul>
<p> The following three link definitions are equivalent: </p>
<blockquote>
<pre> [foo]: <a rel="nofollow" href="http://example.com/">http://example.com/</a> &quot;Optional Title Here&quot;
 [foo]: <a rel="nofollow" href="http://example.com/">http://example.com/</a> 'Optional Title Here'
 [foo]: <a rel="nofollow" href="http://example.com/">http://example.com/</a> (Optional Title Here)</pre>
</blockquote>
<p> <i>Note</i> There is a known bug in Markdown.pl 1.0.1 which prevents single quotes from being used to delimit link titles. </p>
<p> The link URL may, optionally, be surrounded by angle brackets: </p>
<blockquote>
<pre> [id]: &lt;<a rel="nofollow" href="http://example.com/">http://example.com/</a>&gt; &quot;Optional Title Here&quot;</pre>
</blockquote>
<p> You can put the title attribute on the next line and use extra spaces or tabs for padding, which tends to look better with longer URLs: </p>
<blockquote>
<pre> [id]: <a rel="nofollow" href="http://example.com/longish/path/to/resource/here">http://example.com/longish/path/to/resource/here</a>
 &quot;Optional Title Here&quot;</pre>
</blockquote>
<p> Link definitions are only used for creating links during Markdown processing, and are stripped from your document in the HTML output. </p>
<p> Link definition names may constist of letters, numbers, spaces, and punctuation &#8212; but they are <i>not</i> case sensitive. E.g. these two links: </p>
<blockquote>
<pre> [link text][a]
 [link text][A]</pre>
</blockquote>
<p> are equivalent. </p>
<p> The <i>implicit link name</i> shortcut allows you to omit the name of the link, in which case the link text itself is used as the name. Just use an empty set of square brackets &#8212; e.g., to link the word Qq Google to the google.com web site, you could simply write: </p>
<blockquote>
<pre> [Google][]</pre>
</blockquote>
<p> And then define the link: </p>
<blockquote>
<pre> [Google]: <a rel="nofollow" href="http://google.com/">http://google.com/</a></pre>
</blockquote>
<p> Because link names may contain spaces, this shortcut even works for multiple words in the link text: </p>
<blockquote>
<pre> Visit [Daring Fireball][] for more information.</pre>
</blockquote>
<p> And then define the link: </p>
<blockquote>
<pre> [Daring Fireball]: <a rel="nofollow" href="http://daringfireball.net/">http://daringfireball.net/</a></pre>
</blockquote>
<p> Link definitions can be placed anywhere in your Markdown document. I tend to put them immediately after each paragraph in which they&#8217;re used, but if you want, you can put them all at the end of your document, sort of like footnotes. </p>
<p> Here&#8217;s an example of reference links in action: </p>
<blockquote>
<pre> I get 10 times more traffic from [Google] [1] than from
 [Yahoo] [2] or [MSN] [3].
 [1]: <a rel="nofollow" href="http://google.com/">http://google.com/</a> &quot;Google&quot;
 [2]: <a rel="nofollow" href="http://search.yahoo.com/">http://search.yahoo.com/</a> &quot;Yahoo Search&quot;
 [3]: <a rel="nofollow" href="http://search.msn.com/">http://search.msn.com/</a> &quot;MSN Search&quot;</pre>
</blockquote>
<p> Using the implicit link name shortcut, you could instead write: </p>
<blockquote>
<pre> I get 10 times more traffic from [Google][] than from
 [Yahoo][] or [MSN][].
 [google]: <a rel="nofollow" href="http://google.com/">http://google.com/</a> &quot;Google&quot;
 [yahoo]: <a rel="nofollow" href="http://search.yahoo.com/">http://search.yahoo.com/</a> &quot;Yahoo Search&quot;
 [msn]: <a rel="nofollow" href="http://search.msn.com/">http://search.msn.com/</a> &quot;MSN Search&quot;</pre>
</blockquote>
<p> Both of the above examples will produce the following HTML output: </p>
<blockquote>
<pre> &lt;p&gt;I get 10 times more traffic from &lt;a href=&quot;<a rel="nofollow" href="http://google.com/">http://google.com/</a>&quot;
 title=&quot;Google&quot;&gt;Google&lt;/a&gt; than from
 &lt;a href=&quot;<a rel="nofollow" href="http://search.yahoo.com/">http://search.yahoo.com/</a>&quot; title=&quot;Yahoo Search&quot;&gt;Yahoo&lt;/a&gt;
 or
 &lt;a href=&quot;<a rel="nofollow" href="http://search.msn.com/">http://search.msn.com/</a>&quot; title=&quot;MSN Search&quot;&gt;MSN&lt;/a&gt;.&lt;/p&gt;</pre>
</blockquote>
<p> For comparison, here is the same paragraph written using Markdown&#8217;s inline link style: </p>
<blockquote>
<pre> I get 10 times more traffic from
 [Google](<a rel="nofollow" href="http://google.com/">http://google.com/</a> &quot;Google&quot;) than from
 [Yahoo](<a rel="nofollow" href="http://search.yahoo.com/">http://search.yahoo.com/</a> &quot;Yahoo Search&quot;) or
 [MSN](<a rel="nofollow" href="http://search.msn.com/">http://search.msn.com/</a> &quot;MSN Search&quot;).</pre>
</blockquote>
<p> The point of reference-style links is not that they&#8217;re easier to write. The point is that with reference-style links, your document source is vastly more readable. Compare the above examples: using reference-style links, the paragraph itself is only 81 characters long; with inline-style links, it&#8217;s 176 characters; and as raw HTML, it&#8217;s 234 characters. In the raw HTML, there&#8217;s more markup than there is text. </p>
<p> With Markdown&#8217;s reference-style links, a source document much more closely resembles the final output, as rendered in a browser. By allowing you to move the markup-related metadata out of the paragraph, you can add links without interrupting the narrative flow of your prose.</p>
<h3>Emphasis</h3>
<p>Markdown treats asterisks (`*`) and underscores (`_`) as indicators of emphasis. Text wrapped with one `*` or `_` will be wrapped with an HTML `&lt;em&gt;` tag; double `*`&#8217;s or `_`&#8217;s will be wrapped with an HTML `&lt;strong&gt;` tag. E.g., this input: </p>
<blockquote>
<pre> *single asterisks*
 _single underscores_
 **double asterisks**
 __double underscores__</pre>
</blockquote>
<p> will produce: </p>
<blockquote>
<pre> &lt;em&gt;single asterisks&lt;/em&gt;
 &lt;em&gt;single underscores&lt;/em&gt;
 &lt;strong&gt;double asterisks&lt;/strong&gt;
 &lt;strong&gt;double underscores&lt;/strong&gt;</pre>
</blockquote>
<p> You can use whichever style you prefer; the lone restriction is that the same character must be used to open and close an emphasis span. </p>
<p> Emphasis can be used in the middle of a word: </p>
<blockquote>
<pre> un*fucking*believable</pre>
</blockquote>
<p> But if you surround an `*` or `_` with spaces, it&#8217;ll be treated as a literal asterisk or underscore. </p>
<p> To produce a literal asterisk or underscore at a position where it would otherwise be used as an emphasis delimiter, you can backslash escape it: </p>
<blockquote>
<pre> \*this text is surrounded by literal asterisks\*</pre>
</blockquote>
<h3>Code</h3>
<p>To indicate a span of code, wrap it with backtick quotes (&#8220; ` &#8220;). Unlike a pre-formatted code block, a code span indicates code within a normal paragraph. For example: </p>
<blockquote>
<pre> Use the `printf()` function.</pre>
</blockquote>
<p> will produce: </p>
<blockquote>
<pre> &lt;p&gt;Use the &lt;code&gt;printf()&lt;/code&gt; function.&lt;/p&gt;</pre>
</blockquote>
<p> To include a literal backtick character within a code span, you can use multiple backticks as the opening and closing delimiters: </p>
<blockquote>
<pre> ``There is a literal backtick (`) here.``</pre>
</blockquote>
<p> which will produce this: </p>
<blockquote>
<pre> &lt;p&gt;&lt;code&gt;There is a literal backtick (`) here.&lt;/code&gt;&lt;/p&gt;</pre>
</blockquote>
<p> The backtick delimiters surrounding a code span may include spaces &#8212; one after the opening, one before the closing. This allows you to place literal backtick characters at the beginning or end of a code span: </p>
<blockquote>
<pre> A single backtick in a code span: `` ` ``
 
 A backtick-delimited string in a code span: `` `foo` ``</pre>
</blockquote>
<p> will produce: </p>
<blockquote>
<pre> &lt;p&gt;A single backtick in a code span: &lt;code&gt;`&lt;/code&gt;&lt;/p&gt;
 
 &lt;p&gt;A backtick-delimited string in a code span: &lt;code&gt;`foo`&lt;/code&gt;&lt;/p&gt;</pre>
</blockquote>
<p> With a code span, ampersands and angle brackets are encoded as HTML entities automatically, which makes it easy to include example HTML tags. Markdown will turn this: </p>
<blockquote>
<pre> Please don't use any `&lt;blink&gt;` tags.</pre>
</blockquote>
<p> into: </p>
<blockquote>
<pre> &lt;p&gt;Please don't use any &lt;code&gt;&amp;lt;blink&amp;gt;&lt;/code&gt; tags.&lt;/p&gt;</pre>
</blockquote>
<p> You can write this: </p>
<blockquote>
<pre> `&amp;#8212;` is the decimal-encoded equivalent of `&amp;mdash;`.</pre>
</blockquote>
<p> to produce: </p>
<blockquote>
<pre> &lt;p&gt;&lt;code&gt;&amp;amp;#8212;&lt;/code&gt; is the decimal-encoded
 equivalent of &lt;code&gt;&amp;amp;mdash;&lt;/code&gt;.&lt;/p&gt;</pre>
</blockquote>
<h3>Images</h3>
<p>Admittedly, it&#8217;s fairly difficult to devise a Qq natural syntax for placing images into a plain text document format. </p>
<p> Markdown uses an image syntax that is intended to resemble the syntax for links, allowing for two styles: <i>inline</i> and <i>reference</i> </p>
<p> Inline image syntax looks like this: </p>
<blockquote>
<pre> ![Alt text](/path/to/img.jpg)
 ![Alt text](/path/to/img.jpg =Optional size &quot;Optional title&quot;)</pre>
</blockquote>
<p> That is: </p>
<ul>
<li> An exclamation mark: `!`;
<li> followed by a set of square brackets, containing the `alt` attribute text for the image;
<li> followed by a set of parentheses, containing the URL or path to the image, an optional `size` attribute (in <i>width </i><code>c </code><i>height</i> format) prefixed with a `=`, and an optional `title` attribute enclosed in double or single quotes. </ul>
<p> Reference-style image syntax looks like this: </p>
<blockquote>
<pre> ![Alt text][id]</pre>
</blockquote>
<p> Where Qq id is the name of a defined image reference. Image references are defined using syntax identical to link references: </p>
<blockquote>
<pre> [id]: url/to/image =Optional size &quot;Optional title attribute&quot;</pre>
</blockquote>
<h2>Miscellaneous</h2>
<h3>Automatic Links</h3>
<p>supports a shortcut style for creating Qq automatic links for URLs and email addresses: simply surround the URL or email address with angle brackets. What this means is that if you want to<br />
&nbsp;<wbr>show the actual text of a URL or email address, and also have it be<br />
&nbsp;<wbr>&nbsp;<wbr>a clickable link, you can do this: </p>
<blockquote>
<pre> &lt;<a rel="nofollow" href="http://example.com/">http://example.com/</a>&gt;</pre>
</blockquote>
<p> will turn this into: </p>
<blockquote>
<pre> &lt;a href=&quot;<a rel="nofollow" href="http://example.com/">http://example.com/</a>&quot;&gt;<a href="http://example.com/">http://example.com/</a>&lt;/a&gt;</pre>
</blockquote>
<p> Automatic links for email addresses work similarly, except that Markdown will also perform a bit of randomized decimal and hex entity-encoding to help obscure your address from address-harvesting spambots. For example, Markdown will turn this: </p>
<blockquote>
<pre> &lt;address [at] example.com&gt;</pre>
</blockquote>
<p> into something like this: </p>
<blockquote>
<pre> &lt;a href=&quot;&amp;#x6D;&amp;#x61;i&amp;#x6C;&amp;#x74;&amp;#x6F;:&amp;#x61;&amp;#x64;&amp;#x64;&amp;#x72;&amp;#x65;
 &amp;#115;&amp;#115;&amp;#64;&amp;#101;&amp;#120;&amp;#x61;&amp;#109;&amp;#x70;&amp;#x6C;e&amp;#x2E;&amp;#99;&amp;#111;
 &amp;#109;&quot;&gt;&amp;#x61;&amp;#x64;&amp;#x64;&amp;#x72;&amp;#x65;&amp;#115;&amp;#115;&amp;#64;&amp;#101;&amp;#120;&amp;#x61;
 &amp;#109;&amp;#x70;&amp;#x6C;e&amp;#x2E;&amp;#99;&amp;#111;&amp;#109;&lt;/a&gt;</pre>
</blockquote>
<p> which will render in a browser as a clickable link to Qq address [at] example.com . </p>
<p> (This sort of entity-encoding trick will indeed fool many, if not most, address-harvesting bots, but it definitely won&#8217;t fool all of them. It&#8217;s better than nothing, but an address published in this way will probably eventually start receiving spam.)</p>
<h3>Backslash Escapes</h3>
<p>allows you to use backslash escapes to generate literal characters which would otherwise have special meaning in Markdown&#8217;s formatting syntax. For example, if you wanted to surround a word with literal asterisks (instead of an HTML `&lt;em&gt;` tag), you add backslashes before the asterisks, like this: </p>
<blockquote>
<pre> \*literal asterisks\*</pre>
</blockquote>
<p> provides backslash escapes for the following characters:</p>
<dl>
<dt><code>backslash</code></p>
<dd>
<dt><code>`</code></p>
<dd>backtick</p>
<dt><code>*</code></p>
<dd>asterisk</p>
<dt><code>_</code></p>
<dd>underscore</p>
<dd>curly braces</p>
<dt><code>[]</code></p>
<dd>square brackets</p>
<dt><code>()</code></p>
<dd>parentheses</p>
<dt><code>#</code></p>
<dd>hash mark</p>
<dt><code>+</code></p>
<dd>plus sign</p>
<dt><code>&#8211;</code></p>
<dd>minus sign (hyphen)</p>
<dt><code>.</code></p>
<dd>dot</p>
<dd>exclamation mark</dl>
<h2>Bugs</h2>
<p>assumes that tabs are set to 4 spaces.</p>
<h2>Author</h2>
<p>John Gruber <i><a rel="nofollow" href="http://daringfireball.net/">http://daringfireball.net/</a></i></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-markdown/">markdown</a>(1), <a href="/docs/linux/man/3-markdown/">markdown</a>(3), mkd-callbacks3, mkd-functions3, mkd-extensions7. <i><a rel="nofollow" href="http://daringfireball.net/projects/markdown">http://daringfireball.net/projects/markdown</a></i><br />
 <i><a rel="nofollow" href="http://docutils.sourceforge.net/mirror/setext.html">http://docutils.sourceforge.net/mirror/setext.html</a></i><br />
 <i><a rel="nofollow" href="http://www.aaronsw.com/2002/atx/">http://www.aaronsw.com/2002/atx/</a></i><br />
 <i><a rel="nofollow" href="http://textism.com/tools/textile/">http://textism.com/tools/textile/</a></i><br />
 <i><a rel="nofollow" href="http://docutils.sourceforge.net/rst.html">http://docutils.sourceforge.net/rst.html</a></i><br />
 <i><a rel="nofollow" href="http://www.triptico.com/software/grutatxt.html">http://www.triptico.com/software/grutatxt.html</a></i><br />
 <i><a rel="nofollow" href="http://ettext.taint.org/doc/">http://ettext.taint.org/doc/</a></i> </p>
