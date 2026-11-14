---
title: "getopt_long(3)"
name: "getopt_long"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getopt_long/"
description: "getopt, getopt_long, getopt_long_only, optarg, optind, opterr, optopt – Parse command-line options"
---

<h2 class="name">NAME</h2>
<p> getopt, getopt_long, getopt_long_only, optarg, optind, opterr, optopt &#8211; Parse command-line options </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
int getopt(int argc, char *const argv[],
           const char *optstring);
extern char *optarg;
extern int optind, opterr, optopt;
#include &lt;getopt.h&gt;
int getopt_long(int argc, char *const argv[],
                const char *optstring,
                const struct option *longopts, int *longindex);
int getopt_long_only(int argc, char *const argv[],
                     const char *optstring,
                     const struct option *longopts, int *longindex);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getopt</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;2 || _XOPEN_SOURCE<br />
 <code>getopt_long</code>(), <code>getopt_long_only</code>(): _GNU_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>getopt</code>() function parses the command-line arguments. Its arguments <i>argc</i> and <i>argv</i> are the argument count and array as passed to the <i>main</i>() function on program invocation. An element of <i>argv</i> that starts with &#8216;-&#8216; (and is not exactly &quot;-&quot; or &quot;&#8211;&quot;) is an option element. The characters of this element (aside from the initial &#8216;-&#8216;) are option characters. If <code>getopt</code>() is called repeatedly, it returns successively each of the option characters from each of the option elements. </p>
