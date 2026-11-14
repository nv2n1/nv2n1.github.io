---
title: "argtable(3)"
name: "argtable"
section: "3"
letter: "a"
url: "/docs/linux/man/3-argtable/"
description: "argtable2 – an ANSI C library for parsing GNU style command line options"
---

<h2>NAME</h2>
<p> argtable2 &#8211; an ANSI C library for parsing GNU style command line options</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;argtable2.h&gt;
struct arg_lit
struct arg_int
struct arg_dbl
struct arg_str
struct arg_rex
struct arg_file
struct arg_date
struct arg_rem
struct arg_end
struct arg_lit* arg_lit0(const char *shortopts, const char *longopts, const char *glossary)
struct arg_lit* arg_lit1(const char *shortopts, const char *longopts, const char *glossary)
struct arg_lit* arg_litn(const char *shortopts, const char *longopts, int mincount, int maxcount, const char *glossary)
struct arg_int* arg_int0(const char* shortopts, const char* longopts, const char* datatype, const char* glossary)
struct arg_int* arg_int1(const char *shortopts, const char *longopts, const char* datatype, const char *glossary)
struct arg_int* arg_intn(const char *shortopts, const char *longopts, const char* datatype, int mincount, int maxcount, const char *glossary)
struct arg_dbl* arg_dbl0(const char *shortopts, const char *longopts, const char* datatype, const char *glossary)
struct arg_dbl* arg_dbl1(const char *shortopts, const char *longopts, const char* datatype, const char *glossary)
struct arg_dbl* arg_dbln(const char *shortopts, const char *longopts, const char* datatype, int mincount, int maxcount, const char *glossary)
struct arg_str* arg_str0(const char *shortopts, const char *longopts, const char* datatype, const char *glossary)
struct arg_str* arg_str1(const char *shortopts, const char *longopts, const char* datatype, const char *glossary)
struct arg_str* arg_strn(const char *shortopts, const char *longopts, const char* datatype, int mincount, int maxcount, const char *glossary)
struct arg_rex* arg_rex0(const char* shortopts, const char* longopts, const char* pattern, const char* datatype, int flags, const char* glossary)
struct arg_rex* arg_rex1(const char* shortopts, const char* longopts, const char* pattern, const char* datatype, int flags, const char* glossary)
struct arg_rex* arg_rexn(const char* shortopts, const char* longopts, const char* pattern, const char* datatype, int mincount, int maxcount, int flags, const char* glossary)
struct arg_file* arg_file0(const char* shortopts, const char* longopts, const char* datatype, const char* glossary)
struct arg_file* arg_file1(const char *shortopts, const char *longopts, const char* datatype, const char *glossary)
struct arg_file* arg_filen(const char *shortopts, const char *longopts, const char* datatype, int mincount, int maxcount, const char *glossary)
struct arg_date* arg_date0const char* shortopts, const char* longopts, const char* format, const char* datatype, const char *glossary)
struct arg_date* arg_date1const char* shortopts, const char* longopts, const char* format, const char* datatype, const char *glossary)
struct arg_date* arg_datenconst char* shortopts, const char* longopts, const char* format, const char* datatype, int mincount, int maxcount, const char *glossary)
struct arg_rem* arg_rem(const char *datatype, const char *glossary)
struct arg_end* arg_end(int maxerrors)
int arg_nullcheck(void **argtable)
int arg_parse(int argc, char **argv, void **argtable)
void arg_print_option(FILE *fp, const char *shortopts, const char *longopts, const char *datatype, const char *suffix)
void arg_print_syntax(FILE *fp, void **argtable, const char *suffix)
void arg_print_syntaxv(FILE *fp, void **argtable, const char *suffix)
void arg_print_glossary(FILE *fp, void **argtable, const char *format)
void arg_print_glossary_gnu(FILE *fp, void **argtable)
void arg_print_errors(FILE *fp, struct arg_end *end, const char *progname)
void arg_freetable(void **argtable, size_t n)
</code></pre>
<h2>DESCRIPTION</h2>
<p> Argtable is an ANSI C library for parsing GNU style command line arguments with a minimum of fuss. It enables the programmer to define their program&#8217;s argument syntax directly in the source code as an array of structs. The command line is then parsed according to that specification and the resulting values stored directly into user-defined program variables where they are accessible to the main program. </p>
<p> This man page is only for reference. Introductory documentation and example source code is typically installed under <code>/usr/share/doc/argtable2/</code> and is also available from the argtable homepage at <a rel="nofollow" href="http://argtable.sourceforge.net.">http://argtable.sourceforge.net.</a> </p>
<h3>Constructing an arg_&lt;xxx&gt; data structure</h3>
<p> Each <code>arg_&lt;xxx&gt;</code> struct has it own unique set of constructor functions (defined above) which are typically of the form: </p>
<p>struct arg_int *arg_int0(&#8220;f&#8221;, &#8220;foo&#8221;, &#8220;&lt;int&gt;&#8221;, &#8220;the foo factor&#8221;) struct arg_int *arg_int1(&#8220;f&#8221;, &#8220;foo&#8221;, &#8220;&lt;int&gt;&#8221;, &#8220;the foo factor&#8221;) struct arg_int *arg_intn(&#8220;f&#8221;, &#8220;foo&#8221;, &#8220;&lt;int&gt;&#8221;, 2, 4, &#8220;the foo factor&#8221;)</p>
<p> where arg_int0() and arg_int1() are merely abbreviated forms of arg_intn(). They are provided for convenience when defining command line options that have either zero-or-one occurrences (mincount=0,maxcount=1) or exactly one occurrence (mincount=1,maxcount=1) respectively. </p>
<p> The shortopts=&quot;f&quot; parameter defines the option&#8217;s short form tag (eg -f). Multiple alternative tags may be defined by concatenating them (eg shortopts=&quot;abc&quot; defines options -a, -b and -c as equivalent). Specify shortopts=NULL when no short option is required. </p>
<p> The longopts=&quot;foo&quot; parameter defines the option&#8217;s long form tag (eg &#8211;foo). Multiple alternative long form tags may be separated by commas (eg longopts=&quot;size,limit&quot; defines &#8211;size and &#8211;limit). Do not include any whitespace in the longopts string. Specify longopts=NULL when no long option is required. </p>
<p> If both shortopts and longopts are NULL then the option is an untagged argument. </p>
<p> The datatype=&quot;&lt;int&gt;&quot; parameter is a descriptive string that denotes the argument data type in error messages, as in &#8211;foo=&lt;int&gt;. Specifying datatype=NULL indicates the default datatype should be used. Specifying datatype=&quot;&quot; effectively disables the datatype display. </p>
<p> The mincount=2 and maxcount=3 parameters specify the minimum and maximum number of occurrences of the option on the command line. If the command line option does not appear the required number of times then the parser reports a syntax error. </p>
<p> The glossary=&quot;the foo factor&quot; parameter is another descriptive string. It appears only in the glossary table that is generated automatically by the <code>arg_print_glossary</code> function (described later).</p>
<dl>
<dt>
<dd> -f, &#8211;foo=&lt;int&gt; the foo factor</dl>
<p> Specifying a NULL glossary string causes that option to be omitted from the glossary table.</p>
<h3>LITERAL COMMAND LINE OPTIONS</h3>
<p> -x, -y, -z, &#8211;help, &#8211;verbose </p>
<p>struct arg_lit {<br />
    struct arg_hdr hdr; /* internal argtable header */<br />
    int count;          /* number of matching command line options */<br />
};</p>
<p> Literal options take no argument values. Upon a successful parse, <i>count</i> is guaranteed to be within the <i>mincount</i> and <i>maxcount</i> limits specified at construction.</p>
<h3>INTEGER COMMAND LINE OPTIONS</h3>
<p> -x2, -z 32MB, &#8211;size=734kb, &#8211;hex 0x7, &#8211;binary 0b10011010, &#8211;octal 0o123 </p>
<p> Argtable accepts command line integers in decimal (eg 123), hexadecimal (eg 0xFF12), octal (eg 0o123) and binary (eg 0b0101110) formats. It also accepts integers that are suffixed by &quot;KB&quot; (x1024), &quot;MB&quot; (x1048576) or &quot;GB&quot; (x1073741824). All characters are case insensitive </p>
<p>struct arg_int {<br />
    struct arg_hdr hdr; /* internal argtable header */<br />
    int count;          /* number of values returned in ival[] */<br />
    int *ival;          /* array of parsed integer values */<br />
};</p>
<p> Upon a successful parse, <i>count</i> is guaranteed to be within the <i>mincount</i> and <i>maxcount</i> limits set for the option at construction with the appropriate values store in the <i>ival</i> array. The parser will not accept any values beyond that limit. </p>
<p> Hint: It is legal to set default values in the <i>ival</i> array prior to calling the <code>arg_parse</code> function. Argtable will not alter <i>ival</i> entries for which no command line argument is received. </p>
<p> Hint: <i>Untagged</i> numeric arguments are not recommended because GNU getopt mistakes negative values (eg -123) for tagged options (eg -1 -2 -3). <i>Tagged</i> arguments (eg -x -123, &#8211;tag=-123) do not suffer this problem.</p>
<h3>REAL/DOUBLE COMMAND LINE OPTIONS</h3>
<p> -x2.234, -y 7e-03, -z-3.3E+6, &#8211;pi=3.1415, &#8211;tolerance 1.0E-6 </p>
<p>struct arg_dbl {<br />
    struct arg_hdr hdr; /* internal argtable header */<br />
    int count;          /* number of values returned in dval[] */<br />
    double *dval;       /* array of parsed double values */<br />
};</p>
<p> Same as <code>arg_int</code> except the parsed values are stored in <i>dval</i> as doubles.</p>
<h3>STRING COMMAND LINE OPTIONS</h3>
<p> -Dmacro, -t mytitle, -m &quot;my message string&quot;, &#8211;title=&quot;hello world&quot; </p>
<p>struct arg_str {<br />
    struct arg_hdr hdr; /* internal argtable header */<br />
    int count;          /* number of strings returned in sval[] */<br />
    const char **sval;  /* array of pointers to parsed argument strings */<br />
};</p>
<p> Same as <code>arg_int</code> except pointers to the parsed strings are returned in <i>sval</i> rather than a separate copy of the string. Indeed, these pointers actually reference the original string buffers stored in argv[], so their contents should not be altered. However, it is legal to initialise the string pointers in the <i>sval</i> array to reference user-supplied default strings prior to calling arg_parse. Argtable will only alter the contents of <i>sval</i> when matching command line arguments are detected.</p>
<h3>REGULAR EXPRESSION COMMAND LINE OPTIONS</h3>
<p> commit, update, &#8211;command=commit, &#8211;command=update </p>
<p>struct arg_rex {<br />
    struct arg_hdr hdr; /* internal argtable header */<br />
    int count;          /* number of strings returned in sval[] */<br />
    const char **sval;  /* array of pointers to parsed argument strings */<br />
};</p>
<p> Similar to <code>arg_str</code> except the string argument values are only accepted if they match a predefined regular expression. Regular expressions are useful for matching command line keywords, particularly if case insensitive strings or pattern matching is required. The regular expression is defined by the <i>pattern</i> parameter passed to the <i>arg_rex</i> constructor and evaluated using regex. Its behaviour can be controlled via standard regex bit flags. These are passed to argtable via the <i>flags</i> parameter in the <i>arg_rex</i> constructor. However the only two of the standard regex flags are relevant to argtable, namely REG_EXTENDED (use extended regular expressions rather than basic ones) and REG_ICASE (ignore case). These flags may be logically ORed if desired. See <code><a href="/docs/linux/man/3-regex/">regex</a>(3)</code> for more details of regular expression matching. </p>
<p> Restrictions: Argtable does not support <code>arg_rex</code> functionality under Microsoft Windows platforms because the Microsoft compilers do include the necessary <code>regex</code> support as standard.</p>
<h3>FILENAME COMMAND LINE OPTIONS</h3>
<p> -o myfile, -Ihome/foo/bar, &#8211;input=~/doc/letter.txt, &#8211;name a.out </p>
<p>struct arg_file {<br />
    struct arg_hdr hdr;     /* internal argtable header */<br />
    int count;              /* number of filename strings returned */<br />
    const char **filename;  /* pointer to full filename string */<br />
    const char **basename;  /* pointer to filename excluding leading path */<br />
    const char **extension; /* pointer to the filename extension */<br />
};</p>
<p> Similar to <code>arg_str</code> but the argument strings are presumed to refer to filenames hence some additional parsing is done to separate out the filename&#8217;s basename and extension (if they exist). The three arrays filename[], basename[], extension[] each store up to maxcount entries, and the i&#8217;th entry of each of these arrays refer to different components of the same string buffer. </p>
<p> For example, <code>-o /home/heitmann/mydir/foo.txt</code> would be parsed as:<br />
filename[i] = &#8220;/home/heitmann/mydir/foo.txt&#8221; basename[i] = &#8220;foo.txt&#8221; extension[i] = &#8220;.txt&#8221;</p>
<p> If the filename has no leading path then the basename is the same as the filename. If no extension could be identified then it is given as NULL. Extensions are considered as all text from the last dot in the filename. </p>
<p> Hint: Argtable only ever treats the filenames as strings and never attempts to open them as files or perform any directory lookups on them.</p>
<h3>DATE/TIME COMMAND LINE OPTIONS</h3>
<p> 12/31/04, -d 1982-11-28, &#8211;time 23:59 </p>
<p>struct arg_date {<br />
    struct arg_hdr hdr; /* internal argtable header */<br />
    const char *format; /* user-supplied date format string that was passed to constructor */<br />
    int count;          /* number of datestamps returned in tmval[] */<br />
    struct tm *tmval;   /* array of datestamps */<br />
};</p>
<p> Accepts a timestamp string from the command line and converts it to <i>struct tm</i> format using the system <code>strptime</code> function. The time format is defined by the <i>format</i> string passed to the <i>arg_date</i> constructor, and is passed directly to <code>strptime</code>. See <code><a href="/docs/linux/man/3-strptime/">strptime</a>(3)</code> for more details on the format string. </p>
<p> Restrictions: Argtable does not support <code>arg_date</code> functionality under Microsoft Windows because the Microsoft compilers do include the necessary <code>strptime</code> support as standard.</p>
<h3>REMARK OPTIONS</h3>
<p>struct arg_rem {<br />
    struct arg_hdr hdr; /* internal argtable header */<br />
};</p>
<p> The <code>arg_rem</code> struct is a dummy struct in the sense it does not represent a command line option to be parsed. Instead it provides a means to include additional <i>datatype</i> and <i>glossary</i> strings in the output of the <code>arg_print_syntax</code>, <code>arg_print_syntaxv</code>, and <code>arg_print_glossary functions</code>. As such, <code>arg_rem</code> structs may be used in the argument table to insert additional lines of text into the glossary descriptions or to insert additional text fields into the syntax description.</p>
<h3>END-OF-TABLE OPTION</h3>
<pre><code>
struct arg_end {
    struct arg_hdr hdr;  /* internal argtable header */
    int count;           /* number of errors returned */
    int *error;          /* array of error codes */
    void **parent;       /* pointers to the erroneous command line options */
    const char **argval; /* pointers to the erroneous command line argument values */
};
Every argument table must have an arg_end structure as its last entry.It marks the end of an argument table and stores the error codes generated
    by the parser as it processed the argument table.The maxerrors parameter passed to the arg_end constructor
        specifies the maximum number of errors that the structure can store.Any further errors are discarded and replaced with the single error code
            ARG_ELIMIT which is later reported to the user by the message "too many errors".A maxerrors limit of 20 is quite reasonable.The arg_print_errors function will print the errors stored
                in the arg_end struct in the same order as they occurred,
    so there is no need to understand the internals of the arg_end struct.
</code></pre>
<h2>FUNCTION REFERENCE</h2>
<h3>int arg_nullcheck (void **argtable)</h3>
<p> Returns non-zero if the <i>argtable[]</i> array contains any NULL entries up until the terminating <code>arg_end*</code> entry. Returns zero otherwise.</p>
<h3>int arg_parse (int argc, char **argv, void **argtable)</h3>
<p> Parse the command line arguments in <i>argv[]</i> using the command line syntax specified in <i>argtable[]</i>, returning the number of errors encountered. Error details are recorded in the argument table&#8217;s <code>arg_end</code> structure from where they can be displayed later with the <code>arg_print_errors</code> function. Upon a successful parse, the <code>arg_xxx</code> structures referenced in <i>argtable[]</i> will contain the argument values extracted from the command line.</p>
<h3>void arg_print_option (FILE *fp, const char *shortopts, const char *longopts, const char *datatype, const char *suffix)</h3>
<p> This function prints an option&#8217;s syntax, as in <code>-K|&#8211;scalar=&lt;int&gt;</code>, where the short options, long options, and datatype are all given as parameters of this function. It is primarily used within the <code>arg_xxx</code> structures&#8217; <i>errorfn</i> functions as a way of displaying an option&#8217;s syntax inside of error messages. However, it can also be used in user code if desired. The <i>suffix</i> string is provided as a convenience for appending newlines and so forth to the end of the display and can be given as NULL if not required.</p>
<h3>void arg_print_syntax (FILE *fp, void **argtable, const char *suffix)</h3>
<p> Prints the GNU style command line syntax for the given argument table, as in: [-abcv] [&#8211;scalar=&lt;n&gt;] [-o myfile] &lt;file&gt; [&lt;file&gt;]<br />
 The <i>suffix</i> string is provided as a convenience for appending newlines and so forth to the end of the display and can be given as NULL if not required.</p>
<h3>void arg_print_syntaxv (FILE *fp, void **argtable, const char *suffix)</h3>
<p> Prints the verbose form of the command line syntax for the given argument table, as in: [-a] [-b] [-c] [&#8211;scalar=&lt;n&gt;] [-o myfile] [-v|&#8211;verbose] &lt;file&gt; [&lt;file&gt;]<br />
 The <i>suffix</i> string is provided as a convenience for appending newlines and so forth to the end of the display and can be given as NULL if not required.</p>
<h3>void arg_print_glossary (FILE *fp, void **argtable, const char *format)</h3>
<p> Prints a glossary table describing each option in the given argument table. The <i>format</i> string is passed to printf to control the formatting of each entry in the the glossary. It must have exactly two &quot;%s&quot; format parameters as in &quot;%-25s %s
&quot;, the first is for the option&#8217;s syntax and the second for its glossary string. If an option&#8217;s glossary string is NULL then that option in omitted from the glossary display.</p>
<h3>void arg_print_glossary_gnu (FILE *fp, void **argtable)</h3>
<p> An alternate form of <code>arg_print_glossary()</code> that prints the glossary using strict GNU formatting conventions wherein long options are vertically aligned in a second column, and lines are wrapped at 80 characters.</p>
<h3>void arg_print_errors (FILE *fp, struct <code>arg_end</code> *end, const char *progname)</h3>
<p> Prints the details of all errors stored in the <i>end</i> data structure. The <i>progname</i> string is prepended to each error message.</p>
<h3>void arg_freetable (void ** argtable, size_t n)</h3>
<p> Deallocates the memory used by each <code>arg_xxx</code> struct referenced by <i>argtable[]</i>. It does this by calling <code>free</code> for each of the <i>n</i> pointers in the argtable array and then nulling them for safety. </p>
<h2>FILES</h2>
<p> /usr/include/argtable2.h<br />
 /usr/lib/libargtable2.a<br />
 /usr/lib/libargtable2.so<br />
 /usr/man3/argtable2.3<br />
 /usr/share/doc/argtable2/<br />
 /usr/share/doc/argtable2/example/ </p>
<h2>AUTHOR</h2>
<p> Stewart Heitmann &lt;sheitmann [at] users.sourceforge.net&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAY">FILES</a></p>
<dd>
<dt><a href="#lbAZ">AUTHOR</a></p>
<dd></dl>
