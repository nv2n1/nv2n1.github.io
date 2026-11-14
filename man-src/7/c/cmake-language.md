---
title: "cmake-language(7)"
name: "cmake-language"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-language/"
description: "cmake-language – CMake Language Reference"
---

<p>cmake-language &#8211; CMake Language Reference</p>
<h2>Organization</h2>
<p>CMake input files are written in the &quot;CMake Language&quot; in source files named <code>CMakeLists.txt</code> or ending in a <code>.cmake</code> file name extension. </p>
<p> CMake Language source files in a project are organized into:</p>
<dl>
<dt>&bull;</p>
<dd><i>Directories</i> (<code>CMakeLists.txt</code>),</p>
<dt>&bull;</p>
<dd><i>Scripts</i> (<code>&lt;script&gt;.cmake</code>), and</p>
<dt>&bull;</p>
<dd><i>Modules</i> (<code>&lt;module&gt;.cmake</code>).</dl>
<h3>Directories</h3>
<p>When CMake processes a project source tree, the entry point is a source file called <code>CMakeLists.txt</code> in the top-level source directory. This file may contain the entire build specification or use the <code>add_subdirectory()</code> command to add subdirectories to the build. Each subdirectory added by the command must also contain a <code>CMakeLists.txt</code> file as the entry point to that directory. For each source directory whose <code>CMakeLists.txt</code> file is processed CMake generates a corresponding directory in the build tree to act as the default working and output directory.</p>
<h3>Scripts</h3>
<p>An individual <code>&lt;script&gt;.cmake</code> source file may be processed in <i>script mode</i> by using the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> command-line tool with the <code>-P</code> option. Script mode simply runs the commands in the given CMake Language source file and does not generate a build system. It does not allow CMake commands that define build targets or actions.</p>
<h3>Modules</h3>
<p>CMake Language code in either <i>Directories</i> or <i>Scripts</i> may use the <code>include()</code> command to load a <code>&lt;module&gt;.cmake</code> source file in the scope of the including context. See the <code><a href="/docs/linux/man/7-cmake-modules/">cmake-modules</a>(7)</code> manual page for documentation of modules included with the CMake distribution. Project source trees may also provide their own modules and specify their location(s) in the <code>CMAKE_MODULE_PATH</code> variable.</p>
<h2>Syntax</h2>
<h3>Encoding</h3>
<p>A CMake Language source file may be written in 7-bit ASCII text for maximum portability across all supported platforms. Newlines may be encoded as either <code>
</code> or <code>
</code> but will be converted to <code>
</code> as input files are read. </p>
<p> Note that the implementation is 8-bit clean so source files may be encoded as UTF-8 on platforms with system APIs supporting this encoding. In addition, CMake 3.2 and above support source files encoded in UTF-8 on Windows (using UTF-16 to call system APIs). Furthermore, CMake 3.0 and above allow a leading UTF-8 <i>Byte-Order Mark</i> in source files.</p>
<h3>Source Files</h3>
<p>A CMake Language source file consists of zero or more <i>Command Invocations</i> separated by newlines and optionally spaces and <i>Comments</i>: </p>
<pre><code>file </code> ::= <i>file_element</i>*
<code>file_element</code> ::= <i>command_invocation</i> <i>line_ending</i> |
 (<i>bracket_comment</i>|<i>space</i>)* <i>line_ending</i>
<code>line_ending </code> ::= <i>line_comment</i>? <i>newline</i>
<code>space </code> ::= &lt;match '[ 	]+'&gt;
<code>newline </code> ::= &lt;match '
'&gt;</pre>
<p>Note that any source file line not inside <i>Command Arguments</i> or a <i>Bracket Comment</i> can end in a <i>Line Comment</i>.</p>
<h3>Command Invocations</h3>
<p>A <i>command invocation</i> is a name followed by paren-enclosed arguments separated by whitespace: </p>
<pre><code>command_invocation </code> ::= <i>space</i>* <i>identifier</i> <i>space</i>* '(' <i>arguments</i> ')'
<code>identifier </code> ::= &lt;match '[A-Za-z_][A-Za-z0-9_]*'&gt;
<code>arguments </code> ::= <i>argument</i>? <i>separated_arguments</i>*
<code>separated_arguments</code> ::= <i>separation</i>+ <i>argument</i>? |
 <i>separation</i>* '(' <i>arguments</i> ')'
