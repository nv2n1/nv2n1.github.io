---
title: "parseyapp(3)"
name: "parseyapp"
section: "3"
letter: "p"
url: "/docs/linux/man/3-parseyapp/"
description: "Parse::Yapp – Perl extension for generating and using LALR parsers."
---

<p>Parse::Yapp &#8211; Perl extension for generating and using LALR parsers. </p>
<h2>Synopsis</h2>
<pre> yapp -m MyParser grammar_file.yp
 ...
 use MyParser;
 $parser=new MyParser();
 $value=$parser-&gt;YYParse(yylex =&gt; \&amp;lexer_sub, yyerror =&gt; \&amp;error_sub);
 $nberr=$parser-&gt;YYNberr();
 $parser-&gt;YYData-&gt;{DATA}= [ 'Anything', 'You Want' ];
 $data=$parser-&gt;YYData-&gt;{DATA}[0];</pre>
<h2>Description</h2>
<p>Parse::Yapp (Yet Another Perl Parser compiler) is a collection of modules that let you generate and use yacc like thread safe (reentrant) parsers with perl object oriented interface. </p>
<p> The script yapp is a front-end to the Parse::Yapp module and let you easily create a Perl <font SIZE="-1">OO</font> parser from an input grammar file.</p>
<h3>The Grammar file</h3>
<dl COMPACT>
<dt>&quot;Comments&quot;</p>
<dd>Through all your files, comments are either Perl style, introduced by <i>#</i> up to the end of line, or C style, enclosed between <i>/*</i> and <i>*/</i>.</p>
<dt>&quot;Tokens and string literals&quot;</p>
<dd>Through all the grammar files, two kind of symbols may appear: <i>Non-terminal</i> symbols, called also <i>left-hand-side</i> symbols, which are the names of your rules, and <i>Terminal</i> symbols, called also <i>Tokens</i>. </p>
<p> Tokens are the symbols your lexer function will feed your parser with (see below). They are of two flavours: symbolic tokens and string literals. </p>
<p> Non-terminals and symbolic tokens share the same identifier syntax: </p>
<pre> [A-Za-z][A-Za-z0-9_]*</pre>
<p>String literals are enclosed in single quotes and can contain almost anything. They will be output to your parser file double-quoted, making any special character as such. &#8216;&quot;&#8217;, &#8216;$&#8217; and &#8216;@&#8217; will be automatically quoted with &#8216;\&#8217;, making their writing more natural. On the other hand, if you need a single quote inside your literal, just quote it with &#8216;\&#8217;. </p>
<p> You cannot have a literal <i>&#8216;error&#8217;</i> in your grammar as it would confuse the driver with the <i>error</i> token. Use a symbolic token instead. In case you inadvertently use it, this will produce a warning telling you you should have written it <i>error</i> and will treat it as if it were the <i>error</i> token, which is certainly <font SIZE="-1">NOT</font> what you meant.</p>
<dt>&quot;Grammar file syntax&quot;</p>
<dd>It is very close to yacc syntax (in fact, <i>Parse::Yapp</i> should compile a clean <i>yacc</i> grammar without any modification, whereas the opposite is not true). </p>
<p> This file is divided in three sections, separated by <tt>&quot;%%&quot;</tt>: </p>
<pre> header section
 %%
 rules section
 %%
 footer section</pre>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>The Header Section</code> section may optionally contain:</p>
