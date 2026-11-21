---

title: "popt(3)"
name: "popt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-popt/"
description: "popt – Parse command line options"
---

<p> popt - Parse command line options  </p>
<pre><code>
 #include &lt;popt.h&gt; 
 poptContext poptGetContext(const char *  name  , int  argc  , 
                            const char ** argv  , 
                            const struct poptOption *  options  , 
                            int  flags  ); 
 void poptFreeContext(poptContext  con  ); 
 void poptResetContext(poptContext  con  ); 
 int poptGetNextOpt(poptContext  con  ); 
 const char * poptGetOptArg(poptContext  con  ); 
 const char * poptGetArg(poptContext  con  ); 
 const char * poptPeekArg(poptContext  con  ); 
 const char ** poptGetArgs(poptContext  con  ); 
 const char *const poptStrerror(const int  error  ); 
 const char * poptBadOption(poptContext  con  , int  flags  ); 
 int poptReadDefaultConfig(poptContext  con  , int  flags  ); 
 int poptReadConfigFile(poptContext  con  , char *  fn  ); 
 int poptAddAlias(poptContext  con  , struct poptAlias  alias  , 
                  int  flags  ); 
 int poptParseArgvString(char *  s  , int *  argcPtr  , 
                         const char ***  argvPtr  ); 
 int poptDupArgv(int  argc  , const char **  argv  , int *  argcPtr  , 
                         const char ***  argvPtr  ); 
 int poptStuffArgs(poptContext  con  , const char **  argv  ); 
