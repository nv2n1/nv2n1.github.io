---
title: "history(3)"
name: "history"
section: "3"
letter: "h"
url: "/docs/linux/man/3-history/"
description: "history – GNU History Library"
---

<h2 class="name">NAME</h2>
<p> history &#8211; GNU History Library </p>
<h2>COPYRIGHT</h2>
<p> The GNU History Library is Copyright (C) 1989-2011 by the Free Software Foundation, Inc.</p>
<h2>DESCRIPTION</h2>
<p> Many programs read input from the user a line at a time. The GNU History library is able to keep track of those lines, associate arbitrary data with each line, and utilize information from previous lines in composing new ones. </p>
<h2>HISTORY EXPANSION</h2>
<p> The history library supports a history expansion feature that is identical to the history expansion in <code>bash.</code> This section describes what syntax features are available. </p>
<p> History expansions introduce words from the history list into the input stream, making it easy to repeat commands, insert the arguments to a previous command into the current input line, or fix errors in previous commands quickly. </p>
<p> History expansion is usually performed immediately after a complete line is read. It takes place in two parts. The first is to determine which line from the history list to use during substitution. The second is to select portions of that line for inclusion into the current one. The line selected from the history is the <i>event</i>, and the portions of that line that are acted upon are <i>words</i>. Various <i>modifiers</i> are available to manipulate the selected words. The line is broken into words in the same fashion as <code>bash</code> does when reading input, so that several words that would otherwise be separated are considered one word when surrounded by quotes (see the description of <code>history_tokenize()</code> below). History expansions are introduced by the appearance of the history expansion character, which is <code>!</code> by default. Only backslash (<code>\</code>) and single quotes can quote the history expansion character.</p>
<h3>Event Designators</h3>
<p> An event designator is a reference to a command line entry in the history list. Unless the reference is absolute, events are relative to the current position in the history list. </p>
<dl>
<dt><code>!</code></p>
<dd> Start a history substitution, except when followed by a <code>blank</code>, newline, = or (.</p>
<dt><code>!</code><i>n</i></p>
<dd> Refer to command line <i>n</i>.</p>
<dt><code>!-</code><i>n</i></p>
<dd> Refer to the current command minus <i>n</i>.</p>
<dt><code>!!</code></p>
<dd> Refer to the previous command. This is a synonym for `!-1&#8242;.</p>
<dt><code>!</code><i>string</i></p>
<dd> Refer to the most recent command preceding the current position in the history list starting with <i>string</i>.</p>
<dt><code>!?</code><i>string</i><code>[?]</code></p>
<dd> Refer to the most recent command preceding the current postition in the history list containing <i>string</i>. The trailing <code>?</code> may be omitted if <i>string</i> is followed immediately by a newline.</p>
<dt><font SIZE="+2"><code>^</code></font><i>string1</i><font SIZE="+2">^</font><i>string2</i><font SIZE="+2">^</font></p>
<dd> Quick substitution. Repeat the last command, replacing <i>string1</i> with <i>string2</i>. Equivalent to &#8220;!!:s/<i>string1</i>/<i>string2</i>/&#8221; (see <code>Modifiers</code> below).</p>
<dt><code>!#</code></p>
<dd> The entire command line typed so far.</dl>
<h3>Word Designators</h3>
<p> Word designators are used to select desired words from the event. A <code>:</code> separates the event specification from the word designator. It may be omitted if the word designator begins with a <code>^</code>, <code>$</code>, <code>*</code>, <code>&#8211;</code>, or <code>%</code>. Words are numbered from the beginning of the line, with the first word being denoted by 0 (zero). Words are inserted into the current line separated by single spaces. </p>
<dl>
<dt><code>0 (zero)</code></p>
<dd> The zeroth word. For the shell, this is the command word.</p>
<dt><i>n</i></p>
<dd> The <i>n</i>th word.</p>
<dt><code>^</code></p>
<dd> The first argument. That is, word 1.</p>
<dt><code>$</code></p>
<dd> The last argument.</p>
<dt><code>%</code></p>
<dd> The word matched by the most recent `?<i>string</i>?&#8217; search.</p>
<dt><i>x</i><code>&#8211;</code>y</p>
<dd> A range of words; `-<i>y</i>&#8216; abbreviates `0-<i>y</i>&#8216;.</p>
<dt><code>*</code></p>
<dd> All of the words but the zeroth. This is a synonym for `<i>1-$</i>&#8216;. It is not an error to use <code>*</code> if there is just one word in the event; the empty string is returned in that case.</p>
<dt><code>x*</code></p>
<dd> Abbreviates <i>x-$</i>.</p>
<dt><code>x-</code></p>
<dd> Abbreviates <i>x-$</i> like <code>x*</code>, but omits the last word.</dl>
<p> If a word designator is supplied without an event specification, the previous command is used as the event.</p>
<h3>Modifiers</h3>
<p> After the optional word designator, there may appear a sequence of one or more of the following modifiers, each preceded by a `:&#8217;. </p>
<dl>
<dt><code>h</code></p>
<dd> Remove a trailing file name component, leaving only the head.</p>
<dt><code>t</code></p>
<dd> Remove all leading file name components, leaving the tail.</p>
<dt><code>r</code></p>
<dd> Remove a trailing suffix of the form <i>.xxx</i>, leaving the basename.</p>
<dt><code>e</code></p>
<dd> Remove all but the trailing suffix.</p>
<dt><code>p</code></p>
<dd> Print the new command but do not execute it.</p>
<dt><code>q</code></p>
<dd> Quote the substituted words, escaping further substitutions.</p>
<dt><code>x</code></p>
<dd> Quote the substituted words as with <code>q</code>, but break into words at <code>blanks</code> and newlines.</p>
<dt><code>s/</code><i>old</i>/<i>new</i>/</p>
<dd> Substitute <i>new</i> for the first occurrence of <i>old</i> in the event line. Any delimiter can be used in place of /. The final delimiter is optional if it is the last character of the event line. The delimiter may be quoted in <i>old</i> and <i>new</i> with a single backslash. If &amp; appears in <i>new</i>, it is replaced by <i>old</i>. A single backslash will quote the &amp;. If <i>old</i> is null, it is set to the last <i>old</i> substituted, or, if no previous history substitutions took place, the last <i>string</i> in a <code>!?</code><i>string</i><code>[?]</code> search.</p>
<dt><code>&amp;</code></p>
<dd> Repeat the previous substitution.</p>
<dt><code>g</code></p>
<dd> Cause changes to be applied over the entire event line. This is used in conjunction with `<code>:s</code>&#8216; (e.g., `<code>:gs/</code><i>old</i>/<i>new</i>/&#8217;) or `<code>:&amp;</code>&#8216;. If used with `<code>:s</code>&#8216;, any delimiter can be used in place of /, and the final delimiter is optional if it is the last character of the event line. An <code>a</code> may be used as a synonym for <code>g</code>.</p>
<dt><code>G</code></p>
<dd> Apply the following `<code>s</code>&#8216; modifier once to each word in the event line.</dl>
<h2>PROGRAMMING WITH HISTORY FUNCTIONS</h2>
<p> This section describes how to use the History library in other programs.</p>
<h3>Introduction to History</h3>
<p> The programmer using the History library has available functions for remembering lines on a history list, associating arbitrary data with a line, removing lines from the list, searching through the list for a line containing an arbitrary text string, and referencing any line in the list directly. In addition, a history <i>expansion</i> function is available which provides for a consistent user interface across different programs. </p>
<p> The user using programs written with the History library has the benefit of a consistent user interface with a set of well-known commands for manipulating the text of previous lines and using that text in new commands. The basic history manipulation commands are identical to the history substitution provided by <code>bash</code>. </p>
<p> If the programmer desires, he can use the Readline library, which includes some history manipulation by default, and has the added advantage of command line editing. </p>
<p> Before declaring any functions using any functionality the History library provides in other code, an application writer should include the file <i>&lt;readline/history.h&gt;</i> in any file that uses the History library&#8217;s features. It supplies extern declarations for all of the library&#8217;s public functions and variables, and declares all of the public data structures. </p>
<h3>History Storage</h3>
<p> The history list is an array of history entries. A history entry is declared as follows: </p>
<p> <i>typedef void *</i> <code>histdata_t;</code> </p>
<pre><code>
typedef struct _hist_entry {
    char *line;
    char *timestamp;
    histdata_t data;
} HIST_ENTRY;
</code></pre>
<p> The history list itself might therefore be declared as </p>
<p> <i>HIST_ENTRY **</i> <code>the_history_list;</code> </p>
<p> The state of the History library is encapsulated into a single structure: </p>
<pre><code>
/*
 * A structure used to pass around the current state of the history.
 */
typedef struct _hist_state {
    HIST_ENTRY **entries; /* Pointer to the entries themselves. */
    int offset;           /* The location pointer within this array. */
    int length;           /* Number of elements within this array. */
    int size;             /* Number of slots allocated to this array. */
    int flags;
} HISTORY_STATE;
</code></pre>
<p> If the flags member includes <code>HS_STIFLED</code>, the history has been stifled.</p>
<h2>History Functions</h2>
<p> This section describes the calling sequence for the various functions exported by the GNU History library.</p>
<h3>Initializing History and State Management</h3>
<p> This section describes functions used to initialize and manage the state of the History library when you want to use the history functions in your program. </p>
<p> <i>void</i> <code>using_history</code> (<i>void</i>)<br />
 Begin a session in which the history functions might be used. This initializes the interactive variables. </p>
<p> <i>HISTORY_STATE *</i> <code>history_get_history_state</code> (<i>void</i>)<br />
 Return a structure describing the current state of the input history. </p>
<p> <i>void</i> <code>history_set_history_state</code> (<i>HISTORY_STATE *state</i>)<br />
 Set the state of the history list according to <i>state</i>. </p>
<h3>History List Management</h3>
<p> These functions manage individual entries on the history list, or set parameters managing the list itself. </p>
<p> <i>void</i> <code>add_history</code> (<i>const char *string</i>)<br />
 Place <i>string</i> at the end of the history list. The associated data field (if any) is set to <code>NULL</code>. </p>
<p> <i>void</i> <code>add_history_time</code> (<i>const char *string</i>)<br />
 Change the time stamp associated with the most recent history entry to <i>string</i>. </p>
<p> <i>HIST_ENTRY *</i> <code>remove_history</code> (<i>int which</i>)<br />
 Remove history entry at offset <i>which</i> from the history. The removed element is returned so you can free the line, data, and containing structure. </p>
<p> <i>histdata_t</i> <code>free_history_entry</code> (<i>HIST_ENTRY *histent</i>)<br />
 Free the history entry <i>histent</i> and any history library private data associated with it. Returns the application-specific data so the caller can dispose of it. </p>
<p> <i>HIST_ENTRY *</i> <code>replace_history_entry</code> (<i>int which, const char *line, histdata_t data</i>)<br />
 Make the history entry at offset <i>which</i> have <i>line</i> and <i>data</i>. This returns the old entry so the caller can dispose of any application-specific data. In the case of an invalid <i>which</i>, a <code>NULL</code> pointer is returned. </p>
<p> <i>void</i> <code>clear_history</code> (<i>void</i>)<br />
 Clear the history list by deleting all the entries. </p>
<p> <i>void</i> <code>stifle_history</code> (<i>int max</i>)<br />
 Stifle the history list, remembering only the last <i>max</i> entries. </p>
<p> <i>int</i> <code>unstifle_history</code> (<i>void</i>)<br />
 Stop stifling the history. This returns the previously-set maximum number of history entries (as set by <code>stifle_history()</code>). history was stifled. The value is positive if the history was stifled, negative if it wasn&#8217;t. </p>
<p> <i>int</i> <code>history_is_stifled</code> (<i>void</i>)<br />
 Returns non-zero if the history is stifled, zero if it is not. </p>
<h3>Information About the History List</h3>
<p> These functions return information about the entire history list or individual list entries. </p>
<p> <i>HIST_ENTRY **</i> <code>history_list</code> (<i>void</i>)<br />
 Return a <code>NULL</code> terminated array of <i>HIST_ENTRY *</i> which is the current input history. Element 0 of this list is the beginning of time. If there is no history, return <code>NULL</code>. </p>
<p> <i>int</i> <code>where_history</code> (<i>void</i>)<br />
 Returns the offset of the current history element. </p>
<p> <i>HIST_ENTRY *</i> <code>current_history</code> (<i>void</i>)<br />
 Return the history entry at the current position, as determined by <code>where_history()</code>. If there is no entry there, return a <code>NULL</code> pointer. </p>
<p> <i>HIST_ENTRY *</i> <code>history_get</code> (<i>int offset</i>)<br />
 Return the history entry at position <i>offset</i>, starting from <code>history_base</code>. If there is no entry there, or if <i>offset</i> is greater than the history length, return a <code>NULL</code> pointer. </p>
<p> <i>time_t</i> <code>history_get_time</code> (<i>HIST_ENTRY *</i>)<br />
 Return the time stamp associated with the history entry passed as the argument. </p>
<p> <i>int</i> <code>history_total_bytes</code> (<i>void</i>)<br />
 Return the number of bytes that the primary history entries are using. This function returns the sum of the lengths of all the lines in the history. </p>
<h3>Moving Around the History List</h3>
<p> These functions allow the current index into the history list to be set or changed. </p>
<p> <i>int</i> <code>history_set_pos</code> (<i>int pos</i>)<br />
 Set the current history offset to <i>pos</i>, an absolute index into the list. Returns 1 on success, 0 if <i>pos</i> is less than zero or greater than the number of history entries. </p>
<p> <i>HIST_ENTRY *</i> <code>previous_history</code> (<i>void</i>)<br />
 Back up the current history offset to the previous history entry, and return a pointer to that entry. If there is no previous entry, return a <code>NULL</code> pointer. </p>
<p> <i>HIST_ENTRY *</i> <code>next_history</code> (<i>void</i>)<br />
 Move the current history offset forward to the next history entry, and return the a pointer to that entry. If there is no next entry, return a <code>NULL</code> pointer. </p>
<h3>Searching the History List</h3>
<p> These functions allow searching of the history list for entries containing a specific string. Searching may be performed both forward and backward from the current history position. The search may be <i>anchored</i>, meaning that the string must match at the beginning of the history entry. </p>
<p> <i>int</i> <code>history_search</code> (<i>const char *string, int direction</i>)<br />
 Search the history for <i>string</i>, starting at the current history offset. If <i>direction</i> is less than 0, then the search is through previous entries, otherwise through subsequent entries. If <i>string</i> is found, then the current history index is set to that history entry, and the value returned is the offset in the line of the entry where <i>string</i> was found. Otherwise, nothing is changed, and a -1 is returned. </p>
<p> <i>int</i> <code>history_search_prefix</code> (<i>const char *string, int direction</i>)<br />
 Search the history for <i>string</i>, starting at the current history offset. The search is anchored: matching lines must begin with <i>string</i>. If <i>direction</i> is less than 0, then the search is through previous entries, otherwise through subsequent entries. If <i>string</i> is found, then the current history index is set to that entry, and the return value is 0. Otherwise, nothing is changed, and a -1 is returned. </p>
<p> <i>int</i> <code>history_search_pos</code> (<i>const char *string, int direction, int pos</i>)<br />
 Search for <i>string</i> in the history list, starting at <i>pos</i>, an absolute index into the list. If <i>direction</i> is negative, the search proceeds backward from <i>pos</i>, otherwise forward. Returns the absolute index of the history element where <i>string</i> was found, or -1 otherwise. </p>
<h3>Managing the History File</h3>
<p> The History library can read the history from and write it to a file. This section documents the functions for managing a history file. </p>
<p> <i>int</i> <code>read_history</code> (<i>const char *filename</i>)<br />
 Add the contents of <i>filename</i> to the history list, a line at a time. If <i>filename</i> is <code>NULL</code>, then read from <i>~/.history</i>. Returns 0 if successful, or <code>errno</code> if not. </p>
<p> <i>int</i> <code>read_history_range</code> (<i>const char *filename, int from, int to</i>)<br />
 Read a range of lines from <i>filename</i>, adding them to the history list. Start reading at line <i>from</i> and end at <i>to</i>. If <i>from</i> is zero, start at the beginning. If <i>to</i> is less than <i>from</i>, then read until the end of the file. If <i>filename</i> is <code>NULL</code>, then read from <i>~/.history</i>. Returns 0 if successful, or <code>errno</code> if not. </p>
<p> <i>int</i> <code>write_history</code> (<i>const char *filename</i>)<br />
 Write the current history to <i>filename</i>, overwriting <i>filename</i> if necessary. If <i>filename</i> is <code>NULL</code>, then write the history list to <i>~/.history</i>. Returns 0 on success, or <code>errno</code> on a read or write error. </p>
<p> <i>int</i> <code>append_history</code> (<i>int nelements, const char *filename</i>)<br />
 Append the last <i>nelements</i> of the history list to <i>filename</i>. If <i>filename</i> is <code>NULL</code>, then append to <i>~/.history</i>. Returns 0 on success, or <code>errno</code> on a read or write error. </p>
<p> <i>int</i> <code>history_truncate_file</code> (<i>const char *filename, int nlines</i>)<br />
 Truncate the history file <i>filename</i>, leaving only the last <i>nlines</i> lines. If <i>filename</i> is <code>NULL</code>, then <i>~/.history</i> is truncated. Returns 0 on success, or <code>errno</code> on failure. </p>
<h3>History Expansion</h3>
<p> These functions implement history expansion. </p>
<p> <i>int</i> <code>history_expand</code> (<i>char *string, char **output</i>)<br />
 Expand <i>string</i>, placing the result into <i>output</i>, a pointer to a string. Returns:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> If no expansions took place (or, if the only change in the text was the removal of escape characters preceding the history expansion character);</p>
<dt>1</p>
<dd> if expansions did take place;</p>
<dt>-1</p>
<dd> if there was an error in expansion;</p>
<dt>2</p>
<dd> if the returned line should be displayed, but not executed, as with the <code>:p</code> modifier.</dl>
</dl>
<p> If an error ocurred in expansion, then <i>output</i> contains a descriptive error message. </p>
<p> <i>char *</i> <code>get_history_event</code> (<i>const char *string, int *cindex, int qchar</i>)<br />
 Returns the text of the history event beginning at <i>string</i> + <i>*cindex</i>. <i>*cindex</i> is modified to point to after the event specifier. At function entry, <i>cindex</i> points to the index into <i>string</i> where the history event specification begins. <i>qchar</i> is a character that is allowed to end the event specification in addition to the &#8220;normal&#8221; terminating characters. </p>
<p> <i>char **</i> <code>history_tokenize</code> (<i>const char *string</i>)<br />
 Return an array of tokens parsed out of <i>string</i>, much as the shell might. The tokens are split on the characters in the <code>history_word_delimiters</code> variable, and shell quoting conventions are obeyed. </p>
<p> <i>char *</i> <code>history_arg_extract</code> (<i>int first, int last, const char *string</i>)<br />
 Extract a string segment consisting of the <i>first</i> through <i>last</i> arguments present in <i>string</i>. Arguments are split using <code>history_tokenize()</code>. </p>
<h3>History Variables</h3>
<p> This section describes the externally-visible variables exported by the GNU History Library. </p>
<p> <i>int</i> <code>history_base</code><br />
 The logical offset of the first entry in the history list. </p>
<p> <i>int</i> <code>history_length</code><br />
 The number of entries currently stored in the history list. </p>
<p> <i>int</i> <code>history_max_entries</code><br />
 The maximum number of history entries. This must be changed using <code>stifle_history()</code>. </p>
<p> <i>int</i> <code>history_wite_timestamps</code><br />
 If non-zero, timestamps are written to the history file, so they can be preserved between sessions. The default value is 0, meaning that timestamps are not saved. The current timestamp format uses the value of <i>history_comment_char</i> to delimit timestamp entries in the history file. If that variable does not have a value (the default), timestamps will not be written. </p>
<p> <i>char</i> <code>history_expansion_char</code><br />
 The character that introduces a history event. The default is <code>!</code>. Setting this to 0 inhibits history expansion. </p>
<p> <i>char</i> <code>history_subst_char</code><br />
 The character that invokes word substitution if found at the start of a line. The default is <code>^</code>. </p>
<p> <i>char</i> <code>history_comment_char</code><br />
 During tokenization, if this character is seen as the first character of a word, then it and all subsequent characters up to a newline are ignored, suppressing history expansion for the remainder of the line. This is disabled by default. </p>
<p> <i>char *</i> <code>history_word_delimiters</code><br />
 The characters that separate tokens for <code>history_tokenize()</code>. The default value is <code>&quot;&nbsp;<wbr>	
()&lt;&gt;;&amp;|&quot;</code>. </p>
<p> <i>char *</i> <code>history_no_expand_chars</code><br />
 The list of characters which inhibit history expansion if found immediately following <code>history_expansion_char</code>. The default is space, tab, newline, <code></code>, and <code>=</code>. </p>
<p> <i>char *</i> <code>history_search_delimiter_chars</code><br />
 The list of additional characters which can delimit a history search string, in addition to space, tab, <i>:</i> and <i>?</i> in the case of a substring search. The default is empty. </p>
<p> <i>int</i> <code>history_quotes_inhibit_expansion</code><br />
 If non-zero, single-quoted words are not scanned for the history expansion character. The default value is 0. </p>
<p> <i>rl_linebuf_func_t *</i> <code>history_inhibit_expansion_function</code><br />
 This should be set to the address of a function that takes two arguments: a <code>char *</code> (<i>string</i>) and an <code>int</code> index into that string (<i>i</i>). It should return a non-zero value if the history expansion starting at <i>string[i]</i> should not be performed; zero if the expansion should be done. It is intended for use by applications like <code>bash</code> that use the history expansion character for additional purposes. By default, this variable is set to <code>NULL</code>.</p>
<h2>FILES</h2>
<dl>
<dt> <i>~/.history</i></p>
<dd> Default filename for reading and writing saved history</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><i>The Gnu Readline Library</i>, Brian Fox and Chet Ramey</p>
<dd>
<dt><i>The Gnu History Library</i>, Brian Fox and Chet Ramey</p>
<dd>
<dt><i><a href="/docs/linux/man/1-bash/">bash</a></i>(1)</p>
<dd>
<dt><i><a href="/docs/linux/man/3-readline/">readline</a></i>(3)</p>
<dd></dl>
<h2>AUTHORS</h2>
<p> Brian Fox, Free Software Foundation<br />
 bfox [at] gnu.org </p>
<p> Chet Ramey, Case Western Reserve University<br />
 chet [at] ins.CWRU.Edu</p>
<h2>BUG REPORTS</h2>
<p> If you find a bug in the <code>history</code> library, you should report it. But first, you should make sure that it really is a bug, and that it appears in the latest version of the <code>history</code> library that you have. </p>
<p> Once you have determined that a bug actually exists, mail a bug report to <i>bug-readline</i>@<i>gnu.org</i>. If you have a fix, you are welcome to mail that as well! Suggestions and `philosophical&#8217; bug reports may be mailed to bug-readline@<i>gnu.org</i> or posted to the Usenet newsgroup <code>gnu.bash.bug</code>. </p>
<p> Comments and bug reports concerning this manual page should be directed to <i>chet [at] ins.CWRU.Edu</i>. </p>
<h2>Index</h2>