<code>separation </code> ::= <i>space</i> | <i>line_ending</i></pre>
<p>For example: </p>
<pre>add_executable(hello world.c)</pre>
<p>Command names are case-insensitive. Nested unquoted parentheses in the arguments must balance. Each <code>(</code> or <code>)</code> is given to the command invocation as a literal <i>Unquoted Argument</i>. This may be used in calls to the <code>if()</code> command to enclose conditions. For example: </p>
<pre>if(FALSE AND (FALSE OR TRUE)) # evaluates to FALSE</pre>
<p><code>NOTE:</code> CMake versions prior to 3.0 require command name identifiers to be at least 2 characters. </p>
<p> CMake versions prior to 2.8.12 silently accept an <i>Unquoted Argument</i> or a <i>Quoted Argument</i> immediately following a <i>Quoted Argument</i> and not separated by any whitespace. For compatibility, CMake 2.8.12 and higher accept such code but produce a warning.</p>
<h3>Command Arguments</h3>
<p>There are three types of arguments within <i>Command Invocations</i>: </p>
<pre><code>argument</code> ::= <i>bracket_argument</i> | <i>quoted_argument</i> | <i>unquoted_argument</i></pre>
<h3>Bracket Argument</h3>
<p>A <i>bracket argument</i>, inspired by <i>Lua</i> long bracket syntax, encloses content between opening and closing &quot;brackets&quot; of the same length: </p>
<pre><code>bracket_argument</code> ::= <i>bracket_open</i> <i>bracket_content</i> <i>bracket_close</i>
<code>bracket_open </code> ::= '[' '='* '['
<code>bracket_content </code> ::= &lt;any text not containing a <i>bracket_close</i> with
 the same number of '=' as the <i>bracket_open</i>&gt;
<code>bracket_close </code> ::= ']' '='* ']'</pre>
<p>An opening bracket is written <code>[</code> followed by zero or more <code>=</code> followed by <code>[</code>. The corresponding closing bracket is written <code>]</code> followed by the same number of <code>=</code> followed by <code>]</code>. Brackets do not nest. A unique length may always be chosen for the opening and closing brackets to contain closing brackets of other lengths. </p>
<p> Bracket argument content consists of all text between the opening and closing brackets, except that one newline immediately following the opening bracket, if any, is ignored. No evaluation of the enclosed content, such as <i>Escape Sequences</i> or <i>Variable References</i>, is performed. A bracket argument is always given to the command invocation as exactly one argument. </p>
<p> For example: </p>
<pre>message([=[
This is the first line in a bracket argument with bracket length 1.
No \-escape sequences or ${variable} references are evaluated.
This is always one argument even though it contains a ; character.
The text does not end on a closing bracket of length 0 like ]].
It does end in a closing bracket of length 1.
]=])</pre>
<p><code>NOTE:</code> CMake versions prior to 3.0 do not support bracket arguments. They interpret the opening bracket as the start of an <i>Unquoted Argument</i>.</p>
<h3>Quoted Argument</h3>
<p>A <i>quoted argument</i> encloses content between opening and closing double-quote characters: </p>
<pre><code>quoted_argument </code> ::= '&quot;' <i>quoted_element</i>* '&quot;'
<code>quoted_element </code> ::= &lt;any character except '\' or '&quot;'&gt; |
 <i>escape_sequence</i> |
 <i>quoted_continuation</i>
