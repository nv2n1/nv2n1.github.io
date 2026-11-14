---
title: "el_gets(3)"
name: "el_gets"
section: "3"
letter: "e"
url: "/docs/linux/man/3-el_gets/"
description: "editline, el_init, el_end, el_reset, el_gets, el_getc, el_push, el_parse, el_set, el_get, el_source, el_resize, el_line, el_insertstr, el_deletestr, history_init, history_end, history, tok_init, to..."
---

<h2>NAME</h2>
<p> <code>editline</code>, <code>el_init</code>, <code>el_end</code>, <code>el_reset</code>, <code>el_gets</code>, <code>el_getc</code>, <code>el_push</code>, <code>el_parse</code>, <code>el_set</code>, <code>el_get</code>, <code>el_source</code>, <code>el_resize</code>, <code>el_line</code>, <code>el_insertstr</code>, <code>el_deletestr</code>, <code>history_init</code>, <code>history_end</code>, <code>history</code>, <code>tok_init</code>, <code>tok_end</code>, <code>tok_reset</code>, <code>tok_line</code>, <code>tok_str</code> &#8211; line editor, history and tokenization functions</p>
<h2>LIBRARY</h2>
<p> Command Line Editor Library (libedit, -ledit)</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/histedit.h">histedit.h</a>&gt;</code> </p>
<p> <i>EditLine *</i><br />
 <code>el_init</code>(<i>const char *prog</i>, <i>FILE *fin</i>, <i>FILE *fout</i>, <i>FILE *ferr</i>); </p>
<p> <i>void</i><br />
 <code>el_end</code>(<i>EditLine *e</i>); </p>
<p> <i>void</i><br />
 <code>el_reset</code>(<i>EditLine *e</i>); </p>
<p> <i>const char *</i><br />
 <code>el_gets</code>(<i>EditLine *e</i>, <i>int *count</i>); </p>
<p> <i>int</i><br />
 <code>el_getc</code>(<i>EditLine *e</i>, <i>char *ch</i>); </p>
<p> <i>void</i><br />
 <code>el_push</code>(<i>EditLine *e</i>, <i>const char *str</i>); </p>
<p> <i>int</i><br />
 <code>el_parse</code>(<i>EditLine *e</i>, <i>int argc</i>, <i>const char *argv[]</i>); </p>
