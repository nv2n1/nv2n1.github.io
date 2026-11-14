---
title: "ragel(1)"
name: "ragel"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ragel/"
description: "ragel – compile regular languages into executable state machines"
---

<h2>NAME</h2>
<p> ragel &#8211; compile regular languages into executable state machines</p>
<h2>SYNOPSIS</h2>
<p> <code>ragel </code> [<i>options</i>] <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> Ragel compiles executable finite state machines from regular languages. Ragel can generate C, C++, Objective-C, D, Go, or Java code. Ragel state machines can not only recognize byte sequences as regular expression machines do, but can also execute code at arbitrary points in the recognition of a regular language. User code is embedded using inline operators that do not disrupt the regular language syntax. </p>
<p> The core language consists of standard regular expression operators, such as union, concatenation and kleene star, accompanied by action embedding operators. Ragel also provides operators that let you control any non-determinism that you create, construct scanners using the longest match paradigm, and build state machines using the statechart model. It is also possible to influence the execution of a state machine from inside an embedded action by jumping or calling to other parts of the machine and reprocessing input. </p>
<p> Ragel provides a very flexibile interface to the host language that attempts to place minimal restrictions on how the generated code is used and integrated into the application. The generated code has no dependencies. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-H</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Display help and exit.</p>
<dt><code>-v</code></p>
<dd> Print version information and exit.</p>
<dt><code>-o file</code></p>
<dd> Write output to file. If -o is not given, a default file name is chosen by replacing the file extenstion of the input file. For source files ending in .rh the suffix .h is used. For all other source files a suffix based on the output language is used (.c, .cpp, .m, etc.). If -o is not given for Graphviz output the generated dot file is written to standard output.</p>
<dt><code>-s</code></p>
<dd> Print some statistics on standard error.</p>
<dt><code>&#8211;error-format=gnu</code></p>
<dd> Print error messages using the format &quot;file:line:column:&quot; (default)</p>
<dt><code>&#8211;error-format=msvc</code></p>
<dd> Print error messages using the format &quot;file(line,column):&quot;</p>
<dt><code>-d</code></p>
<dd> Do not remove duplicate actions from action lists.</p>
<dt><code>-I dir</code></p>
<dd> Add dir to the list of directories to search for included and imported files</p>
<dt><code>-n</code></p>
<dd> Do not perform state minimization.</p>
<dt><code>-m</code></p>
<dd> Perform minimization once, at the end of the state machine compilation.</p>
<dt><code>-l</code></p>
<dd> Minimize after nearly every operation. Lists of like operations such as unions are minimized once at the end. This is the default minimization option.</p>
<dt><code>-e</code></p>
<dd> Minimize after every operation.</p>
<dt><code>-x</code></p>
<dd> Compile the state machines and emit an XML representation of the host data and the machines.</p>
<dt><code>-V</code></p>
<dd> Generate a dot file for Graphviz.</p>
<dt><code>-p</code></p>
<dd> Display printable characters on labels.</p>
<dt><code>-L</code></p>
<dd> Inhibit writing of #line directives.</p>
<dt><code>-S &lt;spec&gt;</code></p>
<dd> FSM specification to output.</p>
<dt><code>-M &lt;machine&gt;</code></p>
<dd> Machine definition/instantiation to output.</p>
<dt><code>-C</code></p>
<dd> The host language is C, C++, Obj-C or Obj-C++. This is the default host language option.</p>
<dt><code>&#8211;asm &#8211;gas-x86-64-sys-v</code></p>
<dd> GNU AS, x86_64, System V ABI ASM is generated in a code style equiv to -G2</p>
<dt><code>-D</code></p>
<dd> The host language is D.</p>
<dt><code>-Z</code></p>
<dd> The host language is Go.</p>
<dt><code>-J</code></p>
<dd> The host language is Java.</p>
<dt><code>-R</code></p>
<dd> The host language is Ruby.</p>
<dt><code>-A</code></p>
<dd> The host language is C#</p>
<dt><code>-O</code></p>
<dd> The host language is OCaml.</p>
<dt><code>-U</code></p>
<dd> The host language is Rust.</p>
<dt><code>-Y</code></p>
<dd> The host language is Julia.</p>
<dt><code>-K</code></p>
<dd> The host language is Crack.</p>
<dt><code>-P</code></p>
<dd> The host language is JavaScript.</p>
<dt><code>-T0</code></p>
<dd> (C/D/Java/Ruby/C#) Generate a table driven FSM. This is the default code style. The table driven FSM represents the state machine as static data. There are tables of states, transitions, indicies and actions. The current state is stored in a variable. The execution is a loop that looks that given the current state and current character to process looks up the transition to take using a binary search, executes any actions and moves to the target state. In general, the table driven FSM produces a smaller binary and requires a less expensive host language compile but results in slower running code. The table driven FSM is suitable for any FSM.</p>
<dt><code>-T1</code></p>
<dd> (C/D/Ruby/C#) Generate a faster table driven FSM by expanding action lists in the action execute code.</p>
<dt><code>-F0</code></p>
<dd> (C/D/Ruby/C#) Generate a flat table driven FSM. Transitions are represented as an array indexed by the current alphabet character. This eliminates the need for a binary search to locate transitions and produces faster code, however it is only suitable for small alphabets.</p>
<dt><code>-F1</code></p>
<dd> (C/D/Ruby/C#) Generate a faster flat table driven FSM by expanding action lists in the action execute code.</p>
<dt><code>-G0</code></p>
<dd> (C/D/C#) Generate a goto driven FSM. The goto driven FSM represents the state machine as a series of goto statements. While in the machine, the current state is stored by the processor&#8217;s instruction pointer. The execution is a flat function where control is passed from state to state using gotos. In general, the goto FSM produces faster code but results in a larger binary and a more expensive host language compile.</p>
<dt><code>-G1</code></p>
<dd> (C/D/C#) Generate a faster goto driven FSM by expanding action lists in the action execute code.</p>
<dt><code>-G2</code></p>
<dd> (C/D/Go) Generate a really fast goto driven FSM by embedding action lists in the state machine control code.</p>
<dt><code>&#8211;nfa-conds-depth=D</code></p>
<dd> Search for high-cost conditions inside a prefix of the machine (depth D from start state). Search is rooted at NFA union contructs.</p>
<dt><code>&#8211;nfa-term-check</code></p>
<dd> Search for condition-based general repetitions that will not function properly and must be NFA reps. Search is rooted at NFA union constructs.</p>
<dt><code>&#8211;nfa-intermed-state-limit=L</code></p>
<dd> Report fail if number of states exceeds this during compilation.</p>
<dt><code>&#8211;nfa-final-state-limit=L</code></p>
<dd> Report a fail if number states in final machine exceeds this.</p>
<dt><code>&#8211;nfa-breadth-check=E1,E2,..</code></p>
<dd> Report breadth cost of named entry points by (and start). Reporting starts at NFA union contructs.</p>
<dt><code>&#8211;input-histogram=FN</code></p>
<dd> Input char histogram for breadth check. If unspecified a flat histogram is used.</dl>
<h2>RAGEL INPUT</h2>
<p> NOTE: This is a very brief description of Ragel input. Ragel is described in more detail in the user guide available from the homepage (see below). </p>
<p> Ragel normally passes input files straight to the output. When it sees an FSM specification that contains machine instantiations it stops to generate the state machine. If there are write statements (such as &quot;write exec&quot;) then ragel emits the corresponding code. There can be any number of FSM specifications in an input file. A multi-line FSM specification starts with &#8216;%%{&#8216; and ends with &#8216;}%%&#8217;. A single line FSM specification starts with %% and ends at the first newline.</p>
<h2>FSM STATEMENTS</h2>
<dl>
<dt><i>Machine Name:</i></p>
<dd> Set the the name of the machine. If given, it must be the first statement.</p>
<dt><i>Alphabet Type:</i></p>
<dd> Set the data type of the alphabet.</p>
<dt><i>GetKey:</i></p>
<dd> Specify how to retrieve the alphabet character from the element type.</p>
<dt><i>Include:</i></p>
<dd> Include a machine of same name as the current or of a different name in either the current file or some other file.</p>
<dt><i>Action Definition:</i></p>
<dd> Define an action that can be invoked by the FSM.</p>
<dt><i>Fsm Definition, Instantiation and Longest Match Instantiation:</i></p>
<dd> Used to build FSMs. Syntax description in next few sections.</p>
<dt><i>Access:</i></p>
<dd> Specify how to access the persistent state machine variables.</p>
<dt><i>Write:</i></p>
<dd> Write some component of the machine.</p>
<dt><i>Variable:</i></p>
<dd> Override the default variable names (p, pe, cs, act, etc).</dl>
<h2>BASIC MACHINES</h2>
<p> The basic machines are the base operands of the regular language expressions.</p>
<dl>
<dt><i>&#8216;hello&#8217;</i></p>
<dd> Concat literal. Produces a concatenation of the characters in the string. Supports escape sequences with &#8216;\&#8217;. The result will have a start state and a transition to a new state for each character in the string. The last state in the sequence will be made final. To make the string case-insensitive, append an &#8216;i&#8217; to the string, as in &#8216;cmd&#8217;i.</p>
<dt><i>&quot;hello&quot;</i></p>
<dd> Identical to single quote version.</p>
<dt><i>[hello]</i></p>
<dd> Or literal. Produces a union of characters. Supports character ranges with &#8216;-&#8216;, negating the sense of the union with an initial &#8216;^&#8217; and escape sequences with &#8216;\&#8217;. The result will have two states with a transition between them for each character or range.</dl>
<p> NOTE: &#8221;, &quot;&quot;, and [] produce null FSMs. Null machines have one state that is both a start state and a final state and match the zero length string. A null machine may be created with the null builtin machine.</p>
<dl>
<dt><i>integer</i></p>
<dd> Makes a two state machine with one transition on the given integer number.</p>
<dt><i>hex</i></p>
<dd> Makes a two state machine with one transition on the given hexidecimal number.</p>
<dt><i>/simple_regex/</i></p>
<dd> A simple regular expression. Supports the notation &#8216;.&#8217;, &#8216;*&#8217; and &#8216;[]&#8217;, character ranges with &#8216;-&#8216;, negating the sense of an OR expression with and initial &#8216;^&#8217; and escape sequences with &#8216;\&#8217;. Also supports one trailing flag: i. Use it to produce a case-insensitive regular expression, as in /GET/i.</p>
<dt><i>lit .. lit</i></p>
<dd> Specifies a range. The allowable upper and lower bounds are concat literals of length one and number machines. For example, 0x10..0x20, 0..63, and &#8216;a&#8217;..&#8217;z&#8217; are valid ranges.</p>
<dt><i>variable_name</i></p>
<dd> References the machine definition assigned to the variable name given.</p>
<dt><i>builtin_machine</i></p>
<dd> There are several builtin machines available. They are all two state machines for the purpose of matching common classes of characters. They are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>any</code></p>
<dd> Any character in the alphabet.</p>
<dt><code>ascii</code></p>
<dd> Ascii characters 0..127.</p>
<dt><code>extend</code></p>
<dd> Ascii extended characters. This is the range -128..127 for signed alphabets and the range 0..255 for unsigned alphabets.</p>
<dt><code>alpha</code></p>
<dd> Alphabetic characters /[A-Za-z]/.</p>
<dt><code>digit</code></p>
<dd> Digits /[0-9]/.</p>
<dt><code>alnum</code></p>
<dd> Alpha numerics /[0-9A-Za-z]/.</p>
<dt><code>lower</code></p>
<dd> Lowercase characters /[a-z]/.</p>
<dt><code>upper</code></p>
<dd> Uppercase characters /[A-Z]/.</p>
<dt><code>xdigit</code></p>
<dd> Hexidecimal digits /[0-9A-Fa-f]/.</p>
<dt><code>cntrl</code></p>
<dd> Control characters 0..31.</p>
<dt><code>graph</code></p>
<dd> Graphical characters /[!-~]/.</p>
<dt><code>print</code></p>
<dd> Printable characters /[ -~]/.</p>
<dt><code>punct</code></p>
<dd> Punctuation. Graphical characters that are not alpha-numerics /[!-/:-@\[-`{-~]/.</p>
<dt><code>space</code></p>
<dd> Whitespace /[	
 ]/.</p>
<dt><code>null</code></p>
<dd> Zero length string. Equivalent to &#8221;, &quot;&quot; and [].</p>
<dt><code>empty</code></p>
<dd> Empty set. Matches nothing.</dl>
</dl>
</dl>
<h2>BRIEF OPERATOR REFERENCE</h2>
<p> Operators are grouped by precedence, group 1 being the lowest and group 6 the highest. </p>
<p> <code>GROUP 1:</code></p>
<dl>
<dt><i>expr , expr</i></p>
<dd> Join machines together without drawing any transitions, setting up a start state or any final states. Start state must be explicitly specified with the &quot;start&quot; label. Final states may be specified with the an epsilon transitions to the implicitly created &quot;final&quot; state.</dl>
<p> <code>GROUP 2:</code></p>
<dl>
<dt><i>expr | expr</i></p>
<dd> Produces a machine that matches any string in machine one or machine two.</p>
<dt><i>expr &amp; expr</i></p>
<dd> Produces a machine that matches any string that is in both machine one and machine two.</p>
<dt><i>expr &#8211; expr</i></p>
<dd> Produces a machine that matches any string that is in machine one but not in machine two.</p>
<dt><i>expr &#8212; expr</i></p>
<dd> Strong Subtraction. Matches any string in machine one that does not have any string in machine two as a substring.</dl>
<p> <code>GROUP 3:</code></p>
<dl>
<dt><i>expr . expr</i></p>
<dd> Produces a machine that matches all the strings in machine one followed by all the strings in machine two.</p>
<dt><i>expr :&gt; expr</i></p>
<dd> Entry-Guarded Concatenation: terminates machine one upon entry to machine two.</p>
<dt><i>expr :&gt;&gt; expr</i></p>
<dd> Finish-Guarded Concatenation: terminates machine one when machine two finishes.</p>
<dt><i>expr &lt;: expr</i></p>
<dd> Left-Guarded Concatenation: gives a higher priority to machine one.</dl>
<p> NOTE: Concatenation is the default operator. Two machines next to each other with no operator between them results in the concatenation operation. </p>
<p> <code>GROUP 4:</code></p>
<dl>
<dt><i>label: expr</i></p>
<dd> Attaches a label to an expression. Labels can be used by epsilon transitions and fgoto and fcall statements in actions. Also note that the referencing of a machine definition causes the implicit creation of label by the same name.</dl>
<p> <code>GROUP 5:</code></p>
<dl>
<dt><i>expr -&gt; label</i></p>
<dd> Draws an epsilon transition to the state defined by label. Label must be a name in the current scope. Epsilon transitions are resolved when comma operators are evaluated and at the root of the expression tree of machine assignment/instantiation.</dl>
<p> <code>GROUP 6: Actions</code> </p>
<p> An action may be a name predefined with an action statement or may be specified directly with &#8216;{&#8216; and &#8216;}&#8217; in the expression.</p>
<dl>
<dt><i>expr &gt; action</i></p>
<dd> Embeds action into starting transitions.</p>
<dt><i>expr @ action</i></p>
<dd> Embeds action into transitions that go into a final state.</p>
<dt><i>expr $ action</i></p>
<dd> Embeds action into all transitions. Does not include pending out transitions.</p>
<dt><i>expr % action</i></p>
<dd> Embeds action into pending out transitions from final states.</dl>
<p> <code>GROUP 6: EOF Actions</code> </p>
<p> When a machine&#8217;s finish routine is called the current state&#8217;s EOF actions are executed.</p>
<dl>
<dt><i>expr &gt;/ action</i></p>
<dd> Embed an EOF action into the start state.</p>
<dt><i>expr &lt;/ action</i></p>
<dd> Embed an EOF action into all states except the start state.</p>
<dt><i>expr $/ action</i></p>
<dd> Embed an EOF action into all states.</p>
<dt><i>expr %/ action</i></p>
<dd> Embed an EOF action into final states.</p>
<dt><i>expr @/ action</i></p>
<dd> Embed an EOF action into all states that are not final.</p>
<dt><i>expr &lt;&gt;/ action</i></p>
<dd> Embed an EOF action into all states that are not the start state and that are not final (middle states).</dl>
<p> <code>GROUP 6: Global Error Actions</code> </p>
<p> Global error actions are stored in states until the final state machine has been fully constructed. They are then transferred to error transitions, giving the effect of a default action.</p>
<dl>
<dt><i>expr &gt;! action</i></p>
<dd> Embed a global error action into the start state.</p>
<dt><i>expr &lt;! action</i></p>
<dd> Embed a global error action into all states except the start state.</p>
<dt><i>expr $! action</i></p>
<dd> Embed a global error action into all states.</p>
<dt><i>expr %! action</i></p>
<dd> Embed a global error action into the final states.</p>
<dt><i>expr @! action</i></p>
<dd> Embed a global error action into all states which are not final.</p>
<dt><i>expr &lt;&gt;! action</i></p>
<dd> Embed a global error action into all states which are not the start state and are not final (middle states).</dl>
<p> <code>GROUP 6: Local Error Actions </code> </p>
<p> Local error actions are stored in states until the named machine is fully constructed. They are then transferred to error transitions, giving the effect of a default action for a section of the total machine. Note that the name may be omitted, in which case the action will be transferred to error actions upon construction of the current machine.</p>
<dl>
<dt><i>expr &gt;^ action</i></p>
<dd> Embed a local error action into the start state.</p>
<dt><i>expr &lt;^ action</i></p>
<dd> Embed a local error action into all states except the start state.</p>
<dt><i>expr $^ action</i></p>
<dd> Embed a local error action into all states.</p>
<dt><i>expr %^ action</i></p>
<dd> Embed a local error action into the final states.</p>
<dt><i>expr @^ action</i></p>
<dd> Embed a local error action into all states which are not final.</p>
<dt><i>expr &lt;&gt;^ action</i></p>
<dd> Embed a local error action into all states which are not the start state and are not final (middle states).</dl>
<p> <code>GROUP 6: To-State Actions</code> </p>
<p> To state actions are stored in states and executed any time the machine moves into a state. This includes regular transitions, and transfers of control such as fgoto. Note that setting the current state from outside the machine (for example during initialization) does not count as a transition into a state.</p>
<dl>
<dt><i>expr &gt;~ action</i></p>
<dd> Embed a to-state action action into the start state.</p>
<dt><i>expr &lt;~ action</i></p>
<dd> Embed a to-state action into all states except the start state.</p>
<dt><i>expr $~ action</i></p>
<dd> Embed a to-state action into all states.</p>
<dt><i>expr %~ action</i></p>
<dd> Embed a to-state action into the final states.</p>
<dt><i>expr @~ action</i></p>
<dd> Embed a to-state action into all states which are not final.</p>
<dt><i>expr &lt;&gt;~ action</i></p>
<dd> Embed a to-state action into all states which are not the start state and are not final (middle states).</dl>
<p> <code>GROUP 6: From-State Actions</code> </p>
<p> From state actions are executed whenever a state takes a transition on a character. This includes the error transition and a transition to self.</p>
<dl>
<dt><i>expr &gt;* action</i></p>
<dd> Embed a from-state action into the start state.</p>
<dt><i>expr &lt;* action</i></p>
<dd> Embed a from-state action into every state except the start state.</p>
<dt><i>expr $* action</i></p>
<dd> Embed a from-state action into all states.</p>
<dt><i>expr %* action</i></p>
<dd> Embed a from-state action into the final states.</p>
<dt><i>expr @* action</i></p>
<dd> Embed a from-state action into all states which are not final.</p>
<dt><i>expr &lt;&gt;* action</i></p>
<dd> Embed a from-state action into all states which are not the start state and are not final (middle states).</dl>
<p> <code>GROUP 6: Priority Assignment</code> </p>
<p> Priorities are assigned to names within transitions. Only priorities on the same name are allowed to interact. In the first form of priorities the name defaults to the name of the machine definition the priority is assigned in. Transitions do not have default priorities.</p>
<dl>
<dt><i>expr &gt; int</i></p>
<dd> Assigns the priority int in all transitions leaving the start state.</p>
<dt><i>expr @ int</i></p>
<dd> Assigns the priority int in all transitions that go into a final state.</p>
<dt><i>expr $ int</i></p>
<dd> Assigns the priority int in all existing transitions.</p>
<dt><i>expr % int</i></p>
<dd> Assigns the priority int in all pending out transitions.</dl>
<p> A second form of priority assignment allows the programmer to specify the name to which the priority is assigned, allowing interactions to cross machine definition boundaries.</p>
<dl>
<dt><i>expr &gt; (name,int)</i></p>
<dd> Assigns the priority int to name in all transitions leaving the start state.</p>
<dt><i>expr @ (name, int)</i></p>
<dd> Assigns the priority int to name in all transitions that go into a final state.</p>
<dt><i>expr $ (name, int)</i></p>
<dd> Assigns the priority int to name in all existing transitions.</p>
<dt><i>expr % (name, int)</i></p>
<dd> Assigns the priority int to name in all pending out transitions.</dl>
<p> <code>GROUP 7:</code></p>
<dl>
<dt><i>expr *</i></p>
<dd> Produces the kleene star of a machine. Matches zero or more repetitions of the machine.</p>
<dt><i>expr **</i></p>
<dd> Longest-Match Kleene Star. This version of kleene star puts a higher priority on staying in the machine over wrapping around and starting over. This operator is equivalent to ( ( expr ) $0 %1 )*.</p>
<dt><i>expr ?</i></p>
<dd> Produces a machine that accepts the machine given or the null string. This operator is equivalent to ( expr | &#8221; ).</p>
<dt><i>expr +</i></p>
<dd> Produces the machine concatenated with the kleen star of itself. Matches one or more repetitions of the machine. This operator is equivalent to ( expr . expr* ).</p>
<dt><i>expr {n}</i></p>
<dd> Produces a machine that matches exactly n repetitions of expr.</p>
<dt><i>expr {,n}</i></p>
<dd> Produces a machine that matches anywhere from zero to n repetitions of expr.</p>
<dt><i>expr {n,}</i></p>
<dd> Produces a machine that matches n or more repetitions of expr.</p>
<dt><i>expr {n,m}</i></p>
<dd> Produces a machine that matches n to m repetitions of expr.</dl>
<p> <code>GROUP 8:</code></p>
<dl>
<dt><i>! expr</i></p>
<dd> Produces a machine that matches any string not matched by the given machine. This operator is equivalent to ( *extend &#8211; expr ).</p>
<dt><i>^ expr</i></p>
<dd> Character-Level Negation. Matches any single character not matched by the single character machine expr.</dl>
<p> <code>GROUP 9:</code></p>
<dl>
<dt><i>( expr )</i></p>
<dd> Forces precedence on operators.</dl>
<h2>VALUES AVAILABLE IN CODE BLOCKS</h2>
<dl>
<dt><i>fc</i></p>
<dd> The current character. Equivalent to *p.</p>
<dt><i>fpc</i></p>
<dd> A pointer to the current character. Equivalent to p.</p>
<dt><i>fcurs</i></p>
<dd> An integer value representing the current state.</p>
<dt><i>ftargs</i></p>
<dd> An integer value representing the target state.</p>
<dt><i>fentry(&lt;label&gt;)</i></p>
<dd> An integer value representing the entry point &lt;label&gt;.</dl>
<h2>STATEMENTS AVAILABLE IN CODE BLOCKS</h2>
<dl>
<dt><i>fhold;</i></p>
<dd> Do not advance over the current character. Equivalent to &#8211;p;.</p>
<dt><i>fexec &lt;expr&gt;;</i></p>
<dd> Sets the current character to something else. Equivalent to p = (&lt;expr&gt;)-1;</p>
<dt><i>fgoto &lt;label&gt;;</i></p>
<dd> Jump to the machine defined by &lt;label&gt;.</p>
<dt><i>fgoto *&lt;expr&gt;;</i></p>
<dd> Jump to the entry point given by &lt;expr&gt;. The expression must evaluate to an integer value representing a state.</p>
<dt><i>fnext &lt;label&gt;;</i></p>
<dd> Set the next state to be the entry point defined by &lt;label&gt;. The fnext statement does not immediately jump to the specified state. Any action code following the statement is executed.</p>
<dt><i>fnext *&lt;expr&gt;;</i></p>
<dd> Set the next state to be the entry point given by &lt;expr&gt;. The expression must evaluate to an integer value representing a state.</p>
<dt><i>fcall &lt;label&gt;;</i></p>
<dd> Call the machine defined by &lt;label&gt;. The next fret will jump to the target of the transition on which the action is invoked.</p>
<dt><i>fcall *&lt;expr&gt;;</i></p>
<dd> Call the entry point given by &lt;expr&gt;. The next fret will jump to the target of the transition on which the action is invoked.</p>
<dt><i>fret;</i></p>
<dd> Return to the target state of the transition on which the last fcall was made.</p>
<dt><i>fbreak;</i></p>
<dd> Save the current state and immediately break out of the machine.</dl>
<h2>CREDITS</h2>
<p> Ragel was written by Adrian Thurston &lt;thurston [at] complang.org&gt;. Objective-C output contributed by Erich Ocean. D output contributed by Alan West. Ruby output contributed by Victor Hugo Borja. C Sharp code generation contributed by Daniel Tang. Contributions to Java code generation by Colin Fleming. Go code generation contributed by Justine Tunney.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-re2c/">re2c</a></code>(1), <code><a href="/docs/linux/man/1-flex/">flex</a></code>(1) </p>
<p> Homepage: <a rel="nofollow" href="http://www.complang.org/ragel/">http://www.complang.org/ragel/</a> </p>
<h2>Index</h2>
