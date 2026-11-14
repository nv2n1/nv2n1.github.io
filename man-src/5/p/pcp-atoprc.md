---
title: "pcp-atoprc(5)"
name: "pcp-atoprc"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pcp-atoprc/"
description: "atoprc – pcp-atop/pcp-atopsar related resource file"
---

<p><code>atoprc</code> &#8211; pcp-atop/pcp-atopsar related resource file</p>
<h2>Description</h2>
<p>This manual page documents the resource file of the <i>pcp-atop</i> and <i>pcp-atopsar</i> commands. These commands can be used to monitor the system and process load on a system. The pcp-atoprc file contains the default settings. These settings are read during startup, first from the system-wide rcfile <i>/etc/atoprc</i> and after that from the user-specific rcfile <i>~/.atoprc</i> (so system-wide settings can be overruled by an individual user). The options in both rcfiles are identical. </p>
<h2>Options</h2>
<p>The rcfile contains keyword-value pairs, one on every line (blank lines and lines starting with a #-sign are ignored).<br />
 The following keywords can be specified: </p>
<dl>
<dt><code>flags</code></p>
<dd>A list of default flags for <code>pcp-atop</code> can be defined here. The flags which are allowed are &#8216;g&#8217;, &#8216;m&#8217;, &#8216;d&#8217;, &#8216;n&#8217;, &#8216;u&#8217;, &#8216;p&#8217;, &#8216;s&#8217;, &#8216;c&#8217;, &#8216;v&#8217;, &#8216;C&#8217;, &#8216;M&#8217;, &#8216;D&#8217;, &#8216;N&#8217;, &#8216;A&#8217;, &#8216;a&#8217;, &#8216;y&#8217;, &#8216;f&#8217;, &#8216;F&#8217;, &#8216;G&#8217;, &#8216;R&#8217;, &#8216;1&#8217; and &#8216;x&#8217;.</dl>
<dl>
<dt><code>interval</code></p>
<dd>The default interval value in seconds.</dl>
<dl>
<dt><code>linelen</code></p>
<dd>The length of a screen line when sending output to a file or pipe (default 80).</dl>
<dl>
<dt><code>username</code></p>
<dd>The default regular expression for the users for which active processes will be shown.</dl>
<dl>
<dt><code>procname</code></p>
<dd>The default regular expression for the process names to be shown.</dl>
<dl>
<dt><code>maxlinecpu</code></p>
<dd>The maximum number of active CPU&#8217;s that will be shown.</dl>
<dl>
<dt><code>maxlinelvm</code></p>
<dd>The maximum number of active logical volumes that will be shown.</dl>
<dl>
<dt><code>maxlinemdd</code></p>
<dd>The maximum number of active multiple devices that will be shown.</dl>
<dl>
<dt><code>maxlinedisk</code></p>
<dd>The maximum number of active disks that will be shown.</dl>
<dl>
<dt><code>maxlinenfsm</code></p>
<dd>The maximum number of NFS mounts that will be shown on an NFS client.</dl>
<dl>
<dt><code>maxlineintf</code></p>
<dd>The maximum number of active network interfaces that will be shown.</dl>
<dl>
<dt><code>maxlinecont</code></p>
<dd>The maximum number of active containers that will be shown.</dl>
<dl>
<dt><code>cpucritperc</code></p>
<dd>The busy percentage considered critical for a processor (see section COLORS in the man-page of the <i>pcp-atop</i> command). This percentage is used to determine a weighted percentage for line coloring and sorting of active processes. When this value is zero, no line coloring or automatic sorting is performed for this resource.</dl>
<dl>
<dt><code>dskcritperc</code></p>
<dd>The busy percentage considered critical for a disk (see section COLORS in the man-page of the <i>pcp-atop</i> command). This percentage is used to determine a weighted percentage for line coloring and sorting of active processes. When this value is zero, no line coloring or automatic sorting is performed for this resource.</dl>
<dl>
<dt><code>netcritperc</code></p>
<dd>The busy percentage considered critical for a network interface (see section COLORS in the man-page of the <i>pcp-atop</i> command). This percentage is used to determine a weighted percentage for line coloring and sorting of active processes. When this value is zero, no line coloring or automatic sorting is performed for this resource.</dl>
<dl>
<dt><code>memcritperc</code></p>
<dd>The percentage considered critical for memory utilization (see section COLORS in the man-page of the <i>pcp-atop</i> command). This percentage is used to determine a weighted percentage for line coloring and sorting of active processes. When this value is zero, no line coloring or automatic sorting is performed for this resource.</dl>
<dl>
<dt><code>swpcritperc</code></p>
<dd>The occupation percentage considered critical for swap space (see section COLORS in the man-page of the <i>pcp-atop</i> command). This percentage is used to determine a weighted percentage for line coloring and sorting of active processes. When this value is zero, no line coloring or automatic sorting is performed for this resource.</dl>
<dl>
<dt><code>swoutcritsec</code></p>
<dd>The number of pages swapped out per second considered critical for for memory utilization (see section COLORS in the man-page of the <i>pcp-atop</i> command). This threshold is used in combination with &#8216;memcritperc&#8217; to determine a weighted percentage for line coloring and sorting of active processes. When this value is zero, no line coloring or automatic sorting is performed for this resource.</dl>
<dl>
<dt><code>almostcrit</code></p>
<dd>A percentage of the critical percentage to determine if the resource is almost critical (see section COLORS in the man-page of the <i>pcp-atop</i> command). When this value is zero, no line coloring for `almost critical&#8217; is performed.</dl>
<dl>
<dt><code>colorinfo</code></p>
<dd>Definition of color name for information messages (default: green).<br />
 Allowed colors are: red green yellow blue magenta cyan black white.</dl>
<dl>
<dt><code>colorthread</code></p>
<dd>Definition of color name for thread-specific lines when using the &#8216;y&#8217; option (default: yellow).<br />
 Allowed colors are: red green yellow blue magenta cyan black white.</dl>
<dl>
<dt><code>coloralmost</code></p>
<dd>Definition of color name for almost critical resources (default: cyan).<br />
 Allowed colors are: red green yellow blue magenta cyan black white.</dl>
<dl>
<dt><code>colorcritical</code></p>
<dd>Definition of color name for critical resources (default: red).<br />
 Allowed colors are: red green yellow blue magenta cyan black white.</dl>
<dl>
<dt><code>pcp-atopsarflags</code></p>
<dd>A list of default flags for <code>pcp-atopsar</code> can be defined here. The flags that are allowed are &#8216;S&#8217;, &#8216;x&#8217;, &#8216;C&#8217;, &#8216;M&#8217;, &#8216;H&#8217;, &#8216;a&#8217;, &#8216;A&#8217; and the flags to select one or more specific reports.</dl>
<p> An example of the <code>/etc/atoprc</code> or <code>~/.atoprc</code> file:</p>
<dl>
<dt>&nbsp;<wbr></p>
<dd>flags&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Aaf<br />
 interval&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5<br />
 username<br />
 procname<br />
 maxlinecpu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4<br />
 maxlinedisk&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10<br />
 maxlineintf&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5<br />
 cpucritperc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80<br />
 almostcrit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>90<br />
 pcp-atopsarflags&nbsp;<wbr>&nbsp;<wbr>CMH<br />
 ownprocline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PID:50 VGROW:40 RGROW:45 COMMAND-LINE:50<br />
 ownpagline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PAGSCAN:3 BLANKBOX:0 PAGSWIN:3 PAGSWOUT:7</dl>
<p> The keywords &#8216;ownprocline&#8217; and &#8216;ownpagline&#8217; are explained in the subsequent section.</p>
<h2>Own Definition Of Output Line</h2>
<p>Via the rcfile it is possible to define the layout of the output lines yourself, i.e. you can define the layout of one line with process information with the keyword &#8216;ownprocline&#8217; (to be selected with the key &#8216;o&#8217; or the flag -o) and you can redefine all lines with system information. </p>
<p> The layout of an output-line can be defined as follows (notice that this should be specified as one line in the rcfile): </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>keyword&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;columnid&gt;:&lt;prio&gt; [&lt;columnid&gt;:&lt;prio&gt; &#8230;] </p>
<p> The <code>columnid</code> is the symbolic name of a column that should shown at this position in the output line.<br />
 The <code>prio</code> is a positive integer value that determines which columns have precedence whenever not all specified columns fit into the current screen-width. The higher value, the higher priority.<br />
 The column-specifications should be separated by a space. The order in which columns have been specified is the order in which they will be shown, with respect to their priority (columns that do not fit, will be dropped dynamically). </p>
<p> A special columnid for system lines is &#8216;BLANKBOX&#8217;. This indicates that an empty column is required at this position. Also this special columnid is followed by a priority (usually low). </p>
<p> The following definition can be specified for process information: </p>
<dl>
<dt><code>ownprocline</code></p>
<dd>The columnid&#8217;s are the names of the columns that are shown in the normal output of the process-related lines that are shown by <i>pcp-atop</i> such as &#8216;PID&#8217;, &#8216;CMD&#8217;, &#8216;S&#8217;, &#8230;. The only exception is the special columnid &#8216;SORTITEM&#8217; that is used to show one of the columns CPU%/DSK%/MEM%/NET%, depending on the chosen sort-criterium.<br />
 An example of a user-defined process line:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>ownprocline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PID:20 PPID:10 SYSCPU:15 USRCPU:15 VGROW:14 VSIZE:12 RGROW:14 RSIZE:12 ST:8 EXC:7 S:11 SORTITEM:18 CMD:20</dl>
<p> The following definitions are used internally by <i>pcp-atop</i> as the default system lines (you can redefine each of them in the rcfile as one line): </p>
<dl>
<dt><code>ownsysprcline</code></p>
<dd>Redefinition of line labeled with &#8216;PRC&#8217;:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>ownsysprcline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PRCSYS:8 PRCUSER:8 BLANKBOX:0 PRCNPROC:7 PRCNZOMBIE:5 PRCCLONES:4 BLANKBOX:0 PRCNNEXIT:6</dl>
<dl>
<dt><code>ownallcpuline</code></p>
<dd>Redefinition of line labeled with &#8216;CPU&#8217; for total CPU-utilization:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>ownallcpuline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CPUSYS:8 CPUUSER:7 CPUIRQ:4 BLANKBOX:0 CPUIDLE:5 CPUWAIT:6 BLANKBOX:0 CPUSTEAL:1 CPUGUEST:3</dl>
<dl>
<dt><code>ownonecpuline</code></p>
<dd>Redefinition of line labeled with &#8216;CPU&#8217; for utilization of one CPU:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>ownonecpuline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CPUISYS:8 CPUIUSER:7 CPUIIRQ:4 BLANKBOX:0 CPUIIDLE:5 CPUIWAIT:6 BLANKBOX:0 CPUISTEAL:1 CPUIGUEST:3</dl>
<dl>
<dt><code>owncplline</code></p>
<dd>Redefinition of line labeled with &#8216;CPL&#8217;:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>owncplline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CPLAVG1:4 CPLAVG5:3 CPLAVG15:2 BLANKBOX:0 CPLCSW:6 CPLINTR:5 BLANKBOX:0 CPLNUMCPU:1</dl>
<dl>
<dt><code>ownmemline</code></p>
<dd>Redefinition of line labeled with &#8216;MEM&#8217;:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>ownmemline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MEMTOT:2 MEMFREE:5 MEMCACHE:3 MEMDIRTY:1 MEMBUFFER:3 MEMSLAB:3 BLANKBOX:0 BLANKBOX:0 BLANKBOX:0 BLANKBOX:0</dl>
<dl>
<dt><code>ownswpline</code></p>
<dd>Redefinition of line labeled with &#8216;SWP&#8217;:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>ownswpline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SWPTOT:3 SWPFREE:4 BLANKBOX:0 BLANKBOX:0 BLANKBOX:0 BLANKBOX:0 BLANKBOX:0 BLANKBOX:0 SWPCOMMITTED:5 SWPCOMMITLIM:6</dl>
<dl>
<dt><code>ownpagline</code></p>
<dd>Redefinition of line labeled with &#8216;PAG&#8217;:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>ownpagline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PAGSCAN:3 PAGSTALL:1 BLANKBOX:0 PAGSWIN:4 PAGSWOUT:3</dl>
<dl>
<dt><code>owndskline</code></p>
<dd>Redefinition of lines labeled with &#8216;LVM&#8217;, &#8216;MDD&#8217; and &#8216;DSK&#8217;:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>owndskline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DSKNAME:8 DSKBUSY:7 DSKNREAD:6 DSKNWRITE:6 DSKKBPERRD:4 DSKKBPERWR:4 DSKMBPERSECRD:5 DSKMBPERSECWR:5 DSKAVQUEUE:1 DSKAVIO:5</dl>
<dl>
<dt><code>ownnettrline</code></p>
<dd>Redefinition of line labeled with &#8216;NET&#8217; for transport:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>ownnettrline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NETTRANSPORT:9 NETTCPI:8 NETTCPO:8 NETUDPI:8 NETUDPO:8 NETTCPACTOPEN:6 NETTCPPASVOPEN:5 NETTCPRETRANS:4 NETTCPINERR:3 NETTCPORESET:20 NETUDPNOPORT:1 NETUDPINERR:3</dl>
<dl>
<dt><code>ownnetnetline</code></p>
<dd>Redefinition of line labeled with &#8216;NET&#8217; for network:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>ownnetnetline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NETNETWORK:5 NETIPI:4 NETIPO:4 NETIPFRW:4 NETIPDELIV:4 BLANKBOX:0 BLANKBOX:0 BLANKBOX:0 NETICMPIN:1 NETICMPOUT:1</dl>
<dl>
<dt><code>ownnetifline</code></p>
<dd>Redefinition of line labeled with &#8216;NET&#8217; for interfaces:</dl>
<dl>
<dt>&nbsp;<wbr></p>
<dd>ownnetifline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NETNAME:8 NETPCKI:7 NETPCKO:7 NETSPEEDIN:6 NETSPEEDOUT:6 NETCOLLIS:3 NETMULTICASTIN:2 NETRCVERR:5 NETSNDERR:5 NETRCVDROP:4 NETSNDDROP:4</dl>
<p> The lines above are shown in the order as shown by <i>pcp-atop</i> in combination with the <code>-f</code> flag (in a very wide window you should be able to see all of the columns).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1), <code><a href="/docs/linux/man/1-pcp-atop/">pcp-atop</a></code>(1), <code><a href="/docs/linux/man/1-pcp-atopsar/">pcp-atopsar</a></code>(1) and <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
