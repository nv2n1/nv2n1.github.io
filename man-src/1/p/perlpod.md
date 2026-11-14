---
title: "perlpod(1)"
name: "perlpod"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlpod/"
---

<h2 class="name">NAME</h2>
 

 perlpod - the Plain Old Documentation format 

<h2>DESCRIPTION</h2>

 Pod is a simple-to-use markup language used for writing documentation for Perl, Perl programs, and Perl modules. 

 Translators are available for converting Pod to various formats like plain text, <font SIZE="-1">HTML,</font> man pages, and more. 

 Pod markup consists of three basic kinds of paragraphs: ordinary, verbatim, and command.

<h3>Ordinary Paragraph</h3>

 Most paragraphs in your documentation will be ordinary blocks of text, like this one. You can simply type in your text without any markup whatsoever, and with just a blank line before and after. When it gets formatted, it will undergo minimal formatting, like being rewrapped, probably put into a proportionally spaced font, and maybe even justified. 

 You can use formatting codes in ordinary paragraphs, for <b>bold</b>, <i>italic</i>, <tt>&quot;code-style&quot;</tt>, hyperlinks, and more. Such codes are explained in the &quot;Formatting Codes&quot; section, below.

<h3>Verbatim Paragraph</h3>

 Verbatim paragraphs are usually used for presenting a codeblock or other text which does not require any special parsing or formatting, and which shouldn't be wrapped. 

 A verbatim paragraph is distinguished by having its first character be a space or a tab. (And commonly, all its lines begin with spaces and/or tabs.) It should be reproduced exactly, with tabs assumed to be on 8-column boundaries. There are no special formatting codes, so you can't italicize or anything like that. A \ means \, and nothing else.

<h3>Command Paragraph</h3>

 A command paragraph is used for special treatment of whole chunks of text, usually as headings or parts of lists. 

 All command paragraphs (which are typically only one line long) start with ``='', followed by an identifier, followed by arbitrary text that the command can use however it pleases. Currently recognized commands are 

 <pre>
    =pod
    =head1 Heading Text
    =head2 Heading Text
    =head3 Heading Text
    =head4 Heading Text
    =over indentlevel
    =item stuff
    =back
    =begin format
    =end format
    =for format text...
    =encoding type
    =cut
</pre> 

 To explain them each in detail:
<dl>
<dt>&quot;=head1 <i>Heading Text</i>&quot;
<dd>
<dt>&quot;=head2 <i>Heading Text</i>&quot;
<dd>
<dt>&quot;=head3 <i>Heading Text</i>&quot;
<dd>
<dt>&quot;=head4 <i>Heading Text</i>&quot;
<dd> Head1 through head4 produce headings, head1 being the highest level. The text in the rest of this paragraph is the content of the heading. For example: 

 <pre>
  =head2 Object Attributes
</pre> 

 The text ``Object Attributes'' comprises the heading there. The text in these heading commands can use formatting codes, as seen here: 

 <pre>
  =head2 Possible Values for C&lt;$/&gt;
</pre> 

 Such commands are explained in the &quot;Formatting Codes&quot; section, below.