<p> The variable <i>optind</i> is the index of the next element to be processed in <i>argv</i>. The system initializes this value to 1. The caller can reset it to 1 to restart scanning of the same <i>argv</i>, or when scanning a new argument vector. </p>
<p> If <code>getopt</code>() finds another option character, it returns that character, updating the external variable <i>optind</i> and a static variable <i>nextchar</i> so that the next call to <code>getopt</code>() can resume the scan with the following option character or <i>argv</i>-element. </p>
<p> If there are no more option characters, <code>getopt</code>() returns -1. Then <i>optind</i> is the index in <i>argv</i> of the first <i>argv</i>-element that is not an option. </p>
<p> <i>optstring</i> is a string containing the legitimate option characters. If such a character is followed by a colon, the option requires an argument, so <code>getopt</code>() places a pointer to the following text in the same <i>argv</i>-element, or the text of the following <i>argv</i>-element, in <i>optarg</i>. Two colons mean an option takes an optional arg; if there is text in the current <i>argv</i>-element (i.e., in the same word as the option name itself, for example, &quot;-oarg&quot;), then it is returned in <i>optarg</i>, otherwise <i>optarg</i> is set to zero. This is a GNU extension. If <i>optstring</i> contains <code>W</code> followed by a semicolon, then <code>-W foo</code> is treated as the long option <code>&#8211;foo</code>. (The <code>-W</code> option is reserved by POSIX.2 for implementation extensions.) This behavior is a GNU extension, not available with libraries before glibc 2. </p>
<p> By default, <code>getopt</code>() permutes the contents of <i>argv</i> as it scans, so that eventually all the nonoptions are at the end. Two other scanning modes are also implemented. If the first character of <i>optstring</i> is &#8216;+&#8217; or the environment variable <code>POSIXLY_CORRECT</code> is set, then option processing stops as soon as a nonoption argument is encountered. If the first character of <i>optstring</i> is &#8216;-&#8216;, then each nonoption <i>argv</i>-element is handled as if it were the argument of an option with character code 1. (This is used by programs that were written to expect options and other <i>argv</i>-elements in any order and that care about the ordering of the two.) The special argument &quot;&#8211;&quot; forces an end of option-scanning regardless of the scanning mode. </p>
<p> While processing the option list, <code>getopt</code>() can detect two kinds of errors: (1) an option character that was not specified in <i>optstring</i> and (2) a missing option argument (i.e., an option at the end of the command line without an expected argument). Such errors are handled and reported as follows:</p>
<dl>
<dt>*</p>
<dd> By default, <code>getopt</code>() prints an error message on standard error, places the erroneous option character in <i>optopt</i>, and returns &#8216;?&#8217; as the function result.</p>
<dt>*</p>
<dd> If the caller has set the global variable <i>opterr</i> to zero, then <code>getopt</code>() does not print an error message. The caller can determine that there was an error by testing whether the function return value is &#8216;?&#8217;. (By default, <i>opterr</i> has a nonzero value.)</p>
<dt>*</p>
<dd> If the first character (following any optional &#8216;+&#8217; or &#8216;-&#8216; described above) of <i>optstring</i> is a colon (&#8216;:&#8217;), then <code>getopt</code>() likewise does not print an error message. In addition, it returns &#8216;:&#8217; instead of &#8216;?&#8217; to indicate a missing option argument. This allows the caller to distinguish the two different types of errors.</dl>
<h3>getopt_long() and getopt_long_only()</h3>
<p> The <code>getopt_long</code>() function works like <code>getopt</code>() except that it also accepts long options, started with two dashes. (If the program accepts only long options, then <i>optstring</i> should be specified as an empty string (&quot;&quot;), not NULL.) Long option names may be abbreviated if the abbreviation is unique or is an exact match for some defined option. A long option may take a parameter, of the form <code>&#8211;arg=param</code> or <code>&#8211;arg param</code>. </p>
<p> <i>longopts</i> is a pointer to the first element of an array of <i>struct option</i> declared in <i>&lt;getopt.h&gt;</i> as </p>
<p> struct option {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const char&nbsp;*name;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;has_arg;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*flag;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;val; }; </p>
<p> The meanings of the different fields are:</p>
<dl>
<dt><i>name</i></p>
<dd> is the name of the long option.</p>
<dt><i>has_arg</i></p>
<dd> is: <code>no_argument</code> (or 0) if the option does not take an argument; <code>required_argument</code> (or 1) if the option requires an argument; or <code>optional_argument</code> (or 2) if the option takes an optional argument.</p>
<dt><i>flag</i></p>
<dd> specifies how results are returned for a long option. If <i>flag</i> is NULL, then <code>getopt_long</code>() returns <i>val</i>. (For example, the calling program may set <i>val</i> to the equivalent short option character.) Otherwise, <code>getopt_long</code>() returns 0, and <i>flag</i> points to a variable which is set to <i>val</i> if the option is found, but left unchanged if the option is not found.</p>
<dt><i>val</i></p>
<dd> is the value to return, or to load into the variable pointed to by <i>flag</i>.</dl>
<p> The last element of the array has to be filled with zeros. </p>
<p> If <i>longindex</i> is not NULL, it points to a variable which is set to the index of the long option relative to <i>longopts</i>. </p>
<p> <code>getopt_long_only</code>() is like <code>getopt_long</code>(), but &#8216;-&#8216; as well as &quot;&#8211;&quot; can indicate a long option. If an option that starts with &#8216;-&#8216; (not &quot;&#8211;&quot;) doesn&#8217;t match a long option, but does match a short option, it is parsed as a short option instead.</p>
<h2>RETURN VALUE</h2>
<p> If an option was successfully found, then <code>getopt</code>() returns the option character. If all command-line options have been parsed, then <code>getopt</code>() returns -1. If <code>getopt</code>() encounters an option character that was not in <i>optstring</i>, then &#8216;?&#8217; is returned. If <code>getopt</code>() encounters an option with a missing argument, then the return value depends on the first character in <i>optstring</i>: if it is &#8216;:&#8217;, then &#8216;:&#8217; is returned; otherwise &#8216;?&#8217; is returned. </p>
<p> <code>getopt_long</code>() and <code>getopt_long_only</code>() also return the option character when a short option is recognized. For a long option, they return <i>val</i> if <i>flag</i> is NULL, and 0 otherwise. Error and -1 returns are the same as for <code>getopt</code>(), plus &#8216;?&#8217; for an ambiguous match or an extraneous parameter.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>POSIXLY_CORRECT</code></p>
<dd> If this is set, then option processing stops as soon as a nonoption argument is encountered.</p>
<dt><code>_&lt;PID&gt;_GNU_nonoption_argv_flags_</code></p>
<dd> This variable was used by <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1) 2.0 to communicate to glibc which arguments are the results of wildcard expansion and so should not be considered as options. This behavior was removed in <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1) version 2.01, but the support remains in glibc.</dl>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>getopt</code>(), <code>getopt_long</code>(), <code>getopt_long_only</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:getopt env
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<dl>
<dt><code>getopt</code>():</p>
<dd> POSIX.1-2001, POSIX.1-2008, and POSIX.2, provided the environment variable <code>POSIXLY_CORRECT</code> is set. Otherwise, the elements of <i>argv</i> aren&#8217;t really <i>const</i>, because these functions permute them. Nevertheless, <i>const</i> is used in the prototype to be compatible with other systems.</p>
<dt>
<dd> The use of &#8216;+&#8217; and &#8216;-&#8216; in <i>optstring</i> is a GNU extension.</p>
<dt>
<dd> On some older implementations, <code>getopt</code>() was declared in <i>&lt;stdio.h&gt;</i>. SUSv1 permitted the declaration to appear in either <i>&lt;unistd.h&gt;</i> or <i>&lt;stdio.h&gt;</i>. POSIX.1-1996 marked the use of <i>&lt;stdio.h&gt;</i> for this purpose as LEGACY. POSIX.1-2001 does not require the declaration to appear in <i>&lt;stdio.h&gt;</i>.</p>
<dt><code>getopt_long</code>() and <code>getopt_long_only</code>():</p>
<dd> These functions are GNU extensions.</dl>
<h2>NOTES</h2>
<p> A program that scans multiple argument vectors, or rescans the same vector more than once, and wants to make use of GNU extensions such as &#8216;+&#8217; and &#8216;-&#8216; at the start of <i>optstring</i>, or changes the value of <code>POSIXLY_CORRECT</code> between scans, must reinitialize <code>getopt</code>() by resetting <i>optind</i> to 0, rather than the traditional value of 1. (Resetting to 0 forces the invocation of an internal initialization routine that rechecks <code>POSIXLY_CORRECT</code> and checks for GNU extensions in <i>optstring</i>.)</p>
<h2>EXAMPLES</h2>
<h3>getopt()</h3>
<p> The following trivial example program uses <code>getopt</code>() to handle two program options: <i>-n</i>, with no associated value; and <i>-t val</i>, which expects an associated value. </p>
<p> #include &lt;unistd.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int flags, opt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int nsecs, tfnd; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nsecs&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tfnd&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;((opt&nbsp;=&nbsp;getopt(argc, argv,&nbsp;&quot;nt:&quot;))&nbsp;!=&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(opt)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;n&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;t&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nsecs&nbsp;=&nbsp;atoi(optarg);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tfnd&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:&nbsp;/*&nbsp;&#8216;?&#8217;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;[-t nsecs]&nbsp;[-n]&nbsp;name
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;flags=%d;&nbsp;tfnd=%d;&nbsp;nsecs=%d;&nbsp;optind=%d
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags, tfnd, nsecs, optind); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(optind&nbsp;&gt;=&nbsp;argc)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Expected argument after options
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;name argument&nbsp;=&nbsp;%s
&quot;, argv[optind]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Other code omitted&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h3>getopt_long()</h3>
<p> The following example program illustrates the use of <code>getopt_long</code>() with most of its features. </p>
<p> #include &lt;stdio.h&gt; /* for printf */ #include &lt;stdlib.h&gt; /* for exit */ #include &lt;getopt.h&gt; </p>
<p> int main(int argc, char **argv) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int c;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int digit_optind&nbsp;=&nbsp;0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int this_option_optind&nbsp;=&nbsp;optind&nbsp;?&nbsp;optind : 1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int option_index&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static struct option long_options[]&nbsp;=&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&quot;add&quot;,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;required_argument, 0,&nbsp;<wbr>&nbsp;0&nbsp;},<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&quot;append&quot;,&nbsp;<wbr>&nbsp;no_argument,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0,&nbsp;<wbr>&nbsp;0&nbsp;},<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&quot;delete&quot;,&nbsp;<wbr>&nbsp;required_argument, 0,&nbsp;<wbr>&nbsp;0&nbsp;},<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&quot;verbose&quot;, no_argument,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0,&nbsp;<wbr>&nbsp;0&nbsp;},<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&quot;create&quot;,&nbsp;<wbr>&nbsp;required_argument, 0,&nbsp;&#8216;c&#8217;},<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&quot;file&quot;,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;required_argument, 0,&nbsp;<wbr>&nbsp;0&nbsp;},<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{0,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0,&nbsp;<wbr>&nbsp;0&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;c&nbsp;=&nbsp;getopt_long(argc, argv,&nbsp;&quot;abc:d:012&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long_options,&nbsp;&amp;option_index);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(c&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(c)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case 0:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;option&nbsp;%s&quot;, long_options[option_index].name);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(optarg)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;with arg&nbsp;%s&quot;, optarg);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;0&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;1&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;2&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(digit_optind&nbsp;!=&nbsp;0&nbsp;&amp;&amp;&nbsp;digit_optind&nbsp;!=&nbsp;this_option_optind)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;digits occur in two different argv-elements.
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;digit_optind&nbsp;=&nbsp;this_option_optind;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;option&nbsp;%c
&quot;, c);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;a&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;option a
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;b&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;option b
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;c&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;option c with value&nbsp;&#8216;%s&#8217;
&quot;, optarg);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;d&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;option d with value&nbsp;&#8216;%s&#8217;
&quot;, optarg);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;?&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;??&nbsp;getopt returned character code 0%o&nbsp;??
&quot;, c);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(optind&nbsp;&lt;&nbsp;argc)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;non-option ARGV-elements:&nbsp;&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(optind&nbsp;&lt;&nbsp;argc)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s&nbsp;&quot;, argv[optind++]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1), <code><a href="/docs/linux/man/3-getsubopt/">getsubopt</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
