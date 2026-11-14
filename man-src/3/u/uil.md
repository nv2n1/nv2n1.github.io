---
title: "uil(3)"
name: "uil"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uil/"
description: "Uil — Invokes the UIL compiler from within an application"
---

<p><code>Uil</code> &#8212; Invokes the UIL compiler from within an application</p>
<h2>Synopsis</h2>
<pre>#include &lt;uil/UilDef.h&gt;
<code>Uil_status_type Uil</code>(
<code>Uil_command_type *command_desc</code>,
<code>Uil_compile_desc_type **compile_desc</code>,
<code>Uil_continue_type (*message_cb</code>) (),
<code>char *message_data</code>,
<code>Uil_continue_type (*status_cb</code>) (),
<code>char *status_data</code>);</pre>
<h2>Description</h2>
<p>The <code>Uil</code> function provides a callable entry point for the UIL compiler. The <code>Uil</code> callable interface can be used to process a UIL source file and to generate UID files, as well as return a detailed description of the UIL source module in the form of a symbol table (parse tree).</p>
<dl COMPACT>
<dt><i>command_desc</i></p>
<dd>Specifies the <code>uil</code> command line.</p>
<dt><i>compile_desc</i></p>
<dd>Returns the results of the compilation.</p>
<dt><i>message_cb</i></p>
<dd>Specifies a callback function that is called when the compiler encounters errors in the UIL source.</p>
<dt><i>message_data</i></p>
<dd>Specifies user data that is passed to the message callback function (<i>message_cb)</i>. Note that this argument is not interpreted by UIL, and is used exclusively by the calling application.</p>
<dt><i>status_cb</i></p>
<dd>Specifies a callback function that is called to allow X applications to service X events such as updating the screen. This function is called at various check points, which have been hard coded into the UIL compiler. The <i>status_update_delay</i> argument in <i>command_desc</i> specifies the number of check points to be passed before the <i>status_cb</i> function is invoked.</p>
<dt><i>status_data</i></p>
<dd>Specifies user data that is passed to the status callback function (<i>status_cb).</i> Note that this argument is not interpreted by the UIL compiler and is used exclusively by the calling application.</dl>
<p> Following are the data structures <code>Uil_command_type</code> and <code>Uil_compile_desc_type</code>: </p>
<pre><tt>typedef struct Uil_command_type {
char *source_file;
 /* single source to compile */
char *resource_file; /* name of output file */
char *listing_file; /* name of listing file */
unsigned int *include_dir_count;
 /* number of dirs. in include_dir */
char *((*include_dir) []);
 /* dir. to search for include files */
unsigned listing_file_flag: 1;
 /* produce a listing */
unsigned resource_file_flag: 1;
 /* generate UID output */
unsigned machine_code_flag: 1;
 /* generate machine code */
unsigned report_info_msg_flag: 1;
 /* report info messages */
unsigned report_warn_msg_flag: 1;
 /* report warnings */
unsigned parse_tree_flag: 1;
 /* generate parse tree */
unsigned int status_update_delay;
 /* number of times a status point is */
 /* passed before calling status_cb */
 /* function 0 means called every time */
char *database;
 /* name of database file */
unsigned database_flag: 1;
 /* read a new database file */
unsigned use_setlocale_flag: 1;
 /* enable calls to setlocale */
};
typedef struct Uil_compile_desc_type {
unsigned int compiler_version;
 /* version number of compiler */
unsigned int data_version;
 /* version number of structures */
char *parse_tree_root; /* parse tree output */
unsigned int message_count [Uil_k_max_status+1];
/* array of severity counts */
};</tt></pre>
<p>Following is a description of the message callback function specified by <i>message_cb</i>: </p>
<pre>Uil_continue_type (<i>*message_cb</i>) (<i>message_data, message_number, severity, msg_buffer,
src_buffer, ptr_buffer, loc_buffer, message_count</i>)
 char <i>*message_data</i>;
 int <i>message_number</i>;
 int <i>severity</i>;
 char <i>*msg_buffer</i>, <i>*src_buffer</i>;
 char <i>*ptr_buffer</i>, <i>*loc_buffer</i>;
 int <i>message_count</i>[];</pre>
