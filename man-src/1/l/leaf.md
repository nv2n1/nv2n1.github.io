---
title: "leaf(1)"
name: "leaf"
section: "1"
letter: "l"
url: "/docs/linux/man/1-leaf/"
description: "leaf – Lightweight Editor of Ascii(and more) Files"
---

<h2 class="name">NAME</h2>
<p> leaf &#8211; Lightweight Editor of Ascii(and more) Files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>leaf</code> [-f] [-d&nbsp;<wbr><i>dictionary</i>] [+<i>n</i>] [<i>filename</i>]</dl>
<h2>USAGE</h2>
<p> <code>leaf</code></p>
<dd>is a simple console text file editor, with paragraph word-wrapping and spell checking. <code>leaf</code> is based on the text editor in the Cone mail reader and composer. <code>leaf</code> opens <i>filename</i>, positioning the cursor on the first line, or line #<i>n</i>, if specified. </p>
<p> This is not really the best editor for program sources. <code>leaf</code> is meant to be used as a quick editor for writing short notes and memos. As text is typed, words will automatically flow to wrap within a typical 80-character terminal display, even on larger display (due to <code>leaf</code>&#8216;s heritage as an editor for E-mail messages, which are traditionally formatted to fit an 80-character display). Word wrapping is &quot;lazy&quot;: only long text lines are wrapped. Short text lines are not folded together. Individual paragraphs are separated by blank lines of text. Press CTRL-J to optimally rejustify the paragraph under the cursor. The bottom two lines on the screen list which keys to press for other functions.</p>
<h3>Flowed text</h3>
<p> The <code>-f</code> option enables &#8220;flowed text&#8221; formatting convention. Plain text files have no explicit means for joining multiple lines into logical paragraph. Each line of text is an individual line, and a blank line marks the end of a paragraph. </p>
<p> In a &#8220;flowed text&#8221; formatted file, each line in a paragraph except the last one ends with a space character. This makes no visual difference, it&#8217;s just a marker that this line should be merged with the next line. The last line in the paragraph does not end in a space character. </p>
<p> The trailing space character is logically removed from each flowed line, and all flowed lines are merged into a logical paragraph that can be adjusted to any display width. It&#8217;s important to note that text written in non-ideographic languages, where individual words are separated by spaces, will have two space characters at the end of every line: the space character that separates the last word on the line from the first word on the next line, and the a second space character that marks the line as a flowed line. </p>
<p> Because the trailing space marking a flowed line is logically removed, without the second space character there will not be a logical space between the two words, and if the paragraph&#8217;s width is adjusted for display the two words may get combined together. </p>
<p> The <code>-f</code> option puts <code>leaf</code> into flowed text mode, removing spaces from each flowed line of text in an opened file. A flowed line is marked on the screen with a &quot;&lt;&quot; character in the right margin (or a small &quot;next line&quot; character on a UTF-8 display). When saving a file <code>leaf</code> automatically adds a trailing space to each line that&#8217;s marked as flowed. </p>
<p> The flowed text mode stays in effect for each file opened in <code>leaf</code>. When opening another file, press CTRL-F to turn flowed mode on or off for the next file. This change stays in effect until it gets toggled again. </p>
<p> Pressing CTRL-J optimally rejustifies the text in flowed text mode. <code>leaf</code> heuristically determines the start and the end of the paragraph, readjusts the width of the paragraph, and marks each line as flowed, except the last paragraph line. <code>leaf</code> uses a unicode-based algorithm for determining whether the last character line needs a space character, in addition to the flowed space marker. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> <code>leaf</code> is frequently used to edit plain text email message content. Because email messages assign some semantical meaning to lines of text that start with spaces or &quot;&gt;&quot; characters, CTRL-J will not rejustify lines of text that begin with a &quot;&gt;&quot; or a space. These lines will be considered paragraph boundaries, in addition to blank lines. </p>
</dl>
<h3>Spell checking</h3>
<p> The <code>-d</code> option sets the name of the dictionary used for spell checking (overriding the default spell checking dictionary set by the <code>DICTIONARY</code> environment variable). <code>+</code><i>n</i> sets the initial cursor position to line #<i>n</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1), <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Sam Varshavchik</code></p>
<dl>
<dt>
<dd></dl>
<h2>Index</h2>
