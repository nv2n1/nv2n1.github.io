---
title: "lttng-ust(3)"
name: "lttng-ust"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lttng-ust/"
---

<h2 class="name">NAME</h2>
 

 lttng-ust --- Linux Trace Toolkit Next Generation User-Space Tracer 2.x

<h2>SYNOPSIS</h2>

 

 

 <pre>
Link liblttng-ust.so with applications, following this manpage.
</pre>

<h2>DESCRIPTION</h2>

 

 

 LTTng-UST, the Linux Trace Toolkit Next Generation Userspace Tracer, is a port of the low-overhead tracing capabilities of the LTTng kernel tracer to user-space. The library &quot;liblttng-ust&quot; enables tracing of applications and libraries. 

<h2>USAGE</h2>

 

 The simple way to generate the lttng-ust tracepoint probes is to use the <a HREF="/docs/linux/man/1-lttng-gen-tp/">lttng-gen-tp</a>(1) tool. See the <a HREF="/docs/linux/man/1-lttng-gen-tp/">lttng-gen-tp</a>(1) manpage for explanation. 

 

 

 Here is the way to do it manually, without the <a HREF="/docs/linux/man/1-lttng-gen-tp/">lttng-gen-tp</a>(1) helper script, through an example: 

 

<h2>CREATION OF TRACEPOINT PROVIDER</h2>

 

 <pre><code>
To create a tracepoint provider, within a build tree similar to
examples/easy-ust installed with lttng-ust documentation, see
sample_component_provider.h for the general layout. You will need to
define TRACEPOINT_CREATE_PROBES before including your tracepoint
provider probe in one source file of your application. See tp.c from
easy-ust for an example of a tracepoint probe source file. This manpage
will focus on the various types that can be recorded into a trace
event:
TRACEPOINT_EVENT(
        /*
         * provider name, not a variable but a string starting with a
         * letter and containing either letters, numbers or underscores.
         * Needs to be the same as TRACEPOINT_PROVIDER. Needs to
         * follow the namespacing guide-lines in lttng/tracepoint.h:
         *
         * Must be included before include tracepoint provider
         * ex.: project_event
         * ex.: project_component_event
         *
         * Optional company name goes here
         *  ex.: com_efficios_project_component_event
         *
         * In this example, "sample" is the project, and "component" is the
         * component.
         */
        sample_component,
        /*
         * tracepoint name, same format as sample provider. Does not
         * need to be declared before. in this case the name is
         * "message"
         */
        message,
        /*
         * TP_ARGS macro contains the arguments passed for the tracepoint
         * it is in the following format
         *            TP_ARGS(type1, name1, type2, name2, ... type10,
                                 name10)
         * where there can be from zero to ten elements.
         * typeN is the datatype, such as int, struct or double **.
         * name is the variable name (in "int myInt" the name would be
         * myint)
         *            TP_ARGS() is valid to mean no arguments
         *            TP_ARGS(void) is valid too
         */
        TP_ARGS(int, anint, int, netint, long *, values,
                 char *, text, size_t, textlen,
                 double, doublearg, float, floatarg),
        /*
         * TP_FIELDS describes how to write the fields of the trace event.
         * You can put expressions in the "argument expression" area,
         * typically using the input arguments from TP_ARGS.
         */
        TP_FIELDS(
                /*
                 * ctf_integer: standard integer field.
                 * args: (type, field name, argument expression)
                 */
                ctf_integer(int, intfield, anint)
                ctf_integer(long, longfield, anint)
                /*
                 * ctf_integer_hex: integer field printed as hexadecimal.
                 * args: (type, field name, argument expression)
                 */
                ctf_integer_hex(int, intfield2, anint)
                /*
                 * ctf_integer_network: integer field in network byte
                 * order. (_hex: printed as hexadecimal too)
                 * args: (type, field name, argument expression)
                 */
                ctf_integer_network(int, netintfield, netint)
                ctf_integer_network_hex(int, netintfieldhex, netint)
                /*
                 * ctf_array: a statically-sized array.
                 * args: (type, field name, argument expression, value)
                 */
                ctf_array(long, arrfield1, values, 3)
                /*
                 * ctf_array_text: a statically-sized array, printed as
                 * a string. No need to be terminated by a null
                 * character.
                 * Behavior is undefined if "text" argument is NULL.
                 */
                ctf_array_text(char, arrfield2, text, 10)
                /*
                 * ctf_sequence: a dynamically-sized array.
                 * args: (type, field name, argument expression,
                 *      type of length expression, length expression)
                 * The "type of length expression" needs to be an
                 * unsigned type. As a reminder, "unsigned char" should
                 * be preferred to "char", since the signedness of
                 * "char" is implementation-defined.
                 * Behavior is undefined if "text" argument is NULL.
                 */
                ctf_sequence(char, seqfield1, text,
                             size_t, textlen)
                /*
                 * ctf_sequence_text: a dynamically-sized array, printed
                 * as string. No need to be null-terminated.
                 * Behavior is undefined if "text" argument is NULL.
                 */
                ctf_sequence_text(char, seqfield2, text,
                             size_t, textlen)
                /*
                 * ctf_string: null-terminated string.
                 * args: (field name, argument expression)
                 * Behavior is undefined if "text" argument is NULL.
                 */
                ctf_string(stringfield, text)
                /*
                 * ctf_float: floating-point number.
                 * args: (type, field name, argument expression)
                 */
                ctf_float(float, floatfield, floatarg)
                ctf_float(double, doublefield, doublearg)
        )
)
There can be an arbitrary number of tracepoint providers within an
application, but they must each have their own provider name. Duplicate
provider names are not allowed.
</code></pre> 