<p>This function specifies a callback function that UIL invokes instead of printing an error message when the compiler encounters an error in the UIL source. The callback should return one of the following values:</p>
<dl COMPACT>
<dt><code>Uil_k_terminate</code></p>
<dd>Terminate processing of the source file</p>
<dt><code>Uil_k_continue</code></p>
<dd>Continue processing the source file</dl>
<p> The arguments are</p>
<dl COMPACT>
<dt><i>message_data</i></p>
<dd>Data supplied by the application as the <i>message_data</i> argument to the <code>Uil</code> function. UIL does not interpret this data in any way; it just passes it to the callback.</p>
<dt><i>message_number</i></p>
<dd>An index into a table of error messages and severities for internal use by UIL.</p>
<dt><i>severity</i></p>
<dd>An integer that indicates the severity of the error. The possible values are the status constants returned by the <code>Uil</code> function. See <code>Return Value</code> for more information.</p>
<dt><i>msg_buffer</i></p>
<dd>A string that describes the error.</p>
<dt><i>src_buffer</i></p>
<dd>A string consisting of the source line where the error occurred. This string is not always available. In this case, the argument is NULL.</p>
<dt><i>ptr_buffer</i></p>
<dd>A string consisting of whitespace and a printing character in the character position corresponding to the column of the source line where the error occurred. This string may be printed beneath the source line to provide a visual indication of the column where the error occurred. This string is not always available. In this case, the argument is NULL.</p>
<dt><i>loc_buffer</i></p>
<dd>A string identifying the line number and file of the source line where the error occurred. This is not always available; the argument is then NULL.</p>
<dt><i>message_count</i></p>
<dd>An array of integers containing the number of diagnostic messages issued thus far for each severity level. To find the number of messages issued for the current severity level, use the <i>severity</i> argument as the index into this array.</dl>
<p> Following is a description of the status callback function specified by <i>status_cb</i>: </p>
<pre>Uil_continue_type (<i>*status_cb</i>) (<i>status_data, percent_complete,
 lines_processed, current_file, message_count</i>)
 char <i>*status_data</i>;
 int <i>percent_complete</i>;
 int <i>lines_processed</i>;
 char <i>*current_file</i>;
 int <i>message_count</i>[];</pre>
<p>This function specifies a callback function that is invoked to allow X applications to service X events such as updating the screen. The callback should return one of the following values:</p>
<dl COMPACT>
<dt><code>Uil_k_terminate</code></p>
<dd>Terminate processing of the source file</p>
<dt><code>Uil_k_continue</code></p>
<dd>Continue processing the source file</dl>
<p> The arguments are</p>
<dl COMPACT>
<dt><i>status_data</i></p>
<dd>Data supplied by the application as the <i>status_data</i> argument to the <code>Uil</code> function. UIL does not interpret this data in any way; it just passes it to the callback.</p>
<dt><i>percent_complete</i></p>
<dd>An integer indicating what percentage of the current source file has been processed so far.</p>
<dt><i>lines_processed</i></p>
<dd>An integer indicating how many lines of the current source file have been read so far.</p>
<dt><i>current_file</i></p>
<dd>A string containing the pathname of the current source file.</p>
<dt><i>message_count</i></p>
<dd>An array of integers containing the number of diagnostic messages issued thus far for each severity level. To find the number of messages issued for a given severity level, use the severity level as the index into this array. The possible severity levels are the status constants returned by the <code>Uil</code> function. See <code>Return Value</code> for more information.</dl>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>Uil_k_success_status</code></p>
<dd>The operation succeeded.</p>
<dt><code>Uil_k_info_status</code></p>
<dd>The operation succeeded. An informational message is returned.</p>
<dt><code>Uil_k_warning_status</code></p>
<dd>The operation succeeded. A warning message is returned.</p>
<dt><code>Uil_k_error_status</code></p>
<dd>The operation failed due to an error.</p>
<dt><code>Uil_k_severe_status</code></p>
<dd>The operation failed due to an error.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-uildumpsymboltable/">UilDumpSymbolTable</a></code>(3) and <code><a href="/docs/linux/man/1-uil/">uil</a></code>(1).</p>