<dd>
<dt>*</p>
<dd>One or more code blocks enclosed inside <tt>&quot;%{&quot;</tt> and <tt>&quot;%}&quot;</tt> just like in yacc. They may contain any valid Perl code and will be copied verbatim at the very beginning of the parser module. They are not as useful as they are in yacc, but you can use them, for example, for global variable declarations, though you will notice later that such global variables can be avoided to make a reentrant parser module.</p>
<dt>*</p>
<dd>Precedence declarations, introduced by <tt>%left</tt>, <tt>%right</tt> and <tt>%nonassoc</tt> specifying associativity, followed by the list of tokens or litterals having the same precedence and associativity. The precedence beeing the latter declared will be having the highest level. (see the yacc or bison manuals for a full explanation of how they work, as they are implemented exactly the same way in Parse::Yapp)</p>
<dt>*</p>
<dd><tt>%start</tt> followed by a rule&#8217;s left hand side, declaring this rule to be the starting rule of your grammar. The default, when <tt>%start</tt> is not used, is the first rule in your grammar section.</p>
<dt>*</p>
<dd><tt>%token</tt> followed by a list of symbols, forcing them to be recognized as tokens, generating a syntax error if used in the left hand side of a rule declaration. Note that in Parse::Yapp, you <i>don&#8217;t</i> need to declare tokens as in yacc: any symbol not appearing as a left hand side of a rule is considered to be a token. Other yacc declarations or constructs such as <tt>%type</tt> and <tt>%union</tt> are parsed but (almost) ignored.</p>
<dt>*</p>
<dd><tt>%expect</tt> followed by a number, suppress warnings about number of Shift/Reduce conflicts when both numbers match, a la bison.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>The Rule Section</code> contains your grammar rules:</p>
<dd>A rule is made of a left-hand-side symbol, followed by a <tt>':'</tt> and one or more right-hand-sides separated by <tt>'|'</tt> and terminated by a <tt>';'</tt>: </p>
<pre> exp: exp '+' exp
 | exp '-' exp
 ;</pre>
<p>A right hand side may be empty: </p>
<pre> input: #empty
 | input line
 ;</pre>
<p>(if you have more than one empty rhs, Parse::Yapp will issue a warning, as this is usually a mistake, and you will certainly have a reduce/reduce conflict) </p>
<p> A rhs may be followed by an optional <tt>%prec</tt> directive, followed by a token, giving the rule an explicit precedence (see yacc manuals for its precise meaning) and optional semantic action code block (see below). </p>
<pre> exp: '-' exp %prec NEG { -$_[1] }
 | exp '+' exp { $_[1] + $_[3] }
 | NUM
 ;</pre>
<p>Note that in Parse::Yapp, a lhs <i>cannot</i> appear more than once as a rule name (This differs from yacc).</p>
<dt>&quot;The footer section&quot;</p>
<dd>may contain any valid Perl code and will be appended at the very end of your parser module. Here you can write your lexer, error report subs and anything relevant to you parser.</p>
<dt>&quot;Semantic actions&quot;</p>
<dd>Semantic actions are run every time a <i>reduction</i> occurs in the parsing flow and they must return a semantic value. </p>
<p> They are (usually, but see below <tt>&quot;In rule actions&quot;</tt>) written at the very end of the rhs, enclosed with <tt>&quot;{ }&quot;</tt>, and are copied verbatim to your parser file, inside of the rules table. </p>
<p> Be aware that matching braces in Perl is much more difficult than in C: inside strings they don&#8217;t need to match. While in C it is very easy to detect the beginning of a string construct, or a single character, it is much more difficult in Perl, as there are so many ways of writing such literals. So there is no check for that today. If you need a brace in a double-quoted string, just quote it (<tt>&quot;\{&quot;</tt> or <tt>&quot;\}&quot;</tt>). For single-quoted strings, you will need to make a comment matching it <i>in th right order</i>. Sorry for the inconvenience. </p>
<pre> {
 &quot;{ My string block }&quot;.
 &quot;\{ My other string block \}&quot;.
 qq/ My unmatched brace \} /.
 # Force the match: {
 q/ for my closing brace } /
 q/ My opening brace { /
 # must be closed: }
 }</pre>
