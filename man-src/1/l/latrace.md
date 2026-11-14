---
title: "latrace(1)"
name: "latrace"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latrace/"
description: "latrace – LD_AUDIT 2.4+ libc frontend"
---

<h2 class="name">NAME</h2>
<p> latrace &#8211; LD_AUDIT 2.4+ libc frontend </p>
<h2>SYNOPSIS</h2>
<p> latrace [-snltfvhiBdISbcCyYLpoaNADVTFERq] command [arg &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> The latrace tracer is able to run a command and display its dynamic library calls using a LD_AUDIT libc feature, available from libc version 2.4 onward. It is also capable to measure and display various statistics of dynamic calls. See the section called &#8220;DISCUSSION&#8221; for more details. </p>
<p> If the header file with functions&#8217; declarations is provided, latrace will display functions&#8217;s arguments. The header file file syntax is similar to the C language, with several exceptions See the section called &#8220;HEADERS&#8221; for more details. </p>
<p> The latrace by default fully operates inside of the traced program. However another &quot;pipe mode&quot; is available to move the main work to the tracer &#8211; the latrace binary. See the section called &#8220;PIPE mode&#8221; for more details. </p>
<p> The latrace use is similar to <a href="/docs/linux/man/1-strace/">strace</a>(1) and <a href="/docs/linux/man/1-ltrace/">ltrace</a>(1).</p>
<h2>OPTIONS</h2>
<p> -l, &#8211;libs lib1[,lib2,&#8230;]</p>
<dl>
<dt>
<dd> audit from and to lib1, lib2 &#8230;</dl>
<p> -t, &#8211;libs-to lib1[,lib2,&#8230;]</p>
<dl>
<dt>
<dd> audit to lib1, lib2 &#8230;</dl>
<p> -f, &#8211;libs-from lib1[,lib2,&#8230;]</p>
<dl>
<dt>
<dd> audit from lib1, lib2 &#8230;</dl>
<p> -s, &#8211;sym sym1[,sym2,&#8230;]</p>
<dl>
<dt>
<dd> audit symbols sym1, sym2 &#8230;</dl>
<p> -n, &#8211;sym-omit sym1[,sym2,&#8230;]</p>
<dl>
<dt>
<dd> omit symbols sym1, sym2 &#8230;</dl>
<p> -L, &#8211;lib-subst s1[,s2,&#8230;]</p>
<dl>
<dt>
<dd> objsearch LD_AUDIT interface (See the section called &#8220;OBJSEARCH&#8221;)</dl>
<p> -c, &#8211;counts</p>
<dl>
<dt>
<dd> display statistics counts of symbols &#8211; implies pipe mode (see the section called &#8220;PIPE mode&#8221;) an no symbol output is displayed</dl>
<p> -C, &#8211;sort-counts stat</p>
<dl>
<dt>
<dd> implies -c, plus sort the statistics by stat with following values: time,per,call,ucall,lib,sym (default is call)</dl>
<p> -p, &#8211;pipe</p>
<dl>
<dt>
<dd> use pipe to latrace process to send audit data (see the section called &#8220;PIPE mode&#8221;)</dl>
<p> -N, &#8211;conf</p>
<dl>
<dt>
<dd> config file (see the section called &#8220;CONFIG&#8221;)</dl>
<p> -A, &#8211;enable-args</p>
<dl>
<dt>
<dd> enable arguments output (definitions from /etc/latrace.conf)</dl>
<p> -D, &#8211;detail-args</p>
<dl>
<dt>
<dd> display struct arguments in more detail</dl>
<p> -a, &#8211;args file</p>
<dl>
<dt>
<dd> specify arguments definition file, implies -A (without the default definition file of course)</dl>
<p> -y, &#8211;framesize number</p>
<dl>
<dt>
<dd> framesize for storing the stack before pltexit (default 100)</dl>
<p> -Y, &#8211;no-framesize-check</p>
<dl>
<dt>
<dd> disable framesize check</dl>
<p> -F, &#8211;no-follow-fork</p>
<dl>
<dt>
<dd> dont follow fork calls (childs). This is just supressing the latrace output from new childs. The nature of the <code>LD_AUDIT</code> feature prevents to disable it completely.</dl>
<p> -E, &#8211;no-follow-exec</p>
<dl>
<dt>
<dd> dont follow exec calls</dl>
<p> -S, &#8211;timestamp</p>
<dl>
<dt>
<dd> display timestamp for each symbol</dl>
<p> -b, &#8211;flow-below sym1[,sym2,&#8230;]</p>
<dl>
<dt>
<dd> display flow for sym1, sym2 &#8230;</dl>
<p> -I, &#8211;no-indent-sym</p>
<dl>
<dt>
<dd> do no indent symbols based on the their stack depth</dl>
<p> -i, &#8211;indent-sym indent_size</p>
<dl>
<dt>
<dd> indent size specification in indent_size</dl>
<p> -B, &#8211;braces</p>
<dl>
<dt>
<dd> allways display <i>{</i><i>}</i> for the around the symbol body</dl>
<p> -d, &#8211;demangle</p>
<dl>
<dt>
<dd> C++ demangle symbols on the output</dl>
<p> -T, &#8211;hide-tid</p>
<dl>
<dt>
<dd> dont display thread id</dl>
<p> -o, &#8211;output file</p>
<dl>
<dt>
<dd> store output to file</dl>
<p> -R, &#8211;ctl-config</p>
<dl>
<dt>
<dd> controled config feature</dl>
<p> -q, &#8211;disable</p>
<dl>
<dt>
<dd> run with disabled auditing</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> verbose output</dl>
<p> -V, &#8211;version</p>
<dl>
<dt>
<dd> display version</dl>
<p> -h, &#8211;help</p>
<dl>
<dt>
<dd> display help</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; The simplest way to run latrace is like this: </p>
<dl>
<dt>
<dd>
<pre>
latrace cat
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; To see the argument values specified by default config file run: </p>
<dl>
<dt>
<dd>
<pre>
latrace -A cat
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Same as above but using the pipe mode to get all the end symbols printed: </p>
<dl>
<dt>
<dd>
<pre>
latrace -Ap cat
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; To see the argument values specified by specified config file run: </p>
<dl>
<dt>
<dd>
<pre>
latrace -a latrace.conf cat
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; To get output only for specified symbol (eg. read and write) run: </p>
<dl>
<dt>
<dd>
<pre>
latrace -A -s read,write cat
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; To get flow under the specified symbol (eg. sysconf) run: </p>
<dl>
<dt>
<dd>
<pre>
latrace -b sysconf kill
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; To get output only for specified library (eg. libproc) run: </p>
<dl>
<dt>
<dd>
<pre>
latrace -Al libproc w
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; To get symbol statistics run: </p>
<dl>
<dt>
<dd>
<pre>
latrace -c ls
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; To get symbol statistics sorted by time run: </p>
<dl>
<dt>
<dd>
<pre>
latrace -C time ls
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; To get output stored to the text file run: </p>
<dl>
<dt>
<dd>
<pre>
latrace -o output.latrace ls
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; To change the libkrava1.so dependency to the libkrava2.so run one of these: </p>
<dl>
<dt>
<dd>
<pre>
latrace -L krava1%krava2 ex
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
latrace -L krava1~libkrava2.so ex
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
latrace -L libkrava1.so=libkrava2.so ex
</pre>
</dl>
</dl>
<h2>DISCUSSION</h2>
<h3>NAMES CHECK</h3>
<p> For options <code>&quot;-l -t -f -s -n -b&quot;</code> the <code>*</code> symbol can be used to switch to the substring search. If it is not specified, the exact search for the name is done. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
-s &quot;*krava&quot; checks for symbols with &quot;krava&quot; substring.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
-s &quot;krava&quot;  checks only for &quot;krava&quot; symbol
</pre>
</dl>
<h3>LD_AUDIT</h3>
<p> This is just a brief and vague description of the <code>LD_AUDIT</code> feature. For more information look to <code><a href="/docs/linux/man/7-rtld-audit/">rtld-audit</a>(7)</code> man done by Petr Baudis or study the glibc/latrace source code. Very brief explanation follows. </p>
<p> The libc dynamic linker audit feature allows to trace/audit program&#8217;s symbols/libraries. The feature is enabled by the <code>LD_AUDIT</code> environment variable. This variable must contain path to the audit shared library. This audit library needs to follow specific interface. The interface functions will be then called by the dynamic linker appropriatelly. </p>
<p> The audit library needs to export following symbols (the &quot;la_PLTENTER&quot; and &quot;la_PLTEXIT&quot; names are architecture dependent). </p>
<dl>
<dt>
<dd>
<pre>
&quot;la_activity&quot;
&quot;la_objsearch&quot;
&quot;la_objopen&quot;
&quot;la_preinit&quot;
&quot;la_symbind32&quot;
&quot;la_symbind64&quot;
&quot;la_PLTENTER&quot;
&quot;la_PLTEXIT&quot;
&quot;la_objclose&quot;
</pre>
</dl>
<p> As for the latrace package the audit shared library is called libltaudit.so.</p>
<h3>OBJSEARCH</h3>
<p> The objsearch <code>LD_AUDIT</code> interface provide means for changing traced program shared object names/locations. The -L option argument should have following form: </p>
<p> <i>-L s1[,s2,&#8230;]</i> where sN is <i>src [=%~] dst</i> </p>
<p> The <i>src</i> is the source pattern/name and <i>dst</i> is the destination name/pattern. </p>
<table>
<tr VALIGN=top>
<td>
<p> = </td>
<td>
<p> Comparing src with the library name. If matched, replace the library name with dst.</p>
<dl>
<dt>
<dd>
<pre>
library name         - /lib/krava1.so
src                  - /lib/krava1.so
dst                  - /lib/krava2.so
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
final library name   - /lib/krava2.so
</pre>
</dl>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> % </td>
<td>
<p> Looking for the src in the library name. If found, replace the src with dst part.</p>
<dl>
<dt>
<dd>
<pre>
library name         - /lib/krava1.so
src                  - krava1
dst                  - krava2
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
final library name   - /lib/krava2.so
</pre>
</dl>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ~ </td>
<td>
<p> Looking for the src in the library name. If found, replace the library name with dst.</p>
<dl>
<dt>
<dd>
<pre>
library name         - /lib/krava1.so
src                  - krava1
dst                  - /lib/krava2.so
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
final library name   - /lib/krava2.so
</pre>
</dl>
</td>
</tr>
</table>
<h3>PIPE mode</h3>
<p> The <code>latrace</code> can work in two modes. The first one <code>native</code> does does the output directly in the traced program process. The other one, <code>pipe</code> mode use the IPC fifo mechanism to send the data from the traced process to the latrace process. The latrace process is then responsible for the output. Using the pipe mode you loose the traced program standard output context with printed symbols. </p>
<p> By using the <code>pipe</code> mode, the latrace is not dependent on the trace program usage/manipulation of the standard output descriptor. Also the symbol statistics counts <i>-c, -C options</i> use the <code>pipe</code> mode to transfer symbol information to the latrace binary, and the latrace binary does the counts at the end.</p>
<h3>CONFIG</h3>
<p> The latrace provide possibility to enable/disable some of the options by means of configuration file. Some of the options are linked to the command line arguments some of them are not. When latrace starts the global configuration file is read. This file is usually being placed in here: </p>
<dl>
<dt>
<dd>
<pre>
/etc/latrace.d/latrace.conf
</pre>
</dl>
<p> Having default values read from this file, user can overload any of them by command line options or by supling another config file via <code>-N, &#8211;conf</code> option. </p>
<p> The configuration file syntax is roughly: </p>
<dl>
<dt>
<dd>
<pre>
INCLUDE &lt;anotherconfigfile&gt;
OPTIONS {
        OPTION1 = VALUE
        OPTION2 = YES|NO
        ...
        OPTIONN = VALUE
}
# comment
</pre>
</dl>
<p> <code>Configuration file options</code> </p>
<p> HEADERS = FILE</p>
<dl>
<dt>
<dd> -a, &#8211;args</dl>
<p> INDENT_SYM = VALUE</p>
<dl>
<dt>
<dd> -i, &#8211;indent-sym</dl>
<p> PIPE = BOOL</p>
<dl>
<dt>
<dd> -p, &#8211;pipe</dl>
<p> TIMESTAMP = BOOL</p>
<dl>
<dt>
<dd> -S, &#8211;timestamp</dl>
<p> FRAMESIZE = VALUE</p>
<dl>
<dt>
<dd> -y, &#8211;framesize</dl>
<p> FRAMESIZE_CHECK = BOOL</p>
<dl>
<dt>
<dd> -Y, &#8211;no-framesize-check</dl>
<p> HIDE_TID = BOOL</p>
<dl>
<dt>
<dd> -T, &#8211;hide-tid</dl>
<p> FOLLOW_FORK = BOOL</p>
<dl>
<dt>
<dd> -F, &#8211;no-follow-fork</dl>
<p> FOLLOW_EXEC = BOOL</p>
<dl>
<dt>
<dd> -E, &#8211;no-follow-exec</dl>
<p> DEMANGLE = BOOL</p>
<dl>
<dt>
<dd> -d, &#8211;demangle</dl>
<p> BRACES = BOOL</p>
<dl>
<dt>
<dd> -B, &#8211;braces</dl>
<p> ENABLE_ARGS = BOOL</p>
<dl>
<dt>
<dd> -A, &#8211;enable-args</dl>
<p> DETAIL_ARGS = BOOL</p>
<dl>
<dt>
<dd> -D, &#8211;detail-args</dl>
<p> OUTPUT_TTY = FILE</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; stores tracee terminal output to the file</dl>
</dl>
<p> LIBS = LIB1[,LIB2,&#8230;]</p>
<dl>
<dt>
<dd> -l, &#8211;libs</dl>
<p> LIBS_TO = LIB1[,LIB2,&#8230;]</p>
<dl>
<dt>
<dd> -t, &#8211;libs-to</dl>
<p> LIBS_FROM = LIB1[,LIB2,&#8230;]</p>
<dl>
<dt>
<dd> -f, &#8211;libs-from</dl>
<p> SYM = SYM1[,SYM2,&#8230;]</p>
<dl>
<dt>
<dd> -s, &#8211;sym</dl>
<p> SYM_OMIT = SYM1[,SYM2,&#8230;]</p>
<dl>
<dt>
<dd> -n, &#8211;sym-omit</dl>
<p> SYM_BELOW = SYM1[,SYM2,&#8230;]</p>
<dl>
<dt>
<dd> -b, &#8211;flow-below</dl>
<p> SYM_NOEXIT = SYM1[,SYM2,&#8230;]</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; symbols which do no run exit callback (plt_exit)</dl>
</dl>
<p> ARGS_STRING_POINTER_LENGTH = BOOL</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; function arguments &#8211; display string length and pointer value</dl>
</dl>
<h3>HEADERS</h3>
<p> The latrace header file allows user to define symbols as an classic C functions with arguments. Argument names will be displayed together with values as the latrace output. The more arguments are defined, the more performance and memory penalties should be expected. </p>
<p> The package is delivered with several predefined header files for the most commonly used functions. List of the glibc header files used follows (the list mostly follows the ltrace header files list, and author is willing to update it according to the needs) </p>
<dl>
<dt>
<dd>
<pre>
ctype.h dirent.h dlfcn.h fcntl.h getopt.h inet.h ioctl.h
libintl.h libio.h locale.h misc.h mman.h ncurses.h netdb.h
pthread.h pwd.h resource.h signal.h socket.h stat.h stdio.h
stdlib.h string.h syslog.h term.h termios.h time.h typedefs.h
unistd.h utmp.h wait.h
</pre>
</dl>
<p> The latrace header files are usually stored under directory: </p>
<dl>
<dt>
<dd>
<pre>
/etc/latrace.d/headers/
</pre>
</dl>
<p> User can specify single header file using command line option or configuration file. This file then can include other needed headers. As already mentioned, the latrace config file syntax lightly follows the C language syntax. Following part describes the latrace config file language. </p>
<dl>
<dt>
<dd> &bull; Several <code>POD types</code> (plain old data), are hardcoded in latrace. Size of those arguments is determined by the sizeof macro. The list follows. </p>
<dl>
<dt>
<dd>
<pre><code>
void char u_char short u_short int u_int long u_long
    llong u_llong #(long long)float double
</code></pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; The <code>typedef</code> keyword allows to specify new type based on the already existing one (POD or typedefed). Eventhough there&#8217;s a way for multiple pointer layers in the type definition (*), only one is taken. </p>
<dl>
<dt>
<dd>
typedef base_type new_type;<br />
typedef base_type *new_type;<br />
typedef base_type **new_type;
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>Comments</code> follow the C style /\* \*/ logic. </p>
<p> /\* comments \*/</dl>
<dl>
<dt>
<dd> &bull; The <code>include</code> keyword allows to include another config file. </p>
<p> #include &quot;filename&quot;</dl>
<dl>
<dt>
<dd> &bull; The <code>struct</code> keyword allows to define the structure. The syntax folows following grammar rules. </p>
<dl>
<dt>
<dd>
START::struct NAME {<br />
    STRUCT_DEF<br />
};<br />
STRUCT_DEF::DEF | EMPTY DEF::NAME NAME |<br />
    NAME &#8216;*&#8217; NAME |<br />
    struct NAME NAME |<br />
    struct NAME &#8216;*&#8217; NAME<br />
            NAME::[-0 &#8211; 9a &#8211; zA &#8211; Z_] +
</dl>
</dl>
<dl>
<dt>
<dd> &bull; The <code>function</code> definition follows following syntax (DEF and NAME are the same as for struct definition). </p>
<dl>
<dt>
<dd>
<pre>
START::         DEF '(' ARGS ')' ';'
ARGS::          ARGS ',' DEF | DEF | EMPTY
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; The <code>enum</code> definition follows following syntax (NAME is same as for struct definition). </p>
<dl>
<dt>
<dd>
<pre>
START::         ENUM NAME '{' ENUM_DEF '}' ';'
ENUM_DEF::      ENUM_DEF ',' ENUM_ELEM | ENUM_ELEM
ENUM_ELEM::     NAME '=' NAME | NAME
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Example of a simple latrace config file. </p>
<dl>
<dt>
<dd>
<pre><code>
-- -[cut here]-- -- -- -- -- -- -- -- -- -- -- -- -- -- -enum krava {
    krava1 = 1,
    krava2,
    krava3 = 100
};
#include "krava.conf"
typedef u_int pid_t;
struct ex_st {
    pid_t p;
    int cnt;
    char *name;
};
int f1(pid_t p, struct ex_st *k);
int f2(char *name, struct ex_st k, int k = krava);
struct ex_st *f3(pid_t *p, struct ex_st k);
-- -[cut here]-- -- -- -- -- -- -- -- -- -- -- -- -- -- -
</code></pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Arrays are not supported yet, so there&#8217;s no way to define some structures. For such a structures use void* type where the structure argu- ment is passed by pointer. If it is passed by value, there&#8217;s no workaround so far (aside from filling the structure body with POD types up to the actual length of the structure :).</dl>
<dl>
<dt>
<dd> &bull; Variable argument lists (va_list/&#8230;) are not supported yet. The function definition needs to stop before the first variable argument list argument.</dl>
<h2>PORTS</h2>
<p> The latrace should work on any glibc system with LD_AUDIT support. However arguments details are architecture specific and need special support inside latrace itself. </p>
<p> Author is willing to port the latrace to any architecture, as long as he got an access to corresponding system. Currently functional ports are: </p>
<table>
<tr VALIGN=top>
<td>
<p> <code>x86</code> </td>
<td>
<p> ok
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>x86_64</code> </td>
<td>
<p> ok
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>arm</code> </td>
<td>
<p> ok
</td>
</tr>
</table>
<h2>BUGS</h2>
<p> MANY, plz report bugs to &lt;m[blue]<code>latrace [at] lists.fedorahosted.org</code>m[]<font SIZE="-2">[1]</font>&gt; or &lt;m[blue]<code>olsajiri [at] gmail.com</code>m[]<font SIZE="-2">[2]</font>&gt;. </p>
<p> You can also visit the m[blue]<code><a rel="nofollow" href="http://people.redhat.com/jolsa/latrace/">http://people.redhat.com/jolsa/latrace/</a></code>m[] page to see the latest release notes information. </p>
<p> LD_AUDIT related glibc bugs: </p>
<dl>
<dt>
<dd> &bull; <code>Bug 7055 (no longer reproducible)</code></dl>
<dl>
<dt>
<dd> &bull; <code>Bug 9893 (FIXED in 2.10)</code></dl>
<dl>
<dt>
<dd> &bull; <code>Bug 3924 (FIXED in 2.7-2)</code></dl>
<h2>AUTHOR</h2>
<p> Jiri Olsa &lt;m[blue]<code>olsajiri [at] gmail.com</code>m[]<font SIZE="-2">[2]</font>&gt;</p>
<h2>CONTRIBUTORS</h2>
<dl>
<dt>
<dd> &bull; Nix &lt;m[blue]<code>nix [at] esperi.org.uk</code>m[]<font SIZE="-2">[3]</font>&gt;</dl>
<dl>
<dt>
<dd> &bull; Akos Pasztory &lt;m[blue]<code>akos.pasztory [at] gmail.com</code>m[]<font SIZE="-2">[4]</font>&gt;</dl>
<dl>
<dt>
<dd> &bull; Artur Skawina &lt;m[blue]<code>art.08.09 [at] gmail.com</code>m[]<font SIZE="-2">[5]</font>&gt;</dl>
<dl>
<dt>
<dd> &bull; Dr. David Alan Gilbert &lt;m[blue]<code>david.gilbert [at] linaro.org</code>m[]<font SIZE="-2">[6]</font>&gt;</dl>
<dl>
<dt>
<dd> &bull; Sebastian Pipping &lt;m[blue]<code>sping [at] gentoo.org</code>m[]<font SIZE="-2">[7]</font>&gt;</dl>
<h2>LICENSE</h2>
<p> This is free software, distributed under the <code>GPLv3</code> license.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-strace/">strace</a>(1), <a href="/docs/linux/man/1-ltrace/">ltrace</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> <code>Jiri Olsa</code> &lt;olsajiri [at] gmail.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> latrace [at] lists.fedorahosted.org</p>
<dl>
<dt>
<dd> mailto:latrace [at] lists.fedorahosted.org</dl>
<dt> 2.</p>
<dd> olsajiri [at] gmail.com</p>
<dl>
<dt>
<dd> mailto:olsajiri [at] gmail.com</dl>
<dt> 3.</p>
<dd> nix [at] esperi.org.uk</p>
<dl>
<dt>
<dd> mailto:nix [at] esperi.org.uk</dl>
<dt> 4.</p>
<dd> akos.pasztory [at] gmail.com</p>
<dl>
<dt>
<dd> mailto:akos.pasztory [at] gmail.com</dl>
<dt> 5.</p>
<dd> art.08.09 [at] gmail.com</p>
<dl>
<dt>
<dd> mailto:art.08.09 [at] gmail.com</dl>
<dt> 6.</p>
<dd> david.gilbert [at] linaro.org</p>
<dl>
<dt>
<dd> mailto:david.gilbert [at] linaro.org</dl>
<dt> 7.</p>
<dd> sping [at] gentoo.org</p>
<dl>
<dt>
<dd> mailto:sping [at] gentoo.org</dl>
</dl>
<h2>Index</h2>
