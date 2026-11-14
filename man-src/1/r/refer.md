---
title: "refer(1)"
name: "refer"
section: "1"
letter: "r"
url: "/docs/linux/man/1-refer/"
description: "refer – preprocess bibliographic references for groff"
---

<h2 class="name">NAME</h2>
<p> refer &#8211; preprocess bibliographic references for groff </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-benCPRS</code> ] [ <code>-a </code><i>n</i> ] [ <code>-c </code><i>fields</i> ] [ <code>-f </code><i>n</i> ] [ <code>-i </code><i>fields</i> ] [ <code>-k </code><i>field</i> ] [ <code>-l </code><i>m,n</i> ] [ <code>-p </code><i>filename</i> ] [ <code>-s </code><i>fields</i> ] [ <code>-t </code><i>n</i> ] <code>-B </code><i>field</i><code>.</code><i>macro</i> [<i>file</i> &#8230;] <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> This file documents the GNU version of <code>refer</code>, which is part of the groff document formatting system. <code>refer</code> copies the contents of <i>filename</i>&#8230; to the standard output, except that lines between <code>.[</code> and <code>.]</code> are interpreted as citations, and lines between <code>.R1</code> and <code>.R2</code> are interpreted as commands about how citations are to be processed. </p>
<p> Each citation specifies a reference. The citation can specify a reference that is contained in a bibliographic database by giving a set of keywords that only that reference contains. Alternatively it can specify a reference by supplying a database record in the citation. A combination of these alternatives is also possible. </p>
<p> For each citation, <code>refer</code> can produce a mark in the text. This mark consists of some label which can be separated from the text and from other labels in various ways. For each reference it also outputs <code>groff</code> commands that can be used by a macro package to produce a formatted reference for each citation. The output of <code>refer</code> must therefore be processed using a suitable macro package. The <code>-ms</code> and <code>-me</code> macros are both suitable. The commands to format a citation&#8217;s reference can be output immediately after the citation, or the references may be accumulated, and the commands output at some later point. If the references are accumulated, then multiple citations of the same reference will produce a single formatted reference. </p>
<p> The interpretation of lines between <code>.R1</code> and <code>.R2</code> as commands is a new feature of GNU <code>refer</code>. Documents making use of this feature can still be processed by Unix refer just by adding the lines</p>
<dl>
<dt>
<dd>
<pre>
<code>.de R1
.ig R2
..
</code></pre>
</dl>
<p> to the beginning of the document. This will cause <code>troff</code> to ignore everything between <code>.R1</code> and <code>.R2</code>. The effect of some commands can also be achieved by options. These options are supported mainly for compatibility with Unix refer. It is usually more convenient to use commands. </p>
<p> <code>refer</code> generates <code>.lf</code> lines so that filenames and line numbers in messages produced by commands that read <code>refer</code> output will be correct; it also interprets lines beginning with <code>.lf</code> so that filenames and line numbers in the messages and <code>.lf</code> lines that it produces will be accurate even if the input has been preprocessed by a command such as <code><a href="/docs/linux/man/1-soelim/">soelim</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument. </p>
<p> Most options are equivalent to commands (for a description of these commands, see subsection &#8220;Commands&#8221; below).</p>
<dl>
<dt><code>-b</code></p>
<dd> <code>no-label-in-text; no-label-in-reference</code></p>
<dt><code>-e</code></p>
<dd> <code>accumulate</code></p>
<dt><code>-n</code></p>
<dd> <code>no-default-database</code></p>
<dt><code>-C</code></p>
<dd> <code>compatible</code></p>
<dt><code>-P</code></p>
<dd> <code>move-punctuation</code></p>
<dt><code>-S</code></p>
<dd> <code>label&nbsp;&quot;(A.n|Q)&nbsp;&#8216;,&nbsp;&#8216;&nbsp;(D.y|D)&quot;; bracket-label&nbsp;&quot;&nbsp;(&quot;&nbsp;)&nbsp;&quot;;&nbsp;&quot;</code></p>
<dt><code>-a</code><i>n</i></p>
<dd> <code>reverse</code> <code>A</code><i>n</i></p>
<dt><code>-c</code><i>fields</i></p>
<dd> <code>capitalize</code> <i>fields</i></p>
<dt><code>-f</code><i>n</i></p>
<dd> <code>label</code> <code>%</code><i>n</i></p>
<dt><code>-i</code><i>fields</i></p>
<dd> <code>search-ignore</code> <i>fields</i></p>
<dt><code>-k</code></p>
<dd> <code>label</code> <code>L~%a</code></p>
<dt><code>-k</code><i>field</i></p>
<dd> <code>label</code> <i>field</i><code>~%a</code></p>
<dt><code>-l</code></p>
<dd> <code>label</code> <code>A.nD.y%a</code></p>
<dt><code>-l</code><i>m</i></p>
<dd> <code>label</code> <code>A.n+</code><i>m</i><code>D.y%a</code></p>
<dt><code>-l,</code><i>n</i></p>
<dd> <code>label</code> <code>A.nD.y-</code><i>n</i><code>%a</code></p>
<dt><code>-l</code><i>m</i><code>,</code><i>n</i></p>
<dd> <code>label</code> <code>A.n+</code><i>m</i><code>D.y-</code><i>n</i><code>%a</code></p>
<dt><code>-p</code><i>filename</i></p>
<dd> <code>database</code> <i>filename</i></p>
<dt><code>-s</code><i>spec</i></p>
<dd> <code>sort</code> <i>spec</i></p>
<dt><code>-t</code><i>n</i></p>
<dd> <code>search-truncate</code> <i>n</i></dl>
<p> These options are equivalent to the following commands with the addition that the filenames specified on the command line are processed as if they were arguments to the <code>bibliography</code> command instead of in the normal way:</p>
<dl>
<dt><code>-B</code></p>
<dd> <code>annotate X AP; no-label-in-reference</code></p>
<dt><code>-B</code><i>field</i><code>.</code><i>macro</i></p>
<dd> <code>annotate</code> <i>field</i> <i>macro</i><code>;</code> <code>no-label-in-reference</code></dl>
<p> The following options have no equivalent commands:</p>
<dl>
<dt><code>-v</code></p>
<dd> Print the version number.</p>
<dt><code>-R</code></p>
<dd> Don&#8217;t recognize lines beginning with <code>.R1</code>/<code>.R2</code>.</dl>
<h2>USAGE</h2>
<h3>Bibliographic databases</h3>
<p> The bibliographic database is a text file consisting of records separated by one or more blank lines. Within each record fields start with a <code>%</code> at the beginning of a line. Each field has a one character name that immediately follows the <code>%</code>. It is best to use only upper and lower case letters for the names of fields. The name of the field should be followed by exactly one space, and then by the contents of the field. Empty fields are ignored. The conventional meaning of each field is as follows:</p>
<dl>
<dt><code>%A</code></p>
<dd> The name of an author. If the name contains a title such as <code>Jr.</code> at the end, it should be separated from the last name by a comma. There can be multiple occurrences of the <code>%A</code> field. The order is significant. It is a good idea always to supply an <code>%A</code> field or a <code>%Q</code> field.</p>
<dt><code>%B</code></p>
<dd> For an article that is part of a book, the title of the book.</p>
<dt><code>%C</code></p>
<dd> The place (city) of publication.</p>
<dt><code>%D</code></p>
<dd> The date of publication. The year should be specified in full. If the month is specified, the name rather than the number of the month should be used, but only the first three letters are required. It is a good idea always to supply a <code>%D</code> field; if the date is unknown, a value such as <code>in press</code> or <code>unknown</code> can be used.</p>
<dt><code>%E</code></p>
<dd> For an article that is part of a book, the name of an editor of the book. Where the work has editors and no authors, the names of the editors should be given as <code>%A</code> fields and <code>,&nbsp;(ed)</code> or <code>,&nbsp;(eds)</code> should be appended to the last author.</p>
<dt><code>%G</code></p>
<dd> US Government ordering number.</p>
<dt><code>%I</code></p>
<dd> The publisher (issuer).</p>
<dt><code>%J</code></p>
<dd> For an article in a journal, the name of the journal.</p>
<dt><code>%K</code></p>
<dd> Keywords to be used for searching.</p>
<dt><code>%L</code></p>
<dd> Label.</p>
<dt><code>%N</code></p>
<dd> Journal issue number.</p>
<dt><code>%O</code></p>
<dd> Other information. This is usually printed at the end of the reference.</p>
<dt><code>%P</code></p>
<dd> Page number. A range of pages can be specified as <i>m</i><code>&#8211;</code><i>n</i>.</p>
<dt><code>%Q</code></p>
<dd> The name of the author, if the author is not a person. This will only be used if there are no <code>%A</code> fields. There can only be one <code>%Q</code> field.</p>
<dt><code>%R</code></p>
<dd> Technical report number.</p>
<dt><code>%S</code></p>
<dd> Series name.</p>
<dt><code>%T</code></p>
<dd> Title. For an article in a book or journal, this should be the title of the article.</p>
<dt><code>%V</code></p>
<dd> Volume number of the journal or book.</p>
<dt><code>%X</code></p>
<dd> Annotation.</dl>
<p> For all fields except <code>%A</code> and <code>%E</code>, if there is more than one occurrence of a particular field in a record, only the last such field will be used. </p>
<p> If accent strings are used, they should follow the character to be accented. This means that the <code>AM</code> macro must be used with the <code>-ms</code> macros. Accent strings should not be quoted: use one <code>\</code> rather than two.</p>
<h3>Citations</h3>
<p> The format of a citation is</p>
<dl>
<dt>
<dd> <code>.[</code><i>opening-text</i><br />
 <i>flags keywords</i><br />
 <i>fields</i><br />
 <code>.]</code><i>closing-text</i></dl>
<p> The <i>opening-text</i>, <i>closing-text</i>, and <i>flags</i> components are optional. Only one of the <i>keywords</i> and <i>fields</i> components need be specified. </p>
<p> The <i>keywords</i> component says to search the bibliographic databases for a reference that contains all the words in <i>keywords</i>. It is an error if more than one reference if found. </p>
<p> The <i>fields</i> components specifies additional fields to replace or supplement those specified in the reference. When references are being accumulated and the <i>keywords</i> component is non-empty, then additional fields should be specified only on the first occasion that a particular reference is cited, and will apply to all citations of that reference. </p>
<p> The <i>opening-text</i> and <i>closing-text</i> component specifies strings to be used to bracket the label instead of the strings specified in the <code>bracket-label</code> command. If either of these components is non-empty, the strings specified in the <code>bracket-label</code> command will not be used; this behaviour can be altered using the <code>[</code> and <code>]</code> flags. Note that leading and trailing spaces are significant for these components. </p>
<p> The <i>flags</i> component is a list of non-alphanumeric characters each of which modifies the treatment of this particular citation. Unix refer will treat these flags as part of the keywords and so will ignore them since they are non-alphanumeric. The following flags are currently recognized:</p>
<dl>
<dt><code>#</code></p>
<dd> This says to use the label specified by the <code>short-label</code> command, instead of that specified by the <code>label</code> command. If no short label has been specified, the normal label will be used. Typically the short label is used with author-date labels and consists of only the date and possibly a disambiguating letter; the <code>#</code> is supposed to be suggestive of a numeric type of label.</p>
<dt><code>[</code></p>
<dd> Precede <i>opening-text</i> with the first string specified in the <code>bracket-label</code> command.</p>
<dt><code>]</code></p>
<dd> Follow <i>closing-text</i> with the second string specified in the <code>bracket-label</code> command.</dl>
<p> One advantages of using the <code>[</code> and <code>]</code> flags rather than including the brackets in <i>opening-text</i> and <i>closing-text</i> is that you can change the style of bracket used in the document just by changing the <code>bracket-label</code> command. Another advantage is that sorting and merging of citations will not necessarily be inhibited if the flags are used. </p>
<p> If a label is to be inserted into the text, it will be attached to the line preceding the <code>.[</code> line. If there is no such line, then an extra line will be inserted before the <code>.[</code> line and a warning will be given. </p>
<p> There is no special notation for making a citation to multiple references. Just use a sequence of citations, one for each reference. Don&#8217;t put anything between the citations. The labels for all the citations will be attached to the line preceding the first citation. The labels may also be sorted or merged. See the description of the <code>&lt;&gt;</code> label expression, and of the <code>sort-adjacent-labels</code> and <code>abbreviate-label-ranges</code> command. A label will not be merged if its citation has a non-empty <i>opening-text</i> or <i>closing-text</i>. However, the labels for a citation using the <code>]</code> flag and without any <i>closing-text</i> immediately followed by a citation using the <code>[</code> flag and without any <i>opening-text</i> may be sorted and merged even though the first citation&#8217;s <i>opening-text</i> or the second citation&#8217;s <i>closing-text</i> is non-empty. (If you wish to prevent this just make the first citation&#8217;s <i>closing-text</i> <code>\&amp;</code>.)</p>
<h3>Commands</h3>
<p> Commands are contained between lines starting with <code>.R1</code> and <code>.R2</code>. Recognition of these lines can be prevented by the <code>-R</code> option. When a <code>.R1</code> line is recognized any accumulated references are flushed out. Neither <code>.R1</code> nor <code>.R2</code> lines, nor anything between them is output. </p>
<p> Commands are separated by newlines or <code>;</code>s. <code>#</code> introduces a comment that extends to the end of the line (but does not conceal the newline). Each command is broken up into words. Words are separated by spaces or tabs. A word that begins with <code>&quot;</code> extends to the next <code>&quot;</code> that is not followed by another <code>&quot;</code>. If there is no such <code>&quot;</code> the word extends to the end of the line. Pairs of <code>&quot;</code> in a word beginning with <code>&quot;</code> collapse to a single <code>&quot;</code>. Neither <code>#</code> nor <code>;</code> are recognized inside <code>&quot;</code>s. A line can be continued by ending it with <code>\</code>; this works everywhere except after a <code>#</code>. </p>
<p> Each command <i>name</i> that is marked with * has an associated negative command <code>no-</code><i>name</i> that undoes the effect of <i>name</i>. For example, the <code>no-sort</code> command specifies that references should not be sorted. The negative commands take no arguments. </p>
<p> In the following description each argument must be a single word; <i>field</i> is used for a single upper or lower case letter naming a field; <i>fields</i> is used for a sequence of such letters; <i>m</i> and <i>n</i> are used for a non-negative numbers; <i>string</i> is used for an arbitrary string; <i>filename</i> is used for the name of a file.</p>
<dl>
<dt><code>abbreviate*&nbsp;</code><i>fields string1 string2 string3 string4</i></p>
<dd> Abbreviate the first names of <i>fields</i>. An initial letter will be separated from another initial letter by <i>string1</i>, from the last name by <i>string2</i>, and from anything else (such as a <code>von</code> or <code>de</code>) by <i>string3</i>. These default to a period followed by a space. In a hyphenated first name, the initial of the first part of the name will be separated from the hyphen by <i>string4</i>; this defaults to a period. No attempt is made to handle any ambiguities that might result from abbreviation. Names are abbreviated before sorting and before label construction.</p>
<dt><code>abbreviate-label-ranges*&nbsp;</code><i>string</i></p>
<dd> Three or more adjacent labels that refer to consecutive references will be abbreviated to a label consisting of the first label, followed by <i>string</i> followed by the last label. This is mainly useful with numeric labels. If <i>string</i> is omitted it defaults to <code>&#8211;</code>.</p>
<dt><code>accumulate*</code></p>
<dd> Accumulate references instead of writing out each reference as it is encountered. Accumulated references will be written out whenever a reference of the form</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>.[</code><br />
 <code>$LIST$</code><br />
 <code>.]</code></dl>
<p> is encountered, after all input files have been processed, and whenever <code>.R1</code> line is recognized.</dl>
<dt><code>annotate*&nbsp;</code><i>field string</i></p>
<dd> <i>field</i> is an annotation; print it at the end of the reference as a paragraph preceded by the line</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>.</code><i>string</i></dl>
<p> If <i>string</i> is omitted it will default to <code>AP</code>; if <i>field</i> is also omitted it will default to <code>X</code>. Only one field can be an annotation.</dl>
<dt><code>articles&nbsp;</code><i>string</i>&#8230;</p>
<dd> <i>string</i>&#8230; are definite or indefinite articles, and should be ignored at the beginning of <code>T</code> fields when sorting. Initially, <code>the</code>, <code>a</code> and <code>an</code> are recognized as articles.</p>
<dt><code>bibliography&nbsp;</code><i>filename</i>&#8230;</p>
<dd> Write out all the references contained in the bibliographic databases <i>filename</i>&#8230; This command should come last in a <code>.R1</code>/<code>.R2</code> block.</p>
<dt><code>bracket-label&nbsp;</code><i>string1 string2 string3</i></p>
<dd> In the text, bracket each label with <i>string1</i> and <i>string2</i>. An occurrence of <i>string2</i> immediately followed by <i>string1</i> will be turned into <i>string3</i>. The default behaviour is</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>bracket-label \*([. \*(.] &quot;, &quot;</code></dl>
</dl>
<dt><code>capitalize&nbsp;</code><i>fields</i></p>
<dd> Convert <i>fields</i> to caps and small caps.</p>
<dt><code>compatible*</code></p>
<dd> Recognize <code>.R1</code> and <code>.R2</code> even when followed by a character other than space or newline.</p>
<dt><code>database&nbsp;</code><i>filename</i>&#8230;</p>
<dd> Search the bibliographic databases <i>filename</i>&#8230; For each <i>filename</i> if an index <i>filename</i><code>.i</code> created by <code><a href="/docs/linux/man/1-indxbib/">indxbib</a></code>(1) exists, then it will be searched instead; each index can cover multiple databases.</p>
<dt><code>date-as-label*&nbsp;</code><i>string</i></p>
<dd> <i>string</i> is a label expression that specifies a string with which to replace the <code>D</code> field after constructing the label. See subsection &#8220;Label expressions&#8221; below for a description of label expressions. This command is useful if you do not want explicit labels in the reference list, but instead want to handle any necessary disambiguation by qualifying the date in some way. The label used in the text would typically be some combination of the author and date. In most cases you should also use the <code>no-label-in-reference</code> command. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>date-as-label D.+yD.y%a*D.-y</code></dl>
<p> would attach a disambiguating letter to the year part of the <code>D</code> field in the reference.</dl>
<dt><code>default-database*</code></p>
<dd> The default database should be searched. This is the default behaviour, so the negative version of this command is more useful. <code>refer</code> determines whether the default database should be searched on the first occasion that it needs to do a search. Thus a <code>no-default-database</code> command must be given before then, in order to be effective.</p>
<dt><code>discard*&nbsp;</code><i>fields</i></p>
<dd> When the reference is read, <i>fields</i> should be discarded; no string definitions for <i>fields</i> will be output. Initially, <i>fields</i> are <code>XYZ</code>.</p>
<dt><code>et-al*&nbsp;</code><i>string m n</i></p>
<dd> Control use of <code>et al</code> in the evaluation of <code>@</code> expressions in label expressions. If the number of authors needed to make the author sequence unambiguous is <i>u</i> and the total number of authors is <i>t</i> then the last <i>t</i>&#8211;<i>u</i> authors will be replaced by <i>string</i> provided that <i>t</i>&#8211;<i>u</i> is not less than <i>m</i> and <i>t</i> is not less than <i>n</i>. The default behaviour is</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>et-al &quot; et al&quot; 2 3</code></dl>
</dl>
<dt><code>include&nbsp;</code><i>filename</i></p>
<dd> Include <i>filename</i> and interpret the contents as commands.</p>
<dt><code>join-authors&nbsp;</code><i>string1 string2 string3</i></p>
<dd> This says how authors should be joined together. When there are exactly two authors, they will be joined with <i>string1</i>. When there are more than two authors, all but the last two will be joined with <i>string2</i>, and the last two authors will be joined with <i>string3</i>. If <i>string3</i> is omitted, it will default to <i>string1</i>; if <i>string2</i> is also omitted it will also default to <i>string1</i>. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>join-authors &quot; and &quot; &quot;, &quot; &quot;, and &quot;</code></dl>
<p> will restore the default method for joining authors.</dl>
<dt><code>label-in-reference*</code></p>
<dd> When outputting the reference, define the string <code>[F</code> to be the reference&#8217;s label. This is the default behaviour; so the negative version of this command is more useful.</p>
<dt><code>label-in-text*</code></p>
<dd> For each reference output a label in the text. The label will be separated from the surrounding text as described in the <code>bracket-label</code> command. This is the default behaviour; so the negative version of this command is more useful.</p>
<dt><code>label&nbsp;</code><i>string</i></p>
<dd> <i>string</i> is a label expression describing how to label each reference.</p>
<dt><code>separate-label-second-parts&nbsp;</code><i>string</i></p>
<dd> When merging two-part labels, separate the second part of the second label from the first label with <i>string</i>. See the description of the <code>&lt;&gt;</code> label expression.</p>
<dt><code>move-punctuation*</code></p>
<dd> In the text, move any punctuation at the end of line past the label. It is usually a good idea to give this command unless you are using superscripted numbers as labels.</p>
<dt><code>reverse*&nbsp;</code><i>string</i></p>
<dd> Reverse the fields whose names are in <i>string</i>. Each field name can be followed by a number which says how many such fields should be reversed. If no number is given for a field, all such fields will be reversed.</p>
<dt><code>search-ignore*&nbsp;</code><i>fields</i></p>
<dd> While searching for keys in databases for which no index exists, ignore the contents of <i>fields</i>. Initially, fields <code>XYZ</code> are ignored.</p>
<dt><code>search-truncate*&nbsp;</code><i>n</i></p>
<dd> Only require the first <i>n</i> characters of keys to be given. In effect when searching for a given key words in the database are truncated to the maximum of <i>n</i> and the length of the key. Initially <i>n</i> is 6.</p>
<dt><code>short-label*&nbsp;</code><i>string</i></p>
<dd> <i>string</i> is a label expression that specifies an alternative (usually shorter) style of label. This is used when the <code>#</code> flag is given in the citation. When using author-date style labels, the identity of the author or authors is sometimes clear from the context, and so it may be desirable to omit the author or authors from the label. The <code>short-label</code> command will typically be used to specify a label containing just a date and possibly a disambiguating letter.</p>
<dt><code>sort*&nbsp;</code><i>string</i></p>
<dd> Sort references according to <code>string</code>. References will automatically be accumulated. <i>string</i> should be a list of field names, each followed by a number, indicating how many fields with the name should be used for sorting. <code>+</code> can be used to indicate that all the fields with the name should be used. Also <code>.</code> can be used to indicate the references should be sorted using the (tentative) label. (Subsection &#8220;Label expressions&#8221; below describes the concept of a tentative label.)</p>
<dt><code>sort-adjacent-labels*</code></p>
<dd> Sort labels that are adjacent in the text according to their position in the reference list. This command should usually be given if the <code>abbreviate-label-ranges</code> command has been given, or if the label expression contains a <code>&lt;&gt;</code> expression. This will have no effect unless references are being accumulated.</dl>
<h3>Label expressions</h3>
<p> Label expressions can be evaluated both normally and tentatively. The result of normal evaluation is used for output. The result of tentative evaluation, called the <i>tentative label</i>, is used to gather the information that normal evaluation needs to disambiguate the label. Label expressions specified by the <code>date-as-label</code> and <code>short-label</code> commands are not evaluated tentatively. Normal and tentative evaluation are the same for all types of expression other than <code>@</code>, <code>*</code>, and <code>%</code> expressions. The description below applies to normal evaluation, except where otherwise specified.</p>
<dl>
<dt><i>field</i></p>
<dd> <i>field n</i> The <i>n</i>-th part of <i>field</i>. If <i>n</i> is omitted, it defaults to 1.</p>
<dt><code>&#8216;</code><i>string</i><code>&#8216;</code></p>
<dd> The characters in <i>string</i> literally.</p>
<dt><code>@</code></p>
<dd> All the authors joined as specified by the <code>join-authors</code> command. The whole of each author&#8217;s name will be used. However, if the references are sorted by author (that is the sort specification starts with <code>A+</code>), then authors last names will be used instead, provided that this does not introduce ambiguity, and also an initial subsequence of the authors may be used instead of all the authors, again provided that this does not introduce ambiguity. The use of only the last name for the <i>i</i>-th author of some reference is considered to be ambiguous if there is some other reference, such that the first <i>i</i>-1 authors of the references are the same, the <i>i</i>-th authors are not the same, but the <i>i</i>-th authors last names are the same. A proper initial subsequence of the sequence of authors for some reference is considered to be ambiguous if there is a reference with some other sequence of authors which also has that subsequence as a proper initial subsequence. When an initial subsequence of authors is used, the remaining authors are replaced by the string specified by the <code>et-al</code> command; this command may also specify additional requirements that must be met before an initial subsequence can be used. <code>@</code> tentatively evaluates to a canonical representation of the authors, such that authors that compare equally for sorting purpose will have the same representation.</p>
<dt><code>%</code><i>n</i></p>
<dd> <code>%a</code> <code>%A</code> <code>%i</code> <code>%I</code> The serial number of the reference formatted according to the character following the <code>%</code>. The serial number of a reference is 1 plus the number of earlier references with same tentative label as this reference. These expressions tentatively evaluate to an empty string.</p>
<dt><i>expr</i><code>*</code></p>
<dd> If there is another reference with the same tentative label as this reference, then <i>expr</i>, otherwise an empty string. It tentatively evaluates to an empty string.</p>
<dt><i>expr</i><code>+</code><i>n</i></p>
<dd> <i>expr</i><code>&#8211;</code><i>n</i> The first (<code>+</code>) or last (<code>&#8211;</code>) <i>n</i> upper or lower case letters or digits of <i>expr</i>. Troff special characters (such as <code>\(&#8216;a</code>) count as a single letter. Accent strings are retained but do not count towards the total.</p>
<dt><i>expr</i><code>.l</code></p>
<dd> <i>expr</i> converted to lowercase.</p>
<dt><i>expr</i><code>.u</code></p>
<dd> <i>expr</i> converted to uppercase.</p>
<dt><i>expr</i><code>.c</code></p>
<dd> <i>expr</i> converted to caps and small caps.</p>
<dt><i>expr</i><code>.r</code></p>
<dd> <i>expr</i> reversed so that the last name is first.</p>
<dt><i>expr</i><code>.a</code></p>
<dd> <i>expr</i> with first names abbreviated. Note that fields specified in the <code>abbreviate</code> command are abbreviated before any labels are evaluated. Thus <code>.a</code> is useful only when you want a field to be abbreviated in a label but not in a reference.</p>
<dt><i>expr</i><code>.y</code></p>
<dd> The year part of <i>expr</i>.</p>
<dt><i>expr</i><code>.+y</code></p>
<dd> The part of <i>expr</i> before the year, or the whole of <i>expr</i> if it does not contain a year.</p>
<dt><i>expr</i><code>.-y</code></p>
<dd> The part of <i>expr</i> after the year, or an empty string if <i>expr</i> does not contain a year.</p>
<dt><i>expr</i><code>.n</code></p>
<dd> The last name part of <i>expr</i>.</p>
<dt><i>expr1</i><code>~</code><i>expr2</i></p>
<dd> <i>expr1</i> except that if the last character of <i>expr1</i> is <code>&#8211;</code> then it will be replaced by <i>expr2</i>.</p>
<dt><i>expr1 expr2</i></p>
<dd> The concatenation of <i>expr1</i> and <i>expr2</i>.</p>
<dt><i>expr1</i><code>|</code><i>expr2</i></p>
<dd> If <i>expr1</i> is non-empty then <i>expr1</i> otherwise <i>expr2</i>.</p>
<dt><i>expr1</i><code>&amp;</code><i>expr2</i></p>
<dd> If <i>expr1</i> is non-empty then <i>expr2</i> otherwise an empty string.</p>
<dt><i>expr1</i><code>?</code><i>expr2</i><code>:</code><i>expr3</i></p>
<dd> If <i>expr1</i> is non-empty then <i>expr2</i> otherwise <i>expr3</i>.</p>
<dt><code>&lt;</code><i>expr</i><code>&gt;</code></p>
<dd> The label is in two parts, which are separated by <i>expr</i>. Two adjacent two-part labels which have the same first part will be merged by appending the second part of the second label onto the first label separated by the string specified in the <code>separate-label-second-parts</code> command (initially, a comma followed by a space); the resulting label will also be a two-part label with the same first part as before merging, and so additional labels can be merged into it. Note that it is permissible for the first part to be empty; this maybe desirable for expressions used in the <code>short-label</code> command.</p>
<dt><code>(</code><i>expr</i><code>)</code></p>
<dd> The same as <i>expr</i>. Used for grouping.</dl>
<p> The above expressions are listed in order of precedence (highest first); <code>&amp;</code> and <code>|</code> have the same precedence.</p>
<h3>Macro interface</h3>
<p> Each reference starts with a call to the macro <code>]-</code>. The string <code>[F</code> will be defined to be the label for this reference, unless the <code>no-label-in-reference</code> command has been given. There then follows a series of string definitions, one for each field: string <code>[</code><i>X</i> corresponds to field <i>X</i>. The number register <code>[P</code> is set to 1 if the <code>P</code> field contains a range of pages. The <code>[T</code>, <code>[A</code> and <code>[O</code> number registers are set to 1 according as the <code>T</code>, <code>A</code> and <code>O</code> fields end with one of the characters <code>.?!</code>. The <code>[E</code> number register will be set to 1 if the <code>[E</code> string contains more than one name. The reference is followed by a call to the <code>][</code> macro. The first argument to this macro gives a number representing the type of the reference. If a reference contains a <code>J</code> field, it will be classified as type 1, otherwise if it contains a <code>B</code> field, it will type 3, otherwise if it contains a <code>G</code> or <code>R</code> field it will be type 4, otherwise if it contains an <code>I</code> field it will be type 2, otherwise it will be type 0. The second argument is a symbolic name for the type: <code>other</code>, <code>journal-article</code>, <code>book</code>, <code>article-in-book</code> or <code>tech-report</code>. Groups of references that have been accumulated or are produced by the <code>bibliography</code> command are preceded by a call to the <code>]&lt;</code> macro and followed by a call to the <code>]&gt;</code> macro.</p>
<h2>FILES</h2>
<dl>
<dt><i>/usr/:dict/:papers/:Ind</i></p>
<dd> Default database.</p>
<dt>file<i>.i</i></p>
<dd> Index files.</dl>
<p> <code>refer</code> uses temporary files. See the <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) man page for details where such files are created.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>REFER</i></p>
<dd> If set, overrides the default database.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-indxbib/">indxbib</a></code>(1), <code><a href="/docs/linux/man/1-lookbib/">lookbib</a></code>(1), <code><a href="/docs/linux/man/1-lkbib/">lkbib</a></code>(1) </p>
<h2>BUGS</h2>
<p> In label expressions, <code>&lt;&gt;</code> expressions are ignored inside <code>.</code><i>char</i> expressions. </p>
<h2>Index</h2>
