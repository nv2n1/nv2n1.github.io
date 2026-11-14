---
title: "geqn(1)"
name: "geqn"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geqn/"
description: "eqn – format equations for troff or MathML"
---

<h2 class="name">NAME</h2>
<p> eqn &#8211; format equations for troff or MathML </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-rvCNR</code> ] [ <code>-d </code><i>xy</i> ] [ <code>-T </code><i>name</i> ] [ <code>-M </code><i>dir</i> ] [ <code>-f </code><i>F</i> ] [ <code>-s </code><i>n</i> ] [ <code>-p </code><i>n</i> ] [ <code>-m </code><i>n</i> ] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This manual page describes the GNU version of <code>eqn</code>, which is part of the groff document formatting system. <code>eqn</code> compiles descriptions of equations embedded within <code>troff</code> input files into commands that are understood by <code>troff</code>. Normally, it should be invoked using the <code>-e</code> option of <code>groff</code>. The syntax is quite compatible with Unix eqn. The output of GNU <code>eqn</code> cannot be processed with Unix troff; it must be processed with GNU troff. If no files are given on the command line, the standard input is read. A filename of <code>&#8211;</code> causes the standard input to be read. </p>
<p> <code>eqn</code> searches for the file <i>eqnrc</i> in the directories given with the <code>-M</code> option first, then in <i>/usr/lib/groff/site-tmac</i>, <i>/usr/share/groff/site-tmac</i>, and finally in the standard macro directory <i>/usr/share/groff/1.22.4/tmac</i>. If it exists, <code>eqn</code> processes it before the other input files. The <code>-R</code> option prevents this. </p>
<p> GNU <code>eqn</code> does not provide the functionality of neqn: it does not support low-resolution, typewriter-like devices (although it may work adequately for very simple input).</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-d</code><i>xy</i></p>
<dd> Specify delimiters <i>x</i> and~<i>y</i> for the left and right end, respectively, of in-line equations. Any <code>delim</code> statements in the source file overrides this.</p>
<dt><code>-C</code></p>
<dd> Recognize <code>.EQ</code> and <code>.EN</code> even when followed by a character other than space or newline. Also, the statement &#8216;<code>delim on</code>&#8216; is not handled specially.</p>
<dt><code>-N</code></p>
<dd> Don&#8217;t allow newlines within delimiters. This option allows <code>eqn</code> to recover better from missing closing delimiters.</p>
<dt><code>-v</code></p>
<dd> Print the version number.</p>
<dt><code>-r</code></p>
<dd> Only one size reduction.</p>
<dt><code>-m</code><i>n</i></p>
<dd> The minimum point-size is~<i>n</i>. <code>eqn</code> does not reduce the size of subscripts or superscripts to a smaller size than~<i>n</i>.</p>
<dt><code>-T</code><i>name</i></p>
<dd> The output is for device <i>name</i>. Normally, the only effect of this is to define a macro <i>name</i> with a value of~<code>1</code>; <i>eqnrc</i> uses this to provide definitions appropriate for the output device. However, if the specified device is &#8220;MathML&#8221;, the output is MathML markup rather than troff commands, and <i>eqnrc</i> is not loaded at all. The default output device is <code>ps</code>.</p>
<dt><code>-M</code><i>dir</i></p>
<dd> Search <i>dir</i> for <i>eqnrc</i> before the default directories.</p>
<dt><code>-R</code></p>
<dd> Don&#8217;t load <i>eqnrc</i>.</p>
<dt><code>-f</code><i>F</i></p>
<dd> This is equivalent to a <code>gfont&nbsp;</code><i>F</i> command.</p>
<dt><code>-s</code><i>n</i></p>
<dd> This is equivalent to a <code>gsize&nbsp;</code><i>n</i> command. This option is deprecated. <code>eqn</code> normally sets equations at whatever the current point size is when the equation is encountered.</p>
<dt><code>-p</code><i>n</i></p>
<dd> This says that subscripts and superscripts should be <i>n</i>~points smaller than the surrounding text. This option is deprecated. Normally <code>eqn</code> sets subscripts and superscripts at 70% of the size of the surrounding text.</dl>
<h2>USAGE</h2>
<p> Only the differences between GNU <code>eqn</code> and Unix eqn are described here. </p>
<p> GNU <code>eqn</code> emits Presentation MathML output when invoked with the <code>-T~MathML</code> option. </p>
<p> GNU eqn sets the input token <code>&#8230;</code> as three periods or low dots, rather than the three centered dots of classic eqn. To get three centered dots, write <code>cdots</code> or <code>cdot cdot cdot.</code> </p>
<p> Most of the new features of the GNU <code>eqn</code> input language are based on TeX. There are some references to the differences between TeX and GNU <code>eqn</code> below; these may safely be ignored if you do not know TeX.</p>
<h3>Controlling delimiters</h3>
<p> If not in compatibility mode, <code>eqn</code> recognizes</p>
<dl>
<dt>
<dd>
<p> <code>delim on</code></dl>
<p> to restore the delimiters which have been previously disabled with a call to &#8216;<code>delim off</code>&#8216;. If delimiters haven&#8217;t been specified, the call has no effect.</p>
<h3>Automatic spacing</h3>
<p> <code>eqn</code> gives each component of an equation a type, and adjusts the spacing between components using that type. Possible types are described in the table below. </p>
<table>
<tr VALIGN=top>
<td><code>ordinary</code></td>
<td> an ordinary character such as &#8216;1&#8217; or &#8216;<i>x</i>&#8216;
</td>
</tr>
<tr VALIGN=top>
<td><code>operator</code></td>
<td> a large operator such as &#8216;<font SIZE="+5">&Sigma;</font>&#8216;
</td>
</tr>
<tr VALIGN=top>
<td><code>binary</code></td>
<td>a binary operator such as &#8216;+&#8217;
</td>
</tr>
<tr VALIGN=top>
<td><code>relation</code></td>
<td>a relation such as &#8216;=&#8217;
</td>
</tr>
<tr VALIGN=top>
<td><code>opening</code></td>
<td>a opening bracket such as &#8216;(&#8216;
</td>
</tr>
<tr VALIGN=top>
<td><code>closing</code></td>
<td>a closing bracket such as &#8216;)&#8217;
</td>
</tr>
<tr VALIGN=top>
<td><code>punctuation</code></td>
<td>a punctuation character such as &#8216;,&#8217;
</td>
</tr>
<tr VALIGN=top>
<td><code>inner</code></td>
<td>a subformula contained within brackets
</td>
</tr>
<tr VALIGN=top>
<td><code>suppress</code></td>
<td>a type that suppresses automatic spacing adjustment
</td>
</tr>
</table>
<p> Components of an equation get a type in one of two ways.</p>
<dl>
<dt><code>type&nbsp;</code><i>t e</i></p>
<dd> This yields an equation component that contains~<i>e</i> but that has type~<i>t</i>, where <i>t</i> is one of the types mentioned above. For example, <code>times</code> is defined as</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>type &quot;binary&quot; \(mu</code></dl>
</dl>
<dt>
<dd> The name of the type doesn&#8217;t have to be quoted, but quoting protects from macro expansion.</p>
<dt><code>chartype&nbsp;</code><i>t text</i></p>
<dd> Unquoted groups of characters are split up into individual characters, and the type of each character is looked up; this changes the type that is stored for each character; it says that the characters in <i>text</i> from now on have type~<i>t</i>. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>chartype &quot;punctuation&quot; .,;:</code></dl>
</dl>
<dt>
<dd> would make the characters &#8216;.,;:&#8217; have type punctuation whenever they subsequently appeared in an equation. The type~<i>t</i> can also be <code>letter</code> or <code>digit</code>; in these cases <code>chartype</code> changes the font type of the characters. See subsection &#8220;Fonts&#8221; below.</dl>
<h3>New primitives</h3>
<dl>
<dt><code>big&nbsp;</code><i>e</i></p>
<dd> Enlarges the expression it modifies; intended to have semantics like CSS &#8216;large&#8217;. In troff output, the point size is increased by~5; in MathML output, the expression uses</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &lt;mstyle mathsize=&#8217;big&#8217;&gt;</dl>
</dl>
<dt><i>e1&nbsp;</i><code>smallover&nbsp;</code><i>e2</i></p>
<dd> This is similar to <code>over</code>; <code>smallover</code> reduces the size of <i>e1</i> and <i>e2</i>; it also puts less vertical space between <i>e1</i> or <i>e2</i> and the fraction bar. The <code>over</code> primitive corresponds to the TeX <code>\over</code> primitive in display styles; <code>smallover</code> corresponds to <code>\over</code> in non-display styles.</p>
<dt><code>vcenter&nbsp;</code><i>e</i></p>
<dd> This vertically centers <i>e</i> about the math axis. The math axis is the vertical position about which characters such as &#8216;+&#8217; and &#8216;-&#8216; are centered; also it is the vertical position used for the bar of fractions. For example, <code>sum</code> is defined as</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>{ type &quot;operator&quot; vcenter size +5 \(*S }</code></dl>
</dl>
<dt>
<dd> (Note that vcenter is silently ignored when generating MathML.)</p>
<dt><i>e1&nbsp;</i><code>accent&nbsp;</code><i>e2</i></p>
<dd> This sets <i>e2</i> as an accent over <i>e1</i>. <i>e2</i> is assumed to be at the correct height for a lowercase letter; <i>e2</i> is moved down according to whether <i>e1</i> is taller or shorter than a lowercase letter. For example, <code>hat</code> is defined as</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>accent { &quot;^&quot; }</code></dl>
</dl>
<dt>
<dd> <code>dotdot</code>, <code>dot</code>, <code>tilde</code>, <code>vec</code>, and <code>dyad</code> are also defined using the <code>accent</code> primitive.</p>
<dt><i>e1&nbsp;</i><code>uaccent&nbsp;</code><i>e2</i></p>
<dd> This sets <i>e2</i> as an accent under <i>e1</i>. <i>e2</i> is assumed to be at the correct height for a character without a descender; <i>e2</i> is moved down if <i>e1</i> has a descender. <code>utilde</code> is pre-defined using <code>uaccent</code> as a tilde accent below the baseline.</p>
<dt><code>split&nbsp;&quot;</code><i>text</i><code>&quot;</code></p>
<dd> This has the same effect as simply</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <i>text</i></dl>
</dl>
<dt>
<dd> but <i>text</i> is not subject to macro expansion because it is quoted; <i>text</i> is split up and the spacing between individual characters is adjusted.</p>
<dt><code>nosplit&nbsp;</code><i>text</i></p>
<dd> This has the same effect as</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>&quot;</code><i>text</i><code>&quot;</code></dl>
</dl>
<dt>
<dd> but because <i>text</i> is not quoted it is subject to macro expansion; <i>text</i> is not split up and the spacing between individual characters is not adjusted.</p>
<dt><i>e&nbsp;</i><code>opprime</code></p>
<dd> This is a variant of <code>prime</code> that acts as an operator on~<i>e</i>. It produces a different result from <code>prime</code> in a case such as <code>A opprime sub 1</code>: with <code>opprime</code> the~<code>1</code> is tucked under the prime as a subscript to the~<code>A</code> (as is conventional in mathematical typesetting), whereas with <code>prime</code> the~<code>1</code> is a subscript to the prime character. The precedence of <code>opprime</code> is the same as that of <code>bar</code> and <code>under</code>, which is higher than that of everything except <code>accent</code> and <code>uaccent</code>. In unquoted text a~<code>&#8216;</code> that is not the first character is treated like <code>opprime</code>.</p>
<dt><code>special&nbsp;</code><i>text e</i></p>
<dd> This constructs a new object from~<i>e</i> using a <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) macro named <i>text</i>. When the macro is called, the string <code>0s</code> contains the output for~<i>e</i>, and the number registers <code>0w</code>, <code>0h</code>, <code>0d</code>, <code>0skern</code>, and <code>0skew</code> contain the width, height, depth, subscript kern, and skew of~<i>e</i>. (The <i>subscript kern</i> of an object says how much a subscript on that object should be tucked in; the <i>skew</i> of an object says how far to the right of the center of the object an accent over the object should be placed.) The macro must modify <code>0s</code> so that it outputs the desired result with its origin at the current point, and increase the current horizontal position by the width of the object. The number registers must also be modified so that they correspond to the result.</p>
<dt>
<dd> For example, suppose you wanted a construct that &#8216;cancels&#8217; an expression by drawing a diagonal line through it.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code><br />
 .EQ<br />
 define cancel &#8216;special Ca&#8217;<br />
 .EN<br />
 .de Ca<br />
 .&nbsp;<wbr>&nbsp;ds 0s \<br />
 \Z&#8217;\*(0s&#8217;\<br />
 &#8217;\n(0du&#8217;\<br />
 \D&#8217;l \n(0wu -\n(0hu-\n(0du&#8217;\<br />
 &#8217;\n(0hu&#8217;<br />
 .. </code></dl>