<code>quoted_continuation</code> ::= '\' <i>newline</i></pre>
<p>Quoted argument content consists of all text between opening and closing quotes. Both <i>Escape Sequences</i> and <i>Variable References</i> are evaluated. A quoted argument is always given to the command invocation as exactly one argument. </p>
<p> For example: </p>
<pre>message(&quot;This is a quoted argument containing multiple lines.
This is always one argument even though it contains a ; character.
Both \-escape sequences and ${variable} references are evaluated.
The text does not end on an escaped double-quote like \&quot;.
It does end in an unescaped double quote.
&quot;)</pre>
<p>The final <code>\</code> on any line ending in an odd number of backslashes is treated as a line continuation and ignored along with the immediately following newline character. For example: </p>
<pre>message(&quot;\
This is the first line of a quoted argument. \
In fact it is the only line but since it is long \
the source code uses line continuation.\
&quot;)</pre>
<p><code>NOTE:</code> CMake versions prior to 3.0 do not support continuation with <code>\</code>. They report errors in quoted arguments containing lines ending in an odd number of <code>\</code> characters.</p>
<h3>Unquoted Argument</h3>
<p>An <i>unquoted argument</i> is not enclosed by any quoting syntax. It may not contain any whitespace, <code>(</code>, <code>)</code>, <code>#</code>, <code>&quot;</code>, or <code>\</code> except when escaped by a backslash: </p>
<pre><code>unquoted_argument</code> ::= <i>unquoted_element</i>+ | <i>unquoted_legacy</i>
<code>unquoted_element </code> ::= &lt;any character except whitespace or one of '()#&quot;\'&gt; |
 <i>escape_sequence</i>
<code>unquoted_legacy </code> ::= &lt;see note in text&gt;</pre>
<p>Unquoted argument content consists of all text in a contiguous block of allowed or escaped characters. Both <i>Escape Sequences</i> and <i>Variable References</i> are evaluated. The resulting value is divided in the same way <i>Lists</i> divide into elements. Each non-empty element is given to the command invocation as an argument. Therefore an unquoted argument may be given to a command invocation as zero or more arguments. </p>
<p> For example: </p>
<pre>foreach(arg
 NoSpace
 Escaped\ Space
 This;Divides;Into;Five;Arguments
 Escaped\;Semicolon
 )
 message(&quot;${arg}&quot;)