<p>All of these constructs should work. </p>
<p> In Parse::Yapp, semantic actions are called like normal Perl sub calls, with their arguments passed in <tt>@_</tt>, and their semantic value are their return values. </p>
<p> <tt>$_</tt>[1] to <tt>$_</tt>[n] are the parameters just as <tt>$1</tt> to <tt>$n</tt> in yacc, while <tt>$_</tt>[0] is the parser object itself. </p>
<p> Having <tt>$_</tt>[0] beeing the parser object itself allows you to call parser methods. Thats how the yacc macros are implemented: </p>
<pre> yyerrok is done by calling $_[0]-&gt;YYErrok
 YYERROR is done by calling $_[0]-&gt;YYError
 YYACCEPT is done by calling $_[0]-&gt;YYAccept
 YYABORT is done by calling $_[0]-&gt;YYAbort</pre>
<p>All those methods explicitly return <i>undef</i>, for convenience. </p>
<pre> YYRECOVERING is done by calling $_[0]-&gt;YYRecovering</pre>
<p>Four useful methods in error recovery sub </p>
<pre> $_[0]-&gt;YYCurtok
 $_[0]-&gt;YYCurval
 $_[0]-&gt;YYExpect
 $_[0]-&gt;YYLexer</pre>
<p>return respectivly the current input token that made the parse fail, its semantic value (both can be used to modify their values too, but <i>know what you are doing</i> ! See <i>Error reporting routine</i> section for an example), a list which contains the tokens the parser expected when the failure occured and a reference to the lexer routine. </p>
<p> Note that if <tt>&quot;$_[0]-&gt;YYCurtok&quot;</tt> is declared as a <tt>%nonassoc</tt> token, it can be included in <tt>&quot;$_[0]-&gt;YYExpect&quot;</tt> list whenever the input try to use it in an associative way. This is not a bug: the token <font SIZE="-1">IS</font> expected to report an error if encountered. </p>
<p> To detect such a thing in your error reporting sub, the following example should do the trick: </p>
<pre> grep { $_[0]-&gt;YYCurtok eq $_ } $_[0]-&gt;YYExpect
 and do {
 #Non-associative token used in an associative expression
 };</pre>
<p>Accessing semantics values on the left of your reducing rule is done through the method </p>
<pre> $_[0]-&gt;YYSemval( index )</pre>
<p>where index is an integer. Its value being <i>1 .. n</i> returns the same values than <i></i>$_<i>[1] .. </i>$_<i>[n]</i>, but <i>-n .. 0</i> returns values on the left of the rule beeing reduced (It is related to <i>$-n .. </i>$0<i> .. </i>$n<i></i> in yacc, but you cannot use <i></i>$_<i>[0]</i> or <i></i>$_<i>[-n]</i> constructs in Parse::Yapp for obvious reasons) </p>
<p> There is also a provision for a user data area in the parser object, accessed by the method: </p>
<pre> $_[0]-&gt;YYData</pre>
<p>which returns a reference to an anonymous hash, which let you have all of your parsing data held inside the object (see the Calc.yp or ParseYapp.yp files in the distribution for some examples). That&#8217;s how you can make you parser module reentrant: all of your module states and variables are held inside the parser object. </p>
<p> Note: unfortunatly, method calls in Perl have a lot of overhead,<br />
and when YYData is used, it may be called a huge number<br />
of times. If your are not a&nbsp;<wbr>*real*&nbsp;<wbr>purist and efficiency<br />
is your concern, you may access directly the user-space<br />
in the object:&nbsp;<wbr><tt>$parser</tt>-&gt;{<font SIZE="-1">USER</font>}&nbsp;<wbr>wich is a reference to an<br />
anonymous hash array, and then benchmark. </p>
<p> If no action is specified for a rule, the equivalant of a default action is run, which returns the first parameter: </p>
<pre> { $_[1] }</pre>
<dt>&quot;In rule actions&quot;</p>
<dd>It is also possible to embed semantic actions inside of a rule: </p>
<pre> typedef: TYPE { $type = $_[1] } identlist { ... } ;</pre>
<p>When the Parse::Yapp&#8217;s parser encounter such an embedded action, it modifies the grammar as if you wrote (although <tt>@x</tt>-1 is not a legal lhs value): </p>
<pre> @x-1: /* empty */ { $type = $_[1] };
 typedef: TYPE @x-1 identlist { ... } ;</pre>