<p> <i>int</i><br />
 <code>el_set</code>(<i>EditLine *e</i>, <i>int op</i>, <i>&#8230;</i>); </p>
<p> <i>int</i><br />
 <code>el_get</code>(<i>EditLine *e</i>, <i>int op</i>, <i>&#8230;</i>); </p>
<p> <i>int</i><br />
 <code>el_source</code>(<i>EditLine *e</i>, <i>const char *file</i>); </p>
<p> <i>void</i><br />
 <code>el_resize</code>(<i>EditLine *e</i>); </p>
<p> <i>const LineInfo *</i><br />
 <code>el_line</code>(<i>EditLine *e</i>); </p>
<p> <i>int</i><br />
 <code>el_insertstr</code>(<i>EditLine *e</i>, <i>const char *str</i>); </p>
<p> <i>void</i><br />
 <code>el_deletestr</code>(<i>EditLine *e</i>, <i>int count</i>); </p>
<p> <i>History *</i><br />
 <code>history_init</code>(); </p>
<p> <i>void</i><br />
 <code>history_end</code>(<i>History *h</i>); </p>
<p> <i>int</i><br />
 <code>history</code>(<i>History *h</i>, <i>HistEvent *ev</i>, <i>int op</i>, <i>&#8230;</i>); </p>
<p> <i>Tokenizer *</i><br />
 <code>tok_init</code>(<i>const char *IFS</i>); </p>
<p> <i>void</i><br />
 <code>tok_end</code>(<i>Tokenizer *t</i>); </p>
<p> <i>void</i><br />
 <code>tok_reset</code>(<i>Tokenizer *t</i>); </p>
<p> <i>int</i><br />
 <code>tok_line</code>(<i>Tokenizer *t</i>, <i>const LineInfo *li</i>, <i>int *argc</i>, <i>const char **argv[]</i>, <i>int *cursorc</i>, <i>int *cursoro</i>); </p>
<p> <i>int</i><br />
 <code>tok_str</code>(<i>Tokenizer *t</i>, <i>const char *str</i>, <i>int *argc</i>, <i>const char **argv[]</i>);</p>
<h2>DESCRIPTION</h2>
<p> The <code>editline</code> library provides generic line editing, history and tokenization functions, similar to those found in <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1). </p>
<p> These functions are available in the <code>libedit</code> library (which needs the <code>libcurses</code> library). Programs should be linked with <code>-ledit</code> <code>-lcurses</code>.</p>
<h2>LINE EDITING FUNCTIONS</h2>
<p> The line editing functions use a common data structure, <i>EditLine</i>, which is created by <code>el_init</code>() and freed by <code>el_end</code>(). </p>
<p> The following functions are available:</p>
<dl>
<dt><code>el_init</code>()</p>
<dd> Initialise the line editor, and return a data structure to be used by all other line editing functions. <i>prog </i> is the name of the invoking program, used when reading the <code><a href="/docs/linux/man/5-editrc/">editrc</a></code>(5) file to determine which settings to use. <i>fin</i>, <i>fout </i> and <i>ferr </i> are the input, output, and error streams (respectively) to use. In this documentation, references to &#8220;the tty&#8221; are actually to this input/output stream combination.</p>
<dt><code>el_end</code>()</p>
<dd> Clean up and finish with <i>e</i>, assumed to have been created with <code>el_init</code>().</p>
<dt><code>el_reset</code>()</p>
<dd> Reset the tty and the parser. This should be called after an error which may have upset the tty&#8217;s state.</p>
<dt><code>el_gets</code>()</p>
<dd> Read a line from the tty. <i>count </i> is modified to contain the number of characters read. Returns the line read if successful, or NULL if no characters were read or if an error occurred.</p>
<dt><code>el_getc</code>()</p>
<dd> Read a character from the tty. <i>ch </i> is modified to contain the character read. Returns the number of characters read if successful, -1 otherwise.</p>
<dt><code>el_push</code>()</p>
<dd> Pushes <i>str </i> back onto the input stream. This is used by the macro expansion mechanism. Refer to the description of <code>bind</code> <code>-s</code> in <code><a href="/docs/linux/man/5-editrc/">editrc</a></code>(5) for more information.</p>
<dt><code>el_parse</code>()</p>
<dd> Parses the <i>argv </i> array (which is <i>argc </i> elements in size) to execute builtin <code>editline</code> commands. If the command is prefixed with &#8220;prog :&#8221; then <code>el_parse</code>() will only execute the command if &#8220;prog&#8221; matches the <i>prog </i> argument supplied to <code>el_init</code>(). The return value is -1 if the command is unknown, 0 if there was no error or &#8220;prog&#8221; didn&#8217;t match, or 1 if the command returned an error. Refer to <code><a href="/docs/linux/man/5-editrc/">editrc</a></code>(5) for more information.</p>
<dt><code>el_set</code>()</p>
<dd> Set <code>editline</code> parameters. <i>op </i> determines which parameter to set, and each operation has its own parameter list. </p>
<p> The following values for <i>op </i> are supported, along with the required argument list:</p>
<dl>
<dt>
<dd>
<dl>
<dt>EL_PROMPT , <i>char *(*f)(EditLine *)</i></p>
<dd> Define prompt printing function as <i>f</i>, which is to return a string that contains the prompt.</p>
<dt>EL_REFRESH</p>
<dd> Re-display the current line on the next terminal line.</p>
<dt>EL_RPROMPT , <i>char *(*f)(EditLine *)</i></p>
<dd> Define right side prompt printing function as <i>f</i>, which is to return a string that contains the prompt.</p>
<dt>EL_TERMINAL , <i>const char *type</i></p>
<dd> Define terminal type of the tty to be <i>type</i>, or to <i>TERM</i> if <i>type </i> is NULL .</p>
<dt>EL_EDITOR , <i>const char *mode</i></p>
<dd> Set editing mode to <i>mode</i>, which must be one of &#8220;emacs&#8221; or &#8220;vi&#8221;.</p>
<dt>EL_SIGNAL , <i>int flag</i></p>
<dd> If <i>flag </i> is non-zero, <code>editline</code> will install its own signal handler for the following signals when reading command input: SIGCONT , SIGHUP , SIGINT , SIGQUIT , SIGSTOP , SIGTERM , SIGTSTP , and SIGWINCH . Otherwise, the current signal handlers will be used.</p>
<dt>EL_BIND , <i>const char *</i>, <i>&#8230;</i>, NULL</p>
<dd> Perform the <code>bind</code> builtin command. Refer to <code><a href="/docs/linux/man/5-editrc/">editrc</a></code>(5) for more information.</p>
<dt>EL_ECHOTC , <i>const char *</i>, <i>&#8230;</i>, NULL</p>
<dd> Perform the <code>echotc</code> builtin command. Refer to <code><a href="/docs/linux/man/5-editrc/">editrc</a></code>(5) for more information.</p>
<dt>EL_SETTC , <i>const char *</i>, <i>&#8230;</i>, NULL</p>
<dd> Perform the <code>settc</code> builtin command. Refer to <code><a href="/docs/linux/man/5-editrc/">editrc</a></code>(5) for more information.</p>
<dt>EL_SETTY , <i>const char *</i>, <i>&#8230;</i>, NULL</p>
<dd> Perform the <code>setty</code> builtin command. Refer to <code><a href="/docs/linux/man/5-editrc/">editrc</a></code>(5) for more information.</p>
<dt>EL_TELLTC , <i>const char *</i>, <i>&#8230;</i>, NULL</p>
<dd> Perform the <code>telltc</code> builtin command. Refer to <code><a href="/docs/linux/man/5-editrc/">editrc</a></code>(5) for more information.</p>
<dt>EL_ADDFN , <i>const char *name</i>, <i>const char *help</i>, <i>unsigned char (*func)(EditLine *e, int ch)</i></p>
<dd> Add a user defined function, <code>func</code>(), referred to as <i>name </i> which is invoked when a key which is bound to <i>name </i> is entered. <i>help </i> is a description of <i>name</i>. At invocation time, <i>ch </i> is the key which caused the invocation. The return value of <code>func</code>() should be one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt>CC_NORM</p>
<dd> Add a normal character.</p>
<dt>CC_NEWLINE</p>
<dd> End of line was entered.</p>
<dt>CC_EOF</p>
<dd> EOF was entered.</p>
<dt>CC_ARGHACK</p>
<dd> Expecting further command input as arguments, do nothing visually.</p>
<dt>CC_REFRESH</p>
<dd> Refresh display.</p>
<dt>CC_REFRESH_BEEP</p>
<dd> Refresh display, and beep.</p>
<dt>CC_CURSOR</p>
<dd> Cursor moved, so update and perform CC_REFRESH .</p>
<dt>CC_REDISPLAY</p>
<dd> Redisplay entire input line. This is useful if a key binding outputs extra information.</p>
<dt>CC_ERROR</p>
<dd> An error occurred. Beep, and flush tty.</p>
<dt>CC_FATAL</p>
<dd> Fatal error, reset tty to known state.</dl>
</dl>
<dt>EL_HIST , <i>History *(*func)(History *, int op, &#8230;)</i>, <i>const char *ptr</i></p>
<dd> Defines which history function to use, which is usually <code>history</code>(). <i>ptr </i> should be the value returned by <code>history_init</code>().</p>
<dt>EL_EDITMODE , <i>int flag</i></p>
<dd> If <i>flag </i> is non-zero, editing is enabled (the default). Note that this is only an indication, and does not affect the operation of <code>.</code> At this time, it is the caller&#8217;s responsibility to check this (using <code>el_get</code>() ) to determine if editing should be enabled or not.</p>
<dt>EL_GETCFN , <i>int (*f)(EditLine *, char *c)</i></p>
<dd> Define the character reading function as <i>f</i>, which is to return the number of characters read and store them in <i>c</i>. This function is called internally by <code>el_gets</code>() and <code>el_getc</code>(). The builtin function can be set or restored with the special function name &#8220;EL_BUILTIN_GETCFN&#8221;.</p>
<dt>EL_CLIENTDATA , <i>void *data</i></p>
<dd> Register <i>data </i> to be associated with this EditLine structure. It can be retrieved with the corresponding <code>el_get</code>() call.</p>
<dt>EL_SETFP , <i>int fd, Fa FILE *fp</i></p>
<dd> Set the current <code>editline</code> file pointer for &#8220;input&#8221; <i>fd </i> = 0 , &#8220;output&#8221; <i>fd </i> = 1 , or &#8220;error&#8221; <i>fd </i> = 2 from <i>fp</i>.</dl>
</dl>
<dt><code>el_get</code>()</p>
<dd> Get <code>editline</code> parameters. <i>op </i> determines which parameter to retrieve into <i>result</i>. Returns 0 if successful, -1 otherwise. </p>
<p> The following values for <i>op </i> are supported, along with actual type of <i>result : </i></p>
<dl>
<dt>
<dd>
<dl>
<dt>EL_PROMPT , <i>char *(*f)(EditLine *)</i></p>
<dd> Return a pointer to the function that displays the prompt.</p>
<dt>EL_RPROMPT , <i>char *(*f)(EditLine *)</i></p>
<dd> Return a pointer to the function that displays the rightside prompt.</p>
<dt>EL_EDITOR , <i>const char *</i></p>
<dd> Return the name of the editor, which will be one of &#8220;emacs&#8221; or &#8220;vi&#8221;.</p>
<dt>EL_GETTC , <i>const char *name, Fa void *value</i></p>
<dd> Return non-zero if <i>name </i> is a valid <code><a href="/docs/linux/man/5-termcap/">termcap</a></code>(5) capability and set <i>value </i> to the current value of that capability.</p>
<dt>EL_SIGNAL , <i>int *</i></p>
<dd> Return non-zero if <code>editline</code> has installed private signal handlers (see <code>el_get</code>() above).</p>
<dt>EL_EDITMODE , <i>int *</i></p>
<dd> Return non-zero if editing is enabled.</p>
<dt>EL_GETCFN , <i>int (**f)(EditLine *, char *)</i></p>
<dd> Return a pointer to the function that read characters, which is equal to &#8220;EL_BUILTIN_GETCFN&#8221; in the case of the default builtin function.</p>
<dt>EL_CLIENTDATA , <i>void **data</i></p>
<dd> Retrieve <i>data </i> previously registered with the corresponding <code>el_set</code>() call.</p>
<dt>EL_UNBUFFERED , <i>int</i></p>
<dd> Sets or clears unbuffered mode. In this mode, <code>el_gets</code>() will return immediately after processing a single character.</p>
<dt>EL_PREP_TERM , <i>int</i></p>
<dd> Sets or clears terminal editing mode.</p>
<dt>EL_GETFP , <i>int fd&quot;, Fa FILE **fp</i></p>
<dd> Return in <i>fp </i> the current <code>editline</code> file pointer for &#8220;input&#8221; <i>fd </i> = 0 , &#8220;output&#8221; <i>fd </i> = 1 , or &#8220;error&#8221; <i>fd </i> = 2 .</dl>
</dl>
<dt><code>el_source</code>()</p>
<dd> Initialise <code>editline</code> by reading the contents of <i>file</i>. <code>el_parse</code>() is called for each line in <i>file</i>. If <i>file </i> is NULL , try <i>$PWD/.editrc</i> then <i>$HOME/.editrc</i>. Refer to <code><a href="/docs/linux/man/5-editrc/">editrc</a></code>(5) for details on the format of <i>file</i>.</p>
<dt><code>el_resize</code>()</p>
<dd> Must be called if the terminal size changes. If EL_SIGNAL has been set with <code>el_set</code>(), then this is done automatically. Otherwise, it&#8217;s the responsibility of the application to call <code>el_resize</code>() on the appropriate occasions.</p>
<dt><code>el_line</code>()</p>
<dd> Return the editing information for the current line in a <i>LineInfo </i> structure, which is defined as follows: </p>
<p> typedef struct lineinfo { </p>
<p>&nbsp;<wbr>const char&nbsp;<wbr>*buffer;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>address of buffer&nbsp;<wbr>*/ </p>
<p>&nbsp;<wbr>const char&nbsp;<wbr>*cursor;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>address of cursor&nbsp;<wbr>*/ </p>
<p>&nbsp;<wbr>const char&nbsp;<wbr>*lastchar;&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>address of last character&nbsp;<wbr>*/<br />
 } LineInfo; </p>
<p> <i>buffer </i> is not NUL terminated. This function may be called after <code>el_gets</code>() to obtain the <i>LineInfo </i> structure pertaining to line returned by that function, and from within user defined functions added with EL_ADDFN .</p>
<dt><code>el_insertstr</code>()</p>
<dd> Insert <i>str </i> into the line at the cursor. Returns -1 if <i>str </i> is empty or won&#8217;t fit, and 0 otherwise.</p>
<dt><code>el_deletestr</code>()</p>
<dd> Delete <i>count </i> characters before the cursor.</dl>
<h2>HISTORY LIST FUNCTIONS</h2>
<p> The history functions use a common data structure, <i>History</i>, which is created by <code>history_init</code>() and freed by <code>history_end</code>(). </p>
<p> The following functions are available:</p>
<dl>
<dt><code>history_init</code>()</p>
<dd> Initialise the history list, and return a data structure to be used by all other history list functions.</p>
<dt><code>history_end</code>()</p>
<dd> Clean up and finish with <i>h</i>, assumed to have been created with <code>history_init</code>().</p>
<dt><code>history</code>()</p>
<dd> Perform operation <i>op </i> on the history list, with optional arguments as needed by the operation. <i>ev </i> is changed accordingly to operation. The following values for <i>op </i> are supported, along with the required argument list:</p>
<dl>
<dt>
<dd>
<dl>
<dt>H_SETSIZE , <i>int size</i></p>
<dd> Set size of history to <i>size </i> elements.</p>
<dt>H_GETSIZE</p>
<dd> Get number of events currently in history.</p>
<dt>H_END</p>
<dd> Cleans up and finishes with <i>h</i>, assumed to be created with <code>history_init</code>().</p>
<dt>H_CLEAR</p>
<dd> Clear the history.</p>
<dt>H_FUNC , <i>void *ptr</i>, <i>history_gfun_t first</i>, <i>history_gfun_t next</i>, <i>history_gfun_t last</i>, <i>history_gfun_t prev</i>, <i>history_gfun_t curr</i>, <i>history_sfun_t set</i>, <i>history_vfun_t clear</i>, <i>history_efun_t enter</i>, <i>history_efun_t add</i></p>
<dd> Define functions to perform various history operations. <i>ptr </i> is the argument given to a function when it&#8217;s invoked.</p>
<dt>H_FIRST</p>
<dd> Return the first element in the history.</p>
<dt>H_LAST</p>
<dd> Return the last element in the history.</p>
<dt>H_PREV</p>
<dd> Return the previous element in the history.</p>
<dt>H_NEXT</p>
<dd> Return the next element in the history.</p>
<dt>H_CURR</p>
<dd> Return the current element in the history.</p>
<dt>H_SET</p>
<dd> Set the cursor to point to the requested element.</p>
<dt>H_ADD , <i>const char *str</i></p>
<dd> Append <i>str </i> to the current element of the history, or perform the H_ENTER operation with argument <i>str </i> if there is no current element.</p>
<dt>H_APPEND , <i>const char *str</i></p>
<dd> Append <i>str </i> to the last new element of the history.</p>
<dt>H_ENTER , <i>const char *str</i></p>
<dd> Add <i>str </i> as a new element to the history, and, if necessary, removing the oldest entry to keep the list to the created size. If H_SETUNIQUE was has been called with a non-zero arguments, the element will not be entered into the history if its contents match the ones of the current history element. If the element is entered <code>history</code>() returns 1, if it is ignored as a duplicate returns 0. Finally <code>history</code>() returns -1 if an error occurred.</p>
<dt>H_PREV_STR , <i>const char *str</i></p>
<dd> Return the closest previous event that starts with <i>str</i>.</p>
<dt>H_NEXT_STR , <i>const char *str</i></p>
<dd> Return the closest next event that starts with <i>str</i>.</p>
<dt>H_PREV_EVENT , <i>int e</i></p>
<dd> Return the previous event numbered <i>e</i>.</p>
<dt>H_NEXT_EVENT , <i>int e</i></p>
<dd> Return the next event numbered <i>e</i>.</p>
<dt>H_LOAD , <i>const char *file</i></p>
<dd> Load the history list stored in <i>file</i>.</p>
<dt>H_SAVE , <i>const char *file</i></p>
<dd> Save the history list to <i>file</i>.</p>
<dt>H_SETUNIQUE , <i>int unique</i></p>
<dd> Set flag that adjacent identical event strings should not be entered into the history.</p>
<dt>H_GETUNIQUE</p>
<dd> Retrieve the current setting if adjacent identical elements should be entered into the history.</p>
<dt>H_DEL , <i>int e</i></p>
<dd> Delete the event numbered <i>e</i>. This function is only provided for <code><a href="/docs/linux/man/3-readline/">readline</a></code>(3) compatibility. The caller is responsible for free&#8217;ing the string in the returned <i>HistEvent</i>.</dl>
</dl>
<p> <code>history</code>() returns Gt]= 0 if the operation <i>op </i> succeeds. Otherwise, -1 is returned and <i>ev </i> is updated to contain more details about the error.</dl>
<h2>TOKENIZATION FUNCTIONS</h2>
<p> The tokenization functions use a common data structure, <i>Tokenizer</i>, which is created by <code>tok_init</code>() and freed by <code>tok_end</code>(). </p>
<p> The following functions are available:</p>
<dl>
<dt><code>tok_init</code>()</p>
<dd> Initialise the tokenizer, and return a data structure to be used by all other tokenizer functions. <i>IFS </i> contains the Input Field Separators, which defaults to &lt;space&gt; , &lt;tab&gt; , and &lt;newline&gt; if NULL .</p>
<dt><code>tok_end</code>()</p>
<dd> Clean up and finish with <i>t</i>, assumed to have been created with <code>tok_init</code>().</p>
<dt><code>tok_reset</code>()</p>
<dd> Reset the tokenizer state. Use after a line has been successfully tokenized by <code>tok_line</code>() or <code>tok_str</code>() and before a new line is to be tokenized.</p>
<dt><code>tok_line</code>()</p>
<dd> Tokenize <i>li</i>, If successful, modify: <i>argv </i> to contain the words, <i>argc </i> to contain the number of words, <i>cursorc </i> (if not NULL ) to contain the index of the word containing the cursor, and <i>cursoro </i> (if not NULL ) to contain the offset within <i>argv[cursorc] </i> of the cursor. </p>
<p> Returns 0 if successful, -1 for an internal error, 1 for an unmatched single quote, 2 for an unmatched double quote, and 3 for a backslash quoted &lt;newline .&gt; A positive exit code indicates that another line should be read and tokenization attempted again.</p>
<dt><code>tok_str</code>()</p>
<dd> A simpler form of <code>tok_line</code>(; ) <i>str </i> is a NUL terminated string to tokenize.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/3-signal/">signal</a></code>(3), <code><a href="/docs/linux/man/3-termcap/">termcap</a></code>(3), <code><a href="/docs/linux/man/5-editrc/">editrc</a></code>(5), <code><a href="/docs/linux/man/5-termcap/">termcap</a></code>(5)</p>
<h2>HISTORY</h2>
<p> The <code>editline</code> library first appeared in Bx 4.4 . CC_REDISPLAY appeared in Nx 1.3 . CC_REFRESH_BEEP , EL_EDITMODE and the readline emulation appeared in Nx 1.4 . EL_RPROMPT appeared in Nx 1.5 .</p>
<h2>AUTHORS</h2>
<p> The <code>editline</code> library was written by Christos Zoulas. Luke Mewburn wrote this manual and implemented CC_REDISPLAY , CC_REFRESH_BEEP , EL_EDITMODE , and EL_RPROMPT . Jaromir Dolecek implemented the readline emulation.</p>
<h2>BUGS</h2>
<p> At this time, it is the responsibility of the caller to check the result of the EL_EDITMODE operation of <code>el_get</code>() (after an <code>el_source</code>() or <code>el_parse</code>() ) to determine if <code>editline</code> should be used for further input. I.e., EL_EDITMODE is purely an indication of the result of the most recent <code><a href="/docs/linux/man/5-editrc/">editrc</a></code>(5) <code>edit</code> command. </p>
<h2>Index</h2>