</code></pre>
<p> The popt library exists essentially for parsing command-line options. It is found superior in many ways when compared to parsing the argv array by hand or using the getopt functions <code>getopt()</code> and <code>getopt_long()</code> [see <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3)]. Some specific advantages of popt are: it does not utilize global variables, thus enabling multiple passes in parsing <i>argv</i> ; it can parse an arbitrary array of <i>argv</i>-style elements, allowing parsing of command-line-strings from any source; it provides a standard method of option aliasing (to be discussed at length below.); it can exec external option filters; and, finally, it can automatically generate help and usage messages for the application. </p>
<p>Like <code>getopt_long()</code>, the popt library supports short and long style options. Recall that a <code>short option</code> consists of a - character followed by a single alphanumeric character. A <code>long option</code>, common in GNU utilities, consists of two - characters followed by a string made up of letters, numbers and hyphens. Long options are optionally allowed to begin with a single -, primarily to allow command-line compatibility between popt applications and X toolkit applications. Either type of option may be followed by an argument. A space separates a short option from its arguments; either a space or an = separates a long option from an argument. </p>
<p>The popt library is highly portable and should work on any POSIX platform. The latest version is distributed with rpm and is always available from: <a href="ftp://ftp.rpm.org/pub/rpm/dist.">ftp://ftp.rpm.org/pub/rpm/dist.</a> </p>
<p>It may be redistributed under the X consortium license, see the file COPYING in the popt source distribution for details.  </p>
<h2>BASIC POPT USAGE</h2>
<h3>1. THE OPTION TABLE</h3>
<p> Applications provide popt with information on their command-line options by means of an &quot;option table,&quot; i.e., an array of <code>struct poptOption </code> structures: </p>
<p>#include &lt;popt.h&gt; </p>
<pre><code>struct poptOption {
    const char * longName; /* may be NULL */
    char shortName; /* may be '\0' */
    int argInfo;
    void * arg; /* depends on argInfo */
    int val; /* 0 means don't return, just update flag */
    char * descrip; /* description for autohelp -- may be NULL */
    char * argDescrip; /* argument description for autohelp */
};
</code></pre>
<p>Each member of the table defines a single option that may be passed to the program. Long and short options are considered a single option that may occur in two different forms. The first two members, <i>longName</i> and <i>shortName</i>, define the names of the option; the first is a long name, while the latter is a single character. </p>
<p>The <i>argInfo</i> member tells popt what type of argument is expected after the argument. If no option is expected, <code>POPT_ARG_NONE</code> should be used. The rest of the valid values are shown in the following table: </p>
<table>
<tr VALIGN=top>
<td><code>For numeric values, if the <i>argInfo</i> value is bitwise or&#8217;d with one of</code></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><code>POPT_ARGFLAG_OR</code>, <code>POPT_ARGFLAG_AND</code>, or <code>POPT_ARGFLAG_XOR</code>,</code></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>the value is saved by performing an OR, AND, or XOR.</td>
<td>
</td>
<td>
</td>
<td><font SIZE="-9"><i></i></font>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
<td>
</td>
<td><font SIZE="-9"></font>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9"><hr />
</font></td>
<td></td>
<td>
</td>
<td><hr />
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
<td>
</td>
<td>
</td>
<td><font SIZE="-9">&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font>
</td>
<td><i></i>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9"><hr />
</font></td>
<td></td>
<td>
</td>
<td><hr />
</td>
<td><i></i>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
<td><font SIZE="-9">&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font>
</td>
<td>
</td>
<td><i></i>
</td>
<td><font SIZE="-9"><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></font>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9"><hr />
</font></td>
<td></td>
<td>
</td>
<td><i><hr />
</i></td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
<td>
</td>
<td><i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></i>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td><i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></i>
</td>
<td><i></i>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9"><hr />
</font></td>
<td></td>
<td>
</td>
<td><hr />
</td>
<td>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
<td>
</td>
<td>
</td>
<td><i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></i>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
<td><i></i>
</td>
<td>
</td>
<td>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9"><hr />
</font></td>
<td></td>
<td>
</td>
<td><hr />
</td>
<td>
</td>
<td><i></i>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
<td>
</td>
<td><i></i>
</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9"><hr />
</font></td>
<td></td>
<td>
</td>
<td><code><hr />
</code></td>
<td>
</td>
<td>
</td>
<td><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td><i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></i>
</td>
<td><code></code>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9"><hr />
</font></td>
<td></td>
<td>
</td>
<td><code><hr />
</code></td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td><i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></i>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>specified, <code>-longopt</code> is accepted as well.</td>
</tr>
<tr VALIGN=top>
<td>Otherwise it should point to a variable of the type indicated in the </td>
</tr>
<tr VALIGN=top>
<td>right-most column of the table above.</td>
</tr>
<tr VALIGN=top>
<td>will perhaps not escape the attention of hunt-and-peck typists that </td>
</tr>
<tr VALIGN=top>
<td>an argument, the variable that </td>
</tr>
<tr VALIGN=top>
<td>error returned if the conversion fails.</td>
</tr>
<tr VALIGN=top>
<td><code>POPT_ARG_VAL</code> causes <i>arg</i> to be set to the (integer) value of</td>
</tr>
<tr VALIGN=top>
<td><i>val</i> when the argument is found. This is most often useful for</td>
</tr>
<tr VALIGN=top>
<td>mutually-exclusive arguments in cases where it is not an error for</td>
</tr>
<tr VALIGN=top>
<td>multiple arguments to occur and where you want the last argument</td>
</tr>
<tr VALIGN=top>
<td>specified to win; for example, &quot;rm -i -f&quot;. <code>POPT_ARG_VAL</code> causes</td>
</tr>
<tr VALIGN=top>
<td>the parsing function not to return a value, since the value of <i>val</i></td>
</tr>
<tr VALIGN=top>
<td>has already been used.</td>
</tr>
<tr VALIGN=top>
<td>If the <i>argInfo</i> value is bitwise or&#8217;d with <code>POPT_ARGFLAG_OPTIONAL</code>,</td>
</tr>
<tr VALIGN=top>
<td>the argument to the long option may be omitted. If the long option</td>
</tr>
<tr VALIGN=top>
<td>is used without an argument, a default value of zero or NULL will be saved</td>
</tr>
<tr VALIGN=top>
<td>(if the arg pointer is present), otherwise behavior will be identical to</td>
</tr>
<tr VALIGN=top>
<td>a long option with argument.</td>
</tr>
<tr VALIGN=top>
<td>should return when the option is encountered. If it is 0, the parsing</td>
</tr>
<tr VALIGN=top>
<td>function does not return a value, instead parsing the next </td>
</tr>
<tr VALIGN=top>
<td>command-line argument.</td>
</tr>
<tr VALIGN=top>
<td>if automatic help messages are desired (automatic usage messages can</td>
</tr>
<tr VALIGN=top>
<td>arguments.</td>
</tr>
<tr VALIGN=top>
<td>see below) in the main one which provides the table entries for these</td>
</tr>
<tr VALIGN=top>
<td>use popt&#8217;s automatical help, popt displays the appropriate message on </td>
</tr>
<tr VALIGN=top>
<td>stderr as soon as it finds the option, and exits the program with a</td>
</tr>
<tr VALIGN=top>
<td>return code of 0. If you want to use popt&#8217;s automatic help generation in</td>
</tr>
<tr VALIGN=top>
<td>a different way, you need to explicitly add the option entries to your programs </td>
</tr>
<tr VALIGN=top>
<td>If the <i>argInfo</i> value is bitwise or&#8217;d with <code>POPT_ARGFLAG_DOC_HIDDEN</code>,</td>
</tr>
<tr VALIGN=top>
<td>the argument will not be shown in help output.</td>
</tr>
<tr VALIGN=top>
<td>If the <i>argInfo</i> value is bitwise or&#8217;d with <code>POPT_ARGFLAG_SHOW_DEFAULT</code>,</td>
</tr>
<tr VALIGN=top>
<td>the inital value of the arg will be shown in help output.</td>
</tr>
<tr VALIGN=top>
<td>The final structure in the table should have all the pointer values set</td>
</tr>
<tr VALIGN=top>
<td>There are two types of option table entries which do not specify command</td>
</tr>
<tr VALIGN=top>
<td>line options. When either of these types of entries are used, the</td>
</tr>
<tr VALIGN=top>
<td><i>longName</i> element must be <code>NULL</code> and the <code>shortName</code> element</td>
</tr>
<tr VALIGN=top>
<td>must be <code>&#8216;\0&#8217;</code>.</td>
</tr>
<tr VALIGN=top>
<td>The first of these special entry types allows the application to nest</td>
</tr>
<tr VALIGN=top>
<td>another option table in the current one; such nesting may extend quite</td>
</tr>
<tr VALIGN=top>
<td>deeply (the actual depth is limited by the program&#8217;s stack). Including</td>
</tr>
<tr VALIGN=top>
<td>other option tables allows a library to provide a standard set of</td>
</tr>
<tr VALIGN=top>
<td>command-line options to every program which uses it (this is often done</td>
</tr>
<tr VALIGN=top>
<td>in graphical programming toolkits, for example). To do this, set</td>
</tr>
<tr VALIGN=top>
<td>the <i>argInfo</i> field to <code>POPT_ARG_INCLUDE_TABLE</code> and the</td>
</tr>
<tr VALIGN=top>
<td>arg field to point to the table which is being included. If</td>
</tr>
<tr VALIGN=top>
<td>automatic help generation is being used, the <i>descrip</i> field should</td>
</tr>
<tr VALIGN=top>
<td>contain a overall description of the option table being included.</td>
</tr>
<tr VALIGN=top>
<td>The other special option table entry type tells popt to call a function (a</td>
</tr>
<tr VALIGN=top>
<td>callback) when any option in that table is found. This is especially usefull</td>
</tr>
<tr VALIGN=top>
<td>when included option tables are being used, as the program which provides</td>
</tr>
<tr VALIGN=top>
<td>the top-level option table doesn&#8217;t need to be aware of the other options</td>
</tr>
<tr VALIGN=top>
<td>which are provided by the included table. When a callback is set for</td>
</tr>
<tr VALIGN=top>
<td>a table, the parsing function never returns information on an option in</td>
</tr>
<tr VALIGN=top>
<td>the table. Instead, options information must be retained via the callback</td>
</tr>
<tr VALIGN=top>
<td>or by having popt set a variable through the option&#8217;s <i>arg</i> field.</td>
</tr>
<tr VALIGN=top>
<td>Option callbacks should match the following prototype:</td>
</tr>
<tr VALIGN=top>
<td>The first parameter is the context which is being parsed (see the next</td>
</tr>
<tr VALIGN=top>
<td>section for information on contexts), <i>opt</i> points to the option</td>
</tr>
<tr VALIGN=top>
<td>which triggered this callback, and <i>arg</i> is the option&#8217;s argument.</td>
</tr>
<tr VALIGN=top>
<td>If the option does not take an argument, <i>arg</i> is <code>NULL</code>. The</td>
</tr>
<tr VALIGN=top>
<td>final parameter, <i>data</i> is taken from the <i>descrip</i> field</td>
</tr>
<tr VALIGN=top>
<td>of the option table entry which defined the callback. As <i>descrip</i></td>
</tr>
<tr VALIGN=top>
<td>is a pointer, this allows callback functions to be passed an arbitrary</td>
</tr>
<tr VALIGN=top>
<td>set of data (though a typecast will have to be used).</td>
</tr>
<tr VALIGN=top>
<td>The option table entry which defines a callback has an <i>argInfo</i> of</td>
</tr>
<tr VALIGN=top>
<td><code>POPT_ARG_CALLBACK</code>, an <i>arg</i> which points to the callback</td>
</tr>
<tr VALIGN=top>
<td>function, and a <i>descrip</i> field which specifies an arbitrary pointer</td>
</tr>
<tr VALIGN=top>
<td>to be passed to the callback.</td>
</tr>
<tr VALIGN=top>
<td>popt can interleave the parsing of multiple command-line sets. It allows</td>
</tr>
<tr VALIGN=top>
<td>this by keeping all the state information for a particular set of</td>
</tr>
<tr VALIGN=top>
<td>command-line arguments in a </td>
</tr>
<tr VALIGN=top>
<td>modified outside the popt library.</td>
</tr>
<tr VALIGN=top>
<td>The first parameter, </td>
</tr>
<tr VALIGN=top>
<td>should be the name of the application whose options are being parsed,</td>
</tr>
<tr VALIGN=top>
<td>two arguments specify the command-line arguments to parse. These are </td>
</tr>
<tr VALIGN=top>
<td>which was described in the previous section. The final parameter, </td>
</tr>
<tr VALIGN=top>
<td>can take one of three values:</td>
</tr>
<tr VALIGN=top>
<td>lfB lfB</td>
</tr>
<tr VALIGN=top>
<td>lfB lfR.</td>
</tr>
<tr VALIGN=top>
<td>Value</td>
</tr>
<tr VALIGN=top>
<td>POPT_CONTEXT_NO_EXEC</td>
</tr>
<tr VALIGN=top>
<td>POPT_CONTEXT_KEEP_FIRST</td>
</tr>
<tr VALIGN=top>
<td>POPT_CONTEXT_POSIXMEHARDER</td>
</tr>
</table>
<p>A <code>poptContext</code> keeps track of which options have already been parsed and which remain, among other things. If a program wishes to restart option processing of a set of arguments, it can reset the <code>poptContext</code> by passing the context as the sole argument to <code>poptResetContext()</code>. </p>
<p>When argument processing is complete, the process should free the <code>poptContext</code> as it contains dynamically allocated components. The <code>poptFreeContext()</code> function takes a <code>poptContext</code> as its sole argument and frees the resources the context is using. </p>
<p>Here are the prototypes of both <code>poptResetContext()</code> and <code>poptFreeContext()</code>: </p>
<pre><code>
 #include &lt;popt.h&gt; 
 void poptFreeContext(poptContext  con  ); 
 void poptResetContext(poptContext  con  ); 
</code></pre>
<h3>3. PARSING THE COMMAND LINE</h3>
<p> After an application has created a <code>poptContext</code>, it may begin parsing arguments. <code>poptGetNextOpt()</code> performs the actual argument parsing. </p>
<pre><code>
 #include &lt;popt.h&gt; 
 int poptGetNextOpt(poptContext  con  ); 
</code></pre>
<p>Taking the context as its sole argument, this function parses the next command-line argument found. After finding the next argument in the option table, the function fills in the object pointed to by the option table entry&#8217;s <i>arg</i> pointer if it is not <code>NULL</code>. If the val entry for the option is non-0, the function then returns that value. Otherwise, <code>poptGetNextOpt()</code> continues on to the next argument. </p>
<p> <code>poptGetNextOpt()</code> returns -1 when the final argument has been parsed, and other negative values when errors occur. This makes it a good idea to keep the <i>val</i> elements in the options table greater than 0. </p>
<p>If all of the command-line options are handled through <i>arg</i> pointers, command-line parsing is reduced to the following line of code: </p>
<pre><code>rc = poptGetNextOpt(poptcon);
</code></pre>
<p>Many applications require more complex command-line parsing than this, however, and use the following structure: </p>
<pre><code>while ((rc = poptGetNextOpt(poptcon)) &gt; 0) {
     switch (rc) {
          /* specific arguments are handled here */
     }
}
</code></pre>
<p>When returned options are handled, the application needs to know the value of any arguments that were specified after the option. There are two ways to discover them. One is to ask popt to fill in a variable with the value of the option through the option table&#8217;s <i>arg</i> elements. The other is to use <code>poptGetOptArg()</code>: </p>
<pre><code>
 #include &lt;popt.h&gt; 
 char * poptGetOptArg(poptContext  con  ); 
</code></pre>
<p>This function returns the argument given for the final option returned by <code>poptGetNextOpt()</code>, or it returns <code>NULL</code> if no argument was specified. The calling function is responsible for deallocating this string. </p>
<h3>4. LEFTOVER ARGUMENTS</h3>
<p> Many applications take an arbitrary number of command-line arguments, such as a list of file names. When popt encounters an argument that does not begin with a -, it assumes it is such an argument and adds it to a list of leftover arguments. Three functions allow applications to access such arguments: </p>
<pre><code>
<dl>

<dt> const char * poptGetArg(poptContext  con  ); 
</code></pre>
</dt>
<dd> <p> This function returns the next leftover argument and marks it as processed. </p>
 </dd></dl>
<pre><code>
<dl>

<dt> const char * poptPeekArg(poptContext  con  ); 
</code></pre>
</dt>
<dd> <p> The next leftover argument is returned but not marked as processed. This allows an application to look ahead into the argument list, without modifying the list. </p>
 </dd></dl>
<pre><code>
<dl>

<dt> const char ** poptGetArgs(poptContext  con  ); 
</code></pre>
</dt>
<dd> <p> All the leftover arguments are returned in a manner identical to <i>argv</i>. The final element in the returned array points to <code>NULL</code>, indicating the end of the arguments. </p>
 </dd></dl>
<h3>5. AUTOMATIC HELP MESSAGES</h3>
<p> The <code>popt</code> library can automatically generate help messages which describe the options a program accepts. There are two types of help messages which can be generated. Usage messages are a short messages which lists valid options, but does not describe them. Help messages describe each option on one (or more) lines, resulting in a longer, but more useful, message. Whenever automatic help messages are used, the <code>descrip</code> and <code>argDescrip</code> fields <code>struct poptOption</code> members should be filled in for each option. </p>
<p>The <code>POPT_AUTOHELP</code> macro makes it easy to add <code>--usage</code> and <code>--help</code> messages to your program, and is described in part 1 of this man page. If more control is needed over your help messages, the following two functions are available: </p>
<pre><code>
 #include &lt;popt.h&gt; 
 void poptPrintHelp(poptContext  con  , FILE *  f  , int  flags  ); 
 void poptPrintUsage(poptContext  con  , FILE *  f  , int  flags  ); 
</code></pre>
<p> <code>poptPrintHelp()</code> displays the standard help message to the stdio file descriptor f, while <code>poptPrintUsage()</code> displays the shorter usage message. Both functions currently ignore the <code>flags</code> argument; it is there to allow future changes. </p>
<h2>ERROR HANDLING</h2>
<p> All of the popt functions that can return errors return integers. When an error occurs, a negative error code is returned. The following table summarizes the error codes that occur: </p>
<pre><code>
      Error Description 
 POPT_ERROR_NOARG Argument missing for an option.
 POPT_ERROR_BADOPT Option's argument couldn't be parsed.
 POPT_ERROR_OPTSTOODEEP Option aliasing nested too deeply.
 POPT_ERROR_BADQUOTE Quotations do not match.
 POPT_ERROR_BADNUMBER Option couldn't be converted to number.
 POPT_ERROR_OVERFLOW A given number was too big or small.
</code></pre>
<p>Here is a more detailed discussion of each error: </p>
<dl>
<dt><code>POPT_ERROR_NOARG</code></dt>
<dd> <p> An option that requires an argument was specified on the command line, but no argument was given. This can be returned only by <code>poptGetNextOpt()</code>. </p>
 </dd>
<dt><code>POPT_ERROR_BADOPT</code></dt>
<dd> <p> An option was specified in <i>argv</i> but is not in the option table. This error can be returned only from <code>poptGetNextOpt()</code>. </p>
 </dd>
<dt><code>POPT_ERROR_OPTSTOODEEP</code></dt>
<dd> <p> A set of option aliases is nested too deeply. Currently, popt follows options only 10 levels to prevent infinite recursion. Only <code>poptGetNextOpt()</code> can return this error. </p>
 </dd>
<dt><code>POPT_ERROR_BADQUOTE</code></dt>
<dd> <p> A parsed string has a quotation mismatch (such as a single quotation mark). <code>poptParseArgvString()</code>, <code>poptReadConfigFile()</code>, or <code>poptReadDefaultConfig()</code> can return this error. </p>
 </dd>
<dt><code>POPT_ERROR_BADNUMBER</code></dt>
<dd> <p> A conversion from a string to a number (int or long) failed due to the string containing nonnumeric characters. This occurs when <code>poptGetNextOpt()</code> is processing an argument of type <code>POPT_ARG_INT</code>, <code>POPT_ARG_LONG</code>, POPT_ARG_FLOAT <code>, or </code>POPT_ARG_DOUBLE <code>.</code> </p>
 </dd>
<dt><code>POPT_ERROR_OVERFLOW</code></dt>
<dd> <p> A string-to-number conversion failed because the number was too large or too small. Like <code>POPT_ERROR_BADNUMBER</code>, this error can occur only when <code>poptGetNextOpt()</code> is processing an argument of type <code>POPT_ARG_INT</code>, <code>POPT_ARG_LONG</code>, POPT_ARG_FLOAT <code>, or </code>POPT_ARG_DOUBLE <code>.</code> </p>
 </dd>
<dt><code>POPT_ERROR_ERRNO</code></dt>
<dd> <p> A system call returned with an error, and <i>errno</i> still contains the error from the system call. Both <code>poptReadConfigFile()</code> and <code>poptReadDefaultConfig()</code> can return this error. </p>
 </dd></dl>
<p>Two functions are available to make it easy for applications to provide good error messages. </p>
<dl>
<dt><pre><code>
 const char *const poptStrerror(const int  error  ); 
</code></pre>
</dt>
<dd> <p> This function takes a popt error code and returns a string describing the error, just as with the standard <code>strerror()</code> function. </p>
 </dd></dl>
<dl>
<dt><pre><code>
 const char * poptBadOption(poptContext  con  , int  flags  ); 
</code></pre>
 If an error occurred during <code>poptGetNextOpt()</code>, this function returns the option that caused the error. If the <i>flags</i> argument is set to <code>POPT_BADOPTION_NOALIAS</code>, the outermost option is returned. Otherwise, <i>flags</i> should be 0, and the option that is </dt>
<dd> <p> returned may have been specified through an alias. </p>
 </dd></dl>
<p>These two functions make popt error handling trivial for most applications. When an error is detected from most of the functions, an error message is printed along with the error string from <code>poptStrerror()</code>. When an error occurs during argument parsing, code similiar to the following displays a useful error message: </p>
<pre><code>fprintf(stderr, &quot;%s: %s\n&quot;,
        poptBadOption(optCon, POPT_BADOPTION_NOALIAS),
        poptStrerror(rc));
</code></pre>
<h2>OPTION ALIASING</h2>
<p> One of the primary benefits of using popt over <code>getopt()</code> is the ability to use option aliasing. This lets the user specify options that popt expands into other options when they are specified. If the standard grep program made use of popt, users could add a <code>--text</code> option that expanded to <code>-i -n -E -2</code> to let them more easily find information in text files. </p>
<h3>1. SPECIFYING ALIASES</h3>
<p> Aliases are normally specified in two places: <i>/etc/popt</i> and the <code>.popt</code> file in the user&#8217;s home directory (found through the <code>HOME</code> environment variable). Both files have the same format, an arbitrary number of lines formatted like this: </p>
<p> <i>appname</i><code> alias </code><i>newoption</i><i> expansion</i> </p>
<p>The <i>appname</i> is the name of the application, which must be the same as the <i>name</i> parameter passed to <code>poptGetContext()</code>. This allows each file to specify aliases for multiple programs. The <code>alias</code> keyword specifies that an alias is being defined; currently popt configuration files support only aliases, but other abilities may be added in the future. The next option is the option that should be aliased, and it may be either a short or a long option. The rest of the line specifies the expansion for the alias. It is parsed similarly to a shell command, which allows \, &quot;, and &#8216; to be used for quoting. If a backslash is the final character on a line, the next line in the file is assumed to be a logical continuation of the line containing the backslash, just as in shell. </p>
<p>The following entry would add a <code>--text</code> option to the grep command, as suggested at the beginning of this section. </p>
<p> <code>grep alias --text -i -n -E -2</code>  </p>
<h3>2. ENABLING ALIASES</h3>
<p> An application must enable alias expansion for a <code>poptContext</code> before calling <code>poptGetNextArg()</code> for the first time. There are three functions that define aliases for a context: </p>
<dl>
<dt><pre><code>
 int poptReadDefaultConfig(poptContext  con  , int  flags  ); 
</code></pre>
 This function reads aliases from <i>/etc/popt</i> and the <code>.popt</code> file in the user&#8217;s home directory. Currently, <i>flags</i> should be <code>NULL</code>, as it is provided only for future expansion. </dt>
</dl>
<dl>
<dt><pre><code>
 int poptReadConfigFile(poptContext  con  , char *  fn  ); 
</code></pre>
 The file specified by <i>fn</i> is opened and parsed as a popt </dt>
<dd> <p> configuration file. This allows programs to use program-specific configuration files. </p>
 </dd></dl>
<dl>
<dt><pre><code>
 int poptAddAlias(poptContext  con  , struct poptAlias  alias  , 
                  int  flags  ); 
</code></pre>
</dt>
<dd> <p> Occasionally, processes want to specify aliases without having to read them from a configuration file. This function adds a new alias to a context. The <i>flags</i> argument should be 0, as it is currently reserved for future expansion. The new alias is specified as a <code>struct poptAlias</code>, which is defined as: </p>
<pre><code>struct poptAlias {
     const char * longName; /* may be NULL */
     char shortName; /* may be '\0' */
     int argc;
     const char ** argv; /* must be free()able */
};
</code></pre>
<p>The first two elements, <i>longName</i> and <i>shortName</i>, specify the option that is aliased. The final two, <i>argc</i> and <i>argv</i>, define the expansion to use when the aliases option is encountered. </p>
 </dd></dl>
<h2>PARSING ARGUMENT STRINGS</h2>
<p> Although popt is usually used for parsing arguments already divided into an <i>argv</i>-style array, some programs need to parse strings that are formatted identically to command lines. To facilitate this, popt provides a function that parses a string into an array of strings, using rules similiar to normal shell parsing. </p>
<pre><code>
 #include &lt;popt.h&gt; 
 int poptParseArgvString(char *  s  , int *  argcPtr  , 
                         char ***  argvPtr  ); 
 int poptDupArgv(int  argc  , const char **  argv  , int *  argcPtr  , 
                         const char ***  argvPtr  ); 
</code></pre>
<p>The string s is parsed into an <i>argv</i>-style array. The integer pointed to by the <i>argcPtr</i> parameter contains the number of elements parsed, and the final <i>argvPtr</i> parameter contains the address of the newly created array. The routine <code>poptDupArgv()</code> can be used to make a copy of an existing argument array. </p>
<p>The <i>argvPtr</i> created by <code>poptParseArgvString()</code> or <code>poptDupArgv()</code> is suitable to pass directly to <code>poptGetContext()</code>. Both routines return a single dynamically allocated contiguous block of storage and should be <code>free()</code>ed when the application is finished with the storage.  </p>
<h2>HANDLING EXTRA ARGUMENTS</h2>
<p> Some applications implement the equivalent of option aliasing but need to do so through special logic. The <code>poptStuffArgs()</code> function allows an application to insert new arguments into the current <code>poptContext</code>. </p>
<pre><code>
 #include &lt;popt.h&gt; 
 int poptStuffArgs(poptContext con  , const char **  argv  ); 
</code></pre>
<p>The passed <i>argv</i> must have a <code>NULL</code> pointer as its final element. When <code>poptGetNextOpt()</code> is next called, the &quot;stuffed&quot; arguments are the first to be parsed. popt returns to the normal arguments once all the stuffed arguments have been exhausted.  </p>
<h2>EXAMPLE</h2>
<p> The following example is a simplified version of the program &quot;robin&quot; which appears in Chapter 15 of the text cited below. Robin has been stripped of everything but its argument-parsing logic, slightly reworked, and renamed &quot;parse.&quot; It may prove useful in illustrating at least some of the features of the extremely rich popt library. </p>
<pre><code>#include &lt;popt.h&gt;
#include &lt;stdio.h&gt;
void usage(poptContext optCon, int exitcode, char *error, char *addl) {
    poptPrintUsage(optCon, stderr, 0);
    if (error) fprintf(stderr, &quot;%s: %s, error, addl);
    exit(exitcode);
}
int main(int argc, char *argv[]) {
   char c; /* used for argument parsing */
   int i = 0; /* used for tracking options */
   char *portname;
   int speed = 0; /* used in argument parsing to set speed */
   int raw = 0; /* raw mode? */
   int j;
   char buf[BUFSIZ+1];
   poptContext optCon; /* context for parsing command-line options */
   struct poptOption optionsTable[] = {
            { &quot;bps&quot;, 'b', POPT_ARG_INT, &amp;speed, 0,
                &quot;signaling rate in bits-per-second&quot;, &quot;BPS&quot; },
            { &quot;crnl&quot;, 'c', 0, 0, 'c',
                &quot;expand cr characters to cr/lf sequences&quot; },
            { &quot;hwflow&quot;, 'h', 0, 0, 'h',
                &quot;use hardware (RTS/CTS) flow control&quot; },
            { &quot;noflow&quot;, 'n', 0, 0, 'n',
                &quot;use no flow control&quot; },
            { &quot;raw&quot;, 'r', 0, &amp;raw, 0,
                &quot;don't perform any character conversions&quot; },
            { &quot;swflow&quot;, 's', 0, 0, 's',
                &quot;use software (XON/XOF) flow control&quot; } ,
            POPT_AUTOHELP
            { NULL, 0, 0, NULL, 0 }
   };
   optCon = poptGetContext(NULL, argc, argv, optionsTable, 0);
   poptSetOtherOptionHelp(optCon, &quot;[OPTIONS]* &lt;port&gt;&quot;);
   if (argc &lt; 2) {
        poptPrintUsage(optCon, stderr, 0);exit(1);
   }
   /* Now do options processing, get portname */
   while ((c = poptGetNextOpt(optCon)) &gt;= 0) {
      switch (c) {
         case 'c':
            buf[i++] = 'c';
            break;
         case 'h':
            buf[i++] = 'h';
            break;
         case 's':
            buf[i++] = 's';
            break;
         case 'n':
            buf[i++] = 'n';
            break;
      }
   }
   portname = poptGetArg(optCon);
   if((portname == NULL) || !(poptPeekArg(optCon) == NULL))
      usage(optCon, 1, &quot;Specify a single port&quot;, &quot;.e.g., /dev/cua0&quot;);
   if (c &lt; -1) {
      /* an error occurred during option processing */
      fprintf(stderr, &quot;%s: %s\n&quot;,
              poptBadOption(optCon, POPT_BADOPTION_NOALIAS),
              poptStrerror(c));
      return 1;
   }
   /* Print out options, portname chosen */
   printf(&quot;Options chosen: &quot;);
   for(j = 0; j &lt; i ; j++)
      printf(&quot;-%c &quot;, buf[j]);
   if(raw) printf(&quot;-r &quot;);
   if(speed) printf(&quot;-b %d &quot;, speed);
   printf(&quot;\nPortname chosen: %s\n&quot;, portname);
   poptFreeContext(optCon);
   exit(0);
}
</code></pre>
<p>RPM, a popular Linux package management program, makes heavy use of popt&#8217;s features. Many of its command-line arguments are implemented through popt aliases, which makes RPM an excellent example of how to take advantage of the popt library. For more information on RPM, see <a rel="nofollow" href="http://www.rpm.org.">http://www.rpm.org.</a> The popt source code distribution includes test program(s) which use all of the features of the popt libraries in various ways. If a feature isn&#8217;t working for you, the popt test code is the first place to look.  </p>
<h2>BUGS</h2>
<p> None presently known.  </p>
<h2>AUTHOR</h2>
<p> Erik W. Troan &lt;ewt [at] redhat.com&gt; </p>
<p>This man page is derived in part from <i>Linux Application Development</i> by Michael K. Johnson and Erik W. Troan, Copyright (c) 1998 by Addison Wesley Longman, Inc., and included in the popt documentation with the permission of the Publisher and the appreciation of the Authors. </p>
<p>Thanks to Robert Lynch for his extensive work on this man page.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3) </p>
<p> <i>Linux Application Development</i>, by Michael K. Johnson and Erik W. Troan (Addison-Wesley, 1998; ISBN 0-201-30821-5), Chapter 24. </p>
<p> <code>popt.ps</code> is a Postscript version of the above cited book chapter. It can be found in the source archive for popt available at: <a href="ftp://ftp.rpm.org/pub/rpm.">ftp://ftp.rpm.org/pub/rpm.</a> </p>
