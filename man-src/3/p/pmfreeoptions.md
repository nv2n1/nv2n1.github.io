---
title: "pmfreeoptions(3)"
name: "pmfreeoptions"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmfreeoptions/"
description: "pmgetopt_r, pmGetOptions, pmGetContextOptions, pmFreeOptions, pmUsageMessage – command line handling for PMAPI tools"
---

<p><code>pmgetopt_r</code>, <code>pmGetOptions</code>, <code>pmGetContextOptions</code>, <code>pmFreeOptions</code>, <code>pmUsageMessage</code> &#8211; command line handling for PMAPI tools</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmgetopt_r(int </code><i>argc</i>, char *const *<i>argv</i>, pmOptions *<i>opts</i>);<br />
 int pmGetOptions(int <i>argc</i>, char *const *<i>argv</i>, pmOptions *<i>opts</i>);<br />
 int pmGetContextOptions(int <i>ctx</i>, pmOptions *<i>opts</i>);<br />
 void pmUsageMessage(pmOptions *<i>opts</i>);<br />
 void pmFreeOptions(pmOptions *<i>opts</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The <code>pmGetOptions</code> function provides command line option processing services for both monitor and collector <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) tools. It is modelled on the thread-safe variants of the GNU <code><a href="/docs/linux/man/3-getopt_long/">getopt_long</a></code>(3) API, and primarily differs in its focus on providing generalised processing for the (de-facto) standard PCP command line options described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). These common options include the host and archive specification, time windows, timezones, sample counts, time intervals, and so on. </p>
