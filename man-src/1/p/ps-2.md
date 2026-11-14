---
title: "ps-2(1)"
name: "ps-2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ps-2/"
description: "ps – report a snapshot of the current processes."
---

<p>ps &#8211; report a snapshot of the current processes. </p>
<h2>Synopsis</h2>
<p><code>ps</code> [,<i>options/</i>]</p>
<h2>Description</h2>
<p><code>ps</code> displays information about a selection of the active processes. If you want a repetitive update of the selection and the displayed information, use <code>top</code> instead. </p>
<p> This version of <code>ps</code> accepts several kinds of options:</p>
<dl>
<dd>
<dt>1</p>
<dd>UNIX options, which may be grouped and must be preceded by a dash.</p>
<dt>2</p>
<dd>BSD options, which may be grouped and must not be used with a dash.</p>
<dt>3</p>
<dd>GNU long options, which are preceded by two dashes.</dl>
<p> Options of different types may be freely mixed, but conflicts can appear. There are some synonymous options, which are functionally identical, due to the many standards and <code>ps</code> implementations that this <code>ps</code> is compatible with. </p>
<p> Note that <code>ps -aux</code> is distinct from <code>ps aux</code>. The POSIX and UNIX standards require that <code>ps -aux</code> print all processes owned by a user named <i>x</i>, as well as printing all processes that would be selected by the <code>-a</code> option. If the user named <i>x</i> does not exist, this <code>ps</code> may interpret the command as <code>ps aux</code> instead and print a warning. This behavior is intended to aid in transitioning old scripts and habits. It is fragile, subject to change, and thus should not be relied upon. </p>
<p> By default, <code>ps</code> selects all processes with the same effective user ID (euid=EUID) as the current user and associated with the same terminal as the invoker. It displays the process ID (pid=PID), the terminal associated with the process (tname=TTY), the cumulated CPU time in [DD-]hh:mm:ss format (time=TIME), and the executable name (ucmd=CMD). Output is unsorted by default. </p>
<p> The use of BSD-style options will add process state (stat=STAT) to the default display and show the command args (args=COMMAND) instead of the executable name. You can override this with the <code>PS_FORMAT</code> environment variable. The use of BSD-style options will also change the process selection to include processes on other terminals (TTYs) that are owned by you; alternately, this may be described as setting the selection to be the set of all processes filtered to exclude processes owned by other users or not on a terminal. These effects are not considered when options are described as being &quot;identical&quot; below, so <code>-M</code> will be considered identical to <code>Z</code> and so on. </p>
<p> Except as described below, process selection options are additive. The default selection is discarded, and then the selected processes are added to the set of processes to be displayed. A process will thus be shown if it meets any of the given selection criteria.</p>
<h2>Examples</h2>
<dl>
<dt>To see every process on the system using standard syntax:</p>
<dd><code>ps -e</code><br />
 <code>ps -ef</code><br />
 <code>ps -eF</code><br />
 <code>ps -ely</code></p>
<dt>To see every process on the system using BSD syntax:</p>
<dd><code>ps ax</code><br />
 <code>ps axu</code></p>
<dt>To print a process tree:</p>
<dd><code>ps -ejH</code><br />
 <code>ps axjf</code></p>
<dt>To get info about threads:</p>
<dd><code>ps -eLf</code><br />
 <code>ps axms</code></p>
<dt>To get security info:</p>
<dd><code>ps -eo euser,ruser,suser,fuser,f,comm,label</code><br />
 <code>ps axZ</code><br />
 <code>ps -eM</code></p>
<dt>To see every process running as root (real&nbsp;&amp;&nbsp;effective ID) in user format:</p>
<dd><code>ps -U root -u root u</code></p>
<dt>To see every process with a user-defined format:</p>
<dd><code>ps -eo pid,tid,class,rtprio,ni,pri,psr,pcpu,stat,wchan:14,comm</code><br />
 <code>ps axo stat,euid,ruid,tty,tpgid,sess,pgrp,ppid,pid,pcpu,comm</code><br />
 <code>ps -Ao pid,tt,user,fname,tmout,f,wchan</code></p>