<dt>&quot;=over <i>indentlevel</i>&quot;
<dd>
<dt>&quot;=item <i>stuff...</i>&quot;
<dd>
<dt>&quot;=back&quot;
<dd> Item, over, and back require a little more explanation: ``=over'' starts a region specifically for the generation of a list using ``=item'' commands, or for indenting (groups of) normal paragraphs. At the end of your list, use ``=back'' to end it. The <i>indentlevel</i> option to ``=over'' indicates how far over to indent, generally in ems (where one em is the width of an ``M'' in the document's base font) or roughly comparable units; if there is no <i>indentlevel</i> option, it defaults to four. (And some formatters may just ignore whatever <i>indentlevel</i> you provide.) In the <i>stuff</i> in <tt>&quot;=item </tt>stuff...<tt>&quot;</tt>, you may use formatting codes, as seen here: 

 <pre>
  =item Using C&lt;$|&gt; to Control Buffering
</pre> 

 Such commands are explained in the &quot;Formatting Codes&quot; section, below. 

 Note also that there are some basic rules to using ``=over'' ... ``=back'' regions:
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> Don't use ``=item''s outside of an ``=over'' ... ``=back'' region.
<dt>&bull;
<dd> The first thing after the ``=over'' command should be an ``=item'', unless there aren't going to be any items at all in this ``=over'' ... ``=back'' region.
<dt>&bull;
<dd> Don't put &quot;=head<i>n</i>`` commands inside an ''=over`` ... ''=back&quot; region.
<dt>&bull;
<dd> And perhaps most importantly, keep the items consistent: either use ``=item *'' for all of them, to produce bullets; or use ``=item 1.'', ``=item 2.'', etc., to produce numbered lists; or use ``=item foo'', ``=item bar'', etc.--namely, things that look nothing like bullets or numbers. 

 If you start with bullets or numbers, stick with them, as formatters use the first ``=item'' type to decide how to format the list.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>&quot;=cut&quot;
<dd> To end a Pod block, use a blank line, then a line beginning with ``=cut'', and a blank line after it. This lets Perl (and the Pod formatter) know that this is where Perl code is resuming. (The blank line before the ``=cut'' is not technically necessary, but many older Pod processors require it.)
<dt>&quot;=pod&quot;
<dd> The ``=pod'' command by itself doesn't do much of anything, but it signals to Perl (and Pod formatters) that a Pod block starts here. A Pod block starts with <i>any</i> command paragraph, so a ``=pod'' command is usually used just when you want to start a Pod block with an ordinary paragraph or a verbatim paragraph. For example: 

 <pre><code>
= item stuff()
      This function does stuff.= cut
    sub stuff{
        ...} = pod Remember to check its return value,
                         as in : stuff() || die "Couldn't do stuff!";
= cut
</code></pre>
<dt>&quot;=begin <i>formatname</i>&quot;
<dd>
<dt>&quot;=end <i>formatname</i>&quot;
<dd>
<dt>&quot;=for <i>formatname</i> <i>text...</i>&quot;
<dd> For, begin, and end will let you have regions of text/code/data that are not generally interpreted as normal Pod text, but are passed directly to particular formatters, or are otherwise special. A formatter that can use that format will use the region, otherwise it will be completely ignored. 

 A command &quot;=begin <i>formatname</i>``, some paragraphs, and a command ''=end <i>formatname</i>&quot;, mean that the text/data in between is meant for formatters that understand the special format called <i>formatname</i>. For example, 

 <pre>
  =begin html
  &lt;hr&gt; &lt;img src=&quot;thang.png&quot;&gt;
  &lt;p&gt; This is a raw HTML paragraph &lt;/p&gt;
  =end html
</pre> 

 The command &quot;=for <i>formatname</i> <i>text...</i>&quot; specifies that the remainder of just this paragraph (starting right after <i>formatname</i>) is in that special format. 

 <pre>
  =for html &lt;hr&gt; &lt;img src=&quot;thang.png&quot;&gt;
  &lt;p&gt; This is a raw HTML paragraph &lt;/p&gt;
</pre> 

 This means the same thing as the above ``=begin html'' ... ``=end html'' region. 

 That is, with ``=for'', you can have only one paragraph's worth of text (i.e., the text in ``=foo targetname text...''), but with ``=begin targetname'' ... ``=end targetname'', you can have any amount of stuff in between. (Note that there still must be a blank line after the ``=begin'' command and a blank line before the ``=end'' command.) 

 Here are some examples of how to use these: 

 
= begin html&lt;br&gt; Figure 1. &lt; br &gt; &lt;IMG SRC = "figure1.png"&gt;&lt;br&gt; = end html = begin text-- -- -- -- -- -- -- - | foo |
                                                                             | bar |
                                                                             -- -- -- -- -- -- -- -^^^^Figure 1. ^ ^^^ = end text
 

 Some format names that formatters currently are known to accept include ``roff'', ``man'', ``latex'', ``tex'', ``text'', and ``html''. (Some formatters will treat some of these as synonyms.) 

 A format name of ``comment'' is common for just making notes (presumably to yourself) that won't appear in any formatted version of the Pod document: 

 <pre>
  =for comment
  Make sure that all the available options are documented!
</pre> 

 Some <i>formatnames</i> will require a leading colon (as in <tt>&quot;=for :formatname&quot;</tt>, or <tt>&quot;=begin :formatname&quot; ... &quot;=end :formatname&quot;</tt>), to signal that the text is not raw data, but instead <i>is</i> Pod text (i.e., possibly containing formatting codes) that's just not for normal formatting (e.g., may not be a normal-use paragraph, but might be for formatting as a footnote).
<dt>&quot;=encoding <i>encodingname</i>&quot;
<dd> This command is used for declaring the encoding of a document. Most users won't need this; but if your encoding isn't US-ASCII, then put a <tt>&quot;=encoding </tt>encodingname<tt>&quot;</tt> command very early in the document so that pod formatters will know how to decode the document. For <i>encodingname</i>, use a name recognized by the Encode::Supported module. Some pod formatters may try to guess between a Latin-1 or <font SIZE="-1">CP-1252</font> versus <font SIZE="-1">UTF-8</font> encoding, but they may guess wrong. It's best to be explicit if you use anything besides strict <font SIZE="-1">ASCII.</font> Examples: 

 <pre>
  =encoding latin1
  =encoding utf8
  =encoding koi8-r
  =encoding ShiftJIS
  =encoding big5
</pre> 

 <tt>&quot;=encoding&quot;</tt> affects the whole document, and must occur only once.</dl>
 

 And don't forget, all commands but <tt>&quot;=encoding&quot;</tt> last up until the end of its <i>paragraph</i>, not its line. So in the examples below, you can see that every command needs the blank line after it, to end its paragraph. (And some older Pod translators may require the <tt>&quot;=encoding&quot;</tt> line to have a following blank line as well, even though it should be legal to omit.) 

 Some examples of lists include: 

 <pre>
  =over
  =item *
  First item
  =item *
  Second item
  =back
  =over
  =item Foo()
  Description of Foo function
  =item Bar()
  Description of Bar function
  =back
</pre>

<h3>Formatting Codes</h3>

 In ordinary paragraphs and in some command paragraphs, various formatting codes (a.k.a. ``interior sequences'') can be used:
<dl>
<dt>&quot;I&lt;text&gt;&quot; --- italic text
<dd> Used for emphasis (&quot;<tt>&quot;be I&lt;careful!&gt;&quot;</tt>``) and parameters (''<tt>&quot;redo I&lt;LABEL&gt;&quot;</tt>&quot;)
<dt>&quot;B&lt;text&gt;&quot; --- bold text
<dd> Used for switches (&quot;<tt>&quot;perl's B&lt;-n&gt; switch&quot;</tt>``), programs (''<tt>&quot;some systems provide a B&lt;chfn&gt; for that&quot;</tt>``), emphasis (''<tt>&quot;be B&lt;careful!&gt;&quot;</tt>``), and so on (''<tt>&quot;and that feature is known as B&lt;autovivification&gt;&quot;</tt>&quot;).
<dt>&quot;C&lt;code&gt;&quot; --- code text
<dd> Renders code in a typewriter font, or gives some other indication that this represents program text (&quot;<tt>&quot;C&lt;gmtime($^T)&gt;&quot;</tt>``) or some other form of computerese (''<tt>&quot;C&lt;drwxr-xr-x&gt;&quot;</tt>&quot;).
<dt>&quot;L&lt;name&gt;&quot; --- a hyperlink
<dd> There are various syntaxes, listed below. In the syntaxes given, <tt>&quot;text&quot;</tt>, <tt>&quot;name&quot;</tt>, and <tt>&quot;section&quot;</tt> cannot contain the characters '/' and '|'; and any '&lt;' or '&gt;' should be matched.
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> <tt>&quot;L&lt;name&gt;&quot;</tt> 

 Link to a Perl manual page (e.g., <tt>&quot;L&lt;Net::Ping&gt;&quot;</tt>). Note that <tt>&quot;name&quot;</tt> should not contain spaces. This syntax is also occasionally used for references to Unix man pages, as in <tt>&quot;L&lt;<a HREF="/docs/linux/man/5-crontab/">crontab</a>(5)&gt;&quot;</tt>.
<dt>&bull;
<dd> <tt>&quot;L&lt;name/&quot;sec&quot;&gt;&quot;</tt> or <tt>&quot;L&lt;name/sec&gt;&quot;</tt> 

 Link to a section in other manual page. E.g., <tt>&quot;L&lt;perlsyn/&quot;For Loops&quot;&gt;&quot;</tt>
<dt>&bull;
<dd> <tt>&quot;L&lt;/&quot;sec&quot;&gt;&quot;</tt> or <tt>&quot;L&lt;/sec&gt;&quot;</tt> 

 Link to a section in this manual page. E.g., <tt>&quot;L&lt;/&quot;Object Methods&quot;&gt;&quot;</tt></dl>
</dl>

<dl>
<dt>
<dd> 

 A section is started by the named heading or item. For example, <tt>&quot;L&lt;perlvar/$.&gt;&quot;</tt> or <tt>&quot;L&lt;perlvar/&quot;$.&quot;&gt;&quot;</tt> both link to the section started by &quot;<tt>&quot;=item $.&quot;</tt>&quot; in perlvar. And <tt>&quot;L&lt;perlsyn/For Loops&gt;&quot;</tt> or <tt>&quot;L&lt;perlsyn/&quot;For Loops&quot;&gt;&quot;</tt> both link to the section started by &quot;<tt>&quot;=head2 For Loops&quot;</tt>&quot; in perlsyn. 

 To control what text is used for display, you use &quot;<tt>&quot;L&lt;text|...&gt;&quot;</tt>&quot;, as in:
<dl>
<dt>&bull;
<dd> <tt>&quot;L&lt;text|name&gt;&quot;</tt> 

 Link this text to that manual page. E.g., <tt>&quot;L&lt;Perl Error Messages|perldiag&gt;&quot;</tt>
<dt>&bull;
<dd> <tt>&quot;L&lt;text|name/&quot;sec&quot;&gt;&quot;</tt> or <tt>&quot;L&lt;text|name/sec&gt;&quot;</tt> 

 Link this text to that section in that manual page. E.g., <tt>&quot;L&lt;postfix &quot;if&quot;|perlsyn/&quot;Statement Modifiers&quot;&gt;&quot;</tt>
<dt>&bull;
<dd> <tt>&quot;L&lt;text|/&quot;sec&quot;&gt;&quot;</tt> or <tt>&quot;L&lt;text|/sec&gt;&quot;</tt> or <tt>&quot;L&lt;text|&quot;sec&quot;&gt;&quot;</tt> 

 Link this text to that section in this manual page. E.g., <tt>&quot;L&lt;the various attributes|/&quot;Member Data&quot;&gt;&quot;</tt></dl>
</dl>

<dl>
<dt>
<dd> 

 Or you can link to a web page:
<dl>
<dt>&bull;
<dd> <tt>&quot;L&lt;scheme:...&gt;&quot;</tt> 

 <tt>&quot;L&lt;text|scheme:...&gt;&quot;</tt> 

 Links to an absolute <font SIZE="-1">URL.</font> For example, <tt>&quot;L&lt;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&gt;&quot;</tt> or <tt>&quot;L&lt;The Perl Home Page|<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&gt;&quot;</tt>.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>&quot;E&lt;escape&gt;&quot; --- a character escape
<dd> Very similar to <font SIZE="-1">HTML/XML</font> <tt>&quot;&amp;</tt>foo<tt>;&quot;</tt> ``entity references'':
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> <tt>&quot;E&lt;lt&gt;&quot;</tt> --- a literal &lt; (less than)
<dt>&bull;
<dd> <tt>&quot;E&lt;gt&gt;&quot;</tt> --- a literal &gt; (greater than)
<dt>&bull;
<dd> <tt>&quot;E&lt;verbar&gt;&quot;</tt> --- a literal | (<i>ver</i>tical <i>bar</i>)
<dt>&bull;
<dd> <tt>&quot;E&lt;sol&gt;&quot;</tt> --- a literal / (<i>sol</i>idus) 

 The above four are optional except in other formatting codes, notably <tt>&quot;L&lt;...&gt;&quot;</tt>, and when preceded by a capital letter.
<dt>&bull;
<dd> <tt>&quot;E&lt;htmlname&gt;&quot;</tt> 

 Some non-numeric <font SIZE="-1">HTML</font> entity name, such as <tt>&quot;E&lt;eacute&gt;&quot;</tt>, meaning the same thing as <tt>&quot;&amp;eacute;&quot;</tt> in <font SIZE="-1">HTML</font> --- i.e., a lowercase e with an acute (/-shaped) accent.
<dt>&bull;
<dd> <tt>&quot;E&lt;number&gt;&quot;</tt> 

 The ASCII/Latin-1/Unicode character with that number. A leading ``0x'' means that <i>number</i> is hex, as in <tt>&quot;E&lt;0x201E&gt;&quot;</tt>. A leading ``0'' means that <i>number</i> is octal, as in <tt>&quot;E&lt;075&gt;&quot;</tt>. Otherwise <i>number</i> is interpreted as being in decimal, as in <tt>&quot;E&lt;181&gt;&quot;</tt>. 

 Note that older Pod formatters might not recognize octal or hex numeric escapes, and that many formatters cannot reliably render characters above 255. (Some formatters may even have to use compromised renderings of Latin-1/CP-1252 characters, like rendering <tt>&quot;E&lt;eacute&gt;&quot;</tt> as just a plain ``e''.)</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>&quot;F&lt;filename&gt;&quot; --- used for filenames
<dd> Typically displayed in italics. Example: &quot;<tt>&quot;F&lt;.cshrc&gt;&quot;</tt>&quot;
<dt>&quot;S&lt;text&gt;&quot; --- text contains non-breaking spaces
<dd> This means that the words in <i>text</i> should not be broken across lines. Example: <tt>&quot;S&lt;$x ? $y : $z&gt;&quot;</tt>.
<dt>&quot;X&lt;topic name&gt;&quot; --- an index entry
<dd> This is ignored by most formatters, but some may use it for building indexes. It always renders as empty-string. Example: <tt>&quot;X&lt;absolutizing relative URLs&gt;&quot;</tt>
<dt>&quot;Z&lt;&gt;&quot; --- a null (zero-effect) formatting code
<dd> This is rarely used. It's one way to get around using an E&lt;...&gt; code sometimes. For example, instead of &quot;<tt>&quot;NE&lt;lt&gt;3&quot;</tt>`` (for ''N&lt;3``) you could write ''<tt>&quot;NZ&lt;&gt;&lt;3&quot;</tt>`` (the ''Z&lt;&gt;`` breaks up the ''N`` and the ''&lt;`` so they can't be considered the part of a (fictitious) ''N&lt;...&gt;&quot; code).</dl>
 

 Most of the time, you will need only a single set of angle brackets to delimit the beginning and end of formatting codes. However, sometimes you will want to put a real right angle bracket (a greater-than sign, '&gt;') inside of a formatting code. This is particularly common when using a formatting code to provide a different font-type for a snippet of code. As with all things in Perl, there is more than one way to do it. One way is to simply escape the closing bracket using an <tt>&quot;E&quot;</tt> code: 

 <pre>
    C&lt;$a E&lt;lt&gt;=E&lt;gt&gt; $b&gt;
</pre> 

 This will produce: &quot;<tt>&quot;$a &lt;=&gt; $b&quot;</tt>&quot; 

 A more readable, and perhaps more ``plain'' way is to use an alternate set of delimiters that doesn't require a single ``&gt;'' to be escaped. Doubled angle brackets (``&lt;&lt;'' and ``&gt;&gt;'') may be used <i>if and only if there is whitespace right after the opening delimiter and whitespace right before the closing delimiter!</i> For example, the following will do the trick: 

 <pre>
    C&lt;&lt; $a &lt;=&gt; $b &gt;&gt;
</pre> 

 In fact, you can use as many repeated angle-brackets as you like so long as you have the same number of them in the opening and closing delimiters, and make sure that whitespace immediately follows the last '&lt;' of the opening delimiter, and immediately precedes the first '&gt;' of the closing delimiter. (The whitespace is ignored.) So the following will also work: 

 <pre>
    C&lt;&lt;&lt; $a &lt;=&gt; $b &gt;&gt;&gt;
    C&lt;&lt;&lt;&lt;  $a &lt;=&gt; $b     &gt;&gt;&gt;&gt;
</pre> 

 And they all mean exactly the same as this: 

 <pre>
    C&lt;$a E&lt;lt&gt;=E&lt;gt&gt; $b&gt;
</pre> 

 The multiple-bracket form does not affect the interpretation of the contents of the formatting code, only how it must end. That means that the examples above are also exactly the same as this: 

 <pre>
    C&lt;&lt; $a E&lt;lt&gt;=E&lt;gt&gt; $b &gt;&gt;
</pre> 

 As a further example, this means that if you wanted to put these bits of code in <tt>&quot;C&quot;</tt> (code) style: 

 
open(X, "&gt;&gt;thing.dat") || die $ !$foo-&gt;bar();
 

 you could do it like so: 

 
C&lt;&lt;&lt;open(X, "&gt;&gt;thing.dat") || die $ !&gt;&gt;&gt;
        C &lt;&lt; $foo-&gt;bar();
&gt;&gt;
 

 which is presumably easier to read than the old way: 

 <pre><code>
C&lt;open(X, "E&lt;gt&gt;E&lt;gt&gt;thing.dat") || die $ !&gt;
        C &lt; $foo - E&lt;gt&gt; bar();
&gt;
</code></pre> 

 This is currently supported by pod2text (Pod::Text), pod2man (Pod::Man), and any other pod2xxx or Pod::Xxxx translators that use Pod::Parser 1.093 or later, or Pod::Tree 1.02 or later.

<h3>The Intent</h3>

 The intent is simplicity of use, not power of expression. Paragraphs look like paragraphs (block format), so that they stand out visually, and so that I could run them through <tt>&quot;fmt&quot;</tt> easily to reformat them (that's F7 in my version of <b>vi</b>, or Esc Q in my version of <b>emacs</b>). I wanted the translator to always leave the <tt>&quot;'&quot;</tt> and <tt>&quot;`&quot;</tt> and <tt>&quot;&quot;&quot;</tt> quotes alone, in verbatim mode, so I could slurp in a working program, shift it over four spaces, and have it print out, er, verbatim. And presumably in a monospace font. 

 The Pod format is not necessarily sufficient for writing a book. Pod is just meant to be an idiot-proof common source for nroff, <font SIZE="-1">HTML,</font> TeX, and other markup languages, as used for online documentation. Translators exist for <b>pod2text</b>, <b>pod2html</b>, <b>pod2man</b> (that's for <b><a HREF="/docs/linux/man/1-nroff/">nroff</a></b>(1) and <b><a HREF="/docs/linux/man/1-troff/">troff</a></b>(1)), <b>pod2latex</b>, and <b>pod2fm</b>. Various others are available in <font SIZE="-1">CPAN.</font>

<h3>Embedding Pods in Perl Modules</h3>

 You can embed Pod documentation in your Perl modules and scripts. Start your documentation with an empty line, a ``=head1'' command at the beginning, and end it with a ``=cut'' command and an empty line. The <b>perl</b> executable will ignore the Pod text. You can place a Pod statement where <b>perl</b> expects the beginning of a new statement, but not within a statement, as that would result in an error. See any of the supplied library modules for examples. 

 If you're going to put your Pod at the end of the file, and you're using an <tt>&quot;__END__&quot;</tt> or <tt>&quot;__DATA__&quot;</tt> cut mark, make sure to put an empty line there before the first Pod command. 

 <pre>
  __END__
  =head1 NAME
  Time::Local - efficiently compute time from local and GMT time
</pre> 

 Without that empty line before the ``=head1'', many translators wouldn't have recognized the ``=head1'' as starting a Pod block.

<h3>Hints for Writing Pod</h3>

<dl>
<dt>&bull;
<dd> 

 

 The <b>podchecker</b> command is provided for checking Pod syntax for errors and warnings. For example, it checks for completely blank lines in Pod blocks and for unknown commands and formatting codes. You should still also pass your document through one or more translators and proofread the result, or print out the result and proofread that. Some of the problems found may be bugs in the translators, which you may or may not wish to work around.
<dt>&bull;
<dd> If you're more familiar with writing in <font SIZE="-1">HTML</font> than with writing in Pod, you can try your hand at writing documentation in simple <font SIZE="-1">HTML,</font> and converting it to Pod with the experimental Pod::HTML2Pod module, (available in <font SIZE="-1">CPAN</font>), and looking at the resulting code. The experimental Pod::PXML module in <font SIZE="-1">CPAN</font> might also be useful.
<dt>&bull;
<dd> Many older Pod translators require the lines before every Pod command and after every Pod command (including ``=cut''!) to be a blank line. Having something like this: 

 <pre>
 # - - - - - - - - - - - -
 =item $firecracker-&gt;boom()
 This noisily detonates the firecracker object.
 =cut
 sub boom {
 ...
</pre> 

 ...will make such Pod translators completely fail to see the Pod block at all. 

 Instead, have it like this: 

 <pre>
 # - - - - - - - - - - - -
 =item $firecracker-&gt;boom()
 This noisily detonates the firecracker object.
 =cut
 sub boom {
 ...
</pre>
<dt>&bull;
<dd> Some older Pod translators require paragraphs (including command paragraphs like ``=head2 Functions'') to be separated by <i>completely</i> empty lines. If you have an apparently empty line with some spaces on it, this might not count as a separator for those translators, and that could cause odd formatting.
<dt>&bull;
<dd> Older translators might add wording around an L&lt;&gt; link, so that <tt>&quot;L&lt;Foo::Bar&gt;&quot;</tt> may become ``the Foo::Bar manpage'', for example. So you shouldn't write things like <tt>&quot;the L&lt;foo&gt; documentation&quot;</tt>, if you want the translated document to read sensibly. Instead, write <tt>&quot;the L&lt;Foo::Bar|Foo::Bar&gt; documentation&quot;</tt> or <tt>&quot;L&lt;the Foo::Bar documentation|Foo::Bar&gt;&quot;</tt>, to control how the link comes out.
<dt>&bull;
<dd> Going past the 70th column in a verbatim block might be ungracefully wrapped by some formatters.</dl>

<h2>SEE ALSO</h2>

 perlpodspec, ``PODs: Embedded Documentation'' in perlsyn, perlnewmod, perldoc, pod2html, pod2man, podchecker.

<h2>AUTHOR</h2>

 Larry Wall, Sean M. Burke 

<h2>Index</h2>