<p> The primary interface is <code>pmGetOptions</code>, which should be passed the <i>argc</i> argument count and <i>argv</i> array, as passed to the <i>main()</i> function on program invocation. The final <i>opts</i> argument describes the set of long and short options the tools is prepared to process, and other metadata regarding how those options should be processed. </p>
<p> The <code>pmgetopt_r</code> interface, used internally by <code>pmGetOptions</code>, behaves in a similar fashion, but it does not perform any common option processing. It is more suited to PCP collector processes, whereas PCP monitor tools tend to use <code>pmGetOptions</code>. </p>
<p> The <i>opts</i> argument consists of an array of <i>pmLongOpts</i> entries describing the arguments, as well as the enclosing <i>pmOptions</i> struct, which are defined as follows (internal fields are not presented, for brevity): </p>
<pre>typedef struct {
 const char * long_opt;
 int has_arg;
 int short_opt;
 const char * argname;
 const char * message;
} pmLongOptions;
typedef struct {
 int version;
 int flags;
 const char * short_options;
 pmLongOptions * long_options;
 const char * short_usage;
 pmOptionOverride override;
 int index;
 int optind;
 int opterr;
 int optopt;
 char *optarg;
 /* [internal fields, undocumented] */
 int errors;
 int context; /* PM_CONTEXT_{HOST,ARCHIVE,LOCAL} */
 int nhosts;
 int narchives;
 char ** hosts;
 char ** archives;
 struct timeval start;
 struct timeval finish;
 struct timeval origin;
 struct timeval interval;
 char * align_optarg;
 char * start_optarg;
 char * finish_optarg;
 char * origin_optarg;
 char * guiport_optarg;
 char * timezone;
 int samples;
 int guiport;
 int padding;
 unsigned int guiflag : 1;
 unsigned int tzflag : 1;
 unsigned int nsflag : 1;
 unsigned int Lflag : 1;
 unsigned int zeroes : 28;
} pmOptions;</pre>
<p>The initial <i>flags</i> and <i>version</i> fields describe how the rest of the pmOptions structure is to be interpreted. These fields can be zeroed, specifying a default interpretation. Alternatively, the PMAPI_VERSION macro can be used to specify the API level to use (currently, values of 2 or less are allowed). The <i>flags</i> field can be used to modify option processing behaviour as described in the &#8220;FLAGS VALUES&#8221; section below. </p>
<p> The array of <i>long_options</i> pmLongOpts structures must be terminated by a sentinel and the PMAPI_OPTIONS_END macro can be used to effect this termination. Individual records within the <i>long_options</i> array can be of two types &#8211; options headers, or actual options. An options header is constructed using the PMAPI_OPTIONS_HEADER macro, and is used for usage message option grouping. Free form text can be inserted into the usage message at any point using the PMAPI_OPTIONS_TEXT macro &#8211; this is intended for additional explanatory text covering detailed usage that is beyond the scope of the individual headers or options. Otherwise, the array entry specifies an option. These should be named (<i>long_opt</i>) if a long-option form is allowed, specify whether or not they take an argument (<i>has_arg</i>), specify the single character variant argument (<i>short_opt</i>) if a short-option form is allowed, and finally specify how to present the option in the usage message. This latter component consists of a short, one-word description of the optional argument (<i>argname</i>) and a one-line description of what the command-line option does (<i>message</i>). </p>
<p> The <i>short_usage</i> string is also used only when constructing the usage message. It forms the component of the usage message that follows the program name (i.e. <i>argv[0]</i>). </p>
<p> The optional <i>short_options</i> string is the normal <i>getopt</i> command-line option specification string, using individual characters (those with arguments are designated as such using the &#8216;:&#8217; character) &#8211; as used by all <i>getopt</i> implementations. </p>
<p> A facility is provided to extend the existing set of common options with additional options, as well as to re-task the standard options into non-standard roles for individual tools. The latter is achieved using the <i>override</i> method, which allows a callback function to be provided which will be called on receipt of every argument, prior to common processing. If this callback returns a non-zero value the common processing will be short-circuited for that option, otherwise processing continues. Thus, aach client tool is free to choose exactly which of the standard options they wish to support &#8211; this can be all, some, or none, and no matter what they choose, each tool always has access to the long option parsing capability and the usage message generation facility. </p>
<p> The remaining pmOptions structure fields are filled in as a result of processing the arguments, and are largely self-explanatory. Further discussion of these is deferred to the &#8220;FLAGS VALUES&#8221; section below. The <i>error</i> field contains a count of errors detected during option processing. These can be either usage or runtime errors, as indicated by the <i>flags</i> field (set, and passed out to the caller). Typically, a command line tool will fail to start successfully and will produce an error message (e.g. via <code>pmUsageMessage</code>) if the <i>error</i> field is non-zero at the end of either <code>pmGetOptions</code> or <code>pmGetContextOptions</code>. </p>
<p> Some command line option post-processing can only be performed once the tool has established a PMAPI context via <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3). This processing includes use of context-aware timezones (<code>-z</code>), and time window processing (<code>-A</code>, <code>-O</code>, <code>-S</code>, <code>-T</code>) that may be affected by the timezone, for example. The <code>pmGetContextOptions</code> function is available for such situations, and it completes any remaining processing of <i>opts</i> with respect to the <i>ctx</i> context identifier given. </p>
<p> The <code>pmUsageMessage</code> function generates a usage message for the tool, and included both standard PCP options and custom options for each tool, as specified by the pmLongOptions array. It supports grouping of options (via PMAPI_OPTIONS_HEADER) as well as neat formatting of all options &#8211; short and long &#8211; their arguments, and individual explanatory messages. It will build this usage message using <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3) upon which it will issue a single <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3) before returning to the caller, provided the PM_OPTFLAG_USAGE_ERR flag is set in <i>flags</i>, which will happen automatically during option parsing, when usage errors are detected. </p>
<p> In certain situations, such as recording lists of host specifications or PCP archive paths, the <code>pmGetOptions</code> routine may allocate memory, and store pointers to it within <i>opts</i>. Should a program wish to free this memory before exiting, it can use the <code>pmFreeOptions</code> routine to do so. This is safe to call irrespective of whether memory was allocated dynamically, provided that <i>opts</i> was zeroed initially.</p>
<h2>Flags Values</h2>
<dl>
<dt><code>PM_OPTFLAG_INIT</code></p>
<dd>Used internally within the library to indicate initialisation has been done, so that on subsequent calls it will not be done again.</p>
<dt><code>PM_OPTFLAG_DONE</code></p>
<dd>Used primarily internally within the library to indicate that the final option processing has been completed. This processing involves cross-referencing a number of the options, to check for mutual exclusion, for example. There may be other post-processing at this stage also, provided it does not require a PMAPI context.</p>
<dt><code>PM_OPTFLAG_MULTI</code></p>
<dd>Allow more than one host or set of archives to be specified. The default is to allow one source of metrics only, however some of the more sophisticated tools permit multiple metric sources, each of which is handled within a separate context. See also <code>PM_OPTFLAG_MIXED</code>.</p>
<dt><code>PM_OPTFLAG_USAGE_ERR</code></p>
<dd>Indicates that the library has detected a command-line usage error. This is an error such as when an option requires an argument but none is supplied, or conflicting options are specified (such as <code>-s</code> and <code>-T</code>).</p>
<dt><code>PM_OPTFLAG_RUNTIME_ERR</code></p>
<dd>Indicates that the library has detected an error at run time. This is an error such as failing to retrieve timezone information from <code>pmcd (1)</code> or failing to load an alternate metric namespace from a local file (via the <code>-n</code> option).</p>
<dt><code>PM_OPTFLAG_EXIT</code></p>
<dd>Indicates a suggestion from the library that the tool exit cleanly. This is used when the version number is requested, for example (the <code>-V</code> option and PMOPT_VERSION macro).</p>
<dt><code>PM_OPTFLAG_POSIX</code></p>
<dd>Use strict POSIX command line argument handling. This means options and following arguments will not be reordered, so additional options cannot follow command line arguments. This may be important for tools where the arguments can be negative numbers, for example, as these should not be treated as command line options in this case.</p>
<dt><code>PM_OPTFLAG_MIXED</code></p>
<dd>Allow both live and archive metric sources to be specified. The default is to allow one type of metric context only, however some of the more sophisticated tools permit multiple context types. See also <code>PM_OPTFLAG_MULTI</code>.</p>
<dt><code>PM_OPTFLAG_ENV_ONLY</code></p>
<dd>Many options can be specified through the either the command line or from similarly-named environment variables. This flag disables all argument parsing, and only changes <i>opts</i> based on the environment variables. This may be useful for tools wishing to ensure no command line option conflicts occur between their own set and the standard PCP option set (such as an existing tool, reimplemented using PMAPI services).</p>
<dt><code>PM_OPTFLAG_LONG_ONLY</code></p>
<dd>Only process long options, not short options.</p>
<dt><code>PM_OPTFLAG_BOUNDARIES</code></p>
<dd>The default <code>pmGetOptions</code> behaviour is to parse the time window options (namely, <code>-A</code>, <code>-O</code>, <code>-S</code> and <code>-T</code>), only if one of those options has been specified on the command line. However, this flag can be used (particularly with archive contexts) to find the <i>start</i> and <i>finish</i> times associated with the context(s) even if no time window options were specified. In the case of multiple archives, the time window is defined as the time window spanning all of the archives.</p>
<dt><code>PM_OPTFLAG_STDOUT_TZ</code></p>
<dd>The timezone being used will be reported on the standard output stream during option parsing. The default behaviour is to not report, but simply return timezone information via the <i>timezone</i> (<code>-Z</code>) and <i>tzflag</i> (<code>-z</code>) fields in the <i>opts</i> structure.</p>
<dt><code>PM_OPTFLAG_NOFLUSH</code></p>
<dd>The final <code>pmflush</code> call issued by <code>pmUsageMessage</code> will be skipped if this flag is set. This is useful in situations where the caller wishes to append additional test to the generated usage message before flushing.</p>
<dt><code>PM_OPTFLAG_QUIET</code></p>
<dd>Suppress messages from <code>pmgetopt_r</code> about unrecognised command line options. This is the equivalent to setting the <i>opterr</i> field in the <i>opt</i> parameter (which mimics the <code>getopt</code> variable of the same name).</dl>
<h2>Return Value</h2>
<p>The <code>pmGetOptions</code> function returns either when it detects a command-line option that is not one of the standard PCP set, or when the end of the command line options has been reached (at which point -1 is returned). Both the <code>pmgetopt_r</code> and <code>pmGetOptions</code> routines return control to the caller in the same way that a regular <code>getopt</code> call would, with the return value indicating either the end of all processing (-1), or the single character form of the option currently being processed, or zero for the special long-option-only case. For all option-processing cases, the <i>opts</i> structure is returned containing filled out <i>optarg</i>, <i>opterr</i>, <i>optopt</i>, <i>optind</i>, and <i>index</i> fields as normal (do <code>NOT</code> use the global optarg or optind from your platform C library, these will <code>NOT</code> be modified). </p>
<p> <code>pmGetOptions</code> does not return to the caller when any of the standard PCP options are being processed (although the <i>override</i> mechanism can be used to still detect such options if needed). </p>
<p> The <code>pmGetContextOptions</code> function returns zero on success, or a negative PCP error code on failure. The <i>error</i> field within the <i>opts</i> parameter will also be non-zero in the latter case.</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <code><a href="/docs/linux/man/3-pmgetoptions/">pmGetOptions</a></code>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmstat/">pmstat</a></code>(1), <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3), <code><a href="/docs/linux/man/3-getopt_long/">getopt_long</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3), <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3) and <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3). </p>
