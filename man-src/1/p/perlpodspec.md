---
title: "perlpodspec(1)"
name: "perlpodspec"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlpodspec/"
---

<h2 class="name">NAME</h2>
 

 perlpodspec - Plain Old Documentation: format specification and notes 

<h2>DESCRIPTION</h2>

 This document is detailed notes on the Pod markup language. Most people will only have to read perlpod to know how to write in Pod, but this document may answer some incidental questions to do with parsing and rendering Pod. 

 In this document, ``must'' / ``must not'', ``should'' / ``should not'', and ``may'' have their conventional (cf. <font SIZE="-1">RFC 2119</font>) meanings: ``X must do Y'' means that if X doesn't do Y, it's against this specification, and should really be fixed. ``X should do Y'' means that it's recommended, but X may fail to do Y, if there's a good reason. ``X may do Y'' is merely a note that X can do Y at will (although it is up to the reader to detect any connotation of &quot;and I think it would be <i>nice</i> if X did Y`` versus ''it wouldn't really <i>bother</i> me if X did Y&quot;). 

 Notably, when I say ``the parser should do Y'', the parser may fail to do Y, if the calling application explicitly requests that the parser <i>not</i> do Y. I often phrase this as ``the parser should, by default, do Y.'' This doesn't <i>require</i> the parser to provide an option for turning off whatever feature Y is (like expanding tabs in verbatim paragraphs), although it implicates that such an option <i>may</i> be provided.

<h2>Pod Definitions</h2>

 Pod is embedded in files, typically Perl source files, although you can write a file that's nothing but Pod. 

 A <b>line</b> in a file consists of zero or more non-newline characters, terminated by either a newline or the end of the file. 

 A <b>newline sequence</b> is usually a platform-dependent concept, but Pod parsers should understand it to mean any of <font SIZE="-1">CR</font> (<font SIZE="-1">ASCII 13</font>), <font SIZE="-1">LF</font> (<font SIZE="-1">ASCII 10</font>), or a <font SIZE="-1">CRLF</font> (<font SIZE="-1">ASCII 13</font> followed immediately by <font SIZE="-1">ASCII 10</font>), in addition to any other system-specific meaning. The first <font SIZE="-1">CR/CRLF/LF</font> sequence in the file may be used as the basis for identifying the newline sequence for parsing the rest of the file. 

 A <b>blank line</b> is a line consisting entirely of zero or more spaces (<font SIZE="-1">ASCII 32</font>) or tabs (<font SIZE="-1">ASCII 9</font>), and terminated by a newline or end-of-file. A <b>non-blank line</b> is a line containing one or more characters other than space or tab (and terminated by a newline or end-of-file). 

 (<i>Note:</i> Many older Pod parsers did not accept a line consisting of spaces/tabs and then a newline as a blank line. The only lines they considered blank were lines consisting of <i>no characters at all</i>, terminated by a newline.) 

 <b>Whitespace</b> is used in this document as a blanket term for spaces, tabs, and newline sequences. (By itself, this term usually refers to literal whitespace. That is, sequences of whitespace characters in Pod source, as opposed to ``E&lt;32&gt;'', which is a formatting code that <i>denotes</i> a whitespace character.) 

 A <b>Pod parser</b> is a module meant for parsing Pod (regardless of whether this involves calling callbacks or building a parse tree or directly formatting it). A <b>Pod formatter</b> (or <b>Pod translator</b>) is a module or program that converts Pod to some other format (<font SIZE="-1">HTML,</font> plaintext, TeX, PostScript, <font SIZE="-1">RTF</font>). A <b>Pod processor</b> might be a formatter or translator, or might be a program that does something else with the Pod (like counting words, scanning for index points, etc.). 

 Pod content is contained in <b>Pod blocks</b>. A Pod block starts with a line that matches <tt>&quot;m/\A=[a-zA-Z]/&quot;</tt>, and continues up to the next line that matches <tt>&quot;m/\A=cut/&quot;</tt> or up to the end of the file if there is no <tt>&quot;m/\A=cut/&quot;</tt> line. 

 Within a Pod block, there are <b>Pod paragraphs</b>. A Pod paragraph consists of non-blank lines of text, separated by one or more blank lines. 

 For purposes of Pod processing, there are four types of paragraphs in a Pod block:
<dl>
<dt>&bull;
<dd> A command paragraph (also called a ``directive''). The first line of this paragraph must match <tt>&quot;m/\A=[a-zA-Z]/&quot;</tt>. Command paragraphs are typically one line, as in: 

 <pre>
  =head1 NOTES
  =item *
</pre> 

 But they may span several (non-blank) lines: 

 <pre>
  =for comment
  Hm, I wonder what it would look like if
  you tried to write a BNF for Pod from this.
  =head3 Dr. Strangelove, or: How I Learned to
  Stop Worrying and Love the Bomb
</pre> 

 <i>Some</i> command paragraphs allow formatting codes in their content (i.e., after the part that matches <tt>&quot;m/\A=[a-zA-Z]\S*\s*/&quot;</tt>), as in: 

 <pre>
  =head1 Did You Remember to C&lt;use strict;&gt;?
</pre> 

 In other words, the Pod processing handler for ``head1'' will apply the same processing to ``Did You Remember to C&lt;use strict;&gt;?'' that it would to an ordinary paragraph (i.e., formatting codes like ``C&lt;...&gt;'') are parsed and presumably formatted appropriately, and whitespace in the form of literal spaces and/or tabs is not significant.
<dt>&bull;
<dd> A <b>verbatim paragraph</b>. The first line of this paragraph must be a literal space or tab, and this paragraph must not be inside a &quot;=begin <i>identifier</i>``, ... ''=end <i>identifier</i>`` sequence unless ''<i>identifier</i>`` begins with a colon ('':&quot;). That is, if a paragraph starts with a literal space or tab, but <i>is</i> inside a &quot;=begin <i>identifier</i>``, ... ''=end <i>identifier</i>`` region, then it's a data paragraph, unless ''<i>identifier</i>&quot; begins with a colon. 

 Whitespace <i>is</i> significant in verbatim paragraphs (although, in processing, tabs are probably expanded).
<dt>&bull;
<dd> An <b>ordinary paragraph</b>. A paragraph is an ordinary paragraph if its first line matches neither <tt>&quot;m/\A=[a-zA-Z]/&quot;</tt> nor <tt>&quot;m/\A[ \t]/&quot;</tt>, <i>and</i> if it's not inside a &quot;=begin <i>identifier</i>``, ... ''=end <i>identifier</i>`` sequence unless ''<i>identifier</i>`` begins with a colon ('':&quot;).
<dt>&bull;
<dd> A <b>data paragraph</b>. This is a paragraph that <i>is</i> inside a &quot;=begin <i>identifier</i>`` ... ''=end <i>identifier</i>`` sequence where ''<i>identifier</i>&quot; does <i>not</i> begin with a literal colon (``:''). In some sense, a data paragraph is not part of Pod at all (i.e., effectively it's ``out-of-band''), since it's not subject to most kinds of Pod parsing; but it is specified here, since Pod parsers need to be able to call an event for it, or store it in some form in a parse tree, or at least just parse <i>around</i> it.</dl>
 

 For example: consider the following paragraphs: 

 <pre>
  # &lt;- that's the 0th column
  =head1 Foo
  Stuff
    $foo-&gt;bar
  =cut
</pre> 

 Here, ``=head1 Foo'' and ``=cut'' are command paragraphs because the first line of each matches <tt>&quot;m/\A=[a-zA-Z]/&quot;</tt>. &quot;<i>[space][space]</i><tt>$foo</tt>-&gt;bar`` is a verbatim paragraph, because its first line starts with a literal whitespace character (and there's no ''=begin``...''=end&quot; region around). 

 The &quot;=begin <i>identifier</i>`` ... ''=end <i>identifier</i>&quot; commands stop paragraphs that they surround from being parsed as ordinary or verbatim paragraphs, if <i>identifier</i> doesn't begin with a colon. This is discussed in detail in the section ``About Data Paragraphs and ''=begin/=end`` Regions''.

<h2>Pod Commands</h2>

 This section is intended to supplement and clarify the discussion in ``Command Paragraph'' in perlpod. These are the currently recognized Pod commands:
<dl>
<dt>&quot;=head1&quot;, &quot;=head2&quot;, &quot;=head3&quot;, &quot;=head4&quot;
<dd> This command indicates that the text in the remainder of the paragraph is a heading. That text may contain formatting codes. Examples: 

 <pre>
  =head1 Object Attributes
  =head3 What B&lt;Not&gt; to Do!
</pre>
<dt>&quot;=pod&quot;
<dd> This command indicates that this paragraph begins a Pod block. (If we are already in the middle of a Pod block, this command has no effect at all.) If there is any text in this command paragraph after ``=pod'', it must be ignored. Examples: 

 <pre>
  =pod
  This is a plain Pod paragraph.
  =pod This text is ignored.
</pre>
<dt>&quot;=cut&quot;
<dd> This command indicates that this line is the end of this previously started Pod block. If there is any text after ``=cut'' on the line, it must be ignored. Examples: 

 <pre>
  =cut
  =cut The documentation ends here.
  =cut
  # This is the first line of program text.
  sub foo { # This is the second.
</pre> 

 It is an error to try to <i>start</i> a Pod block with a ``=cut'' command. In that case, the Pod processor must halt parsing of the input file, and must by default emit a warning.
<dt>&quot;=over&quot;
<dd> This command indicates that this is the start of a list/indent region. If there is any text following the ``=over'', it must consist of only a nonzero positive numeral. The semantics of this numeral is explained in the ``About =over...=back Regions'' section, further below. Formatting codes are not expanded. Examples: 

 <pre>
  =over 3
  =over 3.5
  =over
</pre>
<dt>&quot;=item&quot;
<dd> This command indicates that an item in a list begins here. Formatting codes are processed. The semantics of the (optional) text in the remainder of this paragraph are explained in the ``About =over...=back Regions'' section, further below. Examples: 

 <pre>
  =item
  =item *
  =item      *    
  =item 14
  =item   3.
  =item C&lt;&lt; $thing-&gt;stuff(I&lt;dodad&gt;) &gt;&gt;
  =item For transporting us beyond seas to be tried for pretended
  offenses
  =item He is at this time transporting large armies of foreign
  mercenaries to complete the works of death, desolation and
  tyranny, already begun with circumstances of cruelty and perfidy
  scarcely paralleled in the most barbarous ages, and totally
  unworthy the head of a civilized nation.
</pre>
<dt>&quot;=back&quot;
<dd> This command indicates that this is the end of the region begun by the most recent ``=over'' command. It permits no text after the ``=back'' command.
<dt>&quot;=begin formatname&quot;
<dd>
<dt>&quot;=begin formatname parameter&quot;
<dd> This marks the following paragraphs (until the matching ``=end formatname'') as being for some special kind of processing. Unless ``formatname'' begins with a colon, the contained non-command paragraphs are data paragraphs. But if ``formatname'' <i>does</i> begin with a colon, then non-command paragraphs are ordinary paragraphs or data paragraphs. This is discussed in detail in the section ``About Data Paragraphs and ''=begin/=end`` Regions''. 

 It is advised that formatnames match the regexp <tt>&quot;m/\A:?[-a-zA-Z0-9_]+\z/&quot;</tt>. Everything following whitespace after the formatname is a parameter that may be used by the formatter when dealing with this region. This parameter must not be repeated in the ``=end'' paragraph. Implementors should anticipate future expansion in the semantics and syntax of the first parameter to ``=begin''/``=end''/``=for''.
<dt>&quot;=end formatname&quot;
<dd> This marks the end of the region opened by the matching ``=begin formatname'' region. If ``formatname'' is not the formatname of the most recent open ``=begin formatname'' region, then this is an error, and must generate an error message. This is discussed in detail in the section ``About Data Paragraphs and ''=begin/=end`` Regions''.
<dt>&quot;=for formatname text...&quot;
<dd> This is synonymous with: 

 <pre>
     =begin formatname
     text...
     =end formatname
</pre> 

 That is, it creates a region consisting of a single paragraph; that paragraph is to be treated as a normal paragraph if ``formatname'' begins with a ``:''; if ``formatname'' <i>doesn't</i> begin with a colon, then ``text...'' will constitute a data paragraph. There is no way to use ``=for formatname text...'' to express ``text...'' as a verbatim paragraph.
<dt>&quot;=encoding encodingname&quot;
<dd> This command, which should occur early in the document (at least before any non-US-ASCII data!), declares that this document is encoded in the encoding <i>encodingname</i>, which must be an encoding name that Encode recognizes. (Encode's list of supported encodings, in Encode::Supported, is useful here.) If the Pod parser cannot decode the declared encoding, it should emit a warning and may abort parsing the document altogether. 

 A document having more than one ``=encoding'' line should be considered an error. Pod processors may silently tolerate this if the not-first ``=encoding'' lines are just duplicates of the first one (e.g., if there's a ``=encoding utf8'' line, and later on another ``=encoding utf8'' line). But Pod processors should complain if there are contradictory ``=encoding'' lines in the same document (e.g., if there is a ``=encoding utf8'' early in the document and ``=encoding big5'' later). Pod processors that recognize BOMs may also complain if they see an ``=encoding'' line that contradicts the <font SIZE="-1">BOM</font> (e.g., if a document with a <font SIZE="-1">UTF-16LE BOM</font> has an ``=encoding shiftjis'' line).</dl>
 

 If a Pod processor sees any command other than the ones listed above (like ``=head'', or ``=haed1'', or ``=stuff'', or ``=cuttlefish'', or ``=w123''), that processor must by default treat this as an error. It must not process the paragraph beginning with that command, must by default warn of this as an error, and may abort the parse. A Pod parser may allow a way for particular applications to add to the above list of known commands, and to stipulate, for each additional command, whether formatting codes should be processed. 

 Future versions of this specification may add additional commands.

<h2>Pod Formatting Codes</h2>

 (Note that in previous drafts of this document and of perlpod, formatting codes were referred to as ``interior sequences'', and this term may still be found in the documentation for Pod parsers, and in error messages from Pod processors.) 

 There are two syntaxes for formatting codes:
<dl>
<dt>&bull;
<dd> A formatting code starts with a capital letter (just US-ASCII [A-Z]) followed by a ``&lt;'', any number of characters, and ending with the first matching ``&gt;''. Examples: 

 <pre>
    That's what I&lt;you&gt; think!
    What's C&lt;CORE::dump()&gt; for?
    X&lt;C&lt;chmod&gt; and C&lt;unlink()&gt; Under Different Operating Systems&gt;
</pre>
<dt>&bull;
<dd> A formatting code starts with a capital letter (just US-ASCII [A-Z]) followed by two or more ``&lt;'''s, one or more whitespace characters, any number of characters, one or more whitespace characters, and ending with the first matching sequence of two or more ``&gt;'''s, where the number of ``&gt;'''s equals the number of ``&lt;'''s in the opening of this formatting code. Examples: 

 <pre><code>
That's what I&lt;&lt; you &gt;&gt; think! C&lt;&lt;&lt;open(X, "&gt;&gt;thing.dat") || die $ !&gt;&gt;&gt;
        B &lt;&lt; $foo-&gt;bar();
&gt;&gt;
</code></pre> 

 With this syntax, the whitespace character(s) after the ``C&lt;&lt;&lt;'' and before the ``&gt;&gt;&gt;'' (or whatever letter) are <i>not</i> renderable. They do not signify whitespace, are merely part of the formatting codes themselves. That is, these are all synonymous: 

 <pre>
    C&lt;thing&gt;
    C&lt;&lt; thing &gt;&gt;
    C&lt;&lt;           thing     &gt;&gt;
    C&lt;&lt;&lt;   thing &gt;&gt;&gt;
    C&lt;&lt;&lt;&lt;
    thing
               &gt;&gt;&gt;&gt;
</pre> 

 and so on. 

 Finally, the multiple-angle-bracket form does <i>not</i> alter the interpretation of nested formatting codes, meaning that the following four example lines are identical in meaning: 

 
B &lt; example : C&lt;$a E&lt;lt &gt;= E&lt;gt&gt; $b&gt;&gt;
                  B &lt; example : C &lt;&lt; $a &lt;=&gt; $b &gt;&gt;&gt;
              B &lt; example : C &lt;&lt; $a E &lt; lt &gt;= E&lt;gt&gt; $b &gt;&gt;&gt;
              B &lt; &lt; &lt;example : C &lt;&lt; $a E&lt;lt &gt;= E&lt;gt&gt; $b&gt;&gt; &gt;&gt;&gt;
</dl>
 

 In parsing Pod, a notably tricky part is the correct parsing of (potentially nested!) formatting codes. Implementors should consult the code in the <tt>&quot;parse_text&quot;</tt> routine in Pod::Parser as an example of a correct implementation.
<dl>
<dt>&quot;I&lt;text&gt;&quot; --- italic text
<dd> See the brief discussion in ``Formatting Codes'' in perlpod.
<dt>&quot;B&lt;text&gt;&quot; --- bold text
<dd> See the brief discussion in ``Formatting Codes'' in perlpod.
<dt>&quot;C&lt;code&gt;&quot; --- code text
<dd> See the brief discussion in ``Formatting Codes'' in perlpod.
<dt>&quot;F&lt;filename&gt;&quot; --- style for filenames
<dd> See the brief discussion in ``Formatting Codes'' in perlpod.
<dt>&quot;X&lt;topic name&gt;&quot; --- an index entry
<dd> See the brief discussion in ``Formatting Codes'' in perlpod. 

 This code is unusual in that most formatters completely discard this code and its content. Other formatters will render it with invisible codes that can be used in building an index of the current document.
<dt>&quot;Z&lt;&gt;&quot; --- a null (zero-effect) formatting code
<dd> Discussed briefly in ``Formatting Codes'' in perlpod. 

 This code is unusual in that it should have no content. That is, a processor may complain if it sees <tt>&quot;Z&lt;potatoes&gt;&quot;</tt>. Whether or not it complains, the <i>potatoes</i> text should ignored.
<dt>&quot;L&lt;name&gt;&quot; --- a hyperlink
<dd> The complicated syntaxes of this code are discussed at length in ``Formatting Codes'' in perlpod, and implementation details are discussed below, in ``About L&lt;...&gt; Codes''. Parsing the contents of L&lt;content&gt; is tricky. Notably, the content has to be checked for whether it looks like a <font SIZE="-1">URL,</font> or whether it has to be split on literal ``|'' and/or ``/'' (in the right order!), and so on, <i>before</i> E&lt;...&gt; codes are resolved.
<dt>&quot;E&lt;escape&gt;&quot; --- a character escape
<dd> See ``Formatting Codes'' in perlpod, and several points in ``Notes on Implementing Pod Processors''.
<dt>&quot;S&lt;text&gt;&quot; --- text contains non-breaking spaces
<dd> This formatting code is syntactically simple, but semantically complex. What it means is that each space in the printable content of this code signifies a non-breaking space. 

 Consider: 

 <pre>
    C&lt;$x ? $y    :  $z&gt;
    S&lt;C&lt;$x ? $y     :  $z&gt;&gt;
</pre> 

 Both signify the monospace (c[ode] style) text consisting of ``$x'', one space, ``?'', one space, ``:'', one space, ``$z''. The difference is that in the latter, with the S code, those spaces are not ``normal'' spaces, but instead are non-breaking spaces.</dl>
 

 If a Pod processor sees any formatting code other than the ones listed above (as in ``N&lt;...&gt;'', or ``Q&lt;...&gt;'', etc.), that processor must by default treat this as an error. A Pod parser may allow a way for particular applications to add to the above list of known formatting codes; a Pod parser might even allow a way to stipulate, for each additional command, whether it requires some form of special processing, as L&lt;...&gt; does. 

 Future versions of this specification may add additional formatting codes. 

 Historical note: A few older Pod processors would not see a ``&gt;'' as closing a ``C&lt;'' code, if the ``&gt;'' was immediately preceded by a ``-''. This was so that this: 

 <pre>
    C&lt;$foo-&gt;bar&gt;
</pre> 

 would parse as equivalent to this: 

 <pre>
    C&lt;$foo-E&lt;gt&gt;bar&gt;
</pre> 

 instead of as equivalent to a ``C'' formatting code containing only ``$foo-'', and then a ``bar&gt;'' outside the ``C'' formatting code. This problem has since been solved by the addition of syntaxes like this: 

 <pre>
    C&lt;&lt; $foo-&gt;bar &gt;&gt;
</pre> 

 Compliant parsers must not treat ``-&gt;'' as special. 

 Formatting codes absolutely cannot span paragraphs. If a code is opened in one paragraph, and no closing code is found by the end of that paragraph, the Pod parser must close that formatting code, and should complain (as in ``Unterminated I code in the paragraph starting at line 123: 'Time objects are not...'''). So these two paragraphs: 

 <pre>
  I&lt;I told you not to do this!
  Don't make me say it again!&gt;
</pre> 

 ...must <i>not</i> be parsed as two paragraphs in italics (with the I code starting in one paragraph and starting in another.) Instead, the first paragraph should generate a warning, but that aside, the above code must parse as if it were: 

 <pre>
  I&lt;I told you not to do this!&gt;
  Don't make me say it again!E&lt;gt&gt;
</pre> 

 (In SGMLish jargon, all Pod commands are like block-level elements, whereas all Pod formatting codes are like inline-level elements.)

<h2>Notes on Implementing Pod Processors</h2>

 The following is a long section of miscellaneous requirements and suggestions to do with Pod processing.
<dl>
<dt>&bull;
<dd> Pod formatters should tolerate lines in verbatim blocks that are of any length, even if that means having to break them (possibly several times, for very long lines) to avoid text running off the side of the page. Pod formatters may warn of such line-breaking. Such warnings are particularly appropriate for lines are over 100 characters long, which are usually not intentional.
<dt>&bull;
<dd> Pod parsers must recognize <i>all</i> of the three well-known newline formats: <font SIZE="-1">CR, LF,</font> and <font SIZE="-1">CRLF.</font> See perlport.
<dt>&bull;
<dd> Pod parsers should accept input lines that are of any length.
<dt>&bull;
<dd> Since Perl recognizes a Unicode Byte Order Mark at the start of files as signaling that the file is Unicode encoded as in <font SIZE="-1">UTF-16</font> (whether big-endian or little-endian) or <font SIZE="-1">UTF-8,</font> Pod parsers should do the same. Otherwise, the character encoding should be understood as being <font SIZE="-1">UTF-8</font> if the first highbit byte sequence in the file seems valid as a <font SIZE="-1">UTF-8</font> sequence, or otherwise as <font SIZE="-1">CP-1252</font> (earlier versions of this specification used Latin-1 instead of <font SIZE="-1">CP-1252</font>). 

 Future versions of this specification may specify how Pod can accept other encodings. Presumably treatment of other encodings in Pod parsing would be as in <font SIZE="-1">XML</font> parsing: whatever the encoding declared by a particular Pod file, content is to be stored in memory as Unicode characters.
<dt>&bull;
<dd> The well known Unicode Byte Order Marks are as follows: if the file begins with the two literal byte values 0xFE 0xFF, this is the <font SIZE="-1">BOM</font> for big-endian <font SIZE="-1">UTF-16.</font> If the file begins with the two literal byte value 0xFF 0xFE, this is the <font SIZE="-1">BOM</font> for little-endian <font SIZE="-1">UTF-16.</font> On an <font SIZE="-1">ASCII</font> platform, if the file begins with the three literal byte values 0xEF 0xBB 0xBF, this is the <font SIZE="-1">BOM</font> for <font SIZE="-1">UTF-8. A</font> mechanism portable to <font SIZE="-1">EBCDIC</font> platforms is to: 

 
my $utf8_bom = "\x{FEFF}";
utf8::encode($utf8_bom);

<dt>&bull;
<dd> A naive, but often sufficient heuristic on <font SIZE="-1">ASCII</font> platforms, for testing the first highbit byte-sequence in a BOM-less file (whether in code or in Pod!), to see whether that sequence is valid as <font SIZE="-1">UTF-8</font> (<font SIZE="-1">RFC 2279</font>) is to check whether that the first byte in the sequence is in the range 0xC2 - 0xFD <i>and</i> whether the next byte is in the range 0x80 - 0xBF. If so, the parser may conclude that this file is in <font SIZE="-1">UTF-8,</font> and all highbit sequences in the file should be assumed to be <font SIZE="-1">UTF-8.</font> Otherwise the parser should treat the file as being in <font SIZE="-1">CP-1252.</font> (A better check, and which works on <font SIZE="-1">EBCDIC</font> platforms as well, is to pass a copy of the sequence to <b>utf8::decode()</b> which performs a full validity check on the sequence and returns <font SIZE="-1">TRUE</font> if it is valid <font SIZE="-1">UTF-8, FALSE</font> otherwise. This function is always pre-loaded, is fast because it is written in C, and will only get called at most once, so you don't need to avoid it out of performance concerns.) In the unlikely circumstance that the first highbit sequence in a truly non-UTF-8 file happens to appear to be <font SIZE="-1">UTF-8,</font> one can cater to our heuristic (as well as any more intelligent heuristic) by prefacing that line with a comment line containing a highbit sequence that is clearly <i>not</i> valid as <font SIZE="-1">UTF-8.</font> A line consisting of simply ``#'', an e-acute, and any non-highbit byte, is sufficient to establish this file's encoding.
<dt>&bull;
<dd> Pod processors must treat a ``=for [label] [content...]'' paragraph as meaning the same thing as a ``=begin [label]'' paragraph, content, and an ``=end [label]'' paragraph. (The parser may conflate these two constructs, or may leave them distinct, in the expectation that the formatter will nevertheless treat them the same.)
<dt>&bull;
<dd> When rendering Pod to a format that allows comments (i.e., to nearly any format other than plaintext), a Pod formatter must insert comment text identifying its name and version number, and the name and version numbers of any modules it might be using to process the Pod. Minimal examples: 

 
% % POD::Pod2PS v3 .14159, using POD::Parser v1 .92 &lt; !--Pod::HTML v3 .14159, using POD::Parser v1 .92 -- &gt; {\doccomm generated by Pod::Tree::RTF 3.14159 using Pod::Tree 1.08}.\" Pod::Man version 3.14159, using POD::Parser version 1.92
 

 Formatters may also insert additional comments, including: the release date of the Pod formatter program, the contact address for the author(s) of the formatter, the current time, the name of input file, the formatting options in effect, version of Perl used, etc. 

 Formatters may also choose to note errors/warnings as comments, besides or instead of emitting them otherwise (as in messages to <font SIZE="-1">STDERR,</font> or <tt>&quot;die&quot;</tt>ing).
<dt>&bull;
<dd> Pod parsers <i>may</i> emit warnings or error messages (``Unknown E code E&lt;zslig&gt;!'') to <font SIZE="-1">STDERR</font> (whether through printing to <font SIZE="-1">STDERR,</font> or <tt>&quot;warn&quot;</tt>ing/<tt>&quot;carp&quot;</tt>ing, or <tt>&quot;die&quot;</tt>ing/<tt>&quot;croak&quot;</tt>ing), but <i>must</i> allow suppressing all such <font SIZE="-1">STDERR</font> output, and instead allow an option for reporting errors/warnings in some other way, whether by triggering a callback, or noting errors in some attribute of the document object, or some similarly unobtrusive mechanism --- or even by appending a ``Pod Errors'' section to the end of the parsed form of the document.
<dt>&bull;
<dd> In cases of exceptionally aberrant documents, Pod parsers may abort the parse. Even then, using <tt>&quot;die&quot;</tt>ing/<tt>&quot;croak&quot;</tt>ing is to be avoided; where possible, the parser library may simply close the input file and add text like ``*** Formatting Aborted ***'' to the end of the (partial) in-memory document.
<dt>&bull;
<dd> In paragraphs where formatting codes (like E&lt;...&gt;, B&lt;...&gt;) are understood (i.e., <i>not</i> verbatim paragraphs, but <i>including</i> ordinary paragraphs, and command paragraphs that produce renderable text, like ``=head1''), literal whitespace should generally be considered ``insignificant'', in that one literal space has the same meaning as any (nonzero) number of literal spaces, literal newlines, and literal tabs (as long as this produces no blank lines, since those would terminate the paragraph). Pod parsers should compact literal whitespace in each processed paragraph, but may provide an option for overriding this (since some processing tasks do not require it), or may follow additional special rules (for example, specially treating period-space-space or period-newline sequences).
<dt>&bull;
<dd> Pod parsers should not, by default, try to coerce apostrophe (') and quote (``) into smart quotes (little 9's, 66's, 99's, etc), nor try to turn backtick (`) into anything else but a single backtick character (distinct from an open quote character!), nor ''--&quot; into anything but two minus signs. They <i>must never</i> do any of those things to text in C&lt;...&gt; formatting codes, and never <i>ever</i> to text in verbatim paragraphs.
<dt>&bull;
<dd> When rendering Pod to a format that has two kinds of hyphens (-), one that's a non-breaking hyphen, and another that's a breakable hyphen (as in ``object-oriented'', which can be split across lines as ``object-'', newline, ``oriented''), formatters are encouraged to generally translate ``-'' to non-breaking hyphen, but may apply heuristics to convert some of these to breaking hyphens.
<dt>&bull;
<dd> Pod formatters should make reasonable efforts to keep words of Perl code from being broken across lines. For example, ``Foo::Bar'' in some formatting systems is seen as eligible for being broken across lines as ``Foo::'' newline ``Bar'' or even ``Foo::-'' newline ``Bar''. This should be avoided where possible, either by disabling all line-breaking in mid-word, or by wrapping particular words with internal punctuation in ``don't break this across lines'' codes (which in some formats may not be a single code, but might be a matter of inserting non-breaking zero-width spaces between every pair of characters in a word.)
<dt>&bull;
<dd> Pod parsers should, by default, expand tabs in verbatim paragraphs as they are processed, before passing them to the formatter or other processor. Parsers may also allow an option for overriding this.
<dt>&bull;
<dd> Pod parsers should, by default, remove newlines from the end of ordinary and verbatim paragraphs before passing them to the formatter. For example, while the paragraph you're reading now could be considered, in Pod source, to end with (and contain) the newline(s) that end it, it should be processed as ending with (and containing) the period character that ends this sentence.
<dt>&bull;
<dd> Pod parsers, when reporting errors, should make some effort to report an approximate line number (``Nested E&lt;&gt;'s in Paragraph #52, near line 633 of Thing/Foo.pm!''), instead of merely noting the paragraph number (``Nested E&lt;&gt;'s in Paragraph #52 of Thing/Foo.pm!''). Where this is problematic, the paragraph number should at least be accompanied by an excerpt from the paragraph (``Nested E&lt;&gt;'s in Paragraph #52 of Thing/Foo.pm, which begins 'Read/write accessor for the C&lt;interest rate&gt; attribute...''').
<dt>&bull;
<dd> Pod parsers, when processing a series of verbatim paragraphs one after another, should consider them to be one large verbatim paragraph that happens to contain blank lines. I.e., these two lines, which have a blank line between them: 

 <pre>
        use Foo;
        print Foo-&gt;VERSION
</pre> 

 should be unified into one paragraph (``\tuse Foo;\n\n\tprint Foo-&gt;<font SIZE="-1">VERSION''</font>) before being passed to the formatter or other processor. Parsers may also allow an option for overriding this. 

 While this might be too cumbersome to implement in event-based Pod parsers, it is straightforward for parsers that return parse trees.
<dt>&bull;
<dd> Pod formatters, where feasible, are advised to avoid splitting short verbatim paragraphs (under twelve lines, say) across pages.
<dt>&bull;
<dd> Pod parsers must treat a line with only spaces and/or tabs on it as a ``blank line'' such as separates paragraphs. (Some older parsers recognized only two adjacent newlines as a ``blank line'' but would not recognize a newline, a space, and a newline, as a blank line. This is noncompliant behavior.)
<dt>&bull;
<dd> Authors of Pod formatters/processors should make every effort to avoid writing their own Pod parser. There are already several in <font SIZE="-1">CPAN,</font> with a wide range of interface styles --- and one of them, Pod::Simple, comes with modern versions of Perl.
<dt>&bull;
<dd> Characters in Pod documents may be conveyed either as literals, or by number in E&lt;n&gt; codes, or by an equivalent mnemonic, as in E&lt;eacute&gt; which is exactly equivalent to E&lt;233&gt;. The numbers are the Latin1/Unicode values, even on <font SIZE="-1">EBCDIC</font> platforms. 

 When referring to characters by using a E&lt;n&gt; numeric code, numbers in the range 32-126 refer to those well known US-ASCII characters (also defined there by Unicode, with the same meaning), which all Pod formatters must render faithfully. Characters whose E&lt;&gt; numbers are in the ranges 0-31 and 127-159 should not be used (neither as literals, nor as E&lt;number&gt; codes), except for the literal byte-sequences for newline (<font SIZE="-1">ASCII 13, ASCII 13 10,</font> or <font SIZE="-1">ASCII 10</font>), and tab (<font SIZE="-1">ASCII 9</font>). 

 Numbers in the range 160-255 refer to Latin-1 characters (also defined there by Unicode, with the same meaning). Numbers above 255 should be understood to refer to Unicode characters.
<dt>&bull;
<dd> Be warned that some formatters cannot reliably render characters outside 32-126; and many are able to handle 32-126 and 160-255, but nothing above 255.
<dt>&bull;
<dd> Besides the well-known ``E&lt;lt&gt;'' and ``E&lt;gt&gt;'' codes for less-than and greater-than, Pod parsers must understand ``E&lt;sol&gt;'' for ``/'' (solidus, slash), and ``E&lt;verbar&gt;'' for ``|'' (vertical bar, pipe). Pod parsers should also understand ``E&lt;lchevron&gt;'' and ``E&lt;rchevron&gt;'' as legacy codes for characters 171 and 187, i.e., ``left-pointing double angle quotation mark'' = ``left pointing guillemet'' and ``right-pointing double angle quotation mark'' = ``right pointing guillemet''. (These look like little ``&lt;&lt;'' and ``&gt;&gt;'', and they are now preferably expressed with the <font SIZE="-1">HTML/XHTML</font> codes ``E&lt;laquo&gt;'' and ``E&lt;raquo&gt;''.)
<dt>&bull;
<dd> Pod parsers should understand all ``E&lt;html&gt;'' codes as defined in the entity declarations in the most recent <font SIZE="-1">XHTML</font> specification at <tt>&quot;<a rel="nofollow" HREF="http://www.W3.org">www.W3.org</a>&quot;</tt>. Pod parsers must understand at least the entities that define characters in the range 160-255 (Latin-1). Pod parsers, when faced with some unknown &quot;E&lt;<i>identifier</i>&gt;&quot; code, shouldn't simply replace it with nullstring (by default, at least), but may pass it through as a string consisting of the literal characters E, less-than, <i>identifier</i>, greater-than. Or Pod parsers may offer the alternative option of processing such unknown &quot;E&lt;<i>identifier</i>&gt;`` codes by firing an event especially for such codes, or by adding a special node-type to the in-memory document tree. Such ''E&lt;<i>identifier</i>&gt;&quot; may have special meaning to some processors, or some processors may choose to add them to a special error report.
<dt>&bull;
<dd> Pod parsers must also support the <font SIZE="-1">XHTML</font> codes ``E&lt;quot&gt;'' for character 34 (doublequote, ``), ''E&lt;amp&gt;`` for character 38 (ampersand, &amp;), and ''E&lt;apos&gt;&quot; for character 39 (apostrophe, ').
<dt>&bull;
<dd> Note that in all cases of ``E&lt;whatever&gt;'', <i>whatever</i> (whether an htmlname, or a number in any base) must consist only of alphanumeric characters --- that is, <i>whatever</i> must match <tt>&quot;m/\A\w+\z/&quot;</tt>. So ``E&lt; 0 1 2 3 &gt;'' is invalid, because it contains spaces, which aren't alphanumeric characters. This presumably does not <i>need</i> special treatment by a Pod processor; `` 0 1 2 3 '' doesn't look like a number in any base, so it would presumably be looked up in the table of HTML-like names. Since there isn't (and cannot be) an HTML-like entity called `` 0 1 2 3 '', this will be treated as an error. However, Pod processors may treat ``E&lt; 0 1 2 3 &gt;'' or ``E&lt;e-acute&gt;'' as <i>syntactically</i> invalid, potentially earning a different error message than the error message (or warning, or event) generated by a merely unknown (but theoretically valid) htmlname, as in ``E&lt;qacute&gt;'' [sic]. However, Pod parsers are not required to make this distinction.
<dt>&bull;
<dd> Note that E&lt;number&gt; <i>must not</i> be interpreted as simply &quot;codepoint <i>number</i> in the current/native character set``. It always means only ''the character represented by codepoint <i>number</i> in Unicode.&quot; (This is identical to the semantics of &amp;#<i>number</i>; in <font SIZE="-1">XML.</font>) 

 This will likely require many formatters to have tables mapping from treatable Unicode codepoints (such as the ``\xE9'' for the e-acute character) to the escape sequences or codes necessary for conveying such sequences in the target output format. A converter to *roff would, for example know that ``\xE9'' (whether conveyed literally, or via a E&lt;...&gt; sequence) is to be conveyed as ``e\\*'''. Similarly, a program rendering Pod in a Mac <font SIZE="-1">OS</font> application window, would presumably need to know that ``\xE9'' maps to codepoint 142 in MacRoman encoding that (at time of writing) is native for Mac <font SIZE="-1">OS.</font> Such Unicode2whatever mappings are presumably already widely available for common output formats. (Such mappings may be incomplete! Implementers are not expected to bend over backwards in an attempt to render Cherokee syllabics, Etruscan runes, Byzantine musical symbols, or any of the other weird things that Unicode can encode.) And if a Pod document uses a character not found in such a mapping, the formatter should consider it an unrenderable character.
<dt>&bull;
<dd> If, surprisingly, the implementor of a Pod formatter can't find a satisfactory pre-existing table mapping from Unicode characters to escapes in the target format (e.g., a decent table of Unicode characters to *roff escapes), it will be necessary to build such a table. If you are in this circumstance, you should begin with the characters in the range 0x00A0 - 0x00FF, which is mostly the heavily used accented characters. Then proceed (as patience permits and fastidiousness compels) through the characters that the (X)HTML standards groups judged important enough to merit mnemonics for. These are declared in the (X)HTML specifications at the <a rel="nofollow" HREF="http://www.W3.org">www.W3.org</a> site. At time of writing (September 2001), the most recent entity declaration files are: 

 <pre>
  <a rel="nofollow" HREF="http://www.w3.org/TR/xhtml1/DTD/xhtml-lat1.ent">http://www.w3.org/TR/xhtml1/DTD/xhtml-lat1.ent</a>
  <a rel="nofollow" HREF="http://www.w3.org/TR/xhtml1/DTD/xhtml-special.ent">http://www.w3.org/TR/xhtml1/DTD/xhtml-special.ent</a>
  <a rel="nofollow" HREF="http://www.w3.org/TR/xhtml1/DTD/xhtml-symbol.ent">http://www.w3.org/TR/xhtml1/DTD/xhtml-symbol.ent</a>
</pre> 

 Then you can progress through any remaining notable Unicode characters in the range 0x2000-0x204D (consult the character tables at <a rel="nofollow" HREF="http://www.unicode.org">www.unicode.org</a>), and whatever else strikes your fancy. For example, in <i>xhtml-symbol.ent</i>, there is the entry: 

 <pre>
  &lt;!ENTITY infin    &quot;&amp;#8734;&quot;&gt; &lt;!-- infinity, U+221E ISOtech --&gt;
</pre> 

 While the mapping ``infin'' to the character ``\x{221E}'' will (hopefully) have been already handled by the Pod parser, the presence of the character in this file means that it's reasonably important enough to include in a formatter's table that maps from notable Unicode characters to the codes necessary for rendering them. So for a Unicode-to-*roff mapping, for example, this would merit the entry: 

 <pre>
  &quot;\x{221E}&quot; =&gt; '\(in',
</pre> 

 It is eagerly hoped that in the future, increasing numbers of formats (and formatters) will support Unicode characters directly (as (X)HTML does with <tt>&quot;&amp;infin;&quot;</tt>, <tt>&quot;&amp;#8734;&quot;</tt>, or <tt>&quot;&amp;#x221E;&quot;</tt>), reducing the need for idiosyncratic mappings of Unicode-to-<i>my_escapes</i>.
<dt>&bull;
<dd> It is up to individual Pod formatter to display good judgement when confronted with an unrenderable character (which is distinct from an unknown E&lt;thing&gt; sequence that the parser couldn't resolve to anything, renderable or not). It is good practice to map Latin letters with diacritics (like ``E&lt;eacute&gt;''/``E&lt;233&gt;'') to the corresponding unaccented US-ASCII letters (like a simple character 101, ``e''), but clearly this is often not feasible, and an unrenderable character may be represented as ``?'', or the like. In attempting a sane fallback (as from E&lt;233&gt; to ``e''), Pod formatters may use the <tt>%Latin1Code_to_fallback</tt> table in Pod::Escapes, or Text::Unidecode, if available. 

 For example, this Pod text: 

 <pre>
  magic is enabled if you set C&lt;$Currency&gt; to 'E&lt;euro&gt;'.
</pre> 

 may be rendered as: &quot;magic is enabled if you set <tt>$Currency</tt> to '<i>?</i>'`` or as ''magic is enabled if you set <tt>$Currency</tt> to '<b>[euro]</b>'``, or as ''magic is enabled if you set <tt>$Currency</tt> to '[x20AC]', etc. 

 A Pod formatter may also note, in a comment or warning, a list of what unrenderable characters were encountered.
<dt>&bull;
<dd> E&lt;...&gt; may freely appear in any formatting code (other than in another E&lt;...&gt; or in an Z&lt;&gt;). That is, ``X&lt;The E&lt;euro&gt;1,000,000 Solution&gt;'' is valid, as is ``L&lt;The E&lt;euro&gt;1,000,000 Solution|Million::Euros&gt;''.
<dt>&bull;
<dd> Some Pod formatters output to formats that implement non-breaking spaces as an individual character (which I'll call ``<font SIZE="-1">NBSP''</font>), and others output to formats that implement non-breaking spaces just as spaces wrapped in a ``don't break this across lines'' code. Note that at the level of Pod, both sorts of codes can occur: Pod can contain a <font SIZE="-1">NBSP</font> character (whether as a literal, or as a ``E&lt;160&gt;'' or ``E&lt;nbsp&gt;'' code); and Pod can contain ``S&lt;foo I&lt;bar&gt; baz&gt;'' codes, where ``mere spaces'' (character 32) in such codes are taken to represent non-breaking spaces. Pod parsers should consider supporting the optional parsing of ``S&lt;foo I&lt;bar&gt; baz&gt;'' as if it were &quot;foo<i></i><font SIZE="-1"><i>NBSP</i></font><i></i>I&lt;bar&gt;<i></i><font SIZE="-1"><i>NBSP</i></font><i></i>baz&quot;, and, going the other way, the optional parsing of groups of words joined by <font SIZE="-1">NBSP</font>'s as if each group were in a S&lt;...&gt; code, so that formatters may use the representation that maps best to what the output format demands.
<dt>&bull;
<dd> Some processors may find that the <tt>&quot;S&lt;...&gt;&quot;</tt> code is easiest to implement by replacing each space in the parse tree under the content of the S, with an <font SIZE="-1">NBSP.</font> But note: the replacement should apply <i>not</i> to spaces in <i>all</i> text, but <i>only</i> to spaces in <i>printable</i> text. (This distinction may or may not be evident in the particular tree/event model implemented by the Pod parser.) For example, consider this unusual case: 

 <pre>
   S&lt;L&lt;/Autoloaded Functions&gt;&gt;
</pre> 

 This means that the space in the middle of the visible link text must not be broken across lines. In other words, it's the same as this: 

 <pre>
   L&lt;&quot;AutoloadedE&lt;160&gt;Functions&quot;/Autoloaded Functions&gt;
</pre> 

 However, a misapplied space-to-NBSP replacement could (wrongly) produce something equivalent to this: 

 <pre>
   L&lt;&quot;AutoloadedE&lt;160&gt;Functions&quot;/AutoloadedE&lt;160&gt;Functions&gt;
</pre> 

 ...which is almost definitely not going to work as a hyperlink (assuming this formatter outputs a format supporting hypertext). 

 Formatters may choose to just not support the S format code, especially in cases where the output format simply has no <font SIZE="-1">NBSP</font> character/code and no code for ``don't break this stuff across lines''.
<dt>&bull;
<dd> Besides the <font SIZE="-1">NBSP</font> character discussed above, implementors are reminded of the existence of the other ``special'' character in Latin-1, the ``soft hyphen'' character, also known as ``discretionary hyphen'', i.e. <tt>&quot;E&lt;173&gt;&quot;</tt> = <tt>&quot;E&lt;0xAD&gt;&quot;</tt> = <tt>&quot;E&lt;shy&gt;&quot;</tt>). This character expresses an optional hyphenation point. That is, it normally renders as nothing, but may render as a ``-'' if a formatter breaks the word at that point. Pod formatters should, as appropriate, do one of the following: 1) render this with a code with the same meaning (e.g., ``\-'' in <font SIZE="-1">RTF</font>), 2) pass it through in the expectation that the formatter understands this character as such, or 3) delete it. 

 For example: 

 <pre>
  sigE&lt;shy&gt;action
  manuE&lt;shy&gt;script
  JarkE&lt;shy&gt;ko HieE&lt;shy&gt;taE&lt;shy&gt;nieE&lt;shy&gt;mi
</pre> 

 These signal to a formatter that if it is to hyphenate ``sigaction'' or ``manuscript'', then it should be done as &quot;sig-<i>[linebreak]</i>action`` or ''manu-<i>[linebreak]</i>script&quot; (and if it doesn't hyphenate it, then the <tt>&quot;E&lt;shy&gt;&quot;</tt> doesn't show up at all). And if it is to hyphenate ``Jarkko'' and/or ``Hietaniemi'', it can do so only at the points where there is a <tt>&quot;E&lt;shy&gt;&quot;</tt> code. 

 In practice, it is anticipated that this character will not be used often, but formatters should either support it, or delete it.
<dt>&bull;
<dd> If you think that you want to add a new command to Pod (like, say, a ``=biblio'' command), consider whether you could get the same effect with a for or begin/end sequence: ``=for biblio ...'' or ``=begin biblio'' ... ``=end biblio''. Pod processors that don't understand ``=for biblio'', etc, will simply ignore it, whereas they may complain loudly if they see ``=biblio''.
<dt>&bull;
<dd> Throughout this document, ``Pod'' has been the preferred spelling for the name of the documentation format. One may also use ``<font SIZE="-1">POD''</font> or ``pod''. For the documentation that is (typically) in the Pod format, you may use ``pod'', or ``Pod'', or ``<font SIZE="-1">POD''.</font> Understanding these distinctions is useful; but obsessing over how to spell them, usually is not.</dl>

<h2>About L&lt;...&gt; Codes</h2>

 As you can tell from a glance at perlpod, the L&lt;...&gt; code is the most complex of the Pod formatting codes. The points below will hopefully clarify what it means and how processors should deal with it.
<dl>
<dt>&bull;
<dd> In parsing an L&lt;...&gt; code, Pod parsers must distinguish at least four attributes:
<dl>
<dt>
<dd>
<dl>
<dt>First:
<dd> The link-text. If there is none, this must be <tt>&quot;undef&quot;</tt>. (E.g., in ``L&lt;Perl Functions|perlfunc&gt;'', the link-text is ``Perl Functions''. In ``L&lt;Time::HiRes&gt;'' and even ``L&lt;|Time::HiRes&gt;'', there is no link text. Note that link text may contain formatting.)
<dt>Second:
<dd> The possibly inferred link-text; i.e., if there was no real link text, then this is the text that we'll infer in its place. (E.g., for ``L&lt;Getopt::Std&gt;'', the inferred link text is ``Getopt::Std''.)
<dt>Third:
<dd> The name or <font SIZE="-1">URL,</font> or <tt>&quot;undef&quot;</tt> if none. (E.g., in ``L&lt;Perl Functions|perlfunc&gt;'', the name (also sometimes called the page) is ``perlfunc''. In ``L&lt;/CAVEATS&gt;'', the name is <tt>&quot;undef&quot;</tt>.)
<dt>Fourth:
<dd> The section (<font SIZE="-1">AKA</font> ``item'' in older perlpods), or <tt>&quot;undef&quot;</tt> if none. E.g., in ``L&lt;Getopt::Std/DESCRIPTION&gt;'', ``<font SIZE="-1">DESCRIPTION''</font> is the section. (Note that this is not the same as a manpage section like the ``5'' in ``man 5 crontab''. ``Section Foo'' in the Pod sense means the part of the text that's introduced by the heading or item whose text is ``Foo''.)</dl>
</dl>

<dl>
<dt>
<dd> 

 Pod parsers may also note additional attributes including:
<dl>
<dt>Fifth:
<dd> A flag for whether item 3 (if present) is a <font SIZE="-1">URL</font> (like ``<a rel="nofollow" HREF="http://lists.perl.org''">http://lists.perl.org''</a> is), in which case there should be no section attribute; a Pod name (like ``perldoc'' and ``Getopt::Std'' are); or possibly a man page name (like ``<b><a HREF="/docs/linux/man/5-crontab/">crontab</a></b>(5)'' is).
<dt>Sixth:
<dd> The raw original L&lt;...&gt; content, before text is split on ``|'', ``/'', etc, and before E&lt;...&gt; codes are expanded.</dl>
</dl>

<dl>
<dt>
<dd> 

 (The above were numbered only for concise reference below. It is not a requirement that these be passed as an actual list or array.) 

 For example: 

 <pre>
  L&lt;Foo::Bar&gt;
    =&gt;  undef,                         # link text
        &quot;Foo::Bar&quot;,                    # possibly inferred link text
        &quot;Foo::Bar&quot;,                    # name
        undef,                         # section
        'pod',                         # what sort of link
        &quot;Foo::Bar&quot;                     # original content
  L&lt;Perlport's section on NL's|perlport/Newlines&gt;
    =&gt;  &quot;Perlport's section on NL's&quot;,  # link text
        &quot;Perlport's section on NL's&quot;,  # possibly inferred link text
        &quot;perlport&quot;,                    # name
        &quot;Newlines&quot;,                    # section
        'pod',                         # what sort of link
        &quot;Perlport's section on NL's|perlport/Newlines&quot;
                                       # original content
  L&lt;perlport/Newlines&gt;
    =&gt;  undef,                         # link text
        '&quot;Newlines&quot; in perlport',      # possibly inferred link text
        &quot;perlport&quot;,                    # name
        &quot;Newlines&quot;,                    # section
        'pod',                         # what sort of link
        &quot;perlport/Newlines&quot;            # original content
  L&lt;<a HREF="//www.systutorials.com/docs/linux/man/5-crontab/">crontab</a>(5)/&quot;DESCRIPTION&quot;&gt;
    =&gt;  undef,                         # link text
        '&quot;DESCRIPTION&quot; in <a HREF="//www.systutorials.com/docs/linux/man/5-crontab/">crontab</a>(5)', # possibly inferred link text
        &quot;<a HREF="//www.systutorials.com/docs/linux/man/5-crontab/">crontab</a>(5)&quot;,                  # name
        &quot;DESCRIPTION&quot;,                 # section
        'man',                         # what sort of link
        '<a HREF="//www.systutorials.com/docs/linux/man/5-crontab/">crontab</a>(5)/&quot;DESCRIPTION&quot;'     # original content
  L&lt;/Object Attributes&gt;
    =&gt;  undef,                         # link text
        '&quot;Object Attributes&quot;',         # possibly inferred link text
        undef,                         # name
        &quot;Object Attributes&quot;,           # section
        'pod',                         # what sort of link
        &quot;/Object Attributes&quot;           # original content
  L&lt;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&gt;
    =&gt;  undef,                         # link text
        &quot;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&quot;,        # possibly inferred link text
        &quot;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&quot;,        # name
        undef,                         # section
        'url',                         # what sort of link
        &quot;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&quot;         # original content
  L&lt;Perl.org|<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&gt;
    =&gt;  &quot;Perl.org&quot;,                    # link text
        &quot;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&quot;,        # possibly inferred link text
        &quot;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&quot;,        # name
        undef,                         # section
        'url',                         # what sort of link
        &quot;Perl.org|<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&quot; # original content
</pre> 

 Note that you can distinguish URL-links from anything else by the fact that they match <tt>&quot;m/\A\w+:[^:\s]\S*\z/&quot;</tt>. So <tt>&quot;L&lt;<a rel="nofollow" HREF="http://www.perl.com">http://www.perl.com</a>&gt;&quot;</tt> is a <font SIZE="-1">URL,</font> but <tt>&quot;L&lt;HTTP::Response&gt;&quot;</tt> isn't.</dl>

<dt>&bull;
<dd> In case of L&lt;...&gt; codes with no ``text|'' part in them, older formatters have exhibited great variation in actually displaying the link or cross reference. For example, L&lt;<b><a HREF="/docs/linux/man/5-crontab/">crontab</a></b>(5)&gt; would render as &quot;the <tt><a HREF="/docs/linux/man/5-crontab/">crontab</a>(5)</tt> manpage``, or ''in the <tt><a HREF="/docs/linux/man/5-crontab/">crontab</a>(5)</tt> manpage`` or just ''<tt><a HREF="/docs/linux/man/5-crontab/">crontab</a>(5)</tt>&quot;. 

 Pod processors must now treat ``text|''-less links as follows: 

 <pre>
  L&lt;name&gt;         =&gt;  L&lt;name|name&gt;
  L&lt;/section&gt;     =&gt;  L&lt;&quot;section&quot;|/section&gt;
  L&lt;name/section&gt; =&gt;  L&lt;&quot;section&quot; in name|name/section&gt;
</pre>
<dt>&bull;
<dd> Note that section names might contain markup. I.e., if a section starts with: 

 <pre>
  =head2 About the C&lt;-M&gt; Operator
</pre> 

 or with: 

 <pre>
  =item About the C&lt;-M&gt; Operator
</pre> 

 then a link to it would look like this: 

 <pre>
  L&lt;somedoc/About the C&lt;-M&gt; Operator&gt;
</pre> 

 Formatters may choose to ignore the markup for purposes of resolving the link and use only the renderable characters in the section name, as in: 

 <pre>
  &lt;h1&gt;&lt;a name=&quot;About_the_-M_Operator&quot;&gt;About the &lt;code&gt;-M&lt;/code&gt;
  Operator&lt;/h1&gt;
  ...
  &lt;a href=&quot;somedoc#About_the_-M_Operator&quot;&gt;About the &lt;code&gt;-M&lt;/code&gt;
  Operator&quot; in somedoc&lt;/a&gt;
</pre>
<dt>&bull;
<dd> Previous versions of perlpod distinguished <tt>&quot;L&lt;name/&quot;section&quot;&gt;&quot;</tt> links from <tt>&quot;L&lt;name/item&gt;&quot;</tt> links (and their targets). These have been merged syntactically and semantically in the current specification, and <i>section</i> can refer either to a &quot;=head<i>n</i> Heading Content`` command or to a ''=item Item Content&quot; command. This specification does not specify what behavior should be in the case of a given document having several things all seeming to produce the same <i>section</i> identifier (e.g., in <font SIZE="-1">HTML,</font> several things all producing the same <i>anchorname</i> in &lt;a name=&quot;<i>anchorname</i>&quot;&gt;...&lt;/a&gt; elements). Where Pod processors can control this behavior, they should use the first such anchor. That is, <tt>&quot;L&lt;Foo/Bar&gt;&quot;</tt> refers to the <i>first</i> ``Bar'' section in Foo. 

 But for some processors/formats this cannot be easily controlled; as with the <font SIZE="-1">HTML</font> example, the behavior of multiple ambiguous &lt;a name=&quot;<i>anchorname</i>&quot;&gt;...&lt;/a&gt; is most easily just left up to browsers to decide.
<dt>&bull;
<dd> In a <tt>&quot;L&lt;text|...&gt;&quot;</tt> code, text may contain formatting codes for formatting or for E&lt;...&gt; escapes, as in: 

 <pre>
  L&lt;B&lt;ummE&lt;234&gt;stuff&gt;|...&gt;
</pre> 

 For <tt>&quot;L&lt;...&gt;&quot;</tt> codes without a ``name|'' part, only <tt>&quot;E&lt;...&gt;&quot;</tt> and <tt>&quot;Z&lt;&gt;&quot;</tt> codes may occur. That is, authors should not use &quot;<tt>&quot;L&lt;B&lt;Foo::Bar&gt;&gt;&quot;</tt>&quot;. 

 Note, however, that formatting codes and Z&lt;&gt;'s can occur in any and all parts of an L&lt;...&gt; (i.e., in <i>name</i>, <i>section</i>, <i>text</i>, and <i>url</i>). 

 Authors must not nest L&lt;...&gt; codes. For example, ``L&lt;The L&lt;Foo::Bar&gt; man page&gt;'' should be treated as an error.
<dt>&bull;
<dd> Note that Pod authors may use formatting codes inside the ``text'' part of ``L&lt;text|name&gt;'' (and so on for L&lt;text|/``sec''&gt;). 

 In other words, this is valid: 

 <pre>
  Go read L&lt;the docs on C&lt;$.&gt;|perlvar/&quot;$.&quot;&gt;
</pre> 

 Some output formats that do allow rendering ``L&lt;...&gt;'' codes as hypertext, might not allow the link-text to be formatted; in that case, formatters will have to just ignore that formatting.
<dt>&bull;
<dd> At time of writing, <tt>&quot;L&lt;name&gt;&quot;</tt> values are of two types: either the name of a Pod page like <tt>&quot;L&lt;Foo::Bar&gt;&quot;</tt> (which might be a real Perl module or program in an <tt>@INC</tt> / <font SIZE="-1">PATH</font> directory, or a .pod file in those places); or the name of a Unix man page, like <tt>&quot;L&lt;<a HREF="/docs/linux/man/5-crontab/">crontab</a>(5)&gt;&quot;</tt>. In theory, <tt>&quot;L&lt;chmod&gt;&quot;</tt> is ambiguous between a Pod page called ``chmod'', or the Unix man page ``chmod'' (in whatever man-section). However, the presence of a string in parens, as in ``<b><a HREF="/docs/linux/man/5-crontab/">crontab</a></b>(5)'', is sufficient to signal that what is being discussed is not a Pod page, and so is presumably a Unix man page. The distinction is of no importance to many Pod processors, but some processors that render to hypertext formats may need to distinguish them in order to know how to render a given <tt>&quot;L&lt;foo&gt;&quot;</tt> code.
<dt>&bull;
<dd> Previous versions of perlpod allowed for a <tt>&quot;L&lt;section&gt;&quot;</tt> syntax (as in <tt>&quot;L&lt;Object Attributes&gt;&quot;</tt>), which was not easily distinguishable from <tt>&quot;L&lt;name&gt;&quot;</tt> syntax and for <tt>&quot;L&lt;&quot;section&quot;&gt;&quot;</tt> which was only slightly less ambiguous. This syntax is no longer in the specification, and has been replaced by the <tt>&quot;L&lt;/section&gt;&quot;</tt> syntax (where the slash was formerly optional). Pod parsers should tolerate the <tt>&quot;L&lt;&quot;section&quot;&gt;&quot;</tt> syntax, for a while at least. The suggested heuristic for distinguishing <tt>&quot;L&lt;section&gt;&quot;</tt> from <tt>&quot;L&lt;name&gt;&quot;</tt> is that if it contains any whitespace, it's a <i>section</i>. Pod processors should warn about this being deprecated syntax.</dl>

<h2>About =over...=back Regions</h2>

 ``=over''...``=back'' regions are used for various kinds of list-like structures. (I use the term ``region'' here simply as a collective term for everything from the ``=over'' to the matching ``=back''.)
<dl>
<dt>&bull;
<dd> The non-zero numeric <i>indentlevel</i> in &quot;=over <i>indentlevel</i>`` ... ''=back`` is used for giving the formatter a clue as to how many ''spaces&quot; (ems, or roughly equivalent units) it should tab over, although many formatters will have to convert this to an absolute measurement that may not exactly match with the size of spaces (or M's) in the document's base font. Other formatters may have to completely ignore the number. The lack of any explicit <i>indentlevel</i> parameter is equivalent to an <i>indentlevel</i> value of 4. Pod processors may complain if <i>indentlevel</i> is present but is not a positive number matching <tt>&quot;m/\A(\d*\.)?\d+\z/&quot;</tt>.
<dt>&bull;
<dd> Authors of Pod formatters are reminded that ``=over'' ... ``=back'' may map to several different constructs in your output format. For example, in converting Pod to (X)HTML, it can map to any of &lt;ul&gt;...&lt;/ul&gt;, &lt;ol&gt;...&lt;/ol&gt;, &lt;dl&gt;...&lt;/dl&gt;, or &lt;blockquote&gt;...&lt;/blockquote&gt;. Similarly, ``=item'' can map to &lt;li&gt; or &lt;dt&gt;.
<dt>&bull;
<dd> Each ``=over'' ... ``=back'' region should be one of the following:
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> An ``=over'' ... ``=back'' region containing only ``=item *'' commands, each followed by some number of ordinary/verbatim paragraphs, other nested ``=over'' ... ``=back'' regions, ``=for...'' paragraphs, and ``=begin''...``=end'' regions. 

 (Pod processors must tolerate a bare ``=item'' as if it were ``=item *''.) Whether ``*'' is rendered as a literal asterisk, an ``o'', or as some kind of real bullet character, is left up to the Pod formatter, and may depend on the level of nesting.
<dt>&bull;
<dd> An ``=over'' ... ``=back'' region containing only <tt>&quot;m/\A=item\s+\d+\.?\s*\z/&quot;</tt> paragraphs, each one (or each group of them) followed by some number of ordinary/verbatim paragraphs, other nested ``=over'' ... ``=back'' regions, ``=for...'' paragraphs, and/or ``=begin''...``=end'' codes. Note that the numbers must start at 1 in each section, and must proceed in order and without skipping numbers. 

 (Pod processors must tolerate lines like ``=item 1'' as if they were ``=item 1.'', with the period.)
<dt>&bull;
<dd> An ``=over'' ... ``=back'' region containing only ``=item [text]'' commands, each one (or each group of them) followed by some number of ordinary/verbatim paragraphs, other nested ``=over'' ... ``=back'' regions, or ``=for...'' paragraphs, and ``=begin''...``=end'' regions. 

 The ``=item [text]'' paragraph should not match <tt>&quot;m/\A=item\s+\d+\.?\s*\z/&quot;</tt> or <tt>&quot;m/\A=item\s+\*\s*\z/&quot;</tt>, nor should it match just <tt>&quot;m/\A=item\s*\z/&quot;</tt>.
<dt>&bull;
<dd> An ``=over'' ... ``=back'' region containing no ``=item'' paragraphs at all, and containing only some number of ordinary/verbatim paragraphs, and possibly also some nested ``=over'' ... ``=back'' regions, ``=for...'' paragraphs, and ``=begin''...``=end'' regions. Such an itemless ``=over'' ... ``=back'' region in Pod is equivalent in meaning to a ``&lt;blockquote&gt;...&lt;/blockquote&gt;'' element in <font SIZE="-1">HTML.</font></dl>
</dl>

<dl>
<dt>
<dd> 

 Note that with all the above cases, you can determine which type of ``=over'' ... ``=back'' you have, by examining the first (non-``=cut'', non-``=pod'') Pod paragraph after the ``=over'' command.</dl>

<dt>&bull;
<dd> Pod formatters <i>must</i> tolerate arbitrarily large amounts of text in the &quot;=item <i>text...</i>&quot; paragraph. In practice, most such paragraphs are short, as in: 

 <pre>
  =item For cutting off our trade with all parts of the world
</pre> 

 But they may be arbitrarily long: 

 <pre>
  =item For transporting us beyond seas to be tried for pretended
  offenses
  =item He is at this time transporting large armies of foreign
  mercenaries to complete the works of death, desolation and
  tyranny, already begun with circumstances of cruelty and perfidy
  scarcely paralleled in the most barbarous ages, and totally
  unworthy the head of a civilized nation.
</pre>
<dt>&bull;
<dd> Pod processors should tolerate ``=item *'' / &quot;=item <i>number</i>&quot; commands with no accompanying paragraph. The middle item is an example: 

 <pre>
  =over
  =item 1
  Pick up dry cleaning.
  =item 2
  =item 3
  Stop by the store.  Get Abba Zabas, Stoli, and cheap lawn chairs.
  =back
</pre>
<dt>&bull;
<dd> No ``=over'' ... ``=back'' region can contain headings. Processors may treat such a heading as an error.
<dt>&bull;
<dd> Note that an ``=over'' ... ``=back'' region should have some content. That is, authors should not have an empty region like this: 

 <pre>
  =over
  =back
</pre> 

 Pod processors seeing such a contentless ``=over'' ... ``=back'' region, may ignore it, or may report it as an error.
<dt>&bull;
<dd> Processors must tolerate an ``=over'' list that goes off the end of the document (i.e., which has no matching ``=back''), but they may warn about such a list.
<dt>&bull;
<dd> Authors of Pod formatters should note that this construct: 

 <pre>
  =item Neque
  =item Porro
  =item Quisquam Est
  Qui dolorem ipsum quia dolor sit amet, consectetur, adipisci 
  velit, sed quia non numquam eius modi tempora incidunt ut
  labore et dolore magnam aliquam quaerat voluptatem.
  =item Ut Enim
</pre> 

 is semantically ambiguous, in a way that makes formatting decisions a bit difficult. On the one hand, it could be mention of an item ``Neque'', mention of another item ``Porro'', and mention of another item ``Quisquam Est'', with just the last one requiring the explanatory paragraph ``Qui dolorem ipsum quia dolor...''; and then an item ``Ut Enim''. In that case, you'd want to format it like so: 

 <pre>
  Neque
  Porro
  Quisquam Est
    Qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
    velit, sed quia non numquam eius modi tempora incidunt ut
    labore et dolore magnam aliquam quaerat voluptatem.
  Ut Enim
</pre> 

 But it could equally well be a discussion of three (related or equivalent) items, ``Neque'', ``Porro'', and ``Quisquam Est'', followed by a paragraph explaining them all, and then a new item ``Ut Enim''. In that case, you'd probably want to format it like so: 

 <pre>
  Neque
  Porro
  Quisquam Est
    Qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
    velit, sed quia non numquam eius modi tempora incidunt ut
    labore et dolore magnam aliquam quaerat voluptatem.
  Ut Enim
</pre> 

 But (for the foreseeable future), Pod does not provide any way for Pod authors to distinguish which grouping is meant by the above ``=item''-cluster structure. So formatters should format it like so: 

 <pre>
  Neque
  Porro
  Quisquam Est
    Qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
    velit, sed quia non numquam eius modi tempora incidunt ut
    labore et dolore magnam aliquam quaerat voluptatem.
  Ut Enim
</pre> 

 That is, there should be (at least roughly) equal spacing between items as between paragraphs (although that spacing may well be less than the full height of a line of text). This leaves it to the reader to use (con)textual cues to figure out whether the ``Qui dolorem ipsum...'' paragraph applies to the ``Quisquam Est'' item or to all three items ``Neque'', ``Porro'', and ``Quisquam Est''. While not an ideal situation, this is preferable to providing formatting cues that may be actually contrary to the author's intent.</dl>

<h2>About Data Paragraphs and =begin/=end Regions</h2>

 Data paragraphs are typically used for inlining non-Pod data that is to be used (typically passed through) when rendering the document to a specific format: 

 
= begin rtf
  \par{\pard\qr\sa4500{\i Printed\~\chdate\~\chtime}\par} = end rtf
 

 The exact same effect could, incidentally, be achieved with a single ``=for'' paragraph: 

 
  =for rtf \par
  {
      \pard\qr\sa4500
      {
          \i Printed\~\chdate\~\chtime
      }
      \par
  }
 

 (Although that is not formally a data paragraph, it has the same meaning as one, and Pod parsers may parse it as one.) 

 Another example of a data paragraph: 

 <pre>
  =begin html
  I like &lt;em&gt;PIE&lt;/em&gt;!
  &lt;hr&gt;Especially pecan pie!
  =end html
</pre> 

 If these were ordinary paragraphs, the Pod parser would try to expand the ``E&lt;/em&gt;'' (in the first paragraph) as a formatting code, just like ``E&lt;lt&gt;'' or ``E&lt;eacute&gt;''. But since this is in a &quot;=begin <i>identifier</i>``...''=end <i>identifier</i>&quot; region <i>and</i> the identifier ``html'' doesn't begin have a ``:'' prefix, the contents of this region are stored as data paragraphs, instead of being processed as ordinary paragraphs (or if they began with a spaces and/or tabs, as verbatim paragraphs). 

 As a further example: At time of writing, no ``biblio'' identifier is supported, but suppose some processor were written to recognize it as a way of (say) denoting a bibliographic reference (necessarily containing formatting codes in ordinary paragraphs). The fact that ``biblio'' paragraphs were meant for ordinary processing would be indicated by prefacing each ``biblio'' identifier with a colon: 

 <pre>
  =begin :biblio
  Wirth, Niklaus.  1976.  I&lt;Algorithms + Data Structures =
  Programs.&gt;  Prentice-Hall, Englewood Cliffs, NJ.
  =end :biblio
</pre> 

 This would signal to the parser that paragraphs in this begin...end region are subject to normal handling as ordinary/verbatim paragraphs (while still tagged as meant only for processors that understand the ``biblio'' identifier). The same effect could be had with: 

 <pre>
  =for :biblio
  Wirth, Niklaus.  1976.  I&lt;Algorithms + Data Structures =
  Programs.&gt;  Prentice-Hall, Englewood Cliffs, NJ.
</pre> 

 The ``:'' on these identifiers means simply ``process this stuff normally, even though the result will be for some special target''. I suggest that parser APIs report ``biblio'' as the target identifier, but also report that it had a ``:'' prefix. (And similarly, with the above ``html'', report ``html'' as the target identifier, and note the <i>lack</i> of a ``:'' prefix.) 

 Note that a &quot;=begin <i>identifier</i>``...''=end <i>identifier</i>&quot; region where <i>identifier</i> begins with a colon, <i>can</i> contain commands. For example: 

 <pre><code>
  =begin :biblio
  Wirth's classic is available in several editions, including:
  =for comment
   hm, check abebooks.com for how much used copies cost.
  =over
  =item
  Wirth, Niklaus.  1975.  I&lt;Algorithmen und Datenstrukturen.&gt;
  Teubner, Stuttgart.  [Yes, it's in German.]
  =item
  Wirth, Niklaus.  1976.  I&lt;Algorithms + Data Structures =
  Programs.&gt;  Prentice-Hall, Englewood Cliffs, NJ.
  =back
  =end :biblio
</code></pre> 

 Note, however, a &quot;=begin <i>identifier</i>``...''=end <i>identifier</i>&quot; region where <i>identifier</i> does <i>not</i> begin with a colon, should not directly contain ``=head1'' ... ``=head4'' commands, nor ``=over'', nor ``=back'', nor ``=item''. For example, this may be considered invalid: 

 <pre>
  =begin somedata
  This is a data paragraph.
  =head1 Don't do this!
  This is a data paragraph too.
  =end somedata
</pre> 

 A Pod processor may signal that the above (specifically the ``=head1'' paragraph) is an error. Note, however, that the following should <i>not</i> be treated as an error: 

 <pre>
  =begin somedata
  This is a data paragraph.
  =cut
  # Yup, this isn't Pod anymore.
  sub excl { (rand() &gt; .5) ? &quot;hoo!&quot; : &quot;hah!&quot; }
  =pod
  This is a data paragraph too.
  =end somedata
</pre> 

 And this too is valid: 

 <pre>
  =begin someformat
  This is a data paragraph.
    And this is a data paragraph.
  =begin someotherformat
  This is a data paragraph too.
    And this is a data paragraph too.
  =begin :yetanotherformat
  =head2 This is a command paragraph!
  This is an ordinary paragraph!
    And this is a verbatim paragraph!
  =end :yetanotherformat
  =end someotherformat
  Another data paragraph!
  =end someformat
</pre> 

 The contents of the above ``=begin :yetanotherformat'' ... ``=end :yetanotherformat'' region <i>aren't</i> data paragraphs, because the immediately containing region's identifier (``:yetanotherformat'') begins with a colon. In practice, most regions that contain data paragraphs will contain <i>only</i> data paragraphs; however, the above nesting is syntactically valid as Pod, even if it is rare. However, the handlers for some formats, like ``html'', will accept only data paragraphs, not nested regions; and they may complain if they see (targeted for them) nested regions, or commands, other than ``=end'', ``=pod'', and ``=cut''. 

 Also consider this valid structure: 

 <pre>
  =begin :biblio
  Wirth's classic is available in several editions, including:
  =over
  =item
  Wirth, Niklaus.  1975.  I&lt;Algorithmen und Datenstrukturen.&gt;
  Teubner, Stuttgart.  [Yes, it's in German.]
  =item
  Wirth, Niklaus.  1976.  I&lt;Algorithms + Data Structures =
  Programs.&gt;  Prentice-Hall, Englewood Cliffs, NJ.
  =back
  Buy buy buy!
  =begin html
  &lt;img src='wirth_spokesmodeling_book.png'&gt;
  &lt;hr&gt;
  =end html
  Now now now!
  =end :biblio
</pre> 

 There, the ``=begin html''...``=end html'' region is nested inside the larger ``=begin :biblio''...``=end :biblio'' region. Note that the content of the ``=begin html''...``=end html'' region is data paragraph(s), because the immediately containing region's identifier (``html'') <i>doesn't</i> begin with a colon. 

 Pod parsers, when processing a series of data paragraphs one after another (within a single region), should consider them to be one large data paragraph that happens to contain blank lines. So the content of the above ``=begin html''...``=end html'' <i>may</i> be stored as two data paragraphs (one consisting of ``&lt;img src='wirth_spokesmodeling_book.png'&gt;\n'' and another consisting of ``&lt;hr&gt;\n''), but <i>should</i> be stored as a single data paragraph (consisting of ``&lt;img src='wirth_spokesmodeling_book.png'&gt;\n\n&lt;hr&gt;\n''). 

 Pod processors should tolerate empty &quot;=begin <i>something</i>``...''=end <i>something</i>`` regions, empty ''=begin :<i>something</i>``...''=end :<i>something</i>`` regions, and contentless ''=for <i>something</i>`` and ''=for :<i>something</i>&quot; paragraphs. I.e., these should be tolerated: 

 <pre>
  =for html
  =begin html
  =end html
  =begin :biblio
  =end :biblio
</pre> 

 Incidentally, note that there's no easy way to express a data paragraph starting with something that looks like a command. Consider: 

 <pre>
  =begin stuff
  =shazbot
  =end stuff
</pre> 

 There, ``=shazbot'' will be parsed as a Pod command ``shazbot'', not as a data paragraph ``=shazbot\n''. However, you can express a data paragraph consisting of ``=shazbot\n'' using this code: 

 <pre>
  =for stuff =shazbot
</pre> 

 The situation where this is necessary, is presumably quite rare. 

 Note that =end commands must match the currently open =begin command. That is, they must properly nest. For example, this is valid: 

 <pre>
  =begin outer
  X
  =begin inner
  Y
  =end inner
  Z
  =end outer
</pre> 

 while this is invalid: 

 <pre>
  =begin outer
  X
  =begin inner
  Y
  =end outer
  Z
  =end inner
</pre> 

 This latter is improper because when the ``=end outer'' command is seen, the currently open region has the formatname ``inner'', not ``outer''. (It just happens that ``outer'' is the format name of a higher-up region.) This is an error. Processors must by default report this as an error, and may halt processing the document containing that error. A corollary of this is that regions cannot ``overlap''. That is, the latter block above does not represent a region called ``outer'' which contains X and Y, overlapping a region called ``inner'' which contains Y and Z. But because it is invalid (as all apparently overlapping regions would be), it doesn't represent that, or anything at all. 

 Similarly, this is invalid: 

 <pre>
  =begin thing
  =end hting
</pre> 

 This is an error because the region is opened by ``thing'', and the ``=end'' tries to close ``hting'' [sic]. 

 This is also invalid: 

 <pre>
  =begin thing
  =end
</pre> 

 This is invalid because every ``=end'' command must have a formatname parameter.

<h2>SEE ALSO</h2>

 perlpod, ``PODs: Embedded Documentation'' in perlsyn, podchecker

<h2>AUTHOR</h2>

 Sean M. Burke 

<h2>Index</h2>