</dl>
<dt>
<dd> Then you could cancel an expression~<i>e</i> with <code>cancel&nbsp;{&nbsp;</code><i>e&nbsp;</i><code>}</code></p>
<dt>
<dd> Here&#8217;s a more complicated construct that draws a box round an expression:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code> .EQ<br />
 define box &#8216;special Bx&#8217;<br />
 .EN<br />
 .de Bx<br />
 .&nbsp;<wbr>&nbsp;ds 0s \<br />
 \Z&#8217;\h&#8217;1n&#8217;\*(0s&#8217;\<br />
 \Z&#8217;\<br />
 &#8217;\n(0du+1n&#8217;\<br />
 \D&#8217;l \n(0wu+2n 0&#8217;\<br />
 \D&#8217;l 0 -\n(0hu-\n(0du-2n&#8217;\<br />
 \D&#8217;l -\n(0wu-2n 0&#8217;\<br />
 \D&#8217;l 0 \n(0hu+\n(0du+2n&#8217;\<br />
 &#8216;\<br />
 \h&#8217;\n(0wu+2n&#8217;<br />
 .&nbsp;<wbr>&nbsp;nr 0w +2n<br />
 .&nbsp;<wbr>&nbsp;nr 0d +1n<br />
 .&nbsp;<wbr>&nbsp;nr 0h +1n<br />
 .. </code></dl>
</dl>
<dt><code>space&nbsp;</code><i>n</i></p>
<dd> A positive value of the integer~<i>n</i> (in hundredths of an em) sets the vertical spacing before the equation, a negative value sets the spacing after the equation, replacing the default values. This primitive provides an interface to <code>groff</code>&#8216;s <code>