<p>where <i>x</i> is a sequential number incremented for each &#8220;in rule&#8221; action, and <i>-1</i> represents the &#8220;dot position&#8221; in the rule where the action arises. </p>
<p> In such actions, you can use <i></i>$_<i>[1]..$_[n]</i> variables, which are the semantic values on the left of your action. </p>
<p> Be aware that the way Parse::Yapp modifies your grammar because of <i>in rule actions</i> can produce, in some cases, spurious conflicts that wouldn&#8217;t happen otherwise.</p>
<dt>&quot;Generating the Parser Module&quot;</p>
<dd>Now that you grammar file is written, you can use yapp on it to generate your parser module: </p>
<pre> yapp -v Calc.yp</pre>
<p>will create two files <i>Calc.pm</i>, your parser module, and <i>Calc.output</i> a verbose output of your parser rules, conflicts, warnings, states and summary. </p>
<p> What your are missing now is a lexer routine.</p>
<dt>&quot;The Lexer sub&quot;</p>
<dd>is called each time the parser need to read the next token. </p>
<p> It is called with only one argument that is the parser object itself, so you can access its methods, specially the </p>
<pre> $_[0]-&gt;YYData</pre>
<p>data area. </p>
<p> It is its duty to return the next token and value to the parser. They <tt>&quot;must&quot;</tt> be returned as a list of two variables, the first one is the token known by the parser (symbolic or literal), the second one beeing anything you want (usually the content of the token, or the literal value) from a simple scalar value to any complex reference, as the parsing driver never use it but to call semantic actions: </p>
<pre> ( 'NUMBER', $num )
or
 ( '&gt;=', '&gt;=' )
or
 ( 'ARRAY', [ @values ] )</pre>
<p>When the lexer reach the end of input, it must return the <tt>''</tt> empty token with an undef value: </p>
<pre> ( '', undef )</pre>
<p>Note that your lexer should <i>never</i> return <tt>'error'</tt> as token value: for the driver, this is the error token used for error recovery and would lead to odd reactions. </p>
<p> Now that you have your lexer written, maybe you will need to output meaningful error messages, instead of the default which is to print &#8216;Parse error.&#8217; on <font SIZE="-1">STDERR.</font> </p>
<p> So you will need an Error reporting sub.</p>
<dt>&quot;Error reporting routine&quot;</p>
<dd>If you want one, write it knowing that it is passed as parameter the parser object. So you can share information whith the lexer routine quite easily. </p>
<p> You can also use the <tt>&quot;$_[0]-&gt;YYErrok&quot;</tt> method in it, which will resume parsing as if no error occured. Of course, since the invalid token is still invalid, you&#8217;re supposed to fix the problem by yourself. </p>
<p> The method <tt>&quot;$_[0]-&gt;YYLexer&quot;</tt> may help you, as it returns a reference to the lexer routine, and can be called as </p>
<pre> ($tok,$val)=&amp;{$_[0]-&gt;Lexer}</pre>
<p>to get the next token and semantic value from the input stream. To make them current for the parser, use: </p>
<pre> ($_[0]-&gt;YYCurtok, $_[0]-&gt;YYCurval) = ($tok, $val)</pre>
<p>and know what you&#8217;re doing&#8230;</p>
<dt>&quot;Parsing&quot;</p>
<dd>Now you&#8217;ve got everything to do the parsing. </p>
<p> First, use the parser module: </p>
<pre> use Calc;</pre>
<p>Then create the parser object: </p>
<pre> $parser=new Calc;</pre>
<p>Now, call the YYParse method, telling it where to find the lexer and error report subs: </p>
<pre> $result=$parser-&gt;YYParse(yylex =&gt; \&amp;Lexer,
 yyerror =&gt; \&amp;ErrorReport);</pre>
