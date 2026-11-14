---
title: "makedumpfile(8)"
name: "makedumpfile"
section: "8"
letter: "m"
url: "/docs/linux/man/8-makedumpfile/"
description: "makedumpfile – make a small dumpfile of kdump"
---

<p>makedumpfile &#8211; make a small dumpfile of kdump</p>
<h2>Synopsis</h2>
<p><code>makedumpfile</code> [<i>OPTION</i>] [-x <i>VMLINUX</i>|-i <i>VMCOREINFO</i>] <i>VMCORE</i> <i>DUMPFILE</i><br />
 <code>makedumpfile</code> -F [<i>OPTION</i>] [-x <i>VMLINUX</i>|-i <i>VMCOREINFO</i>] <i>VMCORE</i><br />
 <code>makedumpfile</code> [<i>OPTION</i>] -x <i>VMLINUX</i> [&#8211;config <i>FILTERCONFIGFILE</i>] [&#8211;eppic <i>EPPICMACRO</i>] <i>VMCORE</i> <i>DUMPFILE</i><br />
 <code>makedumpfile</code> -R <i>DUMPFILE</i><br />
 <code>makedumpfile</code> &#8211;split [<i>OPTION</i>] [-x <i>VMLINUX</i>|-i <i>VMCOREINFO</i>] <i>VMCORE</i> <i>DUMPFILE1</i> <i>DUMPFILE2</i> [<i>DUMPFILE3</i> ..]<br />
 <code>makedumpfile</code> [<i>OPTION</i>] [-x <i>VMLINUX</i>|-i <i>VMCOREINFO</i>] &#8211;num-threads <i>THREADNUM</i> <i>VMCORE</i> <i>DUMPFILE</i><br />
 <code>makedumpfile</code> &#8211;reassemble <i>DUMPFILE1</i> <i>DUMPFILE2</i> [<i>DUMPFILE3</i> ..] <i>DUMPFILE</i><br />
 <code>makedumpfile</code> -g <i>VMCOREINFO</i> -x <i>VMLINUX</i><br />
 <code>makedumpfile</code> [<i>OPTION</i>] [&#8211;xen-syms <i>XEN-SYMS</i>|&#8211;xen-vmcoreinfo <i>VMCOREINFO</i>] <i>VMCORE</i> <i>DUMPFILE</i><br />
 <code>makedumpfile</code> &#8211;dump-dmesg [-x <i>VMLINUX</i>|-i <i>VMCOREINFO</i>] <i>VMCORE</i> <i>LOGFILE</i><br />
 <code>makedumpfile</code> [<i>OPTION</i>] -x <i>VMLINUX</i> &#8211;diskset=<i>VMCORE1</i> &#8211;diskset=<i>VMCORE2</i> [&#8211;diskset=<i>VMCORE3</i> ..] <i>DUMPFILE</i><br />
 <code>makedumpfile</code> -h<br />
 <code>makedumpfile</code> -v</p>
<h2>Description</h2>
<p>With kdump, the memory image of the first kernel (called &quot;panicked kernel&quot;) can be taken as /proc/vmcore while the second kernel (called &quot;kdump kernel&quot; or &quot;capture kernel&quot;) is running. This document represents /proc/vmcore as <i>VMCORE</i>. makedumpfile makes a small <i>DUMPFILE</i> by compressing dump data or by excluding unnecessary pages for analysis, or both. makedumpfile needs the first kernel&#8217;s debug information, so that it can distinguish unnecessary pages by analyzing how the first kernel uses the memory. The information can be taken from <i>VMLINUX</i> or <i>VMCOREINFO</i>. makedumpfile can exclude the following types of pages while copying <i>VMCORE</i> to <i>DUMPFILE</i>, and a user can choose which type of pages will be excluded.<br />
 <code>&#8211; Pages filled with zero</code><br />
 <code>&#8211; Cache pages without private flag (non-private cache)</code><br />
 <code>&#8211; Cache pages with private flag (private cache)</code><br />
 <code>&#8211; User process data pages</code><br />
 <code>&#8211; Free pages</code> makedumpfile provides two <i>DUMPFILE</i> formats (the ELF format and the kdump-compressed format). By default, makedumpfile makes a <i>DUMPFILE</i> in the kdump-compressed format. The kdump-compressed format is readable only with the crash utility, and it can be smaller than the ELF format because of the compression support. The ELF format is readable with GDB and the crash utility. If a user wants to use GDB, <i>DUMPFILE</i> format has to be explicitly specified to be the ELF format. Apart from the exclusion of unnecessary pages mentioned above, makedumpfile allows user to filter out targeted kernel data. The filter config file can be used to specify kernel/module symbols and its members that need to be filtered out through the erase command syntax. makedumpfile reads the filter config and builds the list of memory addresses and its sizes after processing filter commands. The memory locations that require to be filtered out are then poisoned with character &#8216;X&#8217; (58 in Hex). Refer to <code><a href="/docs/linux/man/5-makedumpfile-conf/">makedumpfile.conf</a>(5)</code> for file format. Eppic macros can also be used to specify kernel symbols and its members that need to be filtered. Eppic provides C semantics including language constructs such as conditional statements, logical and arithmetic operators, functions, nested loops to traverse and erase kernel data. &#8211;eppic requires <code>eppic_makedumpfile.so</code> and eppic library. <code>eppic_makedumpfile.so</code> can be built from makedumpfile source. Refer to <code><a rel="nofollow" href="http://code.google.com/p/eppic/">http://code.google.com/p/eppic/</a></code> to build eppic library <code>libeppic.a</code> and for more information on writing eppic macros. To analyze the first kernel&#8217;s memory usage, makedumpfile can refer to <i>VMCOREINFO</i> instead of <i>VMLINUX</i>. <i>VMCOREINFO</i> contains the first kernel&#8217;s information (structure size, field offset, etc.), and <i>VMCOREINFO</i> is small enough to be included into the second kernel&#8217;s initrd.<br />
 If the second kernel is running on its initrd without mounting a root file system, makedumpfile cannot refer to <i>VMLINUX</i> because the second kernel&#8217;s initrd cannot include a large file like <i>VMLINUX</i>. To solve the problem, makedumpfile makes <i>VMCOREINFO</i> beforehand, and it refers to <i>VMCOREINFO</i> instead of <i>VMLINUX</i> while the second kernel is running.<br />
 <i>VMCORE</i> has contained <i>VMCOREINFO</i> since linux-2.6.24, and a user does not need to specify neither -x nor -i option. If the second kernel is running on its initrd without mounting any file system, a user needs to transport the dump data to a remote host. To transport the dump data by SSH, makedumpfile outputs the dump data in the intermediate format (the flattened format) to the standard output. By piping the output data to SSH, a user can transport the dump data to a remote host. Note that analysis tools (crash utility before version 5.1.2 or GDB) cannot read the flattened format directly, so on a remote host the received data in the flattened format needs to be rearranged to a readable <i>DUMPFILE</i> format by makedumpfile (or makedumpfile-R.pl). makedumpfile can read a <i>DUMPFILE</i> in the kdump-compressed format instead of <i>VMCORE</i> and re-filter it. This feature is useful in situation that users need to reduce the file size of <i>DUMPFILE</i> for sending it somewhere by ftp/scp/etc. (If all of the page types, which are specified by a new dump_level, are excluded from an original <i>DUMPFILE</i> already, a new <i>DUMPFILE</i> is the same as an original <i>DUMPFILE</i>.)<br />
 For example, makedumpfile can create a <i>DUMPFILE</i> of dump_level 31 from the one of dump_level 3 like the following:<br />
 <code>Example:</code><br />
 # makedumpfile -c -d 3 /proc/vmcore dumpfile.1<br />
 # makedumpfile -c -d 31 dumpfile.1 dumpfile.2 makedumpfile can read <i>VMCORE</i>(s) in three kinds of sadump formats: single partition format, diskset format and media backup format, and can convert each of them into kdump-compressed format with filtering and compression processing. Note that for <i>VMCORE</i>(s) created by sadump, you always need to pass <i>VMLINUX</i> with -x option. Also, to pass multiple <i>VMCORE</i>s created on diskset configuration, you need to use &#8211;diskset option. </p>
<h2>Options</h2>
<dl>
<dt><code>-c,-l,-p</code></p>
<dd>Compress dump data by each page using zlib for -c option, lzo for -l option or snappy for -p option. (-l option needs USELZO=on and -p option needs USESNAPPY=on when building)<br />
 A user cannot specify this option with -E option, because the ELF format does not support compressed data.<br />
 <code>Example:</code><br />
 # makedumpfile -c -d 31 -x vmlinux /proc/vmcore dumpfile </p>
<dt><code>-d</code><i>&nbsp;<wbr>dump_level</i></p>
<dd>Specify the type of unnecessary page for analysis.<br />
 Pages of the specified type are not copied to <i>DUMPFILE</i>. The page type marked in the following table is excluded. A user can specify multiple page types by setting the sum of each page type for dump_level. The maximum of dump_level is 31. Note that a dump_level for Xen dump filtering is 0 or 1 on a machine other than x86_64. On a x86_64 machine, even 2 or bigger dump level will be effective if you specify domain-0&#8217;s <i>vmlinux</i> with -x option. Then the pages are excluded only from domain-0.<br />
 If specifying multiple dump_levels with the delimiter &#8216;,&#8217;, makedumpfile retries to create a <i>DUMPFILE</i> by other dump_level when &quot;No space on device&quot; error happens. For example, if dump_level is &quot;11,31&quot; and makedumpfile fails by dump_level 11, makedumpfile retries it by dump_level 31.<br />
 <code>Example:</code><br />
 # makedumpfile -d 11 -x vmlinux /proc/vmcore dumpfile<br />
 # makedumpfile -d 11,31 -x vmlinux /proc/vmcore dumpfile<br />
 <code>Base level:</code><br />
 dump_level consists of five bits, so there are five base levels to specify the type of unnecessary page.<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code> 1</code> :<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Exclude the pages filled with zero.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code> 2</code> :<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Exclude the non-private cache pages.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code> 4</code> :<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Exclude all cache pages.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code> 8</code> :<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Exclude the user process data pages.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>16</code> :<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Exclude the free pages.</p>
<p> Here is the all combinations of the bits. </p>
<p>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|non-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>dump | zero |private|private| user | free<br />
&nbsp;<wbr>level | page |cache&nbsp;<wbr>&nbsp;<wbr>|cache&nbsp;<wbr>&nbsp;<wbr>| data | page<br />
 &#8212;&#8212;-+&#8212;&#8212;+&#8212;&#8212;-+&#8212;&#8212;-+&#8212;&#8212;+&#8212;&#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>0 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>1 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>2 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>3 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>4 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>5 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>6 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>7 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>8 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>9 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>10 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>11 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>12 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>13 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>14 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>15 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>16 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>17 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>18 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>19 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>20 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>21 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>22 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>23 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>24 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>25 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>26 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>27 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>28 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>29 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>30 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X<br />
&nbsp;<wbr>31 |&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>X </p>
<dt><code>-E</code></p>
<dd>Create <i>DUMPFILE</i> in the ELF format.<br />
 This option cannot be specified with the -c, -l or -p options, because the ELF format does not support compressed data.<br />
 <code>Example:</code><br />
 # makedumpfile -E -d 31 -x vmlinux /proc/vmcore dumpfile </p>
<dt><code>-f</code></p>
<dd>Force existing DUMPFILE to be overwritten.<br />
 <code>Example:</code><br />
 # makedumpfile -f -d 31 -x vmlinux /proc/vmcore dumpfile<br />
 This command overwrites <i>DUMPFILE</i> even if it already exists. </p>
<dt><code>-x</code> <i>VMLINUX</i></p>
<dd>Specify the first kernel&#8217;s <i>VMLINUX</i> with debug information to analyze the first kernel&#8217;s memory usage.<br />
 This option is necessary if <i>VMCORE</i> does not contain <i>VMCOREINFO</i>, [-i <i>VMCOREINFO</i>] is not specified, and dump_level is 2 or more.<br />
 The page size of the first kernel and the second kernel should match.<br />
 <code>Example:</code><br />
 # makedumpfile -d 31 -x vmlinux /proc/vmcore dumpfile </p>
<dt><code>-i</code> <i>VMCOREINFO</i></p>
<dd>Specify <i>VMCOREINFO</i> instead of <i>VMLINUX</i> for analyzing the first kernel&#8217;s memory usage.<br />
 <i>VMCOREINFO</i> should be made beforehand by makedumpfile with -g option, and it contains the first kernel&#8217;s information.<br />
 This option is necessary if <i>VMCORE</i> does not contain <i>VMCOREINFO</i>, [-x <i>VMLINUX</i>] is not specified, and dump_level is 2 or more.<br />
 <code>Example:</code><br />
 # makedumpfile -d 31 -i vmcoreinfo /proc/vmcore dumpfile </p>
<dt><code>-g</code> <i>VMCOREINFO</i></p>
<dd>Generate <i>VMCOREINFO</i> from the first kernel&#8217;s <i>VMLINUX</i> with debug information.<br />
 <i>VMCOREINFO</i> must be generated on the system that is running the first kernel. With -i option, a user can specify <i>VMCOREINFO</i> generated on the other system that is running the same first kernel. [-x <i>VMLINUX</i>] must be specified.<br />
 <code>Example:</code><br />
 # makedumpfile -g vmcoreinfo -x vmlinux </p>
<dt><code>&#8211;config</code> <i>FILTERCONFIGFILE</i></p>
<dd>Used in conjunction with -x <i>VMLINUX</i> option, to specify the filter config file <i>FILTERCONFIGFILE</i> that contains erase commands to filter out desired kernel data from vmcore while creating <i>DUMPFILE</i>. For filter command syntax please refer to <code><a href="/docs/linux/man/5-makedumpfile-conf/">makedumpfile.conf</a>(5)</code>. </p>
<dt><code>&#8211;eppic</code> <i>EPPICMACRO</i></p>
<dd>Used in conjunction with -x <i>VMLINUX</i> option, to specify the eppic macro file that contains filter rules or directory that contains eppic macro files to filter out desired kernel data from vmcore while creating <i>DUMPFILE</i>. When directory is specified, all the eppic macros in the directory are processed. </p>
<dt><code>-F</code></p>
<dd>Output the dump data in the flattened format to the standard output for transporting the dump data by SSH.<br />
 Analysis tools (crash utility before version 5.1.2 or GDB) cannot read the flattened format directly. For analysis, the dump data in the flattened format should be rearranged to a normal <i>DUMPFILE</i> (readable with analysis tools) by -R option. By which option is specified with -F option, the format of the rearranged <i>DUMPFILE</i> is fixed. In other words, it is impossible to specify the <i>DUMPFILE</i> format when the dump data is rearranged with -R option. If specifying -E option with -F option, the format of the rearranged <i>DUMPFILE</i> is the ELF format. Otherwise, it is the kdump-compressed format. All the messages are output to standard error output by -F option because standard output is used for the dump data.<br />
 <code>Example:</code><br />
 # makedumpfile -F -c -d 31 -x vmlinux /proc/vmcore \<br />
 | ssh user [at] host &quot;cat &gt; dumpfile.tmp&quot;<br />
 # makedumpfile -F -c -d 31 -x vmlinux /proc/vmcore \<br />
 | ssh user [at] host &quot;makedumpfile -R dumpfile&quot;<br />
 # makedumpfile -F -E -d 31 -i vmcoreinfo /proc/vmcore \<br />
 | ssh user [at] host &quot;makedumpfile -R dumpfile&quot;<br />
 # makedumpfile -F -E &#8211;xen-vmcoreinfo <i>VMCOREINFO</i> /proc/vmcore \<br />
 | ssh user [at] host &quot;makedumpfile -R dumpfile&quot; </p>
<dt><code>-R</code></p>
<dd>Rearrange the dump data in the flattened format from the standard input to a normal <i>DUMPFILE</i> (readable with analysis tools).<br />
 <code>Example:</code><br />
 # makedumpfile -R dumpfile &lt; dumpfile.tmp<br />
 # makedumpfile -F -d 31 -x vmlinux /proc/vmcore \<br />
 | ssh user [at] host &quot;makedumpfile -R dumpfile&quot; </p>
<p> Instead of using -R option, a perl script &quot;makedumpfile-R.pl&quot; rearranges the dump data in the flattened format to a normal <i>DUMPFILE</i>, too. The perl script does not depend on architecture, and most systems have perl command. Even if a remote host does not have makedumpfile, it is possible to rearrange the dump data in the flattened format to a readable <i>DUMPFILE</i> on a remote host by running this script.<br />
 <code>Example:</code><br />
 # makedumpfile -F -d 31 -x vmlinux /proc/vmcore \<br />
 | ssh user [at] host &quot;makedumpfile-R.pl dumpfile&quot; </p>
<dt><code>&#8211;split</code></p>
<dd>Split the dump data to multiple <i>DUMPFILE</i>s in parallel. If specifying <i>DUMPFILE</i>s on different storage devices, a device can share I/O load with other devices and it reduces time for saving the dump data. The file size of each <i>DUMPFILE</i> is smaller than the system memory size which is divided by the number of <i>DUMPFILE</i>s. This feature supports only the kdump-compressed format.<br />
 <code>Example:</code><br />
 # makedumpfile &#8211;split -d 31 -x vmlinux /proc/vmcore dumpfile1 dumpfile2 </p>
<dt><code>&#8211;num-threads</code> <i>THREADNUM</i></p>
<dd>Using multiple threads to read and compress data of each page in parallel. And it will reduces time for saving <i>DUMPFILE</i>. Note that if the usable cpu number is less than the thread number, it may lead to great performance degradation. This feature only supports creating <i>DUMPFILE</i> in kdump-comressed format from <i>VMCORE</i> in kdump-compressed format or elf format.<br />
 <code>Example:</code><br />
 # makedumpfile -d 31 &#8211;num-threads 4 /proc/vmcore dumpfile </p>
<dt><code>&#8211;reassemble</code></p>
<dd>Reassemble multiple <i>DUMPFILE</i>s, which are created by &#8211;split option, into one <i>DUMPFILE</i>. dumpfile1 and dumpfile2 are reassembled into dumpfile on the following example.<br />
 <code>Example:</code><br />
 # makedumpfile &#8211;reassemble dumpfile1 dumpfile2 dumpfile </p>
<dt><code>-b</code> <i>&lt;order&gt;</i></p>
<dd>Cache 2^order pages in ram when generating <i>DUMPFILE</i> before writing to output. The default value is 4. </p>
<dt><code>&#8211;cyclic-buffer</code> <i>buffer_size</i></p>
<dd>Specify the buffer size in kilo bytes for bitmap data. Filtering processing will be divided into multi cycles to fix the memory consumption, the number of cycles is represented as: </p>
<p>&nbsp;<wbr>num_of_cycles&nbsp;<wbr>=&nbsp;<wbr>system_memory&nbsp;<wbr>/&nbsp;<wbr>(<i>buffer_size</i>&nbsp;<wbr>*&nbsp;<wbr>1024&nbsp;<wbr>*&nbsp;<wbr>bit_per_bytes&nbsp;<wbr>*&nbsp;<wbr>page_size&nbsp;<wbr>) </p>
<p> The lesser number of cycles, the faster working speed is expected. By default, <i>buffer_size</i> will be calculated automatically depending on system memory size, so ordinary users don&#8217;t need to specify this option. </p>
<p> <code>Example:</code><br />
 # makedumpfile &#8211;cyclic-buffer 1024 -d 31 -x vmlinux /proc/vmcore dumpfile </p>
<dt><code>&#8211;splitblock-size</code> <i>splitblock_size</i></p>
<dd>Specify the splitblock size in kilo bytes for analysis with &#8211;split. If &#8211;splitblock N is specified, difference of each splitted dumpfile size is at most N kilo bytes.<br />
 <code>Example:</code><br />
 # makedumpfile &#8211;splitblock-size 1024 -d 31 -x vmlinux &#8211;split /proc/vmcore dumpfile1 dumpfile2 </p>
<dd><code>&#8211;work-dir</code> Specify the working directory for the temporary bitmap file. If this option isn&#8217;t specified, the bitmap will be saved on memory. Filtering processing has to do 2 pass scanning to fix the memory consumption, but it can be avoided by using working directory on file system. So if you specify this option, the filtering speed may be bit faster. </p>
<p> <code>Example:</code><br />
 # makedumpfile &#8211;work-dir /tmp -d 31 -x vmlinux /proc/vmcore dumpfile </p>
<dt><code>&#8211;non-mmap</code></p>
<dd>Never use <code><a href="/docs/linux/man/2-mmap/">mmap</a>(2)</code> to read <i>VMCORE</i> even if it supports <code><a href="/docs/linux/man/2-mmap/">mmap</a>(2)</code>. Generally, reading <i>VMCORE</i> with <code><a href="/docs/linux/man/2-mmap/">mmap</a>(2)</code> is faster than without it, so ordinary users don&#8217;t need to specify this option. This option is mainly for debugging.<br />
 <code>Example:</code><br />
 # makedumpfile &#8211;non-mmap -d 31 -x vmlinux /proc/vmcore dumpfile </p>
<dt><code>&#8211;xen-syms</code> <i>XEN-SYMS</i></p>
<dd>Specify the <i>XEN-SYMS</i> with debug information to analyze the xen&#8217;s memory usage. This option extracts the part of xen and domain-0.<br />
 <code>Example:</code><br />
 # makedumpfile -E &#8211;xen-syms xen-syms /proc/vmcore dumpfile </p>
<dt><code>&#8211;xen-vmcoreinfo</code> <i>VMCOREINFO</i></p>
<dd>Specify <i>VMCOREINFO</i> instead of <i>XEN-SYMS</i> for analyzing the xen&#8217;s memory usage.<br />
 <i>VMCOREINFO</i> should be made beforehand by makedumpfile with -g option, and it contains the xen&#8217;s information.<br />
 <code>Example:</code><br />
 # makedumpfile -E &#8211;xen-vmcoreinfo <i>VMCOREINFO</i> /proc/vmcore dumpfile </p>
<dt><code>-X</code></p>
<dd>Exclude all the user domain pages from Xen kdump&#8217;s <i>VMCORE</i>, and extracts the part of xen and domain-0. If <i>VMCORE</i> contains <i>VMCOREINFO</i> for Xen, it is not necessary to specify <i>&#8211;xen-syms</i> and <i>&#8211;xen-vmcoreinfo</i>.<br />
 <code>Example:</code><br />
 # makedumpfile -E -X /proc/vmcore dumpfile </p>
<dt><code>&#8211;xen_phys_start</code> <i>xen_phys_start_address</i></p>
<dd>This option is only for x86_64. Specify the <i>xen_phys_start_address</i>, if the xen code/data is relocatable and <i>VMCORE</i> does not contain <i>xen_phys_start_address</i> in the CRASHINFO. <i>xen_phys_start_address</i> can be taken from the line of &quot;Hypervisor code and data&quot; in /proc/iomem. For example, specify 0xcee00000 as <i>xen_phys_start_address</i> if /proc/iomem is the following:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>cat&nbsp;<wbr>/proc/iomem<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>cee00000-cfd99999 : Hypervisor code and data<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;- </p>
<p> <code>Example:</code><br />
 # makedumpfile -E -X &#8211;xen_phys_start 0xcee00000 /proc/vmcore dumpfile </p>
<dt><code>&#8211;message-level</code> <i>message_level</i></p>
<dd>Specify the message types.<br />
 Users can restrict outputs printed by specifying <i>message_level</i> with this option. The message type marked with an X in the following table is printed. For example, according to the table, specifying 7 as <i>message_level</i> means progress indicator, common message, and error message are printed, and this is a default value. Note that the maximum value of <i>message_level</i> is 31. </p>
<p>&nbsp;<wbr>message | progress | common&nbsp;<wbr>&nbsp;<wbr>| error&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| debug&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| report<br />
&nbsp;<wbr>level&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| indicator| message | message | message | message<br />
 &#8212;&#8212;&#8212;+&#8212;&#8212;&#8212;-+&#8212;&#8212;&#8212;+&#8212;&#8212;&#8212;+&#8212;&#8212;&#8212;+&#8212;&#8212;&#8212;<br />
&nbsp;<wbr>0 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>1 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>2 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>3 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>4 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>5 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>6 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>7 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>8 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>9 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
10 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
11 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
12 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
13 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
14 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
15 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
16 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
17 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
18 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
19 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
20 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
21 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
22 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
23 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
24 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
25 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
26 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
27 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
28 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
29 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
30 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X<br />
31 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X </p>
<dt><code>&#8211;vtop</code> <i>virtual_address</i></p>
<dd>This option is useful, when user debugs the translation problem of virtual address. If specifing <i>virtual_address</i>, its physical address is printed. It makes debugging easy by comparing the output of this option with the one of &quot;vtop&quot; subcommand of the crash utility. &quot;&#8211;vtop&quot; option only prints the translation output, and it does not affect the dumpfile creation. </p>
<dt><code>&#8211;dump-dmesg</code></p>
<dd>This option overrides the normal behavior of makedumpfile. Instead of compressing and filtering a <i>VMCORE</i> to make it smaller, it simply extracts the dmesg log from a <i>VMCORE</i> and writes it to the specified <i>LOGFILE</i>. If a <i>VMCORE</i> does not contain <i>VMCOREINFO</i> for dmesg, it is necessary to specfiy [-x <i>VMLINUX</i>] or [-i <i>VMCOREINFO</i>]. </p>
<p> <code>Example:</code><br />
 # makedumpfile &#8211;dump-dmesg /proc/vmcore dmesgfile<br />
 # makedumpfile &#8211;dump-dmesg -x vmlinux /proc/vmcore dmesgfile </p>
<dt><code>&#8211;mem-usage</code></p>
<dd>This option is only for x86_64. This option is used to show the page numbers of current system in different use. It should be executed in 1st kernel. By the help of this, user can know how many pages is dumpable when different dump_level is specified. It analyzes the &#8216;System Ram&#8217; and &#8216;kernel text&#8217; program segment of /proc/kcore excluding the crashkernel range, then calculates the page number of different kind per vmcoreinfo. So currently /proc/kcore need be specified explicitly. </p>
<p> <code>Example:</code><br />
 # makedumpfile &#8211;mem-usage /proc/kcore </p>
<dt><code>&#8211;diskset=VMCORE</code></p>
<dd>Specify multiple <i>VMCORE</i>s created on sadump diskset configuration the same number of times as the number of <i>VMCORE</i>s in increasing order from left to right. <i>VMCORE</i>s are assembled into a single <i>DUMPFILE. </p>
<p> </i><code>Example:</code><br />
 # makedumpfile -x vmlinux &#8211;diskset=vmcore1 &#8211;diskset=vmcore2 dumpfile </p>
<dt><code>-D</code></p>
<dd>Print debugging message. </p>
<dt><code>-h (&#8211;help)</code></p>
<dd>Show help message and LZO/snappy support status (enabled/disabled). </p>
<dt><code>-v</code></p>
<dd>Show the version of makedumpfile. </p>
</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>TMPDIR</code></p>
<dd>This environment variable is used in 1st kernel environment for a temporary memory bitmap file. If your machine has a lots of memory and you use small tmpfs on /tmp, makedumpfile can fail for a little memory because makedumpfile makes a very large temporary memory bitmap file in this case. To avoid this failure, you should specify &#8211;work-dir option to use file system on storage for the bitmap file. </p>
</dl>
<h2>Diagnostics</h2>
<p>makedumpfile exits with the following value.</p>
<dl>
<dt><code>0</code> : makedumpfile succeeded.</p>
<dd>
<dt><code>1</code> : makedumpfile failed without the following reasons.</p>
<dd>
<dt><code>2</code> : makedumpfile failed due to the different version between <i>VMLINUX</i> and <i>VMCORE</i>.</p>
<dd></dl>
<h2>Authors</h2>
<p>Written by Masaki Tachibana, and Ken&#8217;ichi Ohmichi.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-crash/">crash</a>(8), <a href="/docs/linux/man/1-gdb/">gdb</a>(1), <a href="/docs/linux/man/8-kexec/">kexec</a>(8), <a href="/docs/linux/man/5-makedumpfile-conf/">makedumpfile.conf</a>(5) </p>