<h2>ASSIGNING LOGLEVEL TO EVENTS</h2>

 

 
Optionally, a loglevel can be assigned to a TRACEPOINT_EVENT using the
following construct:
        TRACEPOINT_LOGLEVEL(&lt; [com_company_]project[_component] &gt;,
                &lt; event &gt;, &lt; loglevel_name &gt;)
The first field is the provider name, the second field is the name of
the tracepoint, and the third field is the loglevel name.  A
TRACEPOINT_EVENT should be declared prior to the the TRACEPOINT_LOGLEVEL
for a given tracepoint name. The TRACEPOINT_PROVIDER must be already
declared before declaring a TRACEPOINT_LOGLEVEL.
The loglevels go from 0 to 14. Higher numbers imply the most verbosity
(higher event throughput expected.
Loglevels 0 through 6, and loglevel 14, match syslog(3) loglevels
semantic. Loglevels 7 through 13 offer more fine-grained selection of
debug information.
   TRACE_EMERG           0
   system is unusable
   TRACE_ALERT           1
   action must be taken immediately
   TRACE_CRIT            2
   critical conditions
   TRACE_ERR             3
   error conditions
   TRACE_WARNING         4
   warning conditions
   TRACE_NOTICE          5
   normal, but significant, condition
   TRACE_INFO            6
   informational message
   TRACE_DEBUG_SYSTEM    7
   debug information with system-level scope (set of programs)
   TRACE_DEBUG_PROGRAM   8
   debug information with program-level scope (set of processes)
   TRACE_DEBUG_PROCESS   9
   debug information with process-level scope (set of modules)
   TRACE_DEBUG_MODULE    10
   debug information with module (executable/library) scope (set of
   units)
   TRACE_DEBUG_UNIT      11
   debug information with compilation unit scope (set of functions)
   TRACE_DEBUG_FUNCTION  12
   debug information with function-level scope
   TRACE_DEBUG_LINE      13
   debug information with line-level scope (TRACEPOINT_EVENT default)
   TRACE_DEBUG           14
   debug-level message (trace_printf default)
See lttng(1) for information on how to use LTTng-UST loglevels.
 

<h2>ADDING TRACEPOINTS TO YOUR CODE</h2>

 

 <pre>
Include the provider header in each C files you plan to instrument,
following the building/linking directives in the next section.
For instance, add within a function:
                tracepoint(ust_tests_hello, tptest, i, netint, values,
                        text, strlen(text), dbl, flt);
As a call to the tracepoint. It will only be activated when requested by
<a HREF="//www.systutorials.com/docs/linux/man/1-lttng/">lttng</a>(1) through <a HREF="//www.systutorials.com/docs/linux/man/8-lttng-sessiond/">lttng-sessiond</a>(8).
Even though LTTng-UST supports tracepoint() call site duplicates having
the same provider and event name, it is recommended to use a
provider event name pair only once within the source code to help
map events back to their call sites when analyzing the trace.
</pre> 

<h2>BUILDING/LINKING THE TRACEPOINT PROVIDER</h2>

 

 <pre><code>
There are 2 ways to compile the Tracepoint Provider with the
application: either statically or dynamically. Please follow
carefully:
  1.1) Compile the Tracepoint provider with the application, either
       directly or through a static library (.a):
    - Into exactly one object of your application: define
      "TRACEPOINT_DEFINE" and include the tracepoint provider.
    - Use "-I." for the compilation unit containing the tracepoint
      provider include (e.g. tp.c).
    - Link application with "-ldl".
    - If building the provider directly into the application,
      link the application with "-llttng-ust".
    - If building a static library for the provider, link the static
      library with "-llttng-ust".
    - Include the tracepoint provider header into all C files using
      the provider.
    - Examples:
      - doc/examples/easy-ust/   sample.c sample_component_provider.h tp.c
        Makefile
      - doc/examples/hello-static-lib/   hello.c tp.c ust_test_hello.h Makefile
  2) Compile the Tracepoint Provider separately from the application,
     using dynamic linking:
    - Into exactly one object of your application: define
      "TRACEPOINT_DEFINE" _and_ also define
      "TRACEPOINT_PROBE_DYNAMIC_LINKAGE", then include the tracepoint
      provider header.
    - Include the tracepoint provider header into all instrumented C
      files that use the provider.
    - Compile the tracepoint provider with "-I.".
    - Link the tracepoint provider with "-llttng-ust".
    - Link application with "-ldl".
    - Set a LD_PRELOAD environment to preload the tracepoint provider
      shared object before starting the application when tracing is
      needed. Another way is to dlopen the tracepoint probe when needed
      by the application.
    - Example:
      - doc/examples/demo   demo.c  tp*.c ust_tests_demo*.h demo-trace Makefile
  - Note about dlclose() usage: it is not safe to use dlclose on a
    provider shared object that is being actively used for tracing due
    to a lack of reference counting from lttng-ust to the used shared
    object.
  - Enable instrumentation and control tracing with the "lttng" command
    from lttng-tools. See lttng-tools doc/quickstart.txt.
  - Note for C++ support: although an application instrumented with
    tracepoints can be compiled with g++, tracepoint probes should be
    compiled with gcc (only tested with gcc so far).
