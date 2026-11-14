---
title: "perlreguts(1)"
name: "perlreguts"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlreguts/"
description: "perlreguts – Description of the Perl regular expression engine."
---

<h2 class="name">NAME</h2>
<p> perlreguts &#8211; Description of the Perl regular expression engine. </p>
<h2>DESCRIPTION</h2>
<p> This document is an attempt to shine some light on the guts of the regex engine and how it works. The regex engine represents a significant chunk of the perl codebase, but is relatively poorly understood. This document is a meagre attempt at addressing this situation. It is derived from the author&#8217;s experience, comments in the source code, other papers on the regex engine, feedback on the perl5-porters mail list, and no doubt other places as well. </p>
<p> <font SIZE="-1"><code>NOTICE</code></font><code>!</code> It should be clearly understood that the behavior and structures discussed in this represents the state of the engine as the author understood it at the time of writing. It is <font SIZE="-1"><code>NOT</code></font> an <font SIZE="-1">API</font> definition, it is purely an internals guide for those who want to hack the regex engine, or understand how the regex engine works. Readers of this document are expected to understand perl&#8217;s regex syntax and its usage in detail. If you want to learn about the basics of Perl&#8217;s regular expressions, see perlre. And if you want to replace the regex engine with your own, see perlreapi.</p>
<h2>OVERVIEW</h2>
<h3>A quick note on terms</h3>
<p> There is some debate as to whether to say &#8220;regexp&#8221; or &#8220;regex&#8221;. In this document we will use the term &#8220;regex&#8221; unless there is a special reason not to, in which case we will explain why. </p>
<p> When speaking about regexes we need to distinguish between their source code form and their internal form. In this document we will use the term &#8220;pattern&#8221; when we speak of their textual, source code form, and the term &#8220;program&#8221; when we speak of their internal representation. These correspond to the terms <i>S-regex</i> and <i>B-regex</i> that Mark Jason Dominus employs in his paper on &#8220;Rx&#8221; ([1] in &#8220;<font SIZE="-1">REFERENCES&#8221;</font>).</p>
<h3>What is a regular expression engine?</h3>
<p> A regular expression engine is a program that takes a set of constraints specified in a mini-language, and then applies those constraints to a target string, and determines whether or not the string satisfies the constraints. See perlre for a full definition of the language. </p>
<p> In less grandiose terms, the first part of the job is to turn a pattern into something the computer can efficiently use to find the matching point in the string, and the second part is performing the search itself. </p>
<p> To do this we need to produce a program by parsing the text. We then need to execute the program to find the point in the string that matches. And we need to do the whole thing efficiently.</p>
<h3>Structure of a Regexp Program</h3>
<p> <i>High Level</i> </p>
<p> Although it is a bit confusing and some people object to the terminology, it is worth taking a look at a comment that has been in <i>regexp.h</i> for years: </p>
<p> <i>This is essentially a linear encoding of a nondeterministic finite-state machine (aka syntax charts or &#8220;railroad normal form&#8221; in parsing technology).</i> </p>
<p> The term &#8220;railroad normal form&#8221; is a bit esoteric, with &#8220;syntax diagram/charts&#8221;, or &#8220;railroad diagram/charts&#8221; being more common terms. Nevertheless it provides a useful mental image of a regex program: each node can be thought of as a unit of track, with a single entry and in most cases a single exit point (there are pieces of track that fork, but statistically not many), and the whole forms a layout with a single entry and single exit point. The matching process can be thought of as a car that moves along the track, with the particular route through the system being determined by the character read at each possible connector point. A car can fall off the track at any point but it may only proceed as long as it matches the track. </p>
<p> Thus the pattern <tt>&quot;/foo(?:\w+|\d+|\s+)bar/&quot;</tt> can be thought of as the following chart: </p>
<pre><code>
[start] |
    &lt;foo&gt; |
    +-- -- -+-- -- -+ | | |
    &lt;\w +&gt;&lt;\d +&gt;&lt;\s +&gt; | | |
    +-- -- -+-- -- -+ |
    &lt;bar&gt; |
    [end]
</code></pre>
<p> The truth of the matter is that perl&#8217;s regular expressions these days are much more complex than this kind of structure, but visualising it this way can help when trying to get your bearings, and it matches the current implementation pretty closely. </p>
<p> To be more precise, we will say that a regex program is an encoding of a graph. Each node in the graph corresponds to part of the original regex pattern, such as a literal string or a branch, and has a pointer to the nodes representing the next component to be matched. Since &#8220;node&#8221; and &#8220;opcode&#8221; already have other meanings in the perl source, we will call the nodes in a regex program &#8220;regops&#8221;. </p>
<p> The program is represented by an array of <tt>&quot;regnode&quot;</tt> structures, one or more of which represent a single regop of the program. Struct <tt>&quot;regnode&quot;</tt> is the smallest struct needed, and has a field structure which is shared with all the other larger structures. </p>
<p> The &#8220;next&#8221; pointers of all regops except <tt>&quot;BRANCH&quot;</tt> implement concatenation; a &#8220;next&#8221; pointer with a <tt>&quot;BRANCH&quot;</tt> on both ends of it is connecting two alternatives. [Here we have one of the subtle syntax dependencies: an individual <tt>&quot;BRANCH&quot;</tt> (as opposed to a collection of them) is never concatenated with anything because of operator precedence.] </p>
<p> The operand of some types of regop is a literal string; for others, it is a regop leading into a sub-program. In particular, the operand of a <tt>&quot;BRANCH&quot;</tt> node is the first regop of the branch. </p>
<p> <font SIZE="-1"><code>NOTE</code></font>: As the railroad metaphor suggests, this is <code>not</code> a tree structure: the tail of the branch connects to the thing following the set of <tt>&quot;BRANCH&quot;</tt>es. It is a like a single line of railway track that splits as it goes into a station or railway yard and rejoins as it comes out the other side. </p>
<p> <i>Regops</i> </p>
<p> The base structure of a regop is defined in <i>regexp.h</i> as follows: </p>
<p>struct regnode {<br />
    U8 flags;     /* Various purposes, sometimes overridden */<br />
    U8 type;      /* Opcode value as specified by regnodes.h */<br />
    U16 next_off; /* Offset in size regnode */<br />
};</p>
<p> Other larger <tt>&quot;regnode&quot;</tt>-like structures are defined in <i>regcomp.h</i>. They are almost like subclasses in that they have the same fields as <tt>&quot;regnode&quot;</tt>, with possibly additional fields following in the structure, and in some cases the specific meaning (and name) of some of base fields are overridden. The following is a more complete description.</p>
<dl>
<dt>&quot;regnode_1&quot;</p>
<dd>
<dt>&quot;regnode_2&quot;</p>
<dd> <tt>&quot;regnode_1&quot;</tt> structures have the same header, followed by a single four-byte argument; <tt>&quot;regnode_2&quot;</tt> structures contain two two-byte arguments instead: </p>
<pre>
    regnode_1                U32 arg1;
    regnode_2                U16 arg1;  U16 arg2;
</pre>
<dt>&quot;regnode_string&quot;</p>
<dd> <tt>&quot;regnode_string&quot;</tt> structures, used for literal strings, follow the header with a one-byte length and then the string data. Strings are padded on the end with zero bytes so that the total length of the node is a multiple of four bytes: </p>
<p>regnode_string char string[1];<br />
U8 str_len; /* overrides flags */</p>
<dt>&quot;regnode_charclass&quot;</p>
<dd> Bracketed character classes are represented by <tt>&quot;regnode_charclass&quot;</tt> structures, which have a four-byte argument and then a 32-byte (256-bit) bitmap indicating which characters in the Latin1 range are included in the class. </p>
<p>regnode_charclass U32 arg1;<br />
char bitmap[ANYOF_BITMAP_SIZE];</p>
<p> Various flags whose names begin with <tt>&quot;ANYOF_&quot;</tt> are used for special situations. Above Latin1 matches and things not known until run-time are stored in &#8220;Perl&#8217;s pprivate structure&#8221;.</p>
<dt>&quot;regnode_charclass_posixl&quot;</p>
<dd> There is also a larger form of a char class structure used to represent <font SIZE="-1">POSIX</font> char classes under <tt>&quot;/l&quot;</tt> matching, called <tt>&quot;regnode_charclass_posixl&quot;</tt> which has an additional 32-bit bitmap indicating which <font SIZE="-1">POSIX</font> char classes have been included. </p>
<p>regnode_charclass_posixl U32 arg1;<br />
char bitmap[ANYOF_BITMAP_SIZE];<br />
U32 classflags;
</dl>
<p> <i>regnodes.h</i> defines an array called <tt>&quot;regarglen[]&quot;</tt> which gives the size of each opcode in units of <tt>&quot;size regnode&quot;</tt> (4-byte). A macro is used to calculate the size of an <tt>&quot;EXACT&quot;</tt> node based on its <tt>&quot;str_len&quot;</tt> field. </p>
<p> The regops are defined in <i>regnodes.h</i> which is generated from <i>regcomp.sym</i> by <i>regcomp.pl</i>. Currently the maximum possible number of distinct regops is restricted to 256, with about a quarter already used. </p>
<p> A set of macros makes accessing the fields easier and more consistent. These include <tt>&quot;OP()&quot;</tt>, which is used to determine the type of a <tt>&quot;regnode&quot;</tt>-like structure; <tt>&quot;NEXT_OFF()&quot;</tt>, which is the offset to the next node (more on this later); <tt>&quot;ARG()&quot;</tt>, <tt>&quot;ARG1()&quot;</tt>, <tt>&quot;ARG2()&quot;</tt>, <tt>&quot;ARG_SET()&quot;</tt>, and equivalents for reading and setting the arguments; and <tt>&quot;STR_LEN()&quot;</tt>, <tt>&quot;STRING()&quot;</tt> and <tt>&quot;OPERAND()&quot;</tt> for manipulating strings and regop bearing types. </p>
<p> <i>What regop is next?</i> </p>
<p> There are three distinct concepts of &#8220;next&#8221; in the regex engine, and it is important to keep them clear.</p>
<dl>
<dt>&bull;</p>
<dd> There is the &#8220;next regnode&#8221; from a given regnode, a value which is rarely useful except that sometimes it matches up in terms of value with one of the others, and that sometimes the code assumes this to always be so.</p>
<dt>&bull;</p>
<dd> There is the &#8220;next regop&#8221; from a given regop/regnode. This is the regop physically located after the current one, as determined by the size of the current regop. This is often useful, such as when dumping the structure we use this order to traverse. Sometimes the code assumes that the &#8220;next regnode&#8221; is the same as the &#8220;next regop&#8221;, or in other words assumes that the sizeof a given regop type is always going to be one regnode large.</p>
<dt>&bull;</p>
<dd> There is the &#8220;regnext&#8221; from a given regop. This is the regop which is reached by jumping forward by the value of <tt>&quot;NEXT_OFF()&quot;</tt>, or in a few cases for longer jumps by the <tt>&quot;arg1&quot;</tt> field of the <tt>&quot;regnode_1&quot;</tt> structure. The subroutine <tt>&quot;regnext()&quot;</tt> handles this transparently. This is the logical successor of the node, which in some cases, like that of the <tt>&quot;BRANCH&quot;</tt> regop, has special meaning.</dl>
<h2>Process Overview</h2>
<p> Broadly speaking, performing a match of a string against a pattern involves the following steps:</p>
<dl>
<dt>A. Compilation</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>1. Parsing for size</p>
<dd>
<dt>2. Parsing for construction</p>
<dd>
<dt>3. Peep-hole optimisation and analysis</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>B. Execution</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>4. Start position and no-match optimisations</p>
<dd>
<dt>5. Program execution</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Where these steps occur in the actual execution of a perl program is determined by whether the pattern involves interpolating any string variables. If interpolation occurs, then compilation happens at run time. If it does not, then compilation is performed at compile time. (The <tt>&quot;/o&quot;</tt> modifier changes this, as does <tt>&quot;qr//&quot;</tt> to a certain extent.) The engine doesn&#8217;t really care that much.</p>
<h3>Compilation</h3>
<p> This code resides primarily in <i>regcomp.c</i>, along with the header files <i>regcomp.h</i>, <i>regexp.h</i> and <i>regnodes.h</i>. </p>
<p> Compilation starts with <tt>&quot;pregcomp()&quot;</tt>, which is mostly an initialisation wrapper which farms work out to two other routines for the heavy lifting: the first is <tt>&quot;reg()&quot;</tt>, which is the start point for parsing; the second, <tt>&quot;study_chunk()&quot;</tt>, is responsible for optimisation. </p>
<p> Initialisation in <tt>&quot;pregcomp()&quot;</tt> mostly involves the creation and data-filling of a special structure, <tt>&quot;RExC_state_t&quot;</tt> (defined in <i>regcomp.c</i>). Almost all internally-used routines in <i>regcomp.h</i> take a pointer to one of these structures as their first argument, with the name <tt>&quot;pRExC_state&quot;</tt>. This structure is used to store the compilation state and contains many fields. Likewise there are many macros which operate on this variable: anything that looks like <tt>&quot;RExC_xxxx&quot;</tt> is a macro that operates on this pointer/structure. </p>
<p> <i>Parsing for size</i> </p>
<p> In this pass the input pattern is parsed in order to calculate how much space is needed for each regop we would need to emit. The size is also used to determine whether long jumps will be required in the program. </p>
<p> This stage is controlled by the macro <tt>&quot;SIZE_ONLY&quot;</tt> being set. </p>
<p> The parse proceeds pretty much exactly as it does during the construction phase, except that most routines are short-circuited to change the size field <tt>&quot;RExC_size&quot;</tt> and not do anything else. </p>
<p> <i>Parsing for construction</i> </p>
<p> Once the size of the program has been determined, the pattern is parsed again, but this time for real. Now <tt>&quot;SIZE_ONLY&quot;</tt> will be false, and the actual construction can occur. </p>
<p> <tt>&quot;reg()&quot;</tt> is the start of the parse process. It is responsible for parsing an arbitrary chunk of pattern up to either the end of the string, or the first closing parenthesis it encounters in the pattern. This means it can be used to parse the top-level regex, or any section inside of a grouping parenthesis. It also handles the &#8220;special parens&#8221; that perl&#8217;s regexes have. For instance when parsing <tt>&quot;/x(?:foo)y/&quot;</tt> <tt>&quot;reg()&quot;</tt> will at one point be called to parse from the &#8220;?&#8221; symbol up to and including the &#8220;)&#8221;. </p>
<p> Additionally, <tt>&quot;reg()&quot;</tt> is responsible for parsing the one or more branches from the pattern, and for &#8220;finishing them off&#8221; by correctly setting their next pointers. In order to do the parsing, it repeatedly calls out to <tt>&quot;regbranch()&quot;</tt>, which is responsible for handling up to the first <tt>&quot;|&quot;</tt> symbol it sees. </p>
<p> <tt>&quot;regbranch()&quot;</tt> in turn calls <tt>&quot;regpiece()&quot;</tt> which handles &#8220;things&#8221; followed by a quantifier. In order to parse the &#8220;things&#8221;, <tt>&quot;regatom()&quot;</tt> is called. This is the lowest level routine, which parses out constant strings, character classes, and the various special symbols like <tt>&quot;$&quot;</tt>. If <tt>&quot;regatom()&quot;</tt> encounters a &#8220;(&#8221; character it in turn calls <tt>&quot;reg()&quot;</tt>. </p>
<p> The routine <tt>&quot;regtail()&quot;</tt> is called by both <tt>&quot;reg()&quot;</tt> and <tt>&quot;regbranch()&quot;</tt> in order to &#8220;set the tail pointer&#8221; correctly. When executing and we get to the end of a branch, we need to go to the node following the grouping parens. When parsing, however, we don&#8217;t know where the end will be until we get there, so when we do we must go back and update the offsets as appropriate. <tt>&quot;regtail&quot;</tt> is used to make this easier. </p>
<p> A subtlety of the parsing process means that a regex like <tt>&quot;/foo/&quot;</tt> is originally parsed into an alternation with a single branch. It is only afterwards that the optimiser converts single branch alternations into the simpler form. </p>
<p> <i>Parse Call Graph and a Grammar</i> </p>
<p> The call graph looks like this: </p>
<pre>
 reg()                        # parse a top level regex, or inside of
                              # parens
     regbranch()              # parse a single branch of an alternation
         regpiece()           # parse a pattern followed by a quantifier
             regatom()        # parse a simple pattern
                 regclass()   #   used to handle a class
                 reg()        #   used to handle a parenthesised
                              #   subpattern
                 ....
         ...
         regtail()            # finish off the branch
     ...
     regtail()                # finish off the branch sequence. Tie each
                              # branch's tail to the tail of the
                              # sequence
                              # (NEW) In Debug mode this is
                              # regtail_study().
</pre>
<p> A grammar form might be something like this: </p>
<pre>
    atom  : constant | class
    quant : '*' | '+' | '?' | '{min,max}'
    _branch: piece
           | piece _branch
           | nothing
    branch: _branch
          | _branch '|' branch
    group : '(' branch ')'
    _piece: atom | group
    piece : _piece
          | _piece quant
</pre>
<p> <i>Parsing complications</i> </p>
<p> The implication of the above description is that a pattern containing nested parentheses will result in a call graph which cycles through <tt>&quot;reg()&quot;</tt>, <tt>&quot;regbranch()&quot;</tt>, <tt>&quot;regpiece()&quot;</tt>, <tt>&quot;regatom()&quot;</tt>, <tt>&quot;reg()&quot;</tt>, <tt>&quot;regbranch()&quot;</tt> <i>etc</i> multiple times, until the deepest level of nesting is reached. All the above routines return a pointer to a <tt>&quot;regnode&quot;</tt>, which is usually the last regnode added to the program. However, one complication is that <code>reg()</code> returns <font SIZE="-1">NULL</font> for parsing <tt>&quot;(?:)&quot;</tt> syntax for embedded modifiers, setting the flag <tt>&quot;TRYAGAIN&quot;</tt>. The <tt>&quot;TRYAGAIN&quot;</tt> propagates upwards until it is captured, in some cases by <tt>&quot;regatom()&quot;</tt>, but otherwise unconditionally by <tt>&quot;regbranch()&quot;</tt>. Hence it will never be returned by <tt>&quot;regbranch()&quot;</tt> to <tt>&quot;reg()&quot;</tt>. This flag permits patterns such as <tt>&quot;(?i)+&quot;</tt> to be detected as errors (<i>Quantifier follows nothing in regex; marked by &lt;&#8211; </i><font SIZE="-1"><i>HERE</i></font><i> in m/(?i)+ &lt;&#8211; </i><font SIZE="-1"><i>HERE /</i></font><i></i>). </p>
<p> Another complication is that the representation used for the program differs if it needs to store Unicode, but it&#8217;s not always possible to know for sure whether it does until midway through parsing. The Unicode representation for the program is larger, and cannot be matched as efficiently. (See &#8220;Unicode and Localisation Support&#8221; below for more details as to why.) If the pattern contains literal Unicode, it&#8217;s obvious that the program needs to store Unicode. Otherwise, the parser optimistically assumes that the more efficient representation can be used, and starts sizing on this basis. However, if it then encounters something in the pattern which must be stored as Unicode, such as an <tt>&quot;