<dt>Print only the process IDs of syslogd:</p>
<dd><code>ps -C syslogd -o pid=</code></p>
<dt>Print only the name of PID 42:</p>
<dd><code>ps -q 42 -o comm=</code></dl>
<h2>Simple Process Selection</h2>
<dl>
<dt><code>a</code></p>
<dd>Lift the BSD-style &quot;only yourself&quot; restriction, which is imposed upon the set of all processes when some BSD-style (without &quot;-&quot;) options are used or when the <code>ps</code> personality setting is BSD-like. The set of processes selected in this manner is in addition to the set of processes selected by other means. An alternate description is that this option causes <code>ps</code> to list all processes with a terminal (tty), or to list all processes when used together with the <code>x</code> option.</p>
<dt><code>-A</code></p>
<dd>Select all processes. Identical to <code>-e</code>.</p>
<dt><code>-a</code></p>
<dd>Select all processes except both session leaders (see <i><a href="/docs/linux/man/2-getsid/">getsid</a></i>(2)) and processes not associated with a terminal.</p>
<dt><code>-d</code></p>
<dd>Select all processes except session leaders.</p>
<dt><code>&#8211;deselect</code></p>
<dd>Select all processes except those that fulfill the specified conditions (negates the selection). Identical to <code>-N</code>.</p>
<dt><code>-e</code></p>
<dd>Select all processes. Identical to <code>-A</code>.</p>
<dt><code>g</code></p>
<dd>Really all, even session leaders. This flag is obsolete and may be discontinued in a future release. It is normally implied by the <code>a</code> flag, and is only useful when operating in the sunos4 personality.</p>
<dt><code>-N</code></p>
<dd>Select all processes except those that fulfill the specified conditions (negates the selection). Identical to <code>&#8211;deselect</code>.</p>
<dt><code>T</code></p>
<dd>Select all processes associated with this terminal. Identical to the <code>t</code> option without any argument.</p>
<dt><code>r</code></p>
<dd>Restrict the selection to only running processes.</p>
<dt><code>x</code></p>
<dd>Lift the BSD-style &quot;must have a tty&quot; restriction, which is imposed upon the set of all processes when some BSD-style (without &quot;-&quot;) options are used or when the <code>ps</code> personality setting is BSD-like. The set of processes selected in this manner is in addition to the set of processes selected by other means. An alternate description is that this option causes <code>ps</code> to list all processes owned by you (same EUID as <code>ps</code>), or to list all processes when used together with the <code>a</code> option.</dl>
<h2>Process Selection By List</h2>
<p>These options accept a single argument in the form of a blank-separated or comma-separated list. They can be used multiple times. For example: <code>ps -p 1 2 -p 3,4</code></p>
<dl>
<dt>&#8211;<i>123</i></p>
<dd>Identical to <code>&#8211;pid&nbsp;</code><i>123</i>.</p>
<dt><i>123</i></p>
<dd>Identical to <code>&#8211;pid&nbsp;</code><i>123</i>.</p>
<dt><code>-C</code><i>&nbsp;cmdlist</i></p>
<dd>Select by command name. This selects the processes whose executable name is given in <i>cmdlist</i>. NOTE: The command name is not the same as the command line. Previous versions of procps and the kernel truncated this command name to 15 characters. This limitation is no longer present in both. If you depended on matching only 15 characters, you may no longer get a match.</p>
<dt><code>-G</code><i>&nbsp;grplist</i></p>
<dd>Select by real group ID (RGID) or name. This selects the processes whose real group name or ID is in the <i>grplist</i> list. The real group ID identifies the group of the user who created the process, see <i><a href="/docs/linux/man/2-getgid/">getgid</a></i>(2).</p>
<dt><code>-g</code><i>&nbsp;grplist</i></p>
<dd>Select by session OR by effective group name. Selection by session is specified by many standards, but selection by effective group is the logical behavior that several other operating systems use. This <code>ps</code> will select by session when the list is completely numeric (as sessions are). Group ID numbers will work only when some group names are also specified. See the <code>-s</code> and <code>&#8211;group</code> options.</p>
<dt><code>&#8211;Group</code><i>&nbsp;grplist</i></p>
<dd>Select by real group ID (RGID) or name. Identical to <code>-G</code>.</p>
<dt><code>&#8211;group</code><i>&nbsp;grplist</i></p>
<dd>Select by effective group ID (EGID) or name. This selects the processes whose effective group name or ID is in <i>grplist</i>. The effective group ID describes the group whose file access permissions are used by the process (see <i><a href="/docs/linux/man/2-getegid/">getegid</a></i>(2)). The <code>-g</code> option is often an alternative to <code>&#8211;group</code>.</p>
<dt><code>p</code><i>&nbsp;pidlist</i></p>
<dd>Select by process ID. Identical to <code>-p</code> and <code>&#8211;pid</code>.</p>
<dt><code>-p</code><i>&nbsp;pidlist</i></p>
<dd>Select by PID. This selects the processes whose process ID numbers appear in <i>pidlist</i>. Identical to <code>p</code> and <code>&#8211;pid</code>.</p>
<dt><code>&#8211;pid</code><i>&nbsp;pidlist</i></p>
<dd>Select by process ID. Identical to <code>-p</code> and <code>p</code>.</p>
<dt><code>&#8211;ppid</code><i>&nbsp;pidlist</i></p>
<dd>Select by parent process ID. This selects the processes with a parent process ID in <i>pidlist</i>. That is, it selects processes that are children of those listed in <i>pidlist</i>.</p>
<dt><code>q</code><i>&nbsp;pidlist</i></p>
<dd>Select by process ID (quick mode). Identical to <code>-q</code> and <code>&#8211;quick-pid</code>.</p>
<dt><code>-q</code><i>&nbsp;pidlist</i></p>
<dd>Select by PID (quick mode). This selects the processes whose process ID numbers appear in <i>pidlist</i>. With this option <code>ps</code> reads the necessary info only for the pids listed in the <i>pidlist</i> and doesn&#8217;t apply additional filtering rules. The order of pids is unsorted and preserved. No additional selection options, sorting and forest type listings are allowed in this mode. Identical to <code>q</code> and <code>&#8211;quick-pid</code>.</p>
<dt><code>&#8211;quick-pid</code><i>&nbsp;pidlist</i></p>
<dd>Select by process ID (quick mode). Identical to <code>-q</code> and <code>q</code>.</p>
<dt><code>-s</code><i>&nbsp;sesslist</i></p>
<dd>Select by session ID. This selects the processes with a session ID specified in <i>sesslist</i>.</p>
<dt><code>&#8211;sid</code><i>&nbsp;sesslist</i></p>
<dd>Select by session ID. Identical to <code>-s</code>.</p>
<dt><code>t</code><i>&nbsp;ttylist</i></p>
<dd>Select by tty. Nearly identical to <code>-t</code> and <code>&#8211;tty</code>, but can also be used with an empty <i>ttylist</i> to indicate the terminal associated with <code>ps</code>. Using the <code>T</code> option is considered cleaner than using <code>t</code> with an empty <i>ttylist</i>.</p>
<dt><code>-t</code><i>&nbsp;ttylist</i></p>
<dd>Select by tty. This selects the processes associated with the terminals given in <i>ttylist</i>. Terminals (ttys, or screens for text output) can be specified in several forms: /dev/ttyS1, ttyS1, S1. A plain &quot;-&quot; may be used to select processes not attached to any terminal.</p>
<dt><code>&#8211;tty</code><i>&nbsp;ttylist</i></p>
<dd>Select by terminal. Identical to <code>-t</code> and <code>t</code>.</p>
<dt><code>U</code><i>&nbsp;userlist</i></p>
<dd>Select by effective user ID (EUID) or name. This selects the processes whose effective user name or ID is in <i>userlist</i>. The effective user ID describes the user whose file access permissions are used by the process (see <i><a href="/docs/linux/man/2-geteuid/">geteuid</a></i>(2)). Identical to <code>-u</code> and <code>&#8211;user</code>.</p>
<dt><code>-U</code><i>&nbsp;userlist</i></p>
<dd>Select by real user ID (RUID) or name. It selects the processes whose real user name or ID is in the <i>userlist</i> list. The real user ID identifies the user who created the process, see <i><a href="/docs/linux/man/2-getuid/">getuid</a></i>(2).</p>
<dt><code>-u</code><i>&nbsp;userlist</i></p>
<dd>Select by effective user ID (EUID) or name. This selects the processes whose effective user name or ID is in <i>userlist</i>. </p>
<p> The effective user ID describes the user whose file access permissions are used by the process (see <i><a href="/docs/linux/man/2-geteuid/">geteuid</a></i>(2)). Identical to <code>U</code> and <code>&#8211;user</code>.</p>
<dt><code>&#8211;User</code><i>&nbsp;userlist</i></p>
<dd>Select by real user ID (RUID) or name. Identical to <code>-U</code>.</p>
<dt><code>&#8211;user</code><i>&nbsp;userlist</i></p>
<dd>Select by effective user ID (EUID) or name. Identical to <code>-u</code> and <code>U</code>.</dl>
<h2>Output Format Control</h2>
<p>These options are used to choose the information displayed by <code>ps</code>. The output may differ by personality.</p>
<dl>
<dt><code>-c</code></p>
<dd>Show different scheduler information for the <code>-l</code> option.</p>
<dt><code>&#8211;context</code></p>
<dd>Display security context format (for SELinux).</p>
<dt><code>-f</code></p>
<dd>Do full-format listing. This option can be combined with many other UNIX-style options to add additional columns. It also causes the command arguments to be printed. When used with <code>-L</code>, the NLWP (number of threads) and LWP (thread ID) columns will be added. See the <code>c</code> option, the format keyword <code>args</code>, and the format keyword <code>comm</code>.</p>
<dt><code>-F</code></p>
<dd>Extra full format. See the <code>-f</code> option, which <code>-F</code> implies.</p>
<dt><code>&#8211;format</code><i>&nbsp;format</i></p>
<dd>user-defined format. Identical to <code>-o</code> and <code>o</code>.</p>
<dt><code>j</code></p>
<dd>BSD job control format.</p>
<dt><code>-j</code></p>
<dd>Jobs format.</p>
<dt><code>l</code></p>
<dd>Display BSD long format.</p>
<dt><code>-l</code></p>
<dd>Long format. The <code>-y</code> option is often useful with this.</p>
<dt><code>-M</code></p>
<dd>Add a column of security data. Identical to <code>Z</code> (for SELinux).</p>
<dt><code>O</code><i>&nbsp;format</i></p>
<dd>is preloaded <code>o</code> (overloaded). The BSD <code>O</code> option can act like <code>-O</code> (user-defined output format with some common fields predefined) or can be used to specify sort order. Heuristics are used to determine the behavior of this option. To ensure that the desired behavior is obtained (sorting or formatting), specify the option in some other way (e.g. with <code>-O</code> or <code>&#8211;sort</code>). When used as a formatting option, it is identical to <code>-O</code>, with the BSD personality.</p>
<dt><code>-O</code><i>&nbsp;format</i></p>
<dd>Like <code>-o</code>, but preloaded with some default columns. Identical to <code>-o pid,</code><i>format</i><code>,state,tname,time,command</code> or <code>-o pid,</code><i>format</i><code>,tname,time,cmd</code><i></i>, see <code>-o</code> below.</p>
<dt><code>o</code><i>&nbsp;format</i></p>
<dd>Specify user-defined format. Identical to <code>-o</code> and <code>&#8211;format</code>.</p>
<dt><code>-o</code><i>&nbsp;format</i></p>
<dd>User-defined format. <i>format</i> is a single argument in the form of a blank-separated or comma-separated list, which offers a way to specify individual output columns. The recognized keywords are described in the <code>STANDARD FORMAT SPECIFIERS</code> section below. Headers may be renamed (<code>ps -o pid,ruser=RealUser -o comm=Command</code>) as desired. If all column headers are empty (<code>ps -o pid= -o comm=</code>) then the header line will not be output. Column width will increase as needed for wide headers; this may be used to widen up columns such as WCHAN (<code>ps -o pid,wchan=WIDE-WCHAN-COLUMN -o comm</code>). Explicit width control (<code>ps opid,wchan:42,cmd</code>) is offered too. The behavior of <code>ps -o pid=X,comm=Y</code> varies with personality; output may be one column named &quot;X,comm=Y&quot; or two columns named &quot;X&quot; and &quot;Y&quot;. Use multiple <code>-o</code> options when in doubt. Use the <code>PS_FORMAT</code> environment variable to specify a default as desired; DefSysV and DefBSD are macros that may be used to choose the default UNIX or BSD columns.</p>
<dt><code>s</code></p>
<dd>Display signal format.</p>
<dt><code>u</code></p>
<dd>Display user-oriented format.</p>
<dt><code>v</code></p>
<dd>Display virtual memory format.</p>
<dt><code>X</code></p>
<dd>Register format.</p>
<dt><code>-y</code></p>
<dd>Do not show flags; show rss in place of addr. This option can only be used with <code>-l</code>.</p>
<dt><code>Z</code></p>
<dd>Add a column of security data. Identical to <code>-M</code> (for SELinux).</dl>
<h2>Output Modifiers</h2>
<dl>
<dt><code>c</code></p>
<dd>Show the true command name. This is derived from the name of the executable file, rather than from the argv value. Command arguments and any modifications to them are thus not shown. This option effectively turns the <code>args</code> format keyword into the <code>comm</code> format keyword; it is useful with the <code>-f</code> format option and with the various BSD-style format options, which all normally display the command arguments. See the <code>-f</code> option, the format keyword <code>args</code>, and the format keyword <code>comm</code>.</p>
<dt><code>&#8211;cols</code><i>&nbsp;n</i></p>
<dd>Set screen width.</p>
<dt><code>&#8211;columns</code><i>&nbsp;n</i></p>
<dd>Set screen width.</p>
<dt><code>&#8211;cumulative</code></p>
<dd>Include some dead child process data (as a sum with the parent).</p>
<dt><code>e</code></p>
<dd>Show the environment after the command.</p>
<dt><code>f</code></p>
<dd>ASCII art process hierarchy (forest).</p>
<dt><code>&#8211;forest</code></p>
<dd>ASCII art process tree.</p>
<dt><code>h</code></p>
<dd>No header. (or, one header per screen in the BSD personality). The <code>h</code> option is problematic. Standard BSD <code>ps</code> uses this option to print a header on each page of output, but older Linux <code>ps</code> uses this option to totally disable the header. This version of <code>ps</code> follows the Linux usage of not printing the header unless the BSD personality has been selected, in which case it prints a header on each page of output. Regardless of the current personality, you can use the long options <code>&#8211;headers</code> and <code>&#8211;no-headers</code> to enable printing headers each page or disable headers entirely, respectively.</p>
<dt><code>-H</code></p>
<dd>Show process hierarchy (forest).</p>
<dt><code>&#8211;headers</code></p>
<dd>Repeat header lines, one per page of output.</p>
<dt><code>k</code><i>&nbsp;spec</i></p>
<dd>Specify sorting order. Sorting syntax is [<code>+</code>|<code>&#8211;</code>]<i>key/</i>[,[<code>+</code>|<code>&#8211;</code>]<i>key</i>[,&#8230;]]. Choose a multi-letter key from the <code>STANDARD FORMAT SPECIFIERS</code> section. The &quot;+&quot; is optional since default direction is increasing numerical or lexicographic order. Identical to <code>&#8211;sort</code>.</p>
<dl>
<dd>
<dl>
<dd>Examples:<br />
 <code>ps jaxkuid,-ppid,+pid</code><br />
 <code>ps axk comm o comm,args</code><br />
 <code>ps kstart_time -ef</code></dl>
</dl>
<dt><code>&#8211;lines</code><i>&nbsp;n</i></p>
<dd>Set screen height.</p>
<dt><code>n</code></p>
<dd>Numeric output for WCHAN and USER (including all types of UID and GID).</p>
<dt><code>&#8211;no-headers</code></p>
<dd>Print no header line at all. <code>&#8211;no-heading</code> is an alias for this option.</p>
<dt><code>O</code><i>&nbsp;order</i></p>
<dd>Sorting order (overloaded). The BSD <code>O</code> option can act like <code>-O</code> (user-defined output format with some common fields predefined) or can be used to specify sort order. Heuristics are used to determine the behavior of this option. To ensure that the desired behavior is obtained (sorting or formatting), specify the option in some other way (e.g. with <code>-O</code> or <code>&#8211;sort</code>).</p>
<dd>For sorting, obsolete BSD <code>O</code> option syntax is <code>O</code>[<code>+</code>|<code>&#8211;</code>]<i>k1</i>[,[<code>+</code>|<code>&#8211;</code>]<i>k2</i>[,&#8230;]]. It orders the processes listing according to the multilevel sort specified by the sequence of one-letter short keys <i>k1</i>,<i>k2</i>, &#8230; described in the <code>OBSOLETE SORT KEYS</code> section below. The&nbsp;&quot;+&quot; is currently optional, merely re-iterating the default direction on a key, but may help to distinguish an <code>O</code> sort from an <code>O</code> format. The &quot;-&quot; reverses direction only on the key it precedes.</p>
<dt><code>&#8211;rows</code><i>&nbsp;n</i></p>
<dd>Set screen height.</p>
<dt><code>S</code></p>
<dd>Sum up some information, such as CPU usage, from dead child processes into their parent. This is useful for examining a system where a parent process repeatedly forks off short-lived children to do work.</p>
<dt><code>&#8211;sort</code><i>&nbsp;spec</i></p>
<dd>Specify sorting order. Sorting syntax is [<i>+</i>|<i>&#8211;</i>]<i>key</i>[,[<code>+</code>|<code>&#8211;</code>]<i>key</i>[,&#8230;]]. Choose a multi-letter key from the <code>STANDARD FORMAT SPECIFIERS</code> section. The &quot;+&quot; is optional since default direction is increasing numerical or lexicographic order. Identical to <code>k</code>. For example: <code>ps jax &#8211;sort=uid,-ppid,+pid</code></p>
<dt><code>w</code></p>
<dd>Wide output. Use this option twice for unlimited width.</p>
<dt><code>-w</code></p>
<dd>Wide output. Use this option twice for unlimited width.</p>
<dt><code>&#8211;width</code><i>&nbsp;n</i></p>
<dd>Set screen width.</dl>
<h2>Thread Display</h2>
<dl>
<dt><code>H</code></p>
<dd>Show threads as if they were processes.</p>
<dt><code>-L</code></p>
<dd>Show threads, possibly with LWP and NLWP columns.</p>
<dt><code>m</code></p>
<dd>Show threads after processes.</p>
<dt><code>-m</code></p>
<dd>Show threads after processes.</p>
<dt><code>-T</code></p>
<dd>Show threads, possibly with SPID column.</dl>
<h2>Other Information</h2>
<dl>
<dt><code>&#8211;help</code><i>&nbsp;section</i></p>
<dd>Print a help message. The <i>section</i> argument can be one of <i>s</i>imple, <i>l</i>ist, <i>o</i>utput, <i>t</i>hreads, <i>m</i>isc, or <i>a</i>ll. The argument can be shortened to one of the underlined letters as in: s|l|o|t|m|a.</p>
<dt><code>&#8211;info</code></p>
<dd>Print debugging info.</p>
<dt><code>L</code></p>
<dd>List all format specifiers.</p>
<dt><code>V</code></p>
<dd>Print the procps-ng version.</p>
<dt><code>-V</code></p>
<dd>Print the procps-ng version.</p>
<dt><code>&#8211;version</code></p>
<dd>Print the procps-ng version.</dl>
<h2>Notes</h2>
<p>This <code>ps</code> works by reading the virtual files in /proc. This <code>ps</code> does not need to be setuid kmem or have any privileges to run. Do not give this <code>ps</code> any special permissions. </p>
<p> CPU usage is currently expressed as the percentage of time spent running during the entire lifetime of a process. This is not ideal, and it does not conform to the standards that <code>ps</code> otherwise conforms to. CPU usage is unlikely to add up to exactly 100%. </p>
<p> The SIZE and RSS fields don&#8217;t count some parts of a process including the page tables, kernel stack, struct thread_info, and struct task_struct. This is usually at least 20 KiB of memory that is always resident. SIZE is the virtual size of the process (code+data+stack). </p>
<p> Processes marked &lt;defunct&gt; are dead processes (so-called &quot;zombies&quot;) that remain because their parent has not destroyed them properly. These processes will be destroyed by <i><a href="/docs/linux/man/8-init/">init</a></i>(8) if the parent process exits. </p>
<p> If the length of the username is greater than the length of the display column, the username will be truncated. See the <code>-o</code> and <code>-O</code> formatting options to customize length. </p>
<p> Commands options such as <code>ps -aux</code> are not recommended as it is a confusion of two different standards. According to the POSIX and UNIX standards, the above command asks to display all processes with a TTY (generally the commands users are running) plus all processes owned by a user named <i>x</i>. If that user doesn&#8217;t exist, then <code>ps</code> will assume you really meant <code>ps aux</code>.</p>
<h2>Process Flags</h2>
<p>The sum of these values is displayed in the &quot;F&quot; column, which is provided by the <code>flags</code> output specifier: </p>
<dl>
<dd>
<dl>
<dt>1</p>
<dd>forked but didn&#8217;t exec</p>
<dt>4</p>
<dd>used super-user privileges</dl>
</dl>
<h2>Process State Codes</h2>
<p>Here are the different values that the <code>s</code>, <code>stat</code> and <code>state</code> output specifiers (header &quot;STAT&quot; or &quot;S&quot;) will display to describe the state of a process: </p>
<dl>
<dd>
<dl>
<dt>D</p>
<dd>uninterruptible sleep (usually IO)</p>
<dt>I</p>
<dd>Idle kernel thread</p>
<dt>R</p>
<dd>running or runnable (on run queue)</p>
<dt>S</p>
<dd>interruptible sleep (waiting for an event to complete)</p>
<dt>T</p>
<dd>stopped by job control signal</p>
<dt>t</p>
<dd>stopped by debugger during the tracing</p>
<dt>W</p>
<dd>paging (not valid since the 2.6.xx kernel)</p>
<dt>X</p>
<dd>dead (should never be seen)</p>
<dt>Z</p>
<dd>defunct (&quot;zombie&quot;) process, terminated but not reaped by its parent</dl>
</dl>
<p> For BSD formats and when the <code>stat</code> keyword is used, additional characters may be displayed: </p>
<dl>
<dd>
<dl>
<dt>&lt;</p>
<dd>high-priority (not nice to other users)</p>
<dt>N</p>
<dd>low-priority (nice to other users)</p>
<dt>L</p>
<dd>has pages locked into memory (for real-time and custom IO)</p>
<dt>s</p>
<dd>is a session leader</p>
<dt>l</p>
<dd>is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)</p>
<dt>+</p>
<dd>is in the foreground process group</dl>
</dl>
<h2>Obsolete Sort Keys</h2>
<p>These keys are used by the BSD <code>O</code> option (when it is used for sorting). The GNU <code>&#8211;sort</code> option doesn&#8217;t use these keys, but the specifiers described below in the <code>STANDARD FORMAT SPECIFIERS</code> section. Note that the values used in sorting are the internal values <code>ps</code> uses and not the &quot;cooked&quot; values used in some of the output format fields (e.g. sorting on tty will sort into device number, not according to the terminal name displayed). Pipe <code>ps</code> output into the <code><a href="/docs/linux/man/1-sort/">sort</a></code>(1) command if you want to sort the cooked values. </p>
<table>
<tr VALIGN=top>
<td><code>KEY</code></td>
<td>LONG</td>
<td>DESCRIPTION
</td>
</tr>
<tr VALIGN=top>
<td>c</td>
<td>cmd</td>
<td>simple name of executable
</td>
</tr>
<tr VALIGN=top>
<td>C</td>
<td>pcpu</td>
<td>cpu utilization
</td>
</tr>
<tr VALIGN=top>
<td>f</td>
<td>flags</td>
<td>flags as in long format F field
</td>
</tr>
<tr VALIGN=top>
<td>g</td>
<td>pgrp</td>
<td>process group ID
</td>
</tr>
<tr VALIGN=top>
<td>G</td>
<td>tpgid</td>
<td>controlling tty process group ID
</td>
</tr>
<tr VALIGN=top>
<td>j</td>
<td>cutime</td>
<td>cumulative user time
</td>
</tr>
<tr VALIGN=top>
<td>J</td>
<td>cstime</td>
<td>cumulative system time
</td>
</tr>
<tr VALIGN=top>
<td>k</td>
<td>utime</td>
<td>user time
</td>
</tr>
<tr VALIGN=top>
<td>m</td>
<td>min_flt</td>
<td>number of minor page faults
</td>
</tr>
<tr VALIGN=top>
<td>M</td>
<td>maj_flt</td>
<td>number of major page faults
</td>
</tr>
<tr VALIGN=top>
<td>n</td>
<td>cmin_flt</td>
<td>cumulative minor page faults
</td>
</tr>
<tr VALIGN=top>
<td>N</td>
<td>cmaj_flt</td>
<td>cumulative major page faults
</td>
</tr>
<tr VALIGN=top>
<td>o</td>
<td>session</td>
<td>session ID
</td>
</tr>
<tr VALIGN=top>
<td>p</td>
<td>pid</td>
<td>process ID
</td>
</tr>
<tr VALIGN=top>
<td>P</td>
<td>ppid</td>
<td>parent process ID
</td>
</tr>
<tr VALIGN=top>
<td>r</td>
<td>rss</td>
<td>resident set size
</td>
</tr>
<tr VALIGN=top>
<td>R</td>
<td>resident</td>
<td>resident pages
</td>
</tr>
<tr VALIGN=top>
<td>s</td>
<td>size</td>
<td>memory size in kilobytes
</td>
</tr>
<tr VALIGN=top>
<td>S</td>
<td>share</td>
<td>amount of shared pages
</td>
</tr>
<tr VALIGN=top>
<td>t</td>
<td>tty</td>
<td>the device number of the controlling tty
</td>
</tr>
<tr VALIGN=top>
<td>T</td>
<td>start_time</td>
<td>time process was started
</td>
</tr>
<tr VALIGN=top>
<td>U</td>
<td>uid</td>
<td>user ID number
</td>
</tr>
<tr VALIGN=top>
<td>u</td>
<td>user</td>
<td>user name
</td>
</tr>
<tr VALIGN=top>
<td>v</td>
<td>vsize</td>
<td>total VM size in KiB
</td>
</tr>
<tr VALIGN=top>
<td>y</td>
<td>priority</td>
<td>kernel scheduling priority
</td>
</tr>
</table>
<h2>Aix Format Descriptors</h2>
<p>This <code>ps</code> supports AIX format descriptors, which work somewhat like the formatting codes of <i><a href="/docs/linux/man/1-printf/">printf</a></i>(1) and <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3). For example, the normal default output can be produced with this: <code>ps -eo %p %y %x %c</code>. The <code>NORMAL</code> codes are described in the next section. </p>
<table>
<tr VALIGN=top>
<td><code>CODE</code></td>
<td>NORMAL</td>
<td>HEADER
</td>
</tr>
<tr VALIGN=top>
<td>%C</td>
<td>pcpu</td>
<td>%CPU
</td>
</tr>
<tr VALIGN=top>
<td>%G</td>
<td>group</td>
<td>GROUP
</td>
</tr>
<tr VALIGN=top>
<td>%P</td>
<td>ppid</td>
<td>PPID
</td>
</tr>
<tr VALIGN=top>
<td>%U</td>
<td>user</td>
<td>USER
</td>
</tr>
<tr VALIGN=top>
<td>%a</td>
<td>args</td>
<td>COMMAND
</td>
</tr>
<tr VALIGN=top>
<td>%c</td>
<td>comm</td>
<td>COMMAND
</td>
</tr>
<tr VALIGN=top>
<td>%g</td>
<td>rgroup</td>
<td>RGROUP
</td>
</tr>
<tr VALIGN=top>
<td>%n</td>
<td>nice</td>
<td>NI
</td>
</tr>
<tr VALIGN=top>
<td>%p</td>
<td>pid</td>
<td>PID
</td>
</tr>
<tr VALIGN=top>
<td>%r</td>
<td>pgid</td>
<td>PGID
</td>
</tr>
<tr VALIGN=top>
<td>%t</td>
<td>etime</td>
<td>ELAPSED
</td>
</tr>
<tr VALIGN=top>
<td>%u</td>
<td>ruser</td>
<td>RUSER
</td>
</tr>
<tr VALIGN=top>
<td>%x</td>
<td>time</td>
<td>TIME
</td>
</tr>
<tr VALIGN=top>
<td>%y</td>
<td>tty</td>
<td>TTY
</td>
</tr>
<tr VALIGN=top>
<td>%z</td>
<td>vsz</td>
<td>VSZ
</td>
</tr>
</table>
<h2>Standard Format Specifiers</h2>
<p>Here are the different keywords that may be used to control the output format (e.g., with option <code>-o</code>) or to sort the selected processes with the GNU-style <code>&#8211;sort</code> option. </p>
<p> For example: <code>ps -eo pid,user,args &#8211;sort user</code> </p>
<p> This version of <code>ps</code> tries to recognize most of the keywords used in other implementations of <code>ps</code>. </p>
<p> The following user-defined format specifiers may contain spaces: <code>args</code>, <code>cmd</code>, <code>comm</code>, <code>command</code>, <code>fname</code>, <code>ucmd</code>, <code>ucomm</code>, <code>lstart</code>, <code>bsdstart</code>, <code>start</code>. </p>
<p> Some keywords may not be available for sorting. </p>
<table>
<tr VALIGN=top>
<td><code>CODE&nbsp;</code></td>
<td><code>HEADER&nbsp;</code></td>
<td><code>DESCRIPTION</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>%cpu&nbsp;</code></td>
<td>%CPU&nbsp;</td>
<td> cpu utilization of the process in &quot;##.#&quot; format. Currently, it is the CPU time used divided by the time the process has been running (cputime/realtime ratio), expressed as a percentage. It will not add up to 100% unless you are lucky. (alias <code>pcpu</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>%mem&nbsp;</code></td>
<td>%MEM&nbsp;</td>
<td> ratio of the process&#8217;s resident set size to the physical memory on the machine, expressed as a percentage. (alias <code>pmem</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>args&nbsp;</code></td>
<td>COMMAND&nbsp;</td>
<td> command with all its arguments as a string. Modifications to the arguments may be shown. The output in this column may contain spaces. A process marked &lt;defunct&gt; is partly dead, waiting to be fully destroyed by its parent. Sometimes the process args will be unavailable; when this happens, <code>ps</code> will instead print the executable name in brackets. (alias <code>cmd</code>, <code>command</code>). See also the <code>comm</code> format keyword, the <code>-f</code> option, and the <code>c</code> option.<br />
 When specified last, this column will extend to the edge of the display. If <code>ps</code> can not determine display width, as when output is redirected (piped) into a file or another command, the output width is undefined (it may be 80, unlimited, determined by the <code>TERM</code> variable, and so on). The <code>COLUMNS</code> environment variable or <code>&#8211;cols</code> option may be used to exactly determine the width in this case. The <code>w</code> or <code>-w</code> option may be also be used to adjust width.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>blocked&nbsp;</code></td>
<td>BLOCKED&nbsp;</td>
<td> mask of the blocked signals, see <i><a href="/docs/linux/man/7-signal/">signal</a></i>(7). According to the width of the field, a 32 or 64-bit mask in hexadecimal format is displayed. (alias <code>sig_block</code>, <code>sigmask</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>bsdstart&nbsp;</code></td>
<td>START&nbsp;</td>
<td> time the command started. If the process was started less than 24 hours ago, the output format is &quot;&nbsp;HH:MM&quot;, else it is &quot; Mmm:SS&quot; (where Mmm is the three letters of the month). See also <code>lstart</code>, <code>start</code>, <code>start_time</code>, and <code>stime</code>.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>bsdtime&nbsp;</code></td>
<td>TIME&nbsp;</td>
<td> accumulated cpu time, user + system. The display format is usually &quot;MMM:SS&quot;, but can be shifted to the right if the process used more than 999 minutes of cpu time.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>c&nbsp;</code></td>
<td>C&nbsp;</td>
<td> processor utilization. Currently, this is the integer value of the percent usage over the lifetime of the process. (see <code>%cpu</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>caught&nbsp;</code></td>
<td>CAUGHT&nbsp;</td>
<td> mask of the caught signals, see <i><a href="/docs/linux/man/7-signal/">signal</a></i>(7). According to the width of the field, a 32 or 64 bits mask in hexadecimal format is displayed. (alias <code>sig_catch</code>, <code>sigcatch</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>cgname&nbsp;</code></td>
<td>CGNAME&nbsp;</td>
<td> display name of control groups to which the process belongs.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>cgroup&nbsp;</code></td>
<td>CGROUP&nbsp;</td>
<td> display control groups to which the process belongs.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>class&nbsp;</code></td>
<td>CLS&nbsp;</td>
<td> scheduling class of the process. (alias <code>policy</code>, <code>cls</code>). Field&#8217;s possible values are: </p>
<p> &#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>not reported</p>
<p> TS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_OTHER</p>
<p> FF<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_FIFO</p>
<p> RR<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_RR</p>
<p> B<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_BATCH</p>
<p> ISO<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_ISO</p>
<p> IDL<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_IDLE</p>
<p> DLN<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_DEADLINE</p>
<p> ?<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>unknown value</p>
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>cls&nbsp;</code></td>
<td>CLS&nbsp;</td>
<td> scheduling class of the process. (alias <code>policy</code>, <code>cls</code>). Field&#8217;s possible values are: </p>
<p> &#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>not reported</p>
<p> TS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_OTHER</p>
<p> FF<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_FIFO</p>
<p> RR<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_RR</p>
<p> B<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_BATCH</p>
<p> ISO<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_ISO</p>
<p> IDL<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_IDLE</p>
<p> DLN<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_DEADLINE</p>
<p> ?<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>unknown value</p>
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>cmd&nbsp;</code></td>
<td>CMD&nbsp;</td>
<td> see <code>args</code>. (alias <code>args</code>, <code>command</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>comm&nbsp;</code></td>
<td>COMMAND&nbsp;</td>
<td> command name (only the executable name). Modifications to the command name will not be shown. A process marked &lt;defunct&gt; is partly dead, waiting to be fully destroyed by its parent. The output in this column may contain spaces. (alias <code>ucmd</code>, <code>ucomm</code>). See also the <code>args</code> format keyword, the <code>-f</code> option, and the <code>c</code> option.<br />
 When specified last, this column will extend to the edge of the display. If <code>ps</code> can not determine display width, as when output is redirected (piped) into a file or another command, the output width is undefined (it may be 80, unlimited, determined by the <code>TERM</code> variable, and so on). The <code>COLUMNS</code> environment variable or <code>&#8211;cols</code> option may be used to exactly determine the width in this case. The <code>w</code>&nbsp;or<code>&nbsp;-w</code> option may be also be used to adjust width.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>command&nbsp;</code></td>
<td>COMMAND&nbsp;</td>
<td> See <code>args</code>. (alias <code>args</code>, <code>command</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>cp&nbsp;</code></td>
<td>CP&nbsp;</td>
<td> per-mill (tenths of a percent) CPU usage. (see <code>%cpu</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>cputime&nbsp;</code></td>
<td>TIME&nbsp;</td>
<td> cumulative CPU time, &quot;[DD-]hh:mm:ss&quot; format. (alias <code>time</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>cputimes&nbsp;</code></td>
<td>TIME&nbsp;</td>
<td> cumulative CPU time in seconds (alias <code>times</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>drs&nbsp;</code></td>
<td>DRS&nbsp;</td>
<td> data resident set size, the amount of physical memory devoted to other than executable code.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>egid&nbsp;</code></td>
<td>EGID&nbsp;</td>
<td> effective group ID number of the process as a decimal integer. (alias <code>gid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>egroup&nbsp;</code></td>
<td>EGROUP&nbsp;</td>
<td> effective group ID of the process. This will be the textual group ID, if it can be obtained and the field width permits, or a decimal representation otherwise. (alias <code>group</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>eip&nbsp;</code></td>
<td>EIP&nbsp;</td>
<td> instruction pointer.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>esp&nbsp;</code></td>
<td>ESP&nbsp;</td>
<td> stack pointer.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>etime&nbsp;</code></td>
<td>ELAPSED&nbsp;</td>
<td> elapsed time since the process was started, in the form [[DD-]hh:]mm:ss.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>etimes&nbsp;</code></td>
<td>ELAPSED&nbsp;</td>
<td> elapsed time since the process was started, in seconds.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>euid&nbsp;</code></td>
<td>EUID&nbsp;</td>
<td> effective user ID (alias <code>uid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>euser&nbsp;</code></td>
<td>EUSER&nbsp;</td>
<td> effective user name. This will be the textual user ID, if it can be obtained and the field width permits, or a decimal representation otherwise. The <code>n</code> option can be used to force the decimal representation. (alias <code>uname</code>, <code>user</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>exe&nbsp;</code></td>
<td>EXE&nbsp;</td>
<td> path to the executable. Useful if path cannot be printed via <code>cmd</code>, <code>comm</code> or <code>args</code> format options.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>f&nbsp;</code></td>
<td>F&nbsp;</td>
<td> flags associated with the process, see the <code>PROCESS FLAGS</code> section. (alias <code>flag</code>, <code>flags</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fgid&nbsp;</code></td>
<td>FGID&nbsp;</td>
<td> filesystem access group ID. (alias <code>fsgid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fgroup&nbsp;</code></td>
<td>FGROUP&nbsp;</td>
<td> filesystem access group ID. This will be the textual group ID, if it can be obtained and the field width permits, or a decimal representation otherwise. (alias <code>fsgroup</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>flag&nbsp;</code></td>
<td>F&nbsp;</td>
<td> see <code>f</code>. (alias <code>f</code>, <code>flags</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>flags&nbsp;</code></td>
<td>F&nbsp;</td>
<td> see <code>f</code>. (alias <code>f</code>, <code>flag</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fname&nbsp;</code></td>
<td>COMMAND&nbsp;</td>
<td> first 8 bytes of the base name of the process&#8217;s executable file. The output in this column may contain spaces.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fuid&nbsp;</code></td>
<td>FUID&nbsp;</td>
<td> filesystem access user ID. (alias <code>fsuid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fuser&nbsp;</code></td>
<td>FUSER&nbsp;</td>
<td> filesystem access user ID. This will be the textual user ID, if it can be obtained and the field width permits, or a decimal representation otherwise.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>gid&nbsp;</code></td>
<td>GID&nbsp;</td>
<td> see <code>egid</code>. (alias <code>egid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>group&nbsp;</code></td>
<td>GROUP&nbsp;</td>
<td> see <code>egroup</code>. (alias <code>egroup</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ignored&nbsp;</code></td>
<td>IGNORED&nbsp;</td>
<td> mask of the ignored signals, see <i><a href="/docs/linux/man/7-signal/">signal</a></i>(7). According to the width of the field, a 32 or 64 bits mask in hexadecimal format is displayed. (alias <code>sig_ignore</code>, <code>sigignore</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ipcns&nbsp;</code></td>
<td>IPCNS&nbsp;</td>
<td> Unique inode number describing the namespace the process belongs to. See <i><a href="/docs/linux/man/7-namespaces/">namespaces</a></i>(7).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>label&nbsp;</code></td>
<td>LABEL&nbsp;</td>
<td> security label, most commonly used for SELinux context data. This is for the <i>Mandatory Access Control</i> (&quot;MAC&quot;) found on high-security systems.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>lstart&nbsp;</code></td>
<td>STARTED&nbsp;</td>
<td> time the command started. See also <code>bsdstart</code>, <code>start</code>, <code>start_time</code>, and <code>stime</code>.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>lsession&nbsp;</code></td>
<td>SESSION&nbsp;</td>
<td> displays the login session identifier of a process, if systemd support has been included.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>luid&nbsp;</code></td>
<td>LUID&nbsp;</td>
<td> displays Login ID associated with a process.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>lwp&nbsp;</code></td>
<td>LWP&nbsp;</td>
<td> light weight process (thread) ID of the dispatchable entity (alias <code>spid</code>, <code>tid</code>). See <code>tid</code> for additional information.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>lxc&nbsp;</code></td>
<td>LXC&nbsp;</td>
<td> The name of the lxc container within which a task is running. If a process is not running inside a container, a dash (&#8216;-&#8216;) will be shown.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>machine&nbsp;</code></td>
<td>MACHINE&nbsp;</td>
<td> displays the machine name for processes assigned to VM or container, if systemd support has been included.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>maj_flt&nbsp;</code></td>
<td>MAJFLT&nbsp;</td>
<td> The number of major page faults that have occurred with this process.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>min_flt&nbsp;</code></td>
<td>MINFLT&nbsp;</td>
<td> The number of minor page faults that have occurred with this process.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>mntns&nbsp;</code></td>
<td>MNTNS&nbsp;</td>
<td> Unique inode number describing the namespace the process belongs to. See <i><a href="/docs/linux/man/7-namespaces/">namespaces</a></i>(7).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>netns&nbsp;</code></td>
<td>NETNS&nbsp;</td>
<td> Unique inode number describing the namespace the process belongs to. See <i><a href="/docs/linux/man/7-namespaces/">namespaces</a></i>(7).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ni&nbsp;</code></td>
<td>NI&nbsp;</td>
<td> nice value. This ranges from 19 (nicest) to -20 (not nice to others), see <i><a href="/docs/linux/man/1-nice/">nice</a></i>(1). (alias <code>nice</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>nice&nbsp;</code></td>
<td>NI&nbsp;</td>
<td> see <code>ni</code>.<code>(alias</code> <code>ni</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>nlwp&nbsp;</code></td>
<td>NLWP&nbsp;</td>
<td> number of lwps (threads) in the process. (alias <code>thcount</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>numa&nbsp;</code></td>
<td>NUMA&nbsp;</td>
<td> The node associated with the most recently used processor. A <i>-1</i> means that NUMA information is unavailable.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>nwchan&nbsp;</code></td>
<td>WCHAN&nbsp;</td>
<td> address of the kernel function where the process is sleeping (use <code>wchan</code> if you want the kernel function name). Running tasks will display a dash (&#8216;-&#8216;) in this column.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ouid&nbsp;</code></td>
<td>OWNER&nbsp;</td>
<td> displays the Unix user identifier of the owner of the session of a process, if systemd support has been included.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pcpu&nbsp;</code></td>
<td>%CPU&nbsp;</td>
<td> see <code>%cpu</code>. (alias <code>%cpu</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pending&nbsp;</code></td>
<td>PENDING&nbsp;</td>
<td> mask of the pending signals. See <i><a href="/docs/linux/man/7-signal/">signal</a></i>(7). Signals pending on the process are distinct from signals pending on individual threads. Use the <code>m</code> option or the <code>-m</code> option to see both. According to the width of the field, a 32 or 64 bits mask in hexadecimal format is displayed. (alias <code>sig</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pgid&nbsp;</code></td>
<td>PGID&nbsp;</td>
<td> process group ID or, equivalently, the process ID of the process group leader. (alias <code>pgrp</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pgrp&nbsp;</code></td>
<td>PGRP&nbsp;</td>
<td> see <code>pgid</code>. (alias <code>pgid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pid&nbsp;</code></td>
<td>PID&nbsp;</td>
<td> a number representing the process ID (alias <code>tgid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pidns&nbsp;</code></td>
<td>PIDNS&nbsp;</td>
<td> Unique inode number describing the namespace the process belongs to. See <i><a href="/docs/linux/man/7-namespaces/">namespaces</a></i>(7).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pmem&nbsp;</code></td>
<td>%MEM&nbsp;</td>
<td> see <code>%mem</code>. (alias <code>%mem</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>policy&nbsp;</code></td>
<td>POL&nbsp;</td>
<td> scheduling class of the process. (alias <code>class</code>, <code>cls</code>). Possible values are: </p>
<p> &#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>not reported</p>
<p> TS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_OTHER</p>
<p> FF<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_FIFO</p>
<p> RR<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_RR</p>
<p> B<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_BATCH</p>
<p> ISO<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_ISO</p>
<p> IDL<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_IDLE</p>
<p> DLN<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>SCHED_DEADLINE</p>
<p> ?<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>unknown value</p>
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ppid&nbsp;</code></td>
<td>PPID&nbsp;</td>
<td> parent process ID.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pri&nbsp;</code></td>
<td>PRI&nbsp;</td>
<td> priority of the process. Higher number means lower priority.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>psr&nbsp;</code></td>
<td>PSR&nbsp;</td>
<td> processor that process is currently assigned to.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>rgid&nbsp;</code></td>
<td>RGID&nbsp;</td>
<td> real group ID.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>rgroup&nbsp;</code></td>
<td>RGROUP&nbsp;</td>
<td> real group name. This will be the textual group ID, if it can be obtained and the field width permits, or a decimal representation otherwise.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>rss&nbsp;</code></td>
<td>RSS&nbsp;</td>
<td> resident set size, the non-swapped physical memory that a task has used (in kilobytes). (alias <code>rssize</code>, <code>rsz</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>rssize&nbsp;</code></td>
<td>RSS&nbsp;</td>
<td> see <code>rss</code>. (alias <code>rss</code>, <code>rsz</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>rsz&nbsp;</code></td>
<td>RSZ&nbsp;</td>
<td> see <code>rss</code>. (alias <code>rss</code>, <code>rssize</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>rtprio&nbsp;</code></td>
<td>RTPRIO&nbsp;</td>
<td> realtime priority.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ruid&nbsp;</code></td>
<td>RUID&nbsp;</td>
<td> real user ID.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ruser&nbsp;</code></td>
<td>RUSER&nbsp;</td>
<td> real user ID. This will be the textual user ID, if it can be obtained and the field width permits, or a decimal representation otherwise.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>s&nbsp;</code></td>
<td>S&nbsp;</td>
<td> minimal state display (one character). See section <code>PROCESS STATE CODES</code> for the different values. See also <code>stat</code> if you want additional information displayed. (alias <code>state</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sched&nbsp;</code></td>
<td>SCH&nbsp;</td>
<td> scheduling policy of the process. The policies SCHED_OTHER (SCHED_NORMAL), SCHED_FIFO, SCHED_RR, SCHED_BATCH, SCHED_ISO, SCHED_IDLE and SCHED_DEADLINE are respectively displayed as 0, 1, 2, 3, 4, 5 and 6.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>seat&nbsp;</code></td>
<td>SEAT&nbsp;</td>
<td> displays the identifier associated with all hardware devices assigned to a specific workplace, if systemd support has been included.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sess&nbsp;</code></td>
<td>SESS&nbsp;</td>
<td> session ID or, equivalently, the process ID of the session leader. (alias <code>session</code>, <code>sid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sgi_p&nbsp;</code></td>
<td>P&nbsp;</td>
<td> processor that the process is currently executing on. Displays &quot;*&quot; if the process is not currently running or runnable.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sgid&nbsp;</code></td>
<td>SGID&nbsp;</td>
<td> saved group ID. (alias <code>svgid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sgroup&nbsp;</code></td>
<td>SGROUP&nbsp;</td>
<td> saved group name. This will be the textual group ID, if it can be obtained and the field width permits, or a decimal representation otherwise.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sid&nbsp;</code></td>
<td>SID&nbsp;</td>
<td> see <code>sess</code>. (alias <code>sess</code>, <code>session</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sig&nbsp;</code></td>
<td>PENDING&nbsp;</td>
<td> see <code>pending</code>. (alias <code>pending</code>, <code>sig_pend</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sigcatch&nbsp;</code></td>
<td>CAUGHT&nbsp;</td>
<td> see <code>caught</code>. (alias <code>caught</code>, <code>sig_catch</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sigignore&nbsp;</code></td>
<td>IGNORED&nbsp;</td>
<td> see <code>ignored</code>. (alias <code>ignored</code>, <code>sig_ignore</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sigmask&nbsp;</code></td>
<td>BLOCKED&nbsp;</td>
<td> see <code>blocked</code>. (alias <code>blocked</code>, <code>sig_block</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>size&nbsp;</code></td>
<td>SIZE&nbsp;</td>
<td> approximate amount of swap space that would be required if the process were to dirty all writable pages and then be swapped out. This number is very rough!
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>slice&nbsp;</code></td>
<td>SLICE&nbsp;</td>
<td> displays the slice unit which a process belongs to, if systemd support has been included.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>spid&nbsp;</code></td>
<td>SPID&nbsp;</td>
<td> see <code>lwp</code>. (alias <code>lwp</code>, <code>tid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>stackp&nbsp;</code></td>
<td>STACKP&nbsp;</td>
<td> address of the bottom (start) of stack for the process.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>start&nbsp;</code></td>
<td>STARTED&nbsp;</td>
<td> time the command started. If the process was started less than 24 hours ago, the output format is &quot;HH:MM:SS&quot;, else it is &quot;&nbsp;<wbr>&nbsp;Mmm dd&quot; (where Mmm is a three-letter month name). See also <code>lstart</code>, <code>bsdstart</code>, <code>start_time</code>, and <code>stime</code>.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>start_time&nbsp;</code></td>
<td>START&nbsp;</td>
<td> starting time or date of the process. Only the year will be displayed if the process was not started the same year <code>ps</code> was invoked, or &quot;MmmDD&quot; if it was not started the same day, or &quot;HH:MM&quot; otherwise. See also <code>bsdstart</code>, <code>start</code>, <code>lstart</code>, and <code>stime</code>.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>stat&nbsp;</code></td>
<td>STAT&nbsp;</td>
<td> multi-character process state. See section <code>PROCESS STATE CODES</code> for the different values meaning. See also <code>s</code>&nbsp;and<code>&nbsp;state</code> if you just want the first character displayed.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>state&nbsp;</code></td>
<td>S&nbsp;</td>
<td> see <code>s</code>. (alias<code>&nbsp;s</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>stime&nbsp;</code></td>
<td>STIME&nbsp;</td>
<td> see <code>start_time</code>. (alias <code>start_time</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>suid&nbsp;</code></td>
<td>SUID&nbsp;</td>
<td> saved user ID. (alias <code>svuid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>supgid&nbsp;</code></td>
<td>SUPGID&nbsp;</td>
<td> group ids of supplementary groups, if any. See <code><a href="/docs/linux/man/2-getgroups/">getgroups</a></code>(2).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>supgrp&nbsp;</code></td>
<td>SUPGRP&nbsp;</td>
<td> group names of supplementary groups, if any. See <code><a href="/docs/linux/man/2-getgroups/">getgroups</a></code>(2).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>suser&nbsp;</code></td>
<td>SUSER&nbsp;</td>
<td> saved user name. This will be the textual user ID, if it can be obtained and the field width permits, or a decimal representation otherwise. (alias <code>svuser</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>svgid&nbsp;</code></td>
<td>SVGID&nbsp;</td>
<td> see <code>sgid</code>. (alias <code>sgid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>svuid&nbsp;</code></td>
<td>SVUID&nbsp;</td>
<td> see <code>suid</code>. (alias <code>suid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sz&nbsp;</code></td>
<td>SZ&nbsp;</td>
<td> size in physical pages of the core image of the process. This includes text, data, and stack space. Device mappings are currently excluded; this is subject to change. See <code>vsz</code>&nbsp;and<code>&nbsp;rss</code>.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>tgid&nbsp;</code></td>
<td>TGID&nbsp;</td>
<td> a number representing the thread group to which a task belongs (alias <code>pid</code>). It is the process ID of the thread group leader.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>thcount&nbsp;</code></td>
<td>THCNT&nbsp;</td>
<td> see <code>nlwp</code>. (alias <code>nlwp</code>). number of kernel threads owned by the process.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>tid&nbsp;</code></td>
<td>TID&nbsp;</td>
<td> the unique number representing a dispatchable entity (alias <code>lwp</code>, <code>spid</code>). This value may also appear as: a process ID (pid); a process group ID (pgrp); a session ID for the session leader (sid); a thread group ID for the thread group leader (tgid); and a tty process group ID for the process group leader (tpgid).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>time&nbsp;</code></td>
<td>TIME&nbsp;</td>
<td> cumulative CPU time, &quot;[DD-]HH:MM:SS&quot; format. (alias <code>cputime</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>times&nbsp;</code></td>
<td>TIME&nbsp;</td>
<td> cumulative CPU time in seconds (alias <code>cputimes</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>tname&nbsp;</code></td>
<td>TTY&nbsp;</td>
<td> controlling tty (terminal). (alias <code>tt</code>, <code>tty</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>tpgid&nbsp;</code></td>
<td>TPGID&nbsp;</td>
<td> ID of the foreground process group on the tty (terminal) that the process is connected to, or -1 if the process is not connected to a tty.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>trs&nbsp;</code></td>
<td>TRS&nbsp;</td>
<td> text resident set size, the amount of physical memory devoted to executable code.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>tt&nbsp;</code></td>
<td>TT&nbsp;</td>
<td> controlling tty (terminal). (alias <code>tname</code>, <code>tty</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>tty&nbsp;</code></td>
<td>TT&nbsp;</td>
<td> controlling tty (terminal). (alias <code>tname</code>, <code>tt</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ucmd&nbsp;</code></td>
<td>CMD&nbsp;</td>
<td> see <code>comm</code>. (alias <code>comm</code>, <code>ucomm</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ucomm&nbsp;</code></td>
<td>COMMAND&nbsp;</td>
<td> see <code>comm</code>. (alias <code>comm</code>, <code>ucmd</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>uid&nbsp;</code></td>
<td>UID&nbsp;</td>
<td> see <code>euid</code>. (alias <code>euid</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>uname&nbsp;</code></td>
<td>USER&nbsp;</td>
<td> see <code>euser</code>. (alias <code>euser</code>, <code>user</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>unit&nbsp;</code></td>
<td>UNIT&nbsp;</td>
<td> displays unit which a process belongs to, if systemd support has been included.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>user&nbsp;</code></td>
<td>USER&nbsp;</td>
<td> see <code>euser</code>. (alias <code>euser</code>, <code>uname</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>userns&nbsp;</code></td>
<td>USERNS&nbsp;</td>
<td> Unique inode number describing the namespace the process belongs to. See <i><a href="/docs/linux/man/7-namespaces/">namespaces</a></i>(7).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>utsns&nbsp;</code></td>
<td>UTSNS&nbsp;</td>
<td> Unique inode number describing the namespace the process belongs to. See <i><a href="/docs/linux/man/7-namespaces/">namespaces</a></i>(7).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>uunit&nbsp;</code></td>
<td>UUNIT&nbsp;</td>
<td> displays user unit which a process belongs to, if systemd support has been included.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>vsize&nbsp;</code></td>
<td>VSZ&nbsp;</td>
<td> see <code>vsz</code>. (alias <code>vsz</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>vsz&nbsp;</code></td>
<td>VSZ&nbsp;</td>
<td> virtual memory size of the process in KiB (1024-byte units). Device mappings are currently excluded; this is subject to change. (alias <code>vsize</code>).
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>wchan&nbsp;</code></td>
<td>WCHAN&nbsp;</td>
<td> name of the kernel function in which the process is sleeping, a &quot;-&quot; if the process is running, or a &quot;*&quot; if the process is multi-threaded and <code>ps</code> is not displaying threads.
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;</code></td>
<td>&nbsp;</td>
<td>
</td>
</tr>
</table>
<h2>Environment Variables</h2>
<p>The following environment variables could affect <code>ps</code>:</p>
<dl>
<dt><code>COLUMNS</code></p>
<dd>Override default display width.</p>
<dt><code>LINES</code></p>
<dd>Override default display height.</p>
<dt><code>PS_PERSONALITY</code></p>
<dd>Set to one of posix, old, linux, bsd, sun, digital&#8230; (see section <code>PERSONALITY</code> below).</p>
<dt><code>CMD_ENV</code></p>
<dd>Set to one of posix, old, linux, bsd, sun, digital&#8230; (see section <code>PERSONALITY</code> below).</p>
<dt><code>I_WANT_A_BROKEN_PS</code></p>
<dd>Force obsolete command line interpretation.</p>
<dt><code>LC_TIME</code></p>
<dd>Date format.</p>
<dt><code>PS_COLORS</code></p>
<dd>Not currently supported.</p>
<dt><code>PS_FORMAT</code></p>
<dd>Default output format override. You may set this to a format string of the type used for the <code>-o</code> option. The <code>DefSysV</code> and <code>DefBSD</code> values are particularly useful.</p>
<dt><code>POSIXLY_CORRECT</code></p>
<dd>Don&#8217;t find excuses to ignore bad &quot;features&quot;.</p>
<dt><code>POSIX2</code></p>
<dd>When set to &quot;on&quot;, acts as <code>POSIXLY_CORRECT</code>.</p>
<dt><code>UNIX95</code></p>
<dd>Don&#8217;t find excuses to ignore bad &quot;features&quot;.</p>
<dt><code>_XPG</code></p>
<dd>Cancel <code>CMD_ENV</code>=<i>irix</i> non-standard behavior.</dl>
<p> In general, it is a bad idea to set these variables. The one exception is <code>CMD_ENV</code> or <code>PS_PERSONALITY</code>, which could be set to Linux for normal systems. Without that setting, <code>ps</code> follows the useless and bad parts of the Unix98 standard.</p>
<h2>Personality</h2>
<table>
<tr VALIGN=top>
<td>390</td>
<td>like the OS/390 OpenEdition <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>aix</td>
<td>like AIX <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>bsd</td>
<td>like FreeBSD <code>ps</code> (totally non-standard)
</td>
</tr>
<tr VALIGN=top>
<td>compaq</td>
<td>like Digital Unix <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>debian</td>
<td>like the old Debian <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>digital</td>
<td>like Tru64 (was Digital Unix, was OSF/1) <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>gnu</td>
<td>like the old Debian <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>hp</td>
<td>like HP-UX <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>hpux</td>
<td>like HP-UX <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>irix</td>
<td>like Irix <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>linux</td>
<td>***** <code>recommended</code> *****
</td>
</tr>
<tr VALIGN=top>
<td>old</td>
<td>like the original Linux <code>ps</code> (totally non-standard)
</td>
</tr>
<tr VALIGN=top>
<td>os390</td>
<td>like OS/390 Open Edition <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>posix</td>
<td>standard
</td>
</tr>
<tr VALIGN=top>
<td>s390</td>
<td>like OS/390 Open Edition <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>sco</td>
<td>like SCO <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>sgi</td>
<td>like Irix <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>solaris2</td>
<td>like Solaris 2+ (SunOS 5) <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>sunos4</td>
<td>like SunOS 4 (Solaris 1) <code>ps</code> (totally non-standard)
</td>
</tr>
<tr VALIGN=top>
<td>svr4</td>
<td>standard
</td>
</tr>
<tr VALIGN=top>
<td>sysv</td>
<td>standard
</td>
</tr>
<tr VALIGN=top>
<td>tru64</td>
<td>like Tru64 (was Digital Unix, was OSF/1) <code>ps</code>
</td>
</tr>
<tr VALIGN=top>
<td>unix</td>
<td>standard
</td>
</tr>
<tr VALIGN=top>
<td>unix95</td>
<td>standard
</td>
</tr>
<tr VALIGN=top>
<td>unix98</td>
<td>standard
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pgrep/">pgrep</a></code>(1), <code><a href="/docs/linux/man/1-pstree/">pstree</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<h2>Standards</h2>
<p>This <code>ps</code> conforms to: </p>
<dl>
<dt>1</p>
<dd>Version 2 of the Single Unix Specification</p>
<dt>2</p>
<dd>The Open Group Technical Standard Base Specifications, Issue 6</p>
<dt>3</p>
<dd>IEEE Std 1003.1, 2004 Edition</p>
<dt>4</p>
<dd>X/Open System Interfaces Extension [UP XSI]</p>
<dt>5</p>
<dd>ISO/IEC 9945:2003</dl>
<h2>Author</h2>
<p><code>ps</code> was originally written by Branko Lankester Michael K. Johnson re-wrote it significantly to use the proc filesystem, changing a few things in the process. Michael Shields added the pid-list feature. Charles Blake added multi-level sorting, the dirent-style library, the device name-to-number mmaped database, the approximate binary search directly on System.map, and many code and documentation cleanups. David Mossberger-Tang wrote the generic BFD support for psupdate. Albert Cahalan rewrote ps for full Unix98 and BSD support, along with some ugly hacks for obsolete and foreign syntax. </p>
<p> Please send bug reports to No subscription is required or suggested.</p>