</code></pre> 

<h2>USING LTTNG UST WITH DAEMONS</h2>

 

 <pre>
Some extra care is needed when using liblttng-ust with daemon
applications that call fork(), clone(), or BSD rfork() without a
following exec() family system call. The library &quot;liblttng-ust-fork.so&quot;
needs to be preloaded for the application (launch with e.g.
LD_PRELOAD=liblttng-ust-fork.so appname).
</pre> 

<h2>CONTEXT</h2>

 

 

 Context information can be prepended by the tracer before each, or some, events. The following context information is supported by LTTng-UST: 

 

 

<dl>
<dt>vtid
<dd> Virtual thread ID: thread ID as seen from the point of view of the process namespace.</dl>
 

 

 

<dl>
<dt>vpid
<dd> Virtual process ID: process ID as seen from the point of view of the process namespace.</dl>
 

 

 

<dl>
<dt>ip
<dd> Instruction pointer: Enables recording of the exact location where a tracepoint was emitted. Can be used to reverse-lookup the source location that caused the event to be emitted.</dl>
 

 

 

<dl>
<dt>procname
<dd> Thread name, as set by exec() or prctl(). It is recommended that programs set their thread name with prctl() before hitting the first tracepoint for that thread.</dl>
 

 

 

<dl>
<dt>pthread_id
<dd> Pthread identifier. Can be used on architectures where pthread_t maps nicely to an unsigned long type.</dl>
 

 

<h2>BASE ADDRESS STATEDUMP (Experimental feature)</h2>

 

 

 Warning: This is an experimental feature known to cause deadlocks when the traced application uses fork, clone or daemon. Only use it for debugging and testing. Do NOT use it in production. 

 If an application that uses liblttng-ust.so becomes part of a session, information about its currently loaded shared objects will be traced to the session at session-enable time. To record this information, the following event needs to be enabled: 

