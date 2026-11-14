---
title: "ptop(5)"
name: "ptop"
section: "5"
letter: "p"
url: "/docs/linux/man/5-ptop/"
description: "ptop.cfg – The ptop source-beautifier configuration file. ptop is the source beautifier of the FreePascal project. Origin probably Pascal-TO-Pascal.cfg"
---

<p>ptop.cfg &#8211; The ptop source-beautifier configuration file. ptop is the source beautifier of the FreePascal project. Origin probably Pascal-TO-Pascal.cfg </p>
<h2>Description</h2>
<p>This is the main configuration file of the <i>ptop FPC source beautifier</i> The configuration file for <code><a href="/docs/linux/man/1-ptop/">ptop</a></code>(1) isn&#8217;t necessarily called ptop.cfg, and is also not auto-loaded, so the name doesn&#8217;t matter much. This man-page describes the structure of such a configuration file for <code><a href="/docs/linux/man/1-ptop/">ptop</a></code>(1) </p>
<h2>Structure</h2>
<p>The structure of a ptop configuration file is a simple building block repeated several (60-70) times, once for each pascal keyword known to the ptop program. (see the default configuration file or ptopu.pp source to find out which keywords are known) </p>
<p> The basic building block of the configuration file consists out of one, two or three lines, describing how ptop should react on a certain keyword. First a line without square brackets with the following format: </p>
<p> keyword=option1,option2,option3,&#8230; </p>
<p> If one of the options is &quot;dindonkey&quot; (see further below), a second line (with square brackets) is needed like this: </p>
<p> [keyword]=otherkeyword1,otherkeyword2,otherkeyword3,&#8230; </p>
<p> Then if one of the options is &quot;gobsym&quot;, a third line (with angle brackets) is needed like this: </p>
<p> &lt;keyword&gt;=terminalword1,terminalword2,terminalword3,&#8230; </p>
<p> As you can see the block contains two types of identifiers, keywords(keyword, otherkeyword1..3 and terminalword1..3 in the above example) and options, (option1..3 above). </p>
<p> <i>Keywords</i> are the built-in valid Pascal structure-identifiers like BEGIN, END, CASE, IF, THEN, ELSE, IMPLEMENTATION. The default configuration file lists most of these. </p>
<p> Besides the real Pascal keywords, some other codewords are used for operators and comment expressions. These are listed in the following table: </p>
<p> Name of codeword operator<br />
 &#8212;&#8212;&#8212;&#8212;- &#8212;&#8211;<br />
 casevar : in a case label (&lt;&gt;&#8217;colon&#8217;)<br />
 becomes :=<br />
 delphicomment //<br />
 opencomment { or (*<br />
 closecomment } or *)<br />
 semicolon ;<br />
 colon :<br />
 equals =<br />
 openparen [<br />
 closeparen ]<br />
 period . </p>
<p> The <i>Options</i> codewords define actions to be taken when the keyword before the equal sign is found. </p>
<p> Option<tt>&nbsp;<wbr></tt> does what</p>
<p> &#8212;&#8212;- &#8212;&#8212;&#8212;<br />
 crsupp suppress CR before the keyword.<br />
 crbefore force CR before keyword<br />
 (doesn&#8217;t go with crsupp :) )<br />
 blinbefore blank line before keyword.<br />
 dindonkey de-indent on assiociated keywords (see below)<br />
 dindent de-indent (always)<br />
 spbef space before<br />
 spaft space after<br />
 gobsym Print symbols which follow a keyword,<br />
 but which do not affect layout.<br />
 Prints until terminators occur.<br />
 inbytab indent by tab.<br />
 crafter force CR after keyword.<br />
 upper prints keyword all uppercase<br />
 lower prints keyword all lowercase<br />
 capital capitalizes keyword: 1st letter<br />
 uppercase, rest lowercase. </p>
<p> The option &quot;dindonkey&quot; requires some extra parameters, which are set by a second line for that keyword (the one with the square brackets), which is therefore only needed if the options contain &quot;dinkdonkey&quot; (contraction of de-indent on assiociated keyword). </p>
<p> &quot;dinkdonkey&quot; deindents if any of the keywords specified by the extra options of the square-bracket line is found. </p>
<p> In a similar manner the option &quot;gobsym&quot;, short for gobble symbols, requires some additional information in order to perform its function. The &quot;gobsym&quot; option indicates that all symbols following the keyword should be passed through unchanged until a terminal symbol is reached. The list of acceptable termial symbols is provided by the angle-bracket line.</p>
<h2>Examples</h2>
<p>The block else=crbefore,dindonkey,inbytab,upper<br />
 [else]=if,then,else Means: The keyword this is about is <i>else</i> , it&#8217;s on the LEFT side of both equal signs. When the ptop parser finds ELSE, the options tell it to do the following things: &#8211; (crbefore) Don&#8217;t allow other code on the line before<br />
 &nbsp;<wbr> the keyword. (ELSE alone on a line)<br />
 &#8211; (dindonkey) De-indent on the keywords<br />
 &nbsp;<wbr> in square brackets line (if,then,else)<br />
 &#8211; (inbytab) indent by tab.<br />
 &#8211; (upper) uppercase the keyword (ELSE) The block case=spaft,gobsym,inbytab,crafter,capital<br />
 &lt;case&gt;=ofsym Means: The keyword this is about is <i>case</i> , it&#8217;s on the LEFT side of both equal signs. When case is found, the options tell it to do the following things: &#8211; (spaft) Insure that there is a space<br />
 &nbsp;<wbr> after the keyword. (case)<br />
 &#8211; (gobsym) pass symbols through unchanced until one of<br />
 &nbsp;<wbr> the words in the angle brackets line (of) is found.<br />
 &#8211; (crafter) Make sure terminator (of) ends the line.<br />
 &#8211; (inbytab) indent by tab.<br />
 &#8211; (capital) Capitalize the keyword (case becomes Case). Try to play with the configfile until you find the effect you desire. The configurability and possibilities of ptop are quite large compared to other shareware source beautifiers found on e.g. SIMTEL. </p>
<h2>Acknowledgements</h2>
<p>The writer of the program, Michael van Canneyt, who also helped out explaining the format of ptop.cfg. </p>
<p> Questions/corrections can be mailed to fpc-devel [at] vekoll.saturnus.vein.hu </p>
<p> Also thanks to the rest of the FPC development team.</p>
<h2>See Also</h2>
<dl>
<dt>ptop binary</p>
<dd><code><a href="/docs/linux/man/1-ptop/">ptop</a></code>(1)</p>
<dt>Compiler</p>
<dd><code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1)</p>
<dt>Other FPC utils</p>
<dd><code><a href="/docs/linux/man/1-ppdep/">ppdep</a></code>(1) <code><a href="/docs/linux/man/1-ppudump/">ppudump</a></code>(1) <code><a href="/docs/linux/man/1-ppumove/">ppumove</a></code>(1) <code><a href="/docs/linux/man/1-h2pas/">h2pas</a></code>(1) </p>