<p>(assuming Lexer and ErrorReport subs have been written in your current package) </p>
<p> The order in which parameters appear is unimportant. </p>
<p> Et voila. </p>
<p> The YYParse method will do the parse, then return the last semantic value returned, or undef if error recovery cannot recover. </p>
<p> If you need to be sure the parse has been successful (in case your last returned semantic value <i>is</i> undef) make a call to: </p>
<pre> $parser-&gt;YYNberr()</pre>
<p>which returns the total number of time the error reporting sub has been called.</p>
<dt>&quot;Error Recovery&quot;</p>
<dd>in Parse::Yapp is implemented the same way it is in yacc.</p>
<dt>&quot;Debugging Parser&quot;</p>
<dd>To debug your parser, you can call the YYParse method with a debug parameter: </p>
<pre> $parser-&gt;YYParse( ... , yydebug =&gt; value, ... )</pre>
<p>where value is a bitfield, each bit representing a specific debug output: </p>
<pre> Bit Value Outputs
 0x01 Token reading (useful for Lexer debugging)
 0x02 States information
 0x04 Driver actions (shifts, reduces, accept...)
 0x08 Parse Stack dump
 0x10 Error Recovery tracing</pre>
<p>To have a full debugging ouput, use </p>
<pre> debug =&gt; 0x1F</pre>
<p>Debugging output is sent to <font SIZE="-1">STDERR,</font> and be aware that it can produce <tt>&quot;huge&quot;</tt> outputs.</p>
<dt>&quot;Standalone Parsers&quot;</p>
<dd>By default, the parser modules generated will need the Parse::Yapp module installed on the system to run. They use the Parse::Yapp::Driver which can be safely shared between parsers in the same script. </p>
<p> In the case you&#8217;d prefer to have a standalone module generated, use the <tt>&quot;-s&quot;</tt> switch with yapp: this will automagically copy the driver code into your module so you can use/distribute it without the need of the Parse::Yapp module, making it really a <tt>&quot;Standalone Parser&quot;</tt>. </p>
<p> If you do so, please remember to include Parse::Yapp&#8217;s copyright notice in your main module copyright, so others can know about Parse::Yapp module.</p>
<dt>&quot;Source file line numbers&quot;</p>
<dd>by default will be included in the generated parser module, which will help to find the guilty line in your source file in case of a syntax error. You can disable this feature by compiling your grammar with yapp using the <tt>&quot;-n&quot;</tt> switch.</dl>
<h2>Bugs And Suggestions</h2>
<p>If you find bugs, think of anything that could improve Parse::Yapp or have any questions related to it, feel free to contact the author.</p>
<h2>Author</h2>
<p>Francois Desarmenien &lt;francois [at] fdesar.net&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-yapp/">yapp</a></i>(1) <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1) <i><a href="/docs/linux/man/1-yacc/">yacc</a></i>(1) <i><a href="/docs/linux/man/1-bison/">bison</a></i>(1).</p>
<h2>Copyright</h2>
<p>The Parse::Yapp module and its related modules and shell scripts are copyright (c) 1998-2001 Francois Desarmenien, France. All rights reserved. </p>
<p> You may use and distribute them under the terms of either the <font SIZE="-1">GNU</font> General Public License or the Artistic License, as specified in the Perl <font SIZE="-1">README</font> file. </p>
<p> If you use the &#8220;standalone parser&#8221; option so people don&#8217;t need to install Parse::Yapp on their systems in order to run you software, this copyright noticed should be included in your software copyright too, and the copyright notice in the embedded driver should be left untouched.</p>
<h2>Pod Errors</h2>
<p>Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl COMPACT>
<dt>Around line 112:</p>
<dd>Expected text after =item, not a bullet</p>
<dt>Around line 121:</p>
<dd>Expected text after =item, not a bullet</p>
<dt>Around line 130:</p>
<dd>Expected text after =item, not a bullet</p>
<dt>Around line 136:</p>
<dd>Expected text after =item, not a bullet</p>
<dt>Around line 147:</p>
<dd>Expected text after =item, not a bullet </p>
</dl>