endforeach()</pre>
<p><code>NOTE:</code> To support legacy CMake code, unquoted arguments may also contain double-quoted strings (<code>&quot;&#8230;&quot;</code>, possibly enclosing horizontal whitespace), and make-style variable references (<code>$(MAKEVAR)</code>). </p>
<p> Unescaped double-quotes must balance, may not appear at the beginning of an unquoted argument, and are treated as part of the content. For example, the unquoted arguments <code>-Da=&quot;b c&quot;</code>, <code>-Da=$(v)</code>, and <code>a&quot; &quot;b&quot;c&quot;d</code> are each interpreted literally. They may instead be written as quoted arguments <code>&quot;-Da=\&quot;b c\&quot;&quot;</code>, <code>&quot;-Da=$(v)&quot;</code>, and <code>&quot;a\&quot; \&quot;b\&quot;c\&quot;d&quot;</code>, respectively. </p>
<p> Make-style references are treated literally as part of the content and do not undergo variable expansion. They are treated as part of a single argument (rather than as separate <code>$</code>, <code>(</code>, <code>MAKEVAR</code>, and <code>)</code> arguments). </p>
<p> The above &quot;unquoted_legacy&quot; production represents such arguments. We do not recommend using legacy unquoted arguments in new code. Instead use a <i>Quoted Argument</i> or a <i>Bracket Argument</i> to represent the content.</p>
<h3>Escape Sequences</h3>
<p>An <i>escape sequence</i> is a <code>\</code> followed by one character: </p>
<pre><code>escape_sequence </code> ::= <i>escape_identity</i> | <i>escape_encoded</i> | <i>escape_semicolon</i>
<code>escape_identity </code> ::= '\' &lt;match '[^A-Za-z0-9;]'&gt;
<code>escape_encoded </code> ::= '	' | '' | '
'
<code>escape_semicolon</code> ::= '\;'</pre>
<p>A <code>\</code> followed by a non-alphanumeric character simply encodes the literal character without interpreting it as syntax. A <code>	</code>, <code></code>, or <code>
</code> encodes a tab, carriage return, or newline character, respectively. A <code>\;</code> outside of any <i>Variable References</i> encodes itself but may be used in an <i>Unquoted Argument</i> to encode the <code>;</code> without dividing the argument value on it. A <code>\;</code> inside <i>Variable References</i> encodes the literal <code>;</code> character. (See also policy <code>CMP0053</code> documentation for historical considerations.)</p>
<h3>Variable References</h3>
<p>A <i>variable reference</i> has the form <code>${&lt;variable&gt;}</code> and is evaluated inside a <i>Quoted Argument</i> or an <i>Unquoted Argument</i>. A variable reference is replaced by the value of the variable, or by the empty string if the variable is not set. Variable references can nest and are evaluated from the inside out, e.g. <code>${outer_${inner_variable}_variable}</code>. </p>
<p> Literal variable references may consist of alphanumeric characters, the characters <code>/_.+-</code>, and <i>Escape Sequences</i>. Nested references may be used to evaluate variables of any name. See also policy <code>CMP0053</code> documentation for historical considerations and reasons why the <code>$</code> is also technically permitted but is discouraged. </p>
<p> The <i>Variables</i> section documents the scope of variable names and how their values are set. </p>
<p> An <i>environment variable reference</i> has the form <code>$ENV{&lt;variable&gt;}</code>. See the <i>Environment Variables</i> section for more information. </p>
<p> A <i>cache variable reference</i> has the form <code>$CACHE{&lt;variable&gt;}</code>. See <code>CACHE</code> for more information. </p>
<p> The <code>if()</code> command has a special condition syntax that allows for variable references in the short form <code>&lt;variable&gt;</code> instead of <code>${&lt;variable&gt;}</code>. However, environment and cache variables always need to be referenced as <code>$ENV{&lt;variable&gt;}</code> or <code>$CACHE{&lt;variable&gt;}</code>.</p>
<h3>Comments</h3>
<p>A comment starts with a <code>#</code> character that is not inside a <i>Bracket Argument</i>, <i>Quoted Argument</i>, or escaped with <code>\</code> as part of an <i>Unquoted Argument</i>. There are two types of comments: a <i>Bracket Comment</i> and a <i>Line Comment</i>.</p>
<h3>Bracket Comment</h3>
<p>A <code>#</code> immediately followed by a <i>bracket_open</i> forms a <i>bracket comment</i> consisting of the entire bracket enclosure: </p>
<pre><code>bracket_comment</code> ::= '#' <i>bracket_argument</i></pre>
<p>For example: </p>
<pre>#[[This is a bracket comment.
It runs until the close bracket.]]
message(&quot;First Argument
&quot; #[[Bracket Comment]] &quot;Second Argument&quot;)</pre>
<p><code>NOTE:</code> CMake versions prior to 3.0 do not support bracket comments. They interpret the opening <code>#</code> as the start of a <i>Line Comment</i>.</p>
<h3>Line Comment</h3>
<p>A <code>#</code> not immediately followed by a <i>bracket_open</i> forms a <i>line comment</i> that runs until the end of the line: </p>
<pre><code>line_comment</code> ::= '#' &lt;any text not starting in a <i>bracket_open</i>
 and not containing a <i>newline</i>&gt;</pre>
<p>For example: </p>
<pre># This is a line comment.
message(&quot;First Argument
&quot; # This is a line comment :)
 &quot;Second Argument&quot;) # This is a line comment.</pre>
<h2>Control Structures</h2>
<h3>Conditional Blocks</h3>
<p>The <code>if()</code>/<code>elseif()</code>/<code>else()</code>/<code>endif()</code> commands delimit code blocks to be executed conditionally.</p>
<h3>Loops</h3>
<p>The <code>foreach()</code>/<code>endforeach()</code> and <code>while()</code>/<code>endwhile()</code> commands delimit code blocks to be executed in a loop. Inside such blocks the <code>break()</code> command may be used to terminate the loop early whereas the <code>continue()</code> command may be used to start with the next iteration immediately.</p>
<h3>Command Definitions</h3>
<p>The <code>macro()</code>/<code>endmacro()</code>, and <code>function()</code>/<code>endfunction()</code> commands delimit code blocks to be recorded for later invocation as commands.</p>
<h2>Variables</h2>
<p>Variables are the basic unit of storage in the CMake Language. Their values are always of string type, though some commands may interpret the strings as values of other types. The <code>set()</code> and <code>unset()</code> commands explicitly set or unset a variable, but other commands have semantics that modify variables as well. Variable names are case-sensitive and may consist of almost any text, but we recommend sticking to names consisting only of alphanumeric characters plus <code>_</code> and <code>&#8211;</code>. </p>
<p> Variables have dynamic scope. Each variable &quot;set&quot; or &quot;unset&quot; creates a binding in the current scope:</p>
<dl>
<dt><code>Function Scope</code></p>
<dd><i>Command Definitions</i> created by the <code>function()</code> command create commands that, when invoked, process the recorded commands in a new variable binding scope. A variable &quot;set&quot; or &quot;unset&quot; binds in this scope and is visible for the current function and any nested calls within it, but not after the function returns.</p>
<dt><code>Directory Scope</code></p>
<dd>Each of the <i>Directories</i> in a source tree has its own variable bindings. Before processing the <code>CMakeLists.txt</code> file for a directory, CMake copies all variable bindings currently defined in the parent directory, if any, to initialize the new directory scope. CMake <i>Scripts</i>, when processed with <code>cmake -P</code>, bind variables in one &quot;directory&quot; scope. </p>
<p> A variable &quot;set&quot; or &quot;unset&quot; not inside a function call binds to the current directory scope.</p>
<dt><code>Persistent Cache</code></p>
<dd>CMake stores a separate set of &quot;cache&quot; variables, or &quot;cache entries&quot;, whose values persist across multiple runs within a project build tree. Cache entries have an isolated binding scope modified only by explicit request, such as by the <code>CACHE</code> option of the <code>set()</code> and <code>unset()</code> commands. </p>
<p> When evaluating <i>Variable References</i>, CMake first searches the function call stack, if any, for a binding and then falls back to the binding in the current directory scope, if any. If a &quot;set&quot; binding is found, its value is used. If an &quot;unset&quot; binding is found, or no binding is found, CMake then searches for a cache entry. If a cache entry is found, its value is used. Otherwise, the variable reference evaluates to an empty string. The <code>$CACHE{VAR}</code> syntax can be used to do direct cache entry lookups. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-variables/">cmake-variables</a>(7)</code> manual documents the many variables that are provided by CMake or have meaning to CMake when set by project code. </p>
<p> <code>NOTE:</code> CMake reserves identifiers that:</p>
<dt>&bull;</p>
<dd>begin with <code>CMAKE_</code> (upper-, lower-, or mixed-case), or</p>
<dt>&bull;</p>
<dd>begin with <code>_CMAKE_</code> (upper-, lower-, or mixed-case), or</p>
<dt>&bull;</p>
<dd>begin with <code>_</code> followed by the name of any <code>CMake Command</code>.</dl>
<h2>Environment Variables</h2>
<p>Environment Variables are like ordinary <i>Variables</i>, with the following differences:</p>
<dl>
<dt><code>Scope</code></p>
<dd>Environment variables have global scope in a CMake process. They are never cached.</p>
<dt><code>References</code></p>
<dd><i>Variable References</i> have the form <code>$ENV{&lt;variable&gt;}</code>.</p>
<dt><code>Initialization</code></p>
<dd>Initial values of the CMake environment variables are those of the calling process. Values can be changed using the <code>set()</code> and <code>unset()</code> commands. These commands only affect the running CMake process, not the system environment at large. Changed values are not written back to the calling process, and they are not seen by subsequent build or test processes. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-env-variables/">cmake-env-variables</a>(7)</code> manual documents environment variables that have special meaning to CMake.</dl>
<h2>Lists</h2>
<p>Although all values in CMake are stored as strings, a string may be treated as a list in certain contexts, such as during evaluation of an <i>Unquoted Argument</i>. In such contexts, a string is divided into list elements by splitting on <code>;</code> characters not following an unequal number of <code>[</code> and <code>]</code> characters and not immediately preceded by a <code>\</code>. The sequence <code>\;</code> does not divide a value but is replaced by <code>;</code> in the resulting element. </p>
<p> A list of elements is represented as a string by concatenating the elements separated by <code>;</code>. For example, the <code>set()</code> command stores multiple values into the destination variable as a list: </p>
<pre>set(srcs a.c b.c c.c) # sets &quot;srcs&quot; to &quot;a.c;b.c;c.c&quot;</pre>
<p>Lists are meant for simple use cases such as a list of source files and should not be used for complex data processing tasks. Most commands that construct lists do not escape <code>;</code> characters in list elements, thus flattening nested lists: </p>
<pre>set(x a &quot;b;c&quot;) # sets &quot;x&quot; to &quot;a;b;c&quot;, not &quot;a;b\;c&quot;</pre>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