<dl>
<dt>ust_baddr_statedump:soinfo
<dd> This event is used to trace a currently loaded shared object. The base address (where the dynamic linker has placed the shared object) is recorded in the &quot;baddr&quot; field. The path to the shared object gets recorded in the &quot;sopath&quot; field (as string). The file size of the loaded object (in bytes) is recorded to the &quot;size&quot; field and its time of last modification (in seconds since Epoch) is recorded in the &quot;mtime&quot; field.</dl>
 

 If the event above is enabled, a series of &quot;ust_baddr_statedump:soinfo&quot; events is recorded at session-enable time. It represents the state of currently loaded shared objects for the traced process. If this information gets combined with the <a HREF="/docs/linux/man/3-lttng-ust-dl/">lttng-ust-dl</a>(3) instrumentation, all aspects of dynamic loading that are relevant for symbol and line number lookup are traced by LTTng. 

<h2>ENVIRONMENT VARIABLES</h2>

 

 

<dl>
<dt>LTTNG_UST_DEBUG
<dd> Activate liblttng-ust debug output.</dl>
 

<dl>
<dt>LTTNG_UST_REGISTER_TIMEOUT
<dd> The environment variable &quot;LTTNG_UST_REGISTER_TIMEOUT&quot; can be used to specify how long the applications should wait for sessiond &quot;registration done&quot; command before proceeding to execute the main program. The default is 3000ms (3 seconds). The timeout value is specified in milliseconds. The value 0 means &quot;don't wait&quot;. The value -1 means &quot;wait forever&quot;. Setting this environment variable to 0 is recommended for applications with time constraints on the process startup time.</dl>
 

<dl>
<dt>LTTNG_UST_WITH_EXPERIMENTAL_BADDR_STATEDUMP
<dd> Experimentally allow liblttng-ust to perform a base-address statedump on session-enable.</dl>
 

 

<h2>SEE ALSO</h2>

 

 

 <a HREF="/docs/linux/man/1-lttng-gen-tp/">lttng-gen-tp</a>(1), <a HREF="/docs/linux/man/1-lttng/">lttng</a>(1), <a HREF="/docs/linux/man/1-babeltrace/">babeltrace</a>(1), <a HREF="/docs/linux/man/3-lttng-ust-cyg-profile/">lttng-ust-cyg-profile</a>(3), <a HREF="/docs/linux/man/3-lttng-ust-dl/">lttng-ust-dl</a>(3), <a HREF="/docs/linux/man/8-lttng-sessiond/">lttng-sessiond</a>(8) 

 

<h2>COMPATIBILITY</h2>

 

 

 Older lttng-ust libraries reject more recent, and incompatible, probe providers. Newer lttng-ust libraries accept older probe providers, even though some newer features might not be available with those providers. 

 

<h2>BUGS</h2>

 

 

 LTTng-UST 2.0 and 2.1 lttng-ust libraries do not check for probe provider version compatibility. This can lead to out-of-bound accesses when using a more recent probe provider with an older lttng-ust library. These error only trigger when tracing is active. This issue has been fixed in LTTng-UST 2.2. 

 If you encounter any issues or usability problem, please report it on our mailing list &lt;lttng-dev [at] lists.lttng.org&gt; to help improve this project.

<h2>CREDITS</h2>

 

 liblttng-ust is distributed under the GNU Lesser General Public License version 2.1. The headers are distributed under the MIT license. 

 See <a rel="nofollow" HREF="http://lttng.org">http://lttng.org</a> for more information on the LTTng project. 

 Mailing list for support and development: &lt;lttng-dev [at] lists.lttng.org&gt;. 

 You can find us on IRC server irc.oftc.net (OFTC) in #lttng. 

<h2>THANKS</h2>

 

 Thanks to Ericsson for funding this work, providing real-life use-cases, and testing. 

 Special thanks to Michel Dagenais and the DORSAL laboratory at Polytechnique de Montreal for the LTTng journey. 

<h2>AUTHORS</h2>

 

 

 liblttng-ust was originally written by Mathieu Desnoyers, with additional contributions from various other people. It is currently maintained by Mathieu Desnoyers &lt;mathieu.desnoyers [at] efficios.com&gt;. 

 

<h2>Index</h2>


