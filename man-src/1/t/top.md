---
title: "top(1)"
name: "top"
section: "1"
letter: "t"
url: "/docs/linux/man/1-top/"
description: "top – display Linux processes"
---

<h2 class="name">NAME</h2>
<p> top &#8211; display Linux processes</p>
<h2>SYNOPSIS</h2>
<p> <code>top</code> &#8211;<code>hv</code>|-<code>bcEeHiOSs1</code> &#8211;<code>d</code> secs &#8211;<code>n</code> max &#8211;<code>u</code>|<code>U</code> user &#8211;<code>p</code> pids &#8211;<code>o</code> field &#8211;<code>w</code> [cols] </p>
<p> The traditional switches `-&#8216; and whitespace are optional. </p>
<h2>DESCRIPTION</h2>
<p> The <code>top</code> program provides a dynamic real-time view of a running system. It can display<code> system</code> summary information as well as a list of <code>processes</code> or <code>threads</code> currently being managed by the Linux kernel. The types of system summary information shown and the types, order and size of information displayed for processes are all user configurable and that configuration can be made persistent across restarts. </p>
<p> The program provides a limited interactive interface for process manipulation as well as a much more extensive interface for personal configuration &nbsp;&#8212;&nbsp; encompassing every aspect of its operation. And while <code>top</code> is referred to throughout this document, you are free to name the program anything you wish. That new name, possibly an alias, will then be reflected on top&#8217;s display and used when reading and writing a configuration file. </p>
<h2>OVERVIEW</h2>
<h3>Documentation</h3>
<p> The remaining Table of Contents </p>
<pre>
    OVERVIEW
       Operation
       Linux Memory Types
    1. COMMAND-LINE Options
    2. SUMMARY Display
       a. UPTIME and LOAD Averages
       b. TASK and CPU States
       c. MEMORY Usage
    3. FIELDS / Columns Display
       a. DESCRIPTIONS of Fields
       b. MANAGING Fields
    4. INTERACTIVE Commands
       a. GLOBAL Commands
       b. SUMMARY AREA Commands
       c. TASK AREA Commands
          1. Appearance
          2. Content
          3. Size
          4. Sorting
       d. COLOR Mapping
    5. ALTERNATE-DISPLAY Provisions
       a. WINDOWS Overview
       b. COMMANDS for Windows
       c. SCROLLING a Window
       d. SEARCHING in a Window
       e. FILTERING in a Window
    6. FILES
       a. PERSONAL Configuration File
       b. ADDING INSPECT Entries
       c. SYSTEM Configuration File
       d. SYSTEM Restrictions File
    7. STUPID TRICKS Sampler
       a. Kernel Magic
       b. Bouncing Windows
       c. The Big Bird Window
       d. The Ol' Switcheroo
    8. BUGS, 9. SEE Also
</pre>
<h3>Operation</h3>
<p> When operating top, the two most important keys are the help (h or ?) key and quit (`q&#8217;) key. Alternatively, you could simply use the traditional interrupt key (^C) when you&#8217;re done. </p>
<p> When started for the first time, you&#8217;ll be presented with these traditional elements on the main top screen: 1) Summary Area; 2) Fields/Columns Header; 3) Task Area. Each of these will be explored in the sections that follow. There is also an Input/Message line between the Summary Area and Columns Header which needs no further explanation. </p>
<p> The main top screen is <i>generally</i> quite adaptive to changes in terminal dimensions under X-Windows. Other top screens may be less so, especially those with static text. It ultimately depends, however, on your particular window manager and terminal emulator. There may be occasions when their view of terminal size and current contents differs from top&#8217;s view, which is always based on operating system calls. </p>
<p> Following any re-size operation, if a top screen is corrupted, appears incomplete or disordered, simply typing something innocuous like a punctuation character or cursor motion key will usually restore it. In extreme cases, the following sequence almost certainly will: </p>
<pre>
       <i>key/cmd  objective </i>
       ^Z       <code>suspend</code> top
       fg       <code>resume</code> top
       &lt;Left&gt;   force a screen <code>redraw</code> (if necessary)
</pre>
<p> But if the display is still corrupted, there is one more step you could try. Insert this command after top has been suspended but before resuming it. </p>
<pre>
       <i>key/cmd  objective </i>
       reset    restore your <code>terminal settings</code>
</pre>
<p> <code>Note</code>: the width of top&#8217;s display will be limited to 512 positions. Displaying all fields requires approximately 250 characters. Remaining screen width is usually allocated to any variable width columns currently visible. The variable width columns, such as COMMAND, are noted in topic 3a. DESCRIPTIONS of Fields. Actual output width may also be influenced by the -w switch, which is discussed in topic 1. COMMAND-LINE Options. </p>
<p> Lastly, some of top&#8217;s screens or functions require the use of cursor motion keys like the standard arrow keys plus the Home, End, PgUp and PgDn keys. If your terminal or emulator does not provide those keys, the following combinations are accepted as alternatives: </p>
<pre>
      <i> key      equivalent-keys </i>
       Left     alt +<code> h </code>
       Down     alt +<code> j </code>
       Up       alt +<code> k </code>
       Right    alt +<code> l </code>
       Home     alt + ctrl +<code> h </code>
       PgDn     alt + ctrl +<code> j </code>
       PgUp     alt + ctrl +<code> k </code>
       End      alt + ctrl +<code> l </code>
</pre>
<p> The <code>Up</code> and <code>Down</code> arrow keys have special significance when prompted for line input terminated with the &lt;Enter&gt; key. Those keys, or their aliases, can be used to retrieve previous input lines which can then be edited and re-input. And there are four additional keys available with line oriented input. </p>
<pre>
      <i> key      special-significance </i>
       Up       recall <code>older</code> strings for re-editing
       Down     recall <code>newer</code> strings or <code>erase</code> entire line
       Insert   toggle between <code>insert</code> and <code>overtype</code> modes
       Delete   character <code>removed</code> at cursor, moving others left
       Home     jump to <code>beginning</code> of input line
       End      jump to <code>end</code> of input line
</pre>
<h3>Linux Memory Types</h3>
<p> For our purposes there are three types of memory, and one is optional. First is physical memory, a limited resource where code and data must reside when executed or referenced. Next is the optional swap file, where modified (dirty) memory can be saved and later retrieved if too many demands are made on physical memory. Lastly we have virtual memory, a nearly unlimited resource serving the following goals: </p>
<pre>
   1. abstraction, free from physical memory addresses/limits
   2. isolation, every process in a separate address space
   3. sharing, a single mapping can serve multiple needs
   4. flexibility, assign a virtual address to a file
</pre>
<p> Regardless of which of these forms memory may take, all are managed as pages (typically 4096 bytes) but expressed by default in top as KiB (kibibyte). The memory discussed under topic `2c. MEMORY Usage&#8217; deals with physical memory and the swap file for the system as a whole. The memory reviewed in topic `3. FIELDS / Columns Display&#8217; embraces all three memory types, but for individual processes. </p>
<p> For each such process, every memory page is restricted to a single quadrant from the table below. Both physical memory and virtual memory can include any of the four, while the swap file only includes #1 through #3. The memory in quadrant #4, when modified, acts as its own dedicated swap file. </p>
<pre><code>
Private | Shared 1 | 2 Anonymous.stack |
                         .malloc() |
                         .brk() / sbrk() |.POSIX shm *.mmap(PRIVATE, ANON) |.mmap(SHARED, ANON)-- -- -- -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- --.mmap(PRIVATE, fd) |.mmap(SHARED, fd) File - backed.pgms / shared libs |
    3 | 4
</code></pre>
<p> The following may help in interpreting process level memory values displayed as scalable columns and discussed under topic `3a. DESCRIPTIONS of Fields&#8217;. </p>
<pre>
   %MEM - simply RES divided by total physical memory
   CODE - the `pgms' portion of quadrant <code>3</code>
   DATA - the entire quadrant <code>1</code> portion of VIRT plus all
          explicit mmap file-backed pages of quadrant <code>3</code>
   RES  - anything occupying physical memory which, beginning with
          Linux-4.5, is the sum of the following three fields:
          RSan - quadrant <code>1</code> pages, which include any
                 former quadrant <code>3</code> pages if modified
          RSfd - quadrant <code>3</code> and quadrant <code>4</code> pages
          RSsh - quadrant <code>2</code> pages
   RSlk - subset of RES which cannot be swapped out (any quadrant)
   SHR  - subset of RES (excludes <code>1</code>, includes all <code>2</code> &amp; <code>4</code>, some <code>3</code>)
   SWAP - potentially any quadrant except <code>4</code>
   USED - simply the sum of RES and SWAP
   VIRT - everything in-use and/or reserved (all quadrants)
</pre>
<p> <code>Note</code>: Even though program images and shared libraries are considered <i>private</i> to a process, they will be accounted for as <i>shared</i> (SHR) by the kernel. </p>
<h2>1. COMMAND-LINE Options</h2>
<p> The command-line syntax for top consists of: </p>
<p>&nbsp;<wbr>&nbsp;&#8211;<code>hv</code>|-<code>bcEeHiOSs1</code> &#8211;<code>d</code> secs &#8211;<code>n</code> max &#8211;<code>u</code>|<code>U</code> user &#8211;<code>p</code> pids &#8211;<code>o</code> field &#8211;<code>w</code> [cols] </p>
<p> The typically mandatory switch (`-&#8216;) and even whitespace are completely optional. </p>
<dl>
<dt>&#8211;<code>h</code> | &#8211;<code>v</code>&nbsp;<wbr>&nbsp;:<i>Help/Version </i></p>
<dd> Show library version and the usage prompt, then quit. </p>
<dt>&#8211;<code>b</code>&nbsp;<wbr>&nbsp;:<i>Batch-mode</i> operation</p>
<dd> Starts top in Batch mode, which could be useful for sending output from top to other programs or to a file. In this mode, top will not accept input and runs until the iterations limit you&#8217;ve set with the `-n&#8217; command-line option or until killed. </p>
<dt>&#8211;<code>c</code>&nbsp;<wbr>&nbsp;:<i>Command-line/Program-name</i> toggle</p>
<dd> Starts top with the last remembered `c&#8217; state reversed. Thus, if top was displaying command lines, now that field will show program names, and vice versa. See the `c&#8217; interactive command for additional information. </p>
<dt>&#8211;<code>d</code>&nbsp;<wbr>&nbsp;:<i>Delay-time</i> interval as:&nbsp;<wbr>&nbsp;<code>-d ss.t</code> (<i>secs</i>.<i>tenths</i>)</p>
<dd> Specifies the delay between screen updates, and overrides the corresponding value in one&#8217;s personal configuration file or the startup default. Later this can be changed with the `d&#8217; or `s&#8217; interactive commands. </p>
<p> Fractional seconds are honored, but a negative number is not allowed. In all cases, however, such changes are prohibited if top is running in Secure mode, except for root (unless the `s&#8217; command-line option was used). For additional information on Secure mode see topic 6d. SYSTEM Restrictions File. </p>
<dt>&#8211;<code>e</code>&nbsp;<wbr>&nbsp;:<i>Enforce-Task-Memory-Scaling</i> as:&nbsp;<wbr>&nbsp;<code>-e k</code> | <code>m</code> | <code>g</code> | <code>t</code> | <code>p</code></p>
<dd> Instructs top to force task area memory to be scaled as: </p>
<pre>
   k - kibibytes
   m - mebibytes
   g - gibibytes
   t - tebibytes
   p - pebibytes
</pre>
<p> Later this can be changed with the `e&#8217; command toggle. </p>
<dt>&#8211;<code>E</code>&nbsp;<wbr>&nbsp;:<i>Enforce-Summary-Memory-Scaling</i> as:&nbsp;<wbr>&nbsp;<code>-E k</code> | <code>m</code> | <code>g</code> | <code>t</code> | <code>p</code> | <code>e</code></p>
<dd> Instructs top to force summary area memory to be scaled as: </p>
<pre>
   k - kibibytes
   m - mebibytes
   g - gibibytes
   t - tebibytes
   p - pebibytes
   e - exbibytes
</pre>
<p> Later this can be changed with the `E&#8217; command toggle. </p>
<dt>&#8211;<code>H</code>&nbsp;<wbr>&nbsp;:<i>Threads-mode</i> operation</p>
<dd> Instructs top to display individual threads. Without this command-line option a summation of all threads in each process is shown. Later this can be changed with the `H&#8217; interactive command. </p>
<dt>&#8211;<code>i</code>&nbsp;<wbr>&nbsp;:<i>Idle-process</i> toggle</p>
<dd> Starts top with the last remembered `i&#8217; state reversed. When this toggle is <i>Off</i>, tasks that have not used any CPU since the last update will not be displayed. For additional information regarding this toggle see topic 4c. TASK AREA Commands, SIZE. </p>
<dt>&#8211;<code>n</code>&nbsp;<wbr>&nbsp;:<i>Number-of-iterations</i> limit as:<code>&nbsp;<wbr>&nbsp;-n number </code></p>
<dd> Specifies the maximum number of iterations, or frames, top should produce before ending. </p>
<dt>&#8211;<code>o</code>&nbsp;<wbr>&nbsp;:<i>Override-sort-field</i> as:<code>&nbsp;<wbr>&nbsp;-o fieldname </code></p>
<dd> Specifies the name of the field on which tasks will be sorted, independent of what is reflected in the configuration file. You can prepend a `+&#8217; or `-&#8216; to the field name to also override the sort direction. A leading `+&#8217; will force sorting high to low, whereas a `-&#8216; will ensure a low to high ordering. </p>
<p> This option exists primarily to support automated/scripted batch mode operation. </p>
<dt>&#8211;<code>O</code>&nbsp;<wbr>&nbsp;:<i>Output-field-names </i></p>
<dd> This option acts as a form of help for the above -o option. It will cause top to print each of the available field names on a separate line, then quit. Such names are subject to NLS (National Language Support) translation. </p>
<dt>&#8211;<code>p</code>&nbsp;<wbr>&nbsp;:<i>Monitor-PIDs</i> mode as:<code>&nbsp;<wbr>&nbsp;-pN1 -pN2 &#8230;</code>&nbsp;<wbr>&nbsp;or<code>&nbsp;<wbr>&nbsp;-pN1,N2,N3 &#8230; </code></p>
<dd> Monitor only processes with specified process IDs. This option can be given up to 20 times, or you can provide a comma delimited list with up to 20 pids. Co-mingling both approaches is permitted. </p>
<p> A pid value of zero will be treated as the process id of the top program itself once it is running. </p>
<p> This is a command-line option only and should you wish to return to normal operation, it is not necessary to quit and restart top &nbsp;&#8212;&nbsp; just issue any of these interactive commands: `=&#8217;, `u&#8217; or `U&#8217;. </p>
<p> The `p&#8217;, `u&#8217; and `U&#8217; command-line options are mutually exclusive. </p>
<dt>&#8211;<code>s</code>&nbsp;<wbr>&nbsp;:<i>Secure-mode</i> operation</p>
<dd> Starts top with secure mode forced, even for root. This mode is far better controlled through a system configuration file (see topic 6. FILES). </p>
<dt>&#8211;<code>S</code>&nbsp;<wbr>&nbsp;:<i>Cumulative-time</i> toggle</p>
<dd> Starts top with the last remembered `S&#8217; state reversed. When Cumulative time mode is <i>On</i>, each process is listed with the cpu time that it and its dead children have used. See the `S&#8217; interactive command for additional information regarding this mode. </p>
<dt>&#8211;<code>u</code> | &#8211;<code>U</code>&nbsp;<wbr>&nbsp;:<i>User-filter-mode</i> as:&nbsp;<wbr>&nbsp;<code>-u</code> | <code>-U number</code> or<code> name </code></p>
<dd> Display only processes with a user id or user name matching that given. The `-u&#8217; option matches on <i> effective</i> user whereas the `-U&#8217; option matches on<i> any</i> user (real, effective, saved, or filesystem). </p>
<p> Prepending an exclamation point (`!&#8217;) to the user id or name instructs top to display only processes with users not matching the one provided. </p>
<p> The `p&#8217;, `u&#8217; and `U&#8217; command-line options are mutually exclusive. </p>
<dt>&#8211;<code>w</code>&nbsp;<wbr>&nbsp;:<i>Output-width-override</i> as:&nbsp;<wbr>&nbsp;<code>-w</code> [<code> number</code> ]</p>
<dd> In Batch mode, when used without an argument top will format output using the COLUMNS= and LINES= environment variables, if set. Otherwise, width will be fixed at the maximum 512 columns. With an argument, output width can be decreased or increased (up to 512) but the number of rows is considered unlimited. </p>
<p> In normal display mode, when used without an argument top will<i> attempt</i> to format output using the COLUMNS= and LINES= environment variables, if set. With an argument, output width can only be decreased, not increased. Whether using environment variables or an argument with -w, when<i> not</i> in Batch mode actual terminal dimensions can never be exceeded. </p>
<p> <code>Note</code>: Without the use of this command-line option, output width is always based on the terminal at which top was invoked whether or not in Batch mode. </p>
<dt>&#8211;<code>1</code>&nbsp;<wbr>&nbsp;:<i>Single/Separate-Cpu-States</i> toggle</p>
<dd> Starts top with the last remembered Cpu States portion of the summary area reversed. Either all cpu information will be displayed in a single line or each cpu will be displayed separately, depending on the state of the NUMA Node command toggle (&#8216;2&#8242;). </p>
<p> See the `1&#8217; and &#8216;2&#8217; interactive commands for additional information. </p>
</dl>
<h2>2. SUMMARY Display</h2>
<p> Each of the following three areas are individually controlled through one or more interactive commands. See topic 4b. SUMMARY AREA Commands for additional information regarding these provisions. </p>
<h3>2a. UPTIME and LOAD Averages</h3>
<p> This portion consists of a single line containing: </p>
<pre>
    <code>program</code> or<code> window</code> name, depending on display mode
    current time and length of time since last boot
    total number of users
    system load avg over the last 1, 5 and 15 minutes
</pre>
<h3>2b. TASK and CPU States</h3>
<p> This portion consists of a minimum of two lines. In an SMP environment, additional lines can reflect individual CPU state percentages. </p>
<p> Line 1 shows total<code> tasks</code> or<code> threads</code>, depending on the state of the Threads-mode toggle. That total is further classified as: </p>
<pre>
    running; sleeping; stopped; zombie
</pre>
<p> Line 2 shows CPU state percentages based on the interval since the last refresh. </p>
<p> As a default, percentages for these individual categories are displayed. Where two labels are shown below, those for more recent kernel versions are shown first. </p>
<pre>
    <code>us</code>,<code> user</code>    : time running un-niced user processes
    <code>sy</code>,<code> system</code>  : time running kernel processes
    <code>ni</code>,<code> nice</code>    : time running niced user processes
    <code>id</code>,<code> idle</code>    : time spent in the kernel idle handler
    <code>wa</code>,<code> IO-wait</code> : time waiting for I/O completion
    <code>hi</code> : time spent servicing hardware interrupts
    <code>si</code> : time spent servicing software interrupts
    <code>st</code> : time stolen from this vm by the hypervisor
</pre>
<p> In the alternate cpu states display modes, beyond the first tasks/threads line, an abbreviated summary is shown consisting of these elements: </p>
<pre>
               a    b     c    d
    %Cpu(s):  <code>75.0</code>/25.0  <code>100</code>[ ...
</pre>
<p> Where: a) is the `user&#8217; (us + ni) percentage; b) is the `system&#8217; (sy + hi + si) percentage; c) is the total; and d) is one of two visual graphs of those representations. See topic 4b. SUMMARY AREA Commands and the `t&#8217; command for additional information on that special 4-way toggle. </p>
<h3>2c. MEMORY Usage</h3>
<p> This portion consists of two lines which may express values in kibibytes (KiB) through exbibytes (EiB) depending on the scaling factor enforced with the `E&#8217; interactive command. </p>
<p> As a default, Line 1 reflects physical memory, classified as: </p>
<pre>
    total, free, used and buff/cache
</pre>
<p> Line 2 reflects mostly virtual memory, classified as: </p>
<pre>
    total, free, used and avail (which is physical memory)
</pre>
<p> The <code>avail</code> number on line 2 is an estimation of physical memory available for starting new applications, without swapping. Unlike the <code>free</code> field, it attempts to account for readily reclaimable page cache and memory slabs. It is available on kernels 3.14, emulated on kernels 2.6.27+, otherwise the same as <code>free</code>. </p>
<p> In the alternate memory display modes, two abbreviated summary lines are shown consisting of these elements: </p>
<pre>
               a    b          c
    GiB Mem : <code>18.7</code>/15.738   [ ...
    GiB Swap: <code> 0.0</code>/7.999    [ ...
</pre>
<p> Where: a) is the percentage used; b) is the total available; and c) is one of two visual graphs of those representations. </p>
<p> In the case of physical memory, the percentage represents the <code>total</code> minus the estimated <code>avail</code> noted above. The `Mem&#8217; graph itself is divided between <code>used</code> and any remaining memory not otherwise accounted for by <code>avail</code>. See topic 4b. SUMMARY AREA Commands and the `m&#8217; command for additional information on that special 4-way toggle. </p>
<p> This table may help in interpreting the scaled values displayed: </p>
<pre>
    KiB = kibibyte = 1024 bytes
    MiB = mebibyte = 1024 KiB = 1,048,576 bytes
    GiB = gibibyte = 1024 MiB = 1,073,741,824 bytes
    TiB = tebibyte = 1024 GiB = 1,099,511,627,776 bytes
    PiB = pebibyte = 1024 TiB = 1,125,899,906,842,624 bytes
    EiB = exbibyte = 1024 PiB = 1,152,921,504,606,846,976 bytes
</pre>
<h2>3. FIELDS / Columns</h2>
<h3>3a. DESCRIPTIONS of Fields</h3>
<p> Listed below are top&#8217;s available process fields (columns). They are shown in strict ascii alphabetical order. You may customize their position and whether or not they are displayable with the `f&#8217; or `F&#8217; (Fields Management) interactive commands. </p>
<p> Any field is selectable as the sort field, and you control whether they are sorted high-to-low or low-to-high. For additional information on sort provisions see topic 4c. TASK AREA Commands, SORTING. </p>
<p> The fields related to physical memory or virtual memory reference `(KiB)&#8217; which is the unsuffixed display mode. Such fields may, however, be scaled from KiB through PiB. That scaling is influenced via the `e&#8217; interactive command or established for startup through a build option. </p>
<dl>
<dt>
&nbsp;1.<code>&nbsp;%CPU&nbsp;<wbr>&nbsp;&#8212;&nbsp;<wbr>&nbsp;CPU Usage&nbsp;</code></p>
<dd> The task&#8217;s share of the elapsed CPU time since the last screen update, expressed as a percentage of total CPU time. </p>
<p> In a true SMP environment, if a process is multi-threaded and top is <i>not</i> operating in Threads mode, amounts greater than 100% may be reported. You toggle Threads mode with the `H&#8217; interactive command. </p>
<p> Also for multi-processor environments, if Irix mode is <i>Off</i>, top will operate in Solaris mode where a task&#8217;s cpu usage will be divided by the total number of CPUs. You toggle Irix/Solaris modes with the `I&#8217; interactive command. </p>
<p> <code>Note</code>: When running in forest view mode (`V&#8217;) with children collapsed (`v&#8217;), this field will also include the CPU time of those unseen children. See topic 4c. TASK AREA Commands, CONTENT for more information regarding the `V&#8217; and `v&#8217; toggles. </p>
<dt>
&nbsp;2.<code>&nbsp;%MEM&nbsp;<wbr>&nbsp;&#8212;&nbsp;<wbr>&nbsp;Memory Usage&nbsp;(RES)&nbsp;</code></p>
<dd> A task&#8217;s currently resident share of available physical memory. </p>
<p> See `OVERVIEW, Linux Memory Types&#8217; for additional details. </p>
<dt>
&nbsp;3.<code>&nbsp;CGNAME&nbsp;<wbr>&nbsp;&#8212;&nbsp;<wbr>&nbsp;Control Group Name&nbsp;</code></p>
<dd> The name of the control group to which a process belongs, or `-&#8216; if not applicable for that process. </p>
<p> This will typically be the last entry in the full list of control groups as shown under the next heading (CGROUPS). And as is true there, this field is also variable width. </p>
<dt>
&nbsp;4.<code>&nbsp;CGROUPS&nbsp;<wbr>&nbsp;&#8212;&nbsp;<wbr>&nbsp;Control Groups&nbsp;</code></p>
<dd> The names of the control group(s) to which a process belongs, or `-&#8216; if not applicable for that process. </p>
<p> Control Groups provide for allocating resources (cpu, memory, network bandwidth, etc.) among installation-defined groups of processes. They enable fine-grained control over allocating, denying, prioritizing, managing and monitoring those resources. </p>
<p> Many different hierarchies of cgroups can exist simultaneously on a system and each hierarchy is attached to one or more subsystems. A subsystem represents a single resource. </p>
<p> <code>Note</code>: The CGROUPS field, unlike most columns, is not fixed-width. When displayed, it plus any other variable width columns will be allocated all remaining screen width (up to the maximum 512 characters). Even so, such variable width fields could still suffer truncation. See topic 5c. SCROLLING a Window for additional information on accessing any truncated data. </p>
<dt>
&nbsp;5.<code>&nbsp;CODE&nbsp;<wbr>&nbsp;&#8212;&nbsp;<wbr>&nbsp;Code Size&nbsp;(KiB)&nbsp;</code></p>
<dd> The amount of physical memory currently devoted to executable code, also known as the Text Resident Set size or TRS. </p>
<p> See `OVERVIEW, Linux Memory Types&#8217; for additional details. </p>
<dt>
&nbsp;6.<code>&nbsp;COMMAND&nbsp;<wbr>&nbsp;&#8212;&nbsp;<wbr>&nbsp;Command Name</code>&nbsp;or Command<code>&nbsp;Line&nbsp;</code></p>
<dd> Display the command line used to start a task or the name of the associated program. You toggle between command<i> line</i> and<i> name</i> with `c&#8217;, which is both a command-line option and an interactive command. </p>
<p> When you&#8217;ve chosen to display command lines, processes without a command line (like kernel threads) will be shown with only the program name in brackets, as in this example:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[kthreadd] </p>
<p> This field may also be impacted by the forest view display mode. See the `V&#8217; interactive command for additional information regarding that mode. </p>
<p> <code>Note</code>: The COMMAND field, unlike most columns, is not fixed-width. When displayed, it plus any other variable width columns will be allocated all remaining screen width (up to the maximum 512 characters). Even so, such variable width fields could still suffer truncation. This is especially true for this field when command lines are being displayed (the `c&#8217; interactive command.) See topic 5c. SCROLLING a Window for additional information on accessing any truncated data. </p>
<dt>
&nbsp;7.<code>&nbsp;DATA&nbsp;<wbr>&nbsp;&#8212;&nbsp;<wbr>&nbsp;Data&nbsp;+&nbsp;Stack Size&nbsp;(KiB)&nbsp;</code></p>
<dd> The amount of private memory <i>reserved</i> by a process. It is also known as the Data Resident Set or DRS. Such memory may not yet be mapped to physical memory (RES) but will always be included in the virtual memory (VIRT) amount. </p>
<p> See `OVERVIEW, Linux Memory Types&#8217; for additional details. </p>
<dt>
&nbsp;8.<code>&nbsp;ENVIRON&nbsp;<wbr>&nbsp;&#8212;&nbsp;<wbr>&nbsp;Environment variables&nbsp;</code></p>
<dd> Display all of the environment variables, if any, as seen by the respective processes. These variables will be displayed in their raw native order, not the sorted order you are accustomed to seeing with an unqualified `set&#8217;. </p>
<p> <code>Note</code>: The ENVIRON field, unlike most columns, is not fixed-width. When displayed, it plus any other variable width columns will be allocated all remaining screen width (up to the maximum 512 characters). Even so, such variable width fields could still suffer truncation. This is especially true for this field. See topic 5c. SCROLLING a Window for additional information on accessing any truncated data. </p>
<dt>
&nbsp;9.<code>&nbsp;Flags&nbsp;<wbr>&nbsp;&#8212;&nbsp;<wbr>&nbsp;Task Flags&nbsp;</code></p>
<dd> This column represents the task&#8217;s current scheduling flags which are expressed in hexadecimal notation and with zeros suppressed. These flags are officially documented in &lt;linux/sched.h&gt;. </p>
<dt>10.<code> GID &nbsp;&#8212;&nbsp; Group Id </code></p>
<dd> The<i> effective</i> group ID. </p>
<dt>11.<code> GROUP &nbsp;&#8212;&nbsp; Group Name </code></p>
<dd> The<i> effective</i> group name. </p>
<dt>12.<code> LXC &nbsp;&#8212;&nbsp; Lxc Container Name </code></p>
<dd> The name of the lxc container within which a task is running. If a process is not running inside a container, a dash (`-&#8216;) will be shown. </p>
<dt>13.<code> NI &nbsp;&#8212;&nbsp; Nice Value </code></p>
<dd> The nice value of the task. A negative nice value means higher priority, whereas a positive nice value means lower priority. Zero in this field simply means priority will not be adjusted in determining a task&#8217;s dispatch-ability. </p>
<dt>14.<code> NU &nbsp;&#8212;&nbsp; Last known NUMA node </code></p>
<dd> A number representing the NUMA node associated with the last used processor (`P&#8217;). When -1 is displayed it means that NUMA information is not available. </p>
<p> See the `&#8217;2&#8242; and `3&#8242; interactive commands for additional NUMA provisions affecting the summary area. </p>
<dt>15.<code> OOMa &nbsp;&#8212;&nbsp; Out of Memory Adjustment Factor </code></p>
<dd> The value, ranging from -1000 to +1000, added to the current out of memory score (OOMs) which is then used to determine which task to kill when memory is exhausted. </p>
<dt>16.<code> OOMs &nbsp;&#8212;&nbsp; Out of Memory Score </code></p>
<dd> The value, ranging from 0 to +1000, used to select task(s) to kill when memory is exhausted. Zero translates to `never kill&#8217; whereas 1000 means `always kill&#8217;. </p>
<dt>17.<code> P &nbsp;&#8212;&nbsp; Last used CPU (SMP) </code></p>
<dd> A number representing the last used processor. In a true SMP environment this will likely change frequently since the kernel intentionally uses weak affinity. Also, the very act of running top may break this weak affinity and cause more processes to change CPUs more often (because of the extra demand for cpu time). </p>
<dt>18.<code> PGRP &nbsp;&#8212;&nbsp; Process Group Id </code></p>
<dd> Every process is member of a unique process group which is used for distribution of signals and by terminals to arbitrate requests for their input and output. When a process is created (forked), it becomes a member of the process group of its parent. By convention, this value equals the process ID (see PID) of the first member of a process group, called the process group leader. </p>
<dt>19.<code> PID &nbsp;&#8212;&nbsp; Process Id </code></p>
<dd> The task&#8217;s unique process ID, which periodically wraps, though never restarting at zero. In kernel terms, it is a dispatchable entity defined by a task_struct. </p>
<p> This value may also be used as: a process group ID (see PGRP); a session ID for the session leader (see SID); a thread group ID for the thread group leader (see TGID); and a TTY process group ID for the process group leader (see TPGID). </p>
<dt>20.<code> PPID &nbsp;&#8212;&nbsp; Parent Process Id </code></p>
<dd> The process ID (pid) of a task&#8217;s parent. </p>
<dt>21.<code> PR &nbsp;&#8212;&nbsp; Priority </code></p>
<dd> The scheduling priority of the task. If you see `rt&#8217; in this field, it means the task is running under real time scheduling priority. </p>
<p> Under linux, real time priority is somewhat misleading since traditionally the operating itself was not preemptible. And while the 2.6 kernel can be made mostly preemptible, it is not always so. </p>
<dt>22.<code> RES &nbsp;&#8212;&nbsp; Resident Memory Size (KiB) </code></p>
<dd> A subset of the virtual address space (VIRT) representing the non-swapped physical memory a task is currently using. It is also the sum of the RSan, RSfd and RSsh fields. </p>
<p> It can include private anonymous pages, private pages mapped to files (including program images and shared libraries) plus shared anonymous pages. All such memory is backed by the swap file represented separately under SWAP. </p>
<p> Lastly, this field may also include shared file-backed pages which, when modified, act as a dedicated swap file and thus will never impact SWAP. </p>
<p> See `OVERVIEW, Linux Memory Types&#8217; for additional details. </p>
<dt>23.<code> RSan &nbsp;&#8212;&nbsp; Resident Anonymous Memory Size (KiB) </code></p>
<dd> A subset of resident memory (RES) representing private pages not mapped to a file. </p>
<dt>24.<code> RSfd &nbsp;&#8212;&nbsp; Resident File-Backed Memory Size (KiB) </code></p>
<dd> A subset of resident memory (RES) representing the implicitly shared pages supporting program images and shared libraries. It also includes explicit file mappings, both private and shared. </p>
<dt>25.<code> RSlk &nbsp;&#8212;&nbsp; Resident Locked Memory Size (KiB) </code></p>
<dd> A subset of resident memory (RES) which cannot be swapped out. </p>
<dt>26.<code> RSsh &nbsp;&#8212;&nbsp; Resident Shared Memory Size (KiB) </code></p>
<dd> A subset of resident memory (RES) representing the explicitly shared anonymous shm*/mmap pages. </p>
<dt>27.<code> RUID &nbsp;&#8212;&nbsp; Real User Id </code></p>
<dd> The<i> real</i> user ID. </p>
<dt>28.<code> RUSER &nbsp;&#8212;&nbsp; Real User Name </code></p>
<dd> The<i> real</i> user name. </p>
<dt>29.<code> S &nbsp;&#8212;&nbsp; Process Status </code></p>
<dd> The status of the task which can be one of:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>D</code>&nbsp;=&nbsp;uninterruptible sleep<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>I</code>&nbsp;=&nbsp;idle<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>R</code>&nbsp;=&nbsp;running<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>S</code>&nbsp;=&nbsp;sleeping<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>T</code>&nbsp;=&nbsp;stopped by job control signal<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>t</code>&nbsp;=&nbsp;stopped by debugger during trace<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>Z</code>&nbsp;=&nbsp;zombie </p>
<p> Tasks shown as running should be more properly thought of as ready to run &nbsp;&#8212;&nbsp; their task_struct is simply represented on the Linux run-queue. Even without a true SMP machine, you may see numerous tasks in this state depending on top&#8217;s delay interval and nice value. </p>
<dt>30.<code> SHR &nbsp;&#8212;&nbsp; Shared Memory Size (KiB) </code></p>
<dd> A subset of resident memory (RES) that may be used by other processes. It will include shared anonymous pages and shared file-backed pages. It also includes private pages mapped to files representing program images and shared libraries. </p>
<p> See `OVERVIEW, Linux Memory Types&#8217; for additional details. </p>
<dt>31.<code> SID &nbsp;&#8212;&nbsp; Session Id </code></p>
<dd> A session is a collection of process groups (see PGRP), usually established by the login shell. A newly forked process joins the session of its creator. By convention, this value equals the process ID (see PID) of the first member of the session, called the session leader, which is usually the login shell. </p>
<dt>32.<code> SUID &nbsp;&#8212;&nbsp; Saved User Id </code></p>
<dd> The<i> saved</i> user ID. </p>
<dt>33.<code> SUPGIDS &nbsp;&#8212;&nbsp; Supplementary Group IDs </code></p>
<dd> The IDs of any supplementary group(s) established at login or inherited from a task&#8217;s parent. They are displayed in a comma delimited list. </p>
<p> <code>Note</code>: The SUPGIDS field, unlike most columns, is not fixed-width. When displayed, it plus any other variable width columns will be allocated all remaining screen width (up to the maximum 512 characters). Even so, such variable width fields could still suffer truncation. See topic 5c. SCROLLING a Window for additional information on accessing any truncated data. </p>
<dt>34.<code> SUPGRPS &nbsp;&#8212;&nbsp; Supplementary Group Names </code></p>
<dd> The names of any supplementary group(s) established at login or inherited from a task&#8217;s parent. They are displayed in a comma delimited list. </p>
<p> <code>Note</code>: The SUPGRPS field, unlike most columns, is not fixed-width. When displayed, it plus any other variable width columns will be allocated all remaining screen width (up to the maximum 512 characters). Even so, such variable width fields could still suffer truncation. See topic 5c. SCROLLING a Window for additional information on accessing any truncated data. </p>
<dt>35.<code> SUSER &nbsp;&#8212;&nbsp; Saved User Name </code></p>
<dd> The<i> saved</i> user name. </p>
<dt>36.<code> SWAP &nbsp;&#8212;&nbsp; Swapped Size (KiB) </code></p>
<dd> The formerly resident portion of a task&#8217;s address space written to the swap file when physical memory becomes over committed. </p>
<p> See `OVERVIEW, Linux Memory Types&#8217; for additional details. </p>
<dt>37.<code> TGID &nbsp;&#8212;&nbsp; Thread Group Id </code></p>
<dd> The ID of the thread group to which a task belongs. It is the PID of the thread group leader. In kernel terms, it represents those tasks that share an mm_struct. </p>
<dt>38.<code> TIME &nbsp;&#8212;&nbsp; CPU Time </code></p>
<dd> Total CPU time the task has used since it started. When Cumulative mode is <i>On</i>, each process is listed with the cpu time that it and its dead children have used. You toggle Cumulative mode with `S&#8217;, which is both a command-line option and an interactive command. See the `S&#8217; interactive command for additional information regarding this mode. </p>
<dt>39.<code> TIME+ &nbsp;&#8212;&nbsp; CPU Time, hundredths </code></p>
<dd> The same as TIME, but reflecting more granularity through hundredths of a second. </p>
<dt>40.<code> TPGID &nbsp;&#8212;&nbsp; Tty Process Group Id </code></p>
<dd> The process group ID of the foreground process for the connected tty, or -1 if a process is not connected to a terminal. By convention, this value equals the process ID (see PID) of the process group leader (see PGRP). </p>
<dt>41.<code> TTY &nbsp;&#8212;&nbsp; Controlling Tty </code></p>
<dd> The name of the controlling terminal. This is usually the device (serial port, pty, etc.) from which the process was started, and which it uses for input or output. However, a task need not be associated with a terminal, in which case you&#8217;ll see `?&#8217; displayed. </p>
<dt>42.<code> UID &nbsp;&#8212;&nbsp; User Id </code></p>
<dd> The<i> effective</i> user ID of the task&#8217;s owner. </p>
<dt>43.<code> USED &nbsp;&#8212;&nbsp; Memory in Use (KiB) </code></p>
<dd> This field represents the non-swapped physical memory a task is using (RES) plus the swapped out portion of its address space (SWAP). </p>
<p> See `OVERVIEW, Linux Memory Types&#8217; for additional details. </p>
<dt>44.<code> USER &nbsp;&#8212;&nbsp; User Name </code></p>
<dd> The<i> effective</i> user name of the task&#8217;s owner. </p>
<dt>45.<code> VIRT &nbsp;&#8212;&nbsp; Virtual Memory Size (KiB) </code></p>
<dd> The total amount of virtual memory used by the task. It includes all code, data and shared libraries plus pages that have been swapped out and pages that have been mapped but not used. </p>
<p> See `OVERVIEW, Linux Memory Types&#8217; for additional details. </p>
<dt>46.<code> WCHAN &nbsp;&#8212;&nbsp; Sleeping in Function </code></p>
<dd> This field will show the name of the kernel function in which the task is currently sleeping. Running tasks will display a dash (`-&#8216;) in this column. </p>
<dt>47.<code> nDRT &nbsp;&#8212;&nbsp; Dirty Pages Count </code></p>
<dd> The number of pages that have been modified since they were last written to auxiliary storage. Dirty pages must be written to auxiliary storage before the corresponding physical memory location can be used for some other virtual page. </p>
<p> This field was deprecated with linux 2.6 and is always zero. </p>
<dt>48.<code> nMaj &nbsp;&#8212;&nbsp; Major Page Fault Count </code></p>
<dd> The number of<code> major</code> page faults that have occurred for a task. A page fault occurs when a process attempts to read from or write to a virtual page that is not currently present in its address space. A major page fault is when auxiliary storage access is involved in making that page available. </p>
<dt>49.<code> nMin &nbsp;&#8212;&nbsp; Minor Page Fault count </code></p>
<dd> The number of<code> minor</code> page faults that have occurred for a task. A page fault occurs when a process attempts to read from or write to a virtual page that is not currently present in its address space. A minor page fault does not involve auxiliary storage access in making that page available. </p>
<dt>50.<code> nTH &nbsp;&#8212;&nbsp; Number of Threads </code></p>
<dd> The number of threads associated with a process. </p>
<dt>51.<code> nsIPC &nbsp;&#8212;&nbsp; IPC namespace </code></p>
<dd> The Inode of the namespace used to isolate interprocess communication (IPC) resources such as System V IPC objects and POSIX message queues. </p>
<dt>52.<code> nsMNT &nbsp;&#8212;&nbsp; MNT namespace </code></p>
<dd> The Inode of the namespace used to isolate filesystem mount points thus offering different views of the filesystem hierarchy. </p>
<dt>53.<code> nsNET &nbsp;&#8212;&nbsp; NET namespace </code></p>
<dd> The Inode of the namespace used to isolate resources such as network devices, IP addresses, IP routing, port numbers, etc. </p>
<dt>54.<code> nsPID &nbsp;&#8212;&nbsp; PID namespace </code></p>
<dd> The Inode of the namespace used to isolate process ID numbers meaning they need not remain unique. Thus, each such namespace could have its own `init/systemd&#8217; (PID #1) to manage various initialization tasks and reap orphaned child processes. </p>
<dt>55.<code> nsUSER &nbsp;&#8212;&nbsp; USER namespace </code></p>
<dd> The Inode of the namespace used to isolate the user and group ID numbers. Thus, a process could have a normal unprivileged user ID outside a user namespace while having a user ID of 0, with full root privileges, inside that namespace. </p>
<dt>56.<code> nsUTS &nbsp;&#8212;&nbsp; UTS namespace </code></p>
<dd> The Inode of the namespace used to isolate hostname and NIS domain name. UTS simply means &quot;UNIX Time-sharing System&quot;. </p>
<dt>57.<code> vMj &nbsp;&#8212;&nbsp; Major Page Fault Count Delta</code></p>
<dd> The number of<code> major</code> page faults that have occurred since the last update (see nMaj). </p>
<dt>58.<code> vMn &nbsp;&#8212;&nbsp; Minor Page Fault Count Delta</code></p>
<dd> The number of<code> minor</code> page faults that have occurred since the last update (see nMin). </p>
</dl>
<h3>3b. MANAGING Fields</h3>
<p> After pressing the interactive command `f&#8217; or `F&#8217; (Fields Management) you will be presented with a screen showing: 1) the `current&#8217; window name; 2) the designated sort field; 3) all fields in their current order along with descriptions. Entries marked with an asterisk are the currently displayed fields, screen width permitting. </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> As the on screen instructions indicate, you navigate among the fields with the<code> Up</code> and<code> Down</code> arrow keys. The PgUp, PgDn, Home and End keys can also be used to quickly reach the first or last available field. </p>
<dt>&bull;</p>
<dd> The<code> Right</code> arrow key selects a field for repositioning and the<code> Left</code> arrow key or the &lt;<code>Enter</code>&gt; key commits that field&#8217;s placement. </p>
<dt>&bull;</p>
<dd> The `<code>d</code>&#8216; key or the &lt;<code>Space</code>&gt; bar toggles a field&#8217;s display status, and thus the presence or absence of the asterisk. </p>
<dt>&bull;</p>
<dd> The `<code>s</code>&#8216; key designates a field as the sort field. See topic 4c. TASK AREA Commands, SORTING for additional information regarding your selection of a sort field. </p>
<dt>&bull;</p>
<dd> The `<code>a</code>&#8216; and `<code>w</code>&#8216; keys can be used to cycle through all available windows and the `<code>q</code>&#8216; or &lt;<code>Esc</code>&gt; keys exit Fields Management.</dl>
</dl>
<p> The Fields Management screen can also be used to change the `current&#8217; window/field group in either full-screen mode or alternate-display mode. Whatever was targeted when `q&#8217; or &lt;Esc&gt; was pressed will be made current as you return to the top display. See topic 5. ALTERNATE-DISPLAY Provisions and the `g&#8217; interactive command for insight into `current&#8217; windows and field groups. </p>
<p> <code>Note</code>: Any window that has been scrolled<i> horizontally</i> will be reset if any field changes are made via the Fields Management screen. Any<i> vertical</i> scrolled position, however, will not be affected. See topic 5c. SCROLLING a Window for additional information regarding vertical and horizontal scrolling. </p>
<h2>4. INTERACTIVE Commands</h2>
<p> Listed below is a brief index of commands within categories. Some commands appear more than once &nbsp;&#8212;&nbsp; their meaning or scope may vary depending on the context in which they are issued. </p>
<pre>
  4a.<i> Global-Commands </i>
        &lt;Ent/Sp&gt; ?, =, 0,
        A, B, d, E, e, g, h, H, I, k, q, r, s, W, X, Y, Z
  4b.<i> Summary-Area-Commands </i>
        C, l, t, m, 1, 2, 3, 4, !
  4c.<i> Task-Area-Commands </i>
        Appearance:  b, J, j, x, y, z
        Content:     c, f, F, o, O, S, u, U, V, v
        Size:        #, i, n
        Sorting:     &lt;, &gt;, f, F, R
  4d.<i> Color-Mapping </i>
        &lt;Ret&gt;, a, B, b, H, M, q, S, T, w, z, 0 - 7
  5b.<i> Commands-for-Windows </i>
        -, _, =, +, A, a, g, G, w
  5c.<i> Scrolling-a-Window </i>
        C, Up, Dn, Left, Right, PgUp, PgDn, Home, End
  5d.<i> Searching-in-a-Window </i>
        L, &amp;
</pre>
<h3>4a. GLOBAL Commands</h3>
<p> The global interactive commands are<code> always</code> available in both full-screen mode and alternate-display mode. However, some of these interactive commands are<code> not available</code> when running in Secure mode. </p>
<p> If you wish to know in advance whether or not your top has been secured, simply ask for help and view the system summary on the second line. </p>
<dl>
<dt>&nbsp;<wbr>&nbsp;&lt;<code>Enter</code>&gt; or &lt;<code>Space</code>&gt;&nbsp;<wbr>&nbsp;:<i>Refresh-Display </i></p>
<dd> These commands awaken top and following receipt of any input the entire display will be repainted. They also force an update of any hotplugged cpu or physical memory changes. </p>
<p> Use either of these keys if you have a large delay interval and wish to see current status, </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>?</code> | <code>h</code>&nbsp;<wbr>&nbsp;:<i>Help </i></p>
<dd> There are two help levels available. The first will provide a reminder of all the basic interactive commands. If top is<i> secured</i>, that screen will be abbreviated. </p>
<p> Typing `h&#8217; or `?&#8217; on that help screen will take you to help for those interactive commands applicable to alternate-display mode. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>=</code>&nbsp;<wbr>&nbsp;:<i>Exit-Display-Limits </i></p>
<dd> Removes restrictions on what is shown. This command will reverse any `i&#8217; (idle tasks), `n&#8217; (max tasks) and `v&#8217; (hide children) commands that might be active. It also provides for an exit from PID monitoring, User filtering, Other filtering, Locate processing and Combine Cpus mode. </p>
<p> Additionally, if the window has been scrolled it will be reset with this command. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>0</code>&nbsp;<wbr>&nbsp;:<i>Zero-Suppress</i> toggle</p>
<dd> This command determines whether zeros are shown or suppressed for many of the fields in a task window. Fields like UID, GID, NI, PR or P are not affected by this toggle. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>A</code>&nbsp;<wbr>&nbsp;:<i>Alternate-Display-Mode</i> toggle</p>
<dd> This command will switch between full-screen mode and alternate-display mode. See topic 5. ALTERNATE-DISPLAY Provisions and the `g&#8217; interactive command for insight into `current&#8217; windows and field groups. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>B</code>&nbsp;<wbr>&nbsp;:<i>Bold-Disable/Enable</i> toggle</p>
<dd> This command will influence use of the bold terminfo capability and alters<code> both</code> the summary area and task area for the `current&#8217; window. While it is intended primarily for use with dumb terminals, it can be applied anytime. </p>
<p> <code>Note</code>: When this toggle is <i>On</i> and top is operating in monochrome mode, the<code> entire display</code> will appear as normal text. Thus, unless the `x&#8217; and/or `y&#8217; toggles are using reverse for emphasis, there will be no visual confirmation that they are even on. </p>
<dt>*&nbsp;<wbr>&nbsp;<code>d</code> | <code>s</code>&nbsp;<wbr>&nbsp;:<i>Change-Delay-Time-interval </i></p>
<dd> You will be prompted to enter the delay time, in seconds, between display updates. </p>
<p> Fractional seconds are honored, but a negative number is not allowed. Entering 0 causes (nearly) continuous updates, with an unsatisfactory display as the system and tty driver try to keep up with top&#8217;s demands. The delay value is inversely proportional to system loading, so set it with care. </p>
<p> If at any time you wish to know the current delay time, simply ask for help and view the system summary on the second line. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>E</code>&nbsp;<wbr>&nbsp;:<i>Enforce-Summary-Memory-Scale</i> in Summary Area</p>
<dd> With this command you can cycle through the available summary area memory scaling which ranges from KiB (kibibytes or 1,024 bytes) through EiB (exbibytes or 1,152,921,504,606,846,976 bytes). </p>
<p> If you see a `+&#8217; between a displayed number and the following label, it means that top was forced to truncate some portion of that number. By raising the scaling factor, such truncation can be avoided. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>e</code>&nbsp;<wbr>&nbsp;:<i>Enforce-Task-Memory-Scale</i> in Task Area</p>
<dd> With this command you can cycle through the available task area memory scaling which ranges from KiB (kibibytes or 1,024 bytes) through PiB (pebibytes or 1,125,899,906,842,624 bytes). </p>
<p> While top will try to honor the selected target range, additional scaling might still be necessary in order to accommodate current values. If you wish to see a more homogeneous result in the memory columns, raising the scaling range will usually accomplish that goal. Raising it too high, however, is likely to produce an all zero result which cannot be suppressed with the `0&#8242; interactive command. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>g</code>&nbsp;<wbr>&nbsp;:<i>Choose-Another-Window/Field-Group </i></p>
<dd> You will be prompted to enter a number between 1 and 4 designating the field group which should be made the `current&#8217; window. You will soon grow comfortable with these 4 windows, especially after experimenting with alternate-display mode. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>H</code>&nbsp;<wbr>&nbsp;:<i>Threads-mode</i> toggle</p>
<dd> When this toggle is <i>On</i>, individual threads will be displayed for all processes in all visible task windows. Otherwise, top displays a summation of all threads in each process. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>I</code>&nbsp;<wbr>&nbsp;:<i>Irix/Solaris-Mode</i> toggle</p>
<dd> When operating in Solaris mode (`I&#8217; toggled <i>Off</i>), a task&#8217;s cpu usage will be divided by the total number of CPUs. After issuing this command, you&#8217;ll be told the new state of this toggle. </p>
<dt>*&nbsp;<wbr>&nbsp;<code>k</code>&nbsp;<wbr>&nbsp;:<i>Kill-a-task </i></p>
<dd> You will be prompted for a PID and then the signal to send. </p>
<p> Entering no PID or a negative number will be interpreted as the default shown in the prompt (the first task displayed). A PID value of zero means the top program itself. </p>
<p> The default signal, as reflected in the prompt, is SIGTERM. However, you can send any signal, via number or name. </p>
<p> If you wish to abort the kill process, do one of the following depending on your progress: </p>
<pre>
    1) at the pid prompt, type an invalid number
    2) at the signal prompt, type 0 (or any invalid signal)
    3) at any prompt, type &lt;Esc&gt;
</pre>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>q</code>&nbsp;<wbr>&nbsp;:<i>Quit </i></p>
<dd>
<dt>*&nbsp;<wbr>&nbsp;<code>r</code>&nbsp;<wbr>&nbsp;:<i>Renice-a-Task </i></p>
<dd> You will be prompted for a PID and then the value to nice it to. </p>
<p> Entering no PID or a negative number will be interpreted as the default shown in the prompt (the first task displayed). A PID value of zero means the top program itself. </p>
<p> A positive nice value will cause a process to lose priority. Conversely, a negative nice value will cause a process to be viewed more favorably by the kernel. As a general rule, ordinary users can only increase the nice value and are prevented from lowering it. </p>
<p> If you wish to abort the renice process, do one of the following depending on your progress: </p>
<pre>
    1) at the pid prompt, type an invalid number
    2) at the nice prompt, type &lt;Enter&gt; with no input
    3) at any prompt, type &lt;Esc&gt;
</pre>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>W</code>&nbsp;<wbr>&nbsp;:<i>Write-the-Configuration-File </i></p>
<dd> This will save all of your options and toggles plus the current display mode and delay time. By issuing this command just before quitting top, you will be able restart later in exactly that same state. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>X</code>&nbsp;<wbr>&nbsp;:<i>Extra-Fixed-Width </i></p>
<dd> Some fields are fixed width and not scalable. As such, they are subject to truncation which would be indicated by a `+&#8217; in the last position. </p>
<p> This interactive command can be used to alter the widths of the following fields: </p>
<pre>
   <i> field  default    field  default    field  default </i>
    GID       5       GROUP     8       WCHAN    10
    RUID      5       LXC       8       nsIPC    10
    SUID      5       RUSER     8       nsMNT    10
    UID       5       SUSER     8       nsNET    10
                      TTY       8       nsPID    10
                      USER      8       nsUSER   10
                                        nsUTS    10
</pre>
<p> You will be prompted for the amount to be added to the default widths shown above. Entering zero forces a return to those defaults. </p>
<p> If you enter a negative number, top will automatically increase the column size as needed until there is no more truncated data. You can accelerate this process by reducing the delay interval or holding down the &lt;Space&gt; bar. </p>
<p> <code>Note</code>: Whether explicitly or automatically increased, the widths for these fields are never decreased by top. To narrow them you must specify a smaller number or restore the defaults. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>Y</code>&nbsp;<wbr>&nbsp;:<i>Inspect-Other-Output </i></p>
<dd> After issuing the `Y&#8217; interactive command, you will be prompted for a target PID. Typing a value or accepting the default results in a separate screen. That screen can be used to view a variety of files or piped command output while the normal top iterative display is paused. </p>
<p> <code>Note</code>: This interactive command is only fully realized when supporting entries have been manually added to the end of the top configuration file. For details on creating those entries, see topic 6b. ADDING INSPECT Entries. </p>
<p> Most of the keys used to navigate the Inspect feature are reflected in its header prologue. There are, however, additional keys available once you have selected a particular file or command. They are familiar to anyone who has used the pager `less&#8217; and are summarized here for future reference. </p>
<pre>
   <i> key      function </i>
    =        alternate status-line, file or pipeline
    /        find, equivalent to `L' locate
    n        find next, equivalent to `&amp;' locate next
    &lt;Space&gt;  scroll down, equivalent to &lt;PgDn&gt;
    b        scroll up, equivalent to &lt;PgUp&gt;
    g        first line, equivalent to &lt;Home&gt;
    G        last line, equivalent to &lt;End&gt;
</pre>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>Z</code>&nbsp;<wbr>&nbsp;:<i>Change-Color-Mapping </i></p>
<dd> This key will take you to a separate screen where you can change the colors for the `current&#8217; window, or for all windows. For details regarding this interactive command see topic 4d. COLOR Mapping. </p>
<dt>*</p>
<dd> The commands shown with an asterisk (`*&#8217;) are not available in Secure mode, nor will they be shown on the level-1 help screen. </p>
</dl>
<h3>4b. SUMMARY AREA Commands</h3>
<p> The summary area interactive commands are<code> always available</code> in both full-screen mode and alternate-display mode. They affect the beginning lines of your display and will determine the position of messages and prompts. </p>
<p> These commands always impact just the `current&#8217; window/field group. See topic 5. ALTERNATE-DISPLAY Provisions and the `g&#8217; interactive command for insight into `current&#8217; windows and field groups. </p>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>C</code>&nbsp;<wbr>&nbsp;:<i>Show-scroll-coordinates</i> toggle</p>
<dd> Toggle an informational message which is displayed whenever the message line is not otherwise being used. For additional information see topic 5c. SCROLLING a Window. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>l</code>&nbsp;<wbr>&nbsp;:<i>Load-Average/Uptime</i> toggle</p>
<dd> This is also the line containing the program name (possibly an alias) when operating in full-screen mode or the `current&#8217; window name when operating in alternate-display mode. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>t</code>&nbsp;<wbr>&nbsp;:<i>Task/Cpu-States</i> toggle</p>
<dd> This command affects from 2 to many summary area lines, depending on the state of the `1&#8242;, `2&#8242; or `3&#8242; command toggles and whether or not top is running under true SMP. </p>
<p> This portion of the summary area is also influenced by the `H&#8217; interactive command toggle, as reflected in the total label which shows either Tasks or Threads. </p>
<p> This command serves as a 4-way toggle, cycling through these modes: </p>
<pre>
    1. detailed percentages by category
    2. abbreviated user/system and total % + bar graph
    3. abbreviated user/system and total % + block graph
    4. turn off task and cpu states display
</pre>
<p> When operating in either of the graphic modes, the display becomes much more meaningful when individual CPUs or NUMA nodes are also displayed. See the the `1&#8242;, `2&#8242; and `3&#8242; commands below for additional information. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>m</code>&nbsp;<wbr>&nbsp;:<i>Memory/Swap-Usage</i> toggle</p>
<dd> This command affects the two summary area lines dealing with physical and virtual memory. </p>
<p> This command serves as a 4-way toggle, cycling through these modes: </p>
<pre>
    1. detailed percentages by memory type
    2. abbreviated % used/total available + bar graph
    3. abbreviated % used/total available + block graph
    4. turn off memory display
</pre>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>1</code>&nbsp;<wbr>&nbsp;:<i>Single/Separate-Cpu-States</i> toggle</p>
<dd> This command affects how the `t&#8217; command&#8217;s Cpu States portion is shown. Although this toggle exists primarily to serve massively-parallel SMP machines, it is not restricted to solely SMP environments. </p>
<p> When you see `%Cpu(s):&#8217; in the summary area, the `1&#8242; toggle is <i>On</i> and all cpu information is gathered in a single line. Otherwise, each cpu is displayed separately as: `%Cpu0, %Cpu1, &#8230;&#8217; up to available screen height. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>2</code>&nbsp;<wbr>&nbsp;:<i>NUMA-Nodes/Cpu-Summary</i> toggle</p>
<dd> This command toggles between the `1&#8242; command cpu summary display (only) or a summary display plus the cpu usage statistics for each NUMA Node. It is only available if a system has the requisite NUMA support. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>3</code>&nbsp;<wbr>&nbsp;:<i>Expand-NUMA-Node </i></p>
<dd> You will be invited to enter a number representing a NUMA Node. Thereafter, a node summary plus the statistics for each cpu in that node will be shown until the `1&#8242;, `2&#8242; or `4&#8242; command toggle is pressed. This interactive command is only available if a system has the requisite NUMA support. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>4</code>&nbsp;<wbr>&nbsp;:<i>Display-Cpus-Two-Abreast </i></p>
<dd> This command turns the `1&#8242; toggle <i>Off</i> for individual cpu display but prints the results two abreast. It requires a terminal with a minimum width of 80 columns. If a terminal&#8217;s width is decreased below the minimum while top is running, top reverts to the normal `1&#8242; toggle <i>Off</i> state. </p>
<p> To avoid truncation when displaying detailed cpu statistcs, as opposed to the graphic representations, a minimum width of 165 columns would be required. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>!</code>&nbsp;<wbr>&nbsp;:<i>Combine-Cpus-Mode </i></p>
<dd> This command toggle is intended for massively parallel SMP environments where, even with the `4&#8242; command toggle, not all processors can be displayed. With each press of `!&#8217; the number of additional cpu&#8217;s combined is doubled thus reducing the total number of cpu lines displayed. </p>
<p> For example, with the first press of `!&#8217; one additional cpu will be combined and displayed as `0-1, 2-3, &#8230;&#8217; instead of the normal `%Cpu0, %Cpu1, %Cpu2, %Cpu3, &#8230;&#8217;. With a second `!&#8217; command toggle two additional cpus are combined and shown as `0-2, 3-5, &#8230;&#8217;. Then the third &#8216;!&#8217; press, combining four additional cpus, shows as `0-4, 5-9, &#8230;&#8217;, etc. </p>
<p> Such progression continues until individual cpus are again displayed and impacts both the `1&#8242; and `4&#8242; toggles (one or two columns). Use the `=&#8217; command to exit <code>Combine Cpus</code> mode. </p>
</dl>
<p> <code>Note</code>: If the entire summary area has been toggled <i>Off</i> for any window, you would be left with just the<code> message line</code>. In that way, you will have maximized available task rows but (temporarily) sacrificed the program name in full-screen mode or the `current&#8217; window name when in alternate-display mode. </p>
<h3>4c. TASK AREA Commands</h3>
<p> The task area interactive commands are<code> always</code> available in full-screen mode. </p>
<p> The task area interactive commands are<code> never available</code> in alternate-display mode<i> if</i> the `current&#8217; window&#8217;s task display has been toggled <i>Off</i> (see topic 5. ALTERNATE-DISPLAY Provisions). </p>
<p> <code>APPEARANCE</code> of task window </p>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>J</code>&nbsp;<wbr>&nbsp;:<i>Justify-Numeric-Columns</i> toggle</p>
<dd> Alternates between right-justified (the default) and left-justified numeric data. If the numeric data completely fills the available column, this command toggle may impact the column header only. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>j</code>&nbsp;<wbr>&nbsp;:<i>Justify-Character-Columns</i> toggle</p>
<dd> Alternates between left-justified (the default) and right-justified character data. If the character data completely fills the available column, this command toggle may impact the column header only. </p>
</dl>
<dl>
<dt>
<dd> The following commands will also be influenced by the state of the global `B&#8217; (bold enable) toggle.</dl>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>b</code>&nbsp;<wbr>&nbsp;:<i>Bold/Reverse</i> toggle</p>
<dd> This command will impact how the `x&#8217; and `y&#8217; toggles are displayed. It may also impact the summary area when a bar graph has been selected for cpu states or memory usage via the `t&#8217; or `m&#8217; toggles. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>x</code>&nbsp;<wbr>&nbsp;:<i>Column-Highlight</i> toggle</p>
<dd> Changes highlighting for the current sort field. If you forget which field is being sorted this command can serve as a quick visual reminder, providing the sort field is being displayed. The sort field might<i> not</i> be visible because:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1)&nbsp;there is insufficient<i>&nbsp;Screen Width&nbsp;</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2)&nbsp;the&nbsp;`f&#8217;&nbsp;interactive command turned it&nbsp;<i>Off</i> </p>
<p> <code>Note</code>: Whenever Searching and/or Other Filtering is active in a window, column highlighting is temporarily disabled. See the notes at the end of topics 5d. SEARCHING and 5e. FILTERING for an explanation why. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>y</code>&nbsp;<wbr>&nbsp;:<i>Row-Highlight</i> toggle</p>
<dd> Changes highlighting for &quot;running&quot; tasks. For additional insight into this task state, see topic 3a. DESCRIPTIONS of Fields, the `S&#8217; field (Process Status). </p>
<p> Use of this provision provides important insight into your system&#8217;s health. The only costs will be a few additional tty escape sequences. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>z</code>&nbsp;<wbr>&nbsp;:<i>Color/Monochrome</i> toggle</p>
<dd> Switches the `current&#8217; window between your last used color scheme and the older form of black-on-white or white-on-black. This command will alter<code> both</code> the summary area and task area but does not affect the state of the `x&#8217;, `y&#8217; or `b&#8217; toggles. </p>
</dl>
<p> <code>CONTENT</code> of task window </p>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>c</code>&nbsp;<wbr>&nbsp;:<i>Command-Line/Program-Name</i> toggle</p>
<dd> This command will be honored whether or not the COMMAND column is currently visible. Later, should that field come into view, the change you applied will be seen. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>f</code> | <code>F</code>&nbsp;<wbr>&nbsp;:<i>Fields-Management </i></p>
<dd> These keys display a separate screen where you can change which fields are displayed, their order and also designate the sort field. For additional information on these interactive commands see topic 3b. MANAGING Fields. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>o</code> | <code>O</code>&nbsp;<wbr>&nbsp;:<i>Other-Filtering </i></p>
<dd> You will be prompted for the selection criteria which then determines which tasks will be shown in the `current&#8217; window. Your criteria can be made case sensitive or case can be ignored. And you determine if top should include or exclude matching tasks. </p>
<p> See topic 5e. FILTERING in a window for details on these and additional related interactive commands. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>S</code>&nbsp;<wbr>&nbsp;:<i>Cumulative-Time-Mode</i> toggle</p>
<dd> When Cumulative mode is <i>On</i>, each process is listed with the cpu time that it and its dead children have used. </p>
<p> When <i>Off</i>, programs that fork into many separate tasks will appear less demanding. For programs like `init&#8217; or a shell this is appropriate but for others, like compilers, perhaps not. Experiment with two task windows sharing the same sort field but with different `S&#8217; states and see which representation you prefer. </p>
<p> After issuing this command, you&#8217;ll be informed of the new state of this toggle. If you wish to know in advance whether or not Cumulative mode is in effect, simply ask for help and view the window summary on the second line. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>u</code> | <code>U</code>&nbsp;<wbr>&nbsp;:<i>Show-Specific-User-Only </i></p>
<dd> You will be prompted for the<code> uid</code> or<code> name</code> of the user to display. The -u option matches on <code> effective</code> user whereas the -U option matches on<code> any</code> user (real, effective, saved, or filesystem). </p>
<p> Thereafter, in that task window only matching users will be shown, or possibly no processes will be shown. Prepending an exclamation point (`!&#8217;) to the user id or name instructs top to display only processes with users not matching the one provided. </p>
<p> Different task windows can be used to filter different users. Later, if you wish to monitor all users again in the `current&#8217; window, re-issue this command but just press &lt;Enter&gt; at the prompt. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>V</code>&nbsp;<wbr>&nbsp;:<i>Forest-View-Mode</i> toggle</p>
<dd> In this mode, processes are reordered according to their parents and the layout of the COMMAND column resembles that of a tree. In forest view mode it is still possible to toggle between program name and command line (see the `c&#8217; interactive command) or between processes and threads (see the `H&#8217; interactive command). </p>
<p> <code>Note</code>: Typing any key affecting the sort order will exit forest view mode in the `current&#8217; window. See topic 4c. TASK AREA Commands, SORTING for information on those keys. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>v</code>&nbsp;<wbr>&nbsp;:<i>Hide/Show-Children</i> toggle</p>
<dd> When in forest view mode, this key serves as a toggle to collapse or expand the children of a parent. </p>
<p> The toggle is applied against the first (topmost) process in the `current&#8217; window. See topic 5c. SCROLLING a Window for additional information regarding vertical scrolling. </p>
<p> If the target process has not forked any children, this key has no effect. It also has no effect when not in forest view mode. </p>
</dl>
<p> <code>SIZE</code> of task window </p>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>i</code>&nbsp;<wbr>&nbsp;:<i>Idle-Process</i> toggle</p>
<dd> Displays all tasks or just active tasks. When this toggle is <i>Off</i>, tasks that have not used any CPU since the last update will not be displayed. However, due to the granularity of the %CPU and TIME+ fields, some processes may still be displayed that<i> appear</i> to have used<i> no</i> CPU. </p>
<p> If this command is applied to the last task display when in alternate-display mode, then it will not affect the window&#8217;s size, as all prior task displays will have already been painted. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>n</code> | <code>#</code>&nbsp;<wbr>&nbsp;:<i>Set-Maximum-Tasks </i></p>
<dd> You will be prompted to enter the number of tasks to display. The lessor of your number and available screen rows will be used. </p>
<p> When used in alternate-display mode, this is the command that gives you precise control over the size of each currently visible task display, except for the very last. It will not affect the last window&#8217;s size, as all prior task displays will have already been painted. </p>
<p> <code>Note</code>: If you wish to increase the size of the last visible task display when in alternate-display mode, simply decrease the size of the task display(s) above it. </p>
</dl>
<p> <code>SORTING</code> of task window </p>
<dl>
<dt>
<dd> For compatibility, this top supports most of the former top sort keys. Since this is primarily a service to former top users, these commands do not appear on any help screen. </p>
<pre>
     <i> command   sorted-field                  supported </i>
      A         start time (non-display)     <code> No </code>
      M         %MEM                          Yes
      N         PID                           Yes
      P         %CPU                          Yes
      T         TIME+                         Yes
</pre>
<p> Before using any of the following sort provisions, top suggests that you temporarily turn on column highlighting using the `x&#8217; interactive command. That will help ensure that the actual sort environment matches your intent. </p>
<p> The following interactive commands will<code> only</code> be honored when the current sort field is<code> visible</code>. The sort field might<i> not</i> be visible because:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1)&nbsp;there is insufficient<i>&nbsp;Screen Width&nbsp;</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2)&nbsp;the&nbsp;`f&#8217;&nbsp;interactive command turned it&nbsp;<i>Off</i> </p>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&lt;</code>&nbsp;<wbr>&nbsp;:<i>Move-Sort-Field-Left </i></p>
<dd> Moves the sort column to the left unless the current sort field is the first field being displayed. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&gt;</code>&nbsp;<wbr>&nbsp;:<i>Move-Sort-Field-Right </i></p>
<dd> Moves the sort column to the right unless the current sort field is the last field being displayed. </p>
</dl>
<p> The following interactive commands will<code> always</code> be honored whether or not the current sort field is visible. </p>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>f</code> | <code>F</code>&nbsp;<wbr>&nbsp;:<i>Fields-Management </i></p>
<dd> These keys display a separate screen where you can change which field is used as the sort column, among other functions. This can be a convenient way to simply verify the current sort field, when running top with column highlighting turned <i>Off</i>. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>R</code>&nbsp;<wbr>&nbsp;:<i>Reverse/Normal-Sort-Field</i> toggle</p>
<dd> Using this interactive command you can alternate between high-to-low and low-to-high sorts. </p>
</dl>
<p> <code>Note</code>: Field sorting uses internal values, not those in column display. Thus, the TTY and WCHAN fields will violate strict ASCII collating sequence.</dl>
<h3>4d. COLOR Mapping</h3>
<p> When you issue the `Z&#8217; interactive command, you will be presented with a separate screen. That screen can be used to change the colors in just the `current&#8217; window or in all four windows before returning to the top display. </p>
<p> The following interactive commands are available. </p>
<pre>
    <code>4</code> upper case letters to select a<code> target </code>
    <code>8</code> numbers to select a<code> color </code>
    normal toggles available 
        B         :bold disable/enable
        b         :running tasks &quot;bold&quot;/reverse
        z         :color/mono
    other commands available 
        a/w       :apply, then go to next/prior
        &lt;Enter&gt;   :apply and exit
        q         :abandon current changes and exit
</pre>
<p> If you use `a&#8217; or `w&#8217; to cycle the targeted window, you will have applied the color scheme that was displayed when you left that window. You can, of course, easily return to any window and reapply different colors or turn colors <i>Off</i> completely with the `z&#8217; toggle. </p>
<p> The Color Mapping screen can also be used to change the `current&#8217; window/field group in either full-screen mode or alternate-display mode. Whatever was targeted when `q&#8217; or &lt;Enter&gt; was pressed will be made current as you return to the top display. </p>
<h2>5. ALTERNATE-DISPLAY Provisions</h2>
<h3>5a. WINDOWS Overview</h3>
<dl>
<dt><code>Field Groups/Windows</code>:</p>
<dd> In full-screen mode there is a single window represented by the entire screen. That single window can still be changed to display 1 of 4 different<code> field groups</code> (see the `g&#8217; interactive command, repeated below). Each of the 4 field groups has a unique separately configurable<code> summary area </code> and its own configurable<code> task area</code>. </p>
<p> In alternate-display mode, those 4 underlying field groups can now be made visible simultaneously, or can be turned <i>Off</i> individually at your command. </p>
<p> The summary area will always exist, even if it&#8217;s only the message line. At any given time only<i> one</i> summary area can be displayed. However, depending on your commands, there could be from<i> zero </i> to<i> four</i> separate task displays currently showing on the screen. </p>
<dt><code>Current Window</code>:</p>
<dd> The `current&#8217; window is the window associated with the summary area and the window to which task related commands are always directed. Since in alternate-display mode you can toggle the task display <i>Off</i>, some commands might be restricted for the `current&#8217; window. </p>
<p> A further complication arises when you have toggled the first summary area line <i>Off</i>. With the loss of the window name (the `l&#8217; toggled line), you&#8217;ll not easily know what window is the `current&#8217; window. </p>
</dl>
<h3>5b. COMMANDS for Windows</h3>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;</code> | <code>_</code>&nbsp;<wbr>&nbsp;:<i>Show/Hide-Window(s)</i> toggles</p>
<dd> The `-&#8216; key turns the `current&#8217; window&#8217;s task display <i>On</i> and <i>Off</i>. When <i>On</i>, that task area will show a minimum of the columns header you&#8217;ve established with the `f&#8217; interactive command. It will also reflect any other task area options/toggles you&#8217;ve applied yielding zero or more tasks. </p>
<p> The `_&#8217; key does the same for all task displays. In other words, it switches between the currently visible task display(s) and any task display(s) you had toggled <i>Off</i>. If all 4 task displays are currently visible, this interactive command will leave the summary area as the only display element. </p>
<dt>*&nbsp;<wbr>&nbsp;<code>=</code> | <code>+</code>&nbsp;<wbr>&nbsp;:<i>Equalize/Reset-Window(s) </i></p>
<dd> The `=&#8217; key forces the `current&#8217; window&#8217;s task display to be visible. It also reverses any active `i&#8217; (idle tasks), `n&#8217; (max tasks), `u/U&#8217; (user filter), `o/O&#8217; (other filter), `v&#8217; (hide children), `L&#8217; (locate) and `!&#8217; (combine cpus) commands. Also, if the window had been scrolled, it will be reset with this command. See topic 5c. SCROLLING a Window for additional information regarding vertical and horizontal scrolling. </p>
<p> The `+&#8217; key does the same for all windows. The four task displays will reappear, evenly balanced, while retaining any customizations previously applied beyond those noted for the `=&#8217; command toggle. </p>
<dt>*&nbsp;<wbr>&nbsp;<code>A</code>&nbsp;<wbr>&nbsp;:<i>Alternate-Display-Mode</i> toggle</p>
<dd> This command will switch between full-screen mode and alternate-display mode. </p>
<p> The first time you issue this command, all four task displays will be shown. Thereafter when you switch modes, you will see only the task display(s) you&#8217;ve chosen to make visible. </p>
<dt>*&nbsp;<wbr>&nbsp;<code>a</code> | <code>w</code>&nbsp;<wbr>&nbsp;:<i>Next-Window-Forward/Backward </i></p>
<dd> This will change the `current&#8217; window, which in turn changes the window to which commands are directed. These keys act in a circular fashion so you can reach any desired window using either key. </p>
<p> Assuming the window name is visible (you have not toggled `l&#8217; <i>Off</i>), whenever the `current&#8217; window name loses its emphasis/color, that&#8217;s a reminder the task display is <i>Off</i> and many commands will be restricted. </p>
<dt>*&nbsp;<wbr>&nbsp;<code>g</code>&nbsp;<wbr>&nbsp;:<i>Choose-Another-Window/Field-Group </i></p>
<dd> You will be prompted to enter a number between 1 and 4 designating the field group which should be made the `current&#8217; window. </p>
<p> In full-screen mode, this command is necessary to alter the `current&#8217; window. In alternate-display mode, it is simply a less convenient alternative to the `a&#8217; and `w&#8217; commands. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>G</code>&nbsp;<wbr>&nbsp;:<i>Change-Window/Field-Group-Name </i></p>
<dd> You will be prompted for a new name to be applied to the `current&#8217; window. It does not require that the window name be visible (the `l&#8217; toggle to be <i>On</i>). </p>
<dt>*</p>
<dd> The interactive commands shown with an asterisk (`*&#8217;) have use beyond alternate-display mode. </p>
<pre>
    =, A, g    are always available
    a, w       act the same with color mapping
               and fields management
</pre>
</dl>
<h3>5c. SCROLLING a Window</h3>
<p> Typically a task window is a partial view into a systems&#8217;s total tasks/threads which shows only some of the available fields/columns. With these scrolling keys, you can move that view vertically or horizontally to reveal any desired task or column. </p>
<dl>
<dt><code>Up</code>,<code>PgUp</code>&nbsp;<wbr>&nbsp;:<i>Scroll-Tasks </i></p>
<dd> Move the view up toward the first task row, until the first task is displayed at the top of the `current&#8217; window. The <i>Up</i> arrow key moves a single line while <i>PgUp</i> scrolls the entire window. </p>
<dt><code>Down</code>,<code>PgDn</code>&nbsp;<wbr>&nbsp;:<i>Scroll-Tasks </i></p>
<dd> Move the view down toward the last task row, until the last task is the only task displayed at the top of the `current&#8217; window. The <i>Down</i> arrow key moves a single line while <i>PgDn</i> scrolls the entire window. </p>
<dt><code>Left</code>,<code>Right</code>&nbsp;<wbr>&nbsp;:<i>Scroll-Columns </i></p>
<dd> Move the view of displayable fields horizontally one column at a time. </p>
<p> <code>Note</code>: As a reminder, some fields/columns are not fixed-width but allocated all remaining screen width when visible. When scrolling right or left, that feature may produce some unexpected results initially. </p>
<p> Additionally, there are special provisions for any variable width field when positioned as the last displayed field. Once that field is reached via the right arrow key, and is thus the only column shown, you can continue scrolling horizontally within such a field. See the `C&#8217; interactive command below for additional information. </p>
<dt><code>Home</code>&nbsp;<wbr>&nbsp;:<i>Jump-to-Home-Position </i></p>
<dd> Reposition the display to the un-scrolled coordinates. </p>
<dt><code>End</code>&nbsp;<wbr>&nbsp;:<i>Jump-to-End-Position </i></p>
<dd> Reposition the display so that the rightmost column reflects the last displayable field and the bottom task row represents the last task. </p>
<p> <code>Note</code>: From this position it is still possible to scroll<i> down</i> and<i> right</i> using the arrow keys. This is true until a single column and a single task is left as the only display element. </p>
<dt><code>C</code>&nbsp;<wbr>&nbsp;:<i>Show-scroll-coordinates</i> toggle</p>
<dd> Toggle an informational message which is displayed whenever the message line is not otherwise being used. That message will take one of two forms depending on whether or not a variable width column has also been scrolled. </p>
<pre>
  <code>scroll coordinates: y = n/n (tasks), x = n/n (fields)</code>
  scroll coordinates: y = n/n (tasks), x = n/n (fields)<code> + nn</code>
</pre>
<p> The coordinates shown as <code>n</code>/<code>n</code> are relative to the upper left corner of the `current&#8217; window. The additional `<code>+&nbsp;nn</code>&#8216; represents the displacement into a variable width column when it has been scrolled horizontally. Such displacement occurs in normal 8 character tab stop amounts via the right and left arrow keys. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>y = n/n (tasks) </code></p>
<dd> The first <code>n</code> represents the topmost visible task and is controlled by scrolling keys. The second <code>n</code> is updated automatically to reflect total tasks. </p>
<dt><code>x = n/n (fields) </code></p>
<dd> The first <code>n</code> represents the leftmost displayed column and is controlled by scrolling keys. The second <code>n</code> is the total number of displayable fields and is established with the `<code>f</code>&#8216; interactive command.</dl>
</dl>
</dl>
<p> The above interactive commands are<code> always</code> available in full-screen mode but<code> never</code> available in alternate-display mode if the `current&#8217; window&#8217;s task display has been toggled <i>Off</i>. </p>
<p> <code>Note</code>: When any form of filtering is active, you can expect some slight aberrations when scrolling since not all tasks will be visible. This is particularly apparent when using the Up/Down arrow keys. </p>
<h3>5d. SEARCHING in a Window</h3>
<p> You can use these interactive commands to locate a task row containing a particular value. </p>
<dl>
<dt><code>L</code>&nbsp;<wbr>&nbsp;:<i>Locate-a-string</i></p>
<dd> You will be prompted for the case-sensitive string to locate starting from the current window coordinates. There are no restrictions on search string content. </p>
<p> Searches are not limited to values from a single field or column. All of the values displayed in a task row are allowed in a search string. You may include spaces, numbers, symbols and even forest view artwork. </p>
<p> Keying &lt;Enter&gt; with no input will effectively disable the `&amp;&#8217; key until a new search string is entered. </p>
<dt><code>&amp;</code>&nbsp;<wbr>&nbsp;:<i>Locate-next</i></p>
<dd> Assuming a search string has been established, top will attempt to locate the next occurrence. </p>
</dl>
<p> When a match is found, the current window is repositioned vertically so the task row containing that string is first. The scroll coordinates message can provide confirmation of such vertical repositioning (see the `C&#8217; interactive command). Horizontal scrolling, however, is never altered via searching. </p>
<p> The availability of a matching string will be influenced by the following factors.</p>
<dl>
<dt>
<dd>
<dl>
<dt>a. Which fields are displayable from the total available,</p>
<dd> see topic 3b. MANAGING Fields.</p>
<dt>b. Scrolling a window vertically and/or horizontally,</p>
<dd> see topic 5c. SCROLLING a Window.</p>
<dt>c. The state of the command/command-line toggle,</p>
<dd> see the `c&#8217; interactive command.</p>
<dt>d. The stability of the chosen sort column,</p>
<dd> for example PID is good but %CPU bad.</dl>
</dl>
<p> If a search fails, restoring the `current&#8217; window home (unscrolled) position, scrolling horizontally, displaying command-lines or choosing a more stable sort field could yet produce a successful `&amp;&#8217; search. </p>
<p> The above interactive commands are<code> always</code> available in full-screen mode but<code> never</code> available in alternate-display mode if the `current&#8217; window&#8217;s task display has been toggled <i>Off</i>. </p>
<p> <code>Note</code>: Whenever a Search is active in a window, top will turn column highlighting <i>Off</i> to prevent false matches on internal non-display escape sequences. Such highlighting will be restored when a window&#8217;s search string is empty. See the `x&#8217; interactive command for additional information on sort column highlighting. </p>
<h3>5e. FILTERING in a Window</h3>
<p> You can use this `Other Filter&#8217; feature to establish selection criteria which will then determine which tasks are shown in the `current&#8217; window. Such filters can be made presistent if preserved in the rcfile via the &#8216;W&#8217; interactive command. </p>
<p> Establishing a filter requires: 1) a field name; 2) an operator; and 3) a selection value, as a minimum. This is the most complex of top&#8217;s user input requirements so, when you make a mistake, command recall will be your friend. Remember the Up/Down arrow keys or their aliases when prompted for input. </p>
<p> <code>Filter Basics</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>1. field names are case sensitive and spelled as in the header</p>
<dd>
<dt>2. selection values need not comprise the full displayed field</p>
<dd>
<dt>3. a selection is either case insensitive or sensitive to case</p>
<dd>
<dt>4. the default is inclusion, prepending `!&#8217; denotes exclusions</p>
<dd>
<dt>5. multiple selection criteria can be applied to a task window</p>
<dd>
<dt>6. inclusion and exclusion criteria can be used simultaneously</p>
<dd>
<dt>7. the 1 equality and 2 relational filters can be freely mixed</p>
<dd>
<dt>8. separate unique filters are maintained for each task window</p>
<dd>
</dl>
<p> If a field is not turned on or is not currently in view, then your selection criteria will not affect the display. Later, should a filtered field become visible, the selection criteria will then be applied.</dl>
<p> <code>Keyboard Summary</code></p>
<dl>
<dt>&nbsp;<wbr>&nbsp;<code>o</code>&nbsp;<wbr>&nbsp;:<i>Other-Filter</i> (lower case)</p>
<dd> You will be prompted to establish a filter that <code>ignores case</code> when matching. </p>
<dt>&nbsp;<wbr>&nbsp;<code>O</code>&nbsp;<wbr>&nbsp;:<i>Other-Filter</i> (upper case)</p>
<dd> You will be prompted to establish a <code>case sensitive</code> filter. </p>
<dt>&nbsp;<code>^O</code>&nbsp;<wbr>&nbsp;:<i>Show-Active-Filters</i> (Ctrl key + `o&#8217;)</p>
<dd> This can serve as a reminder of which filters are active in the `current&#8217; window. A summary will be shown on the message line until you press the &lt;Enter&gt; key. </p>
<dt>&nbsp;<wbr>&nbsp;<code>=</code>&nbsp;<wbr>&nbsp;:<i>Reset-Filtering</i> in current window</p>
<dd> This clears all of your selection criteria in the `current&#8217; window. It also has additional impact so please see topic 4a. GLOBAL Commands. </p>
<dt>&nbsp;<wbr>&nbsp;<code>+</code>&nbsp;<wbr>&nbsp;:<i>Reset-Filtering</i> in all windows</p>
<dd> This clears the selection criteria in all windows, assuming you are in alternate-display mode. As with the `=&#8217; interactive command, it too has additional consequences so you might wish to see topic 5b. COMMANDS for Windows. </p>
</dl>
<p> <code>Input Requirements</code></p>
<dl>
<dt>
<dd>
<p> When prompted for selection criteria, the data you provide must take one of two forms. There are 3 required pieces of information, with a 4th as optional. These examples use spaces for clarity but your input generally would not. </p>
<pre>
        #1           <code>#2</code>  #3              ( required )
        Field-Name   ?   include-if-value
     <code>!</code>  Field-Name   ?   <code>exclude</code>-if-value
     #4                                  ( optional )
</pre>
<p> Items #1, #3 and #4 should be self-explanatory. Item <code>#2</code> represents both a required <i>delimiter</i> and the <i>operator</i> which must be one of either equality (`=&#8217;) or relation (`&lt;&#8216; or `&gt;&#8217;). </p>
<p> The `=&#8217; equality operator requires only a partial match and that can reduce your `if-value&#8217; input requirements. The `&gt;&#8217; or `&lt;&#8216; relational operators always employ string comparisons, even with numeric fields. They are designed to work with a field&#8217;s default <i>justification</i> and with homogeneous data. When some field&#8217;s numeric amounts have been subjected to <i>scaling</i> while others have not, that data is no longer homogeneous. </p>
<p> If you establish a relational filter and you <code>have</code> changed the default Numeric or Character <i>justification</i>, that filter is likely to fail. When a relational filter is applied to a memory field and you <code>have not</code> changed the <i>scaling</i>, it may produce misleading results. This happens, for example, because `100.0m&#8217; (MiB) would appear greater than `1.000g&#8217; (GiB) when compared as strings. </p>
<p> If your filtered results appear suspect, simply altering justification or scaling may yet achieve the desired objective. See the `j&#8217;, `J&#8217; and `e&#8217; interactive commands for additional information.</dl>
<p> <code>Potential Problems</code></p>
<dl>
<dt>
<dd>
<p> These <code>GROUP</code> filters could produce the exact same results or the second one might not display anything at all, just a blank task window. </p>
<pre>
     GROUP=root        ( only the same results when )
     GROUP=ROOT        ( invoked via lower case `o' )
</pre>
<p> Either of these <code>RES</code> filters might yield inconsistent and/or misleading results, depending on the current memory scaling factor. Or both filters could produce the exact same results. </p>
<pre>
     RES&gt;9999          ( only the same results when )
     !RES&lt;10000        ( memory scaling is at `KiB' )
</pre>
<p> This <code>nMin</code> filter illustrates a problem unique to scalable fields. This particular field can display a maximum of 4 digits, beyond which values are automatically scaled to KiB or above. So while amounts greater than 9999 exist, they will appear as 2.6m, 197k, etc. </p>
<pre>
     nMin&gt;9999         ( always a blank task window )
</pre>
</dl>
<p> <code>Potential Solutions</code></p>
<dl>
<dt>
<dd>
<p> These examples illustrate how Other Filtering can be creatively applied to achieve almost any desired result. Single quotes are sometimes shown to delimit the spaces which are part of a filter or to represent a request for status (^O) accurately. But if you used them with if-values in real life, no matches would be found. </p>
<p> Assuming field <code>nTH</code> is displayed, the first filter will result in only multi-threaded processes being shown. It also reminds us that a trailing space is part of every displayed field. The second filter achieves the exact same results with less typing. </p>
<pre>
     !nTH=` 1 '                ( ' for clarity only )
     nTH&gt;1                     ( same with less i/p )
</pre>
<p> With Forest View mode active and the <code>COMMAND</code> column in view, this filter effectively collapses child processes so that just 3 levels are shown. </p>
<pre>
     !COMMAND=`       `- '     ( ' for clarity only )
</pre>
<p> The final two filters appear as in response to the status request key (^O). In reality, each filter would have required separate input. The <code>PR</code> example shows the two concurrent filters necessary to display tasks with priorities of 20 or more, since some might be negative. Then by exploiting trailing spaces, the <code>nMin</code> series of filters could achieve the failed `9999&#8242; objective discussed above. </p>
<pre>
     `PR&gt;20' + `!PR=-'         ( 2 for right result )
     `!nMin=0 ' + `!nMin=1 ' + `!nMin=2 ' + `!nMin=3 ' ...
</pre>
</dl>
<p> <code>Note</code>: Whenever Other Filtering is active in a window, top will turn column highlighting <i>Off</i> to prevent false matches on internal non-display escape sequences. Such highlighting will be restored when a window is no longer subject to filtering. See the `x&#8217; interactive command for additional information on sort column highlighting. </p>
<h2>6. FILES</h2>
<h3>6a. PERSONAL Configuration File</h3>
<p> This file is created or updated via the &#8216;W&#8217; interactive command. </p>
<p> The legacy version is written as `$HOME/.your-name-4-top&#8217; + `rc&#8217; with a leading period. </p>
<p> A newly created configuration file is written as procps/your-name-4-top&#8217; + `rc&#8217; without a leading period. The procps directory will be subordinate to either $XDG_CONFIG_HOME when set as an absolute path or the $HOME/.config directory. </p>
<p> While not intended to be edited manually, here is the general layout: </p>
<pre>
    global   # line  1: the program name/alias notation
      &quot;      # line  2: id,altscr,irixps,delay,curwin
    per ea   # line  a: winname,fieldscur
    window   # line  b: winflags,sortindx,maxtasks,etc
      &quot;      # line  c: summclr,msgsclr,headclr,taskclr
    global   # line 15: additional miscellaneous settings
      &quot;      # any remaining lines are devoted to optional
      &quot;      # active 'other filters' discussed in section 5e above
      &quot;      # plus 'inspect' entries discussed in section 6b below
</pre>
<p> If a valid absolute path to the rcfile cannot be established, customizations made to a running top will be impossible to preserve. </p>
<h3>6b. ADDING INSPECT Entries</h3>
<p> To exploit the `Y&#8217; interactive command, you must add entries at the<code> end</code> of the top personal configuration file. Such entries simply reflect a file to be read or command/pipeline to be executed whose results will then be displayed in a separate scrollable, searchable window. </p>
<p> If you don&#8217;t know the location or name of your top rcfile, use the `W&#8217; interactive command to rewrite it and note those details. </p>
<p> Inspect entries can be added with a redirected echo or by editing the configuration file. Redirecting an echo risks overwriting the rcfile should it replace (&gt;) rather than append (&gt;&gt;) to that file. Conversely, when using an editor care must be taken not to corrupt existing lines, some of which will contain unprintable data or unusual characters. </p>
<p> Those Inspect entries beginning with a `#&#8217; character are ignored, regardless of content. Otherwise they consist of the following 3 elements, each of which<i> must</i> be separated by a tab character (thus 2 `	&#8217; total): </p>
<pre>
  .type:  literal `file' or `pipe'
  .name:  selection shown on the Inspect screen
  .fmts:  string representing a path or command
</pre>
<p> The two types of Inspect entries are<i> not</i> interchangeable. Those designated `<code>file</code>&#8216; will be accessed using fopen and must reference a single file in the `.fmts&#8217; element. Entries specifying `<code>pipe</code>&#8216; will employ popen, their `.fmts&#8217; element could contain many pipelined commands and, none can be interactive. </p>
<p> If the file or pipeline represented in your `.fmts&#8217; deals with the specific PID input or accepted when prompted, then the format string must also contain the `<code>%d</code>&#8216; specifier, as these examples illustrate. </p>
<pre>
  .fmts=  /proc/<i>%d</i>/numa_maps
  .fmts=  lsof -P -p<i> %d</i>
</pre>
<p> For `<code>pipe</code>&#8216; type entries only, you may also wish to redirect stderr to stdout for a more comprehensive result. Thus the format string becomes: </p>
<pre>
  .fmts=  pmap -x %d<i> 2&gt;&amp;1</i>
</pre>
<p> Here are examples of both types of Inspect entries as they might appear in the rcfile. The first entry will be ignored due to the initial `#&#8217; character. For clarity, the pseudo tab depictions (^I) are surrounded by an extra space but the actual tabs would not be. </p>
<pre>
  # pipe ^I Sockets ^I lsof -n -P -i 2&gt;&amp;1
  pipe ^I Open Files ^I lsof -P -p %d 2&gt;&amp;1
  file ^I NUMA Info ^I /proc/%d/numa_maps
  pipe ^I Log ^I tail -n100 /var/log/syslog | sort -Mr
</pre>
<p> Except for the commented entry above, these next examples show what could be echoed to achieve similar results, assuming the rcfile name was `.toprc&#8217;. However, due to the embedded tab characters, each of these lines should be preceded by `<code>/bin/echo -e</code>&#8216;, not just a simple an `echo&#8217;, to enable backslash interpretation regardless of which shell you use. </p>
<pre>
  &quot;pipe	Open Files	lsof -P -p %d 2&gt;&amp;1&quot; &gt;&gt; ~/.toprc
  &quot;file	NUMA Info	/proc/%d/numa_maps&quot; &gt;&gt; ~/.toprc
  &quot;pipe	Log	tail -n200 /var/log/syslog | sort -Mr&quot; &gt;&gt; ~/.toprc
</pre>
<p> If any inspect entry you create produces output with unprintable characters they will be displayed in either the ^C notation or hexadecimal &lt;FF&gt; form, depending on their value. This applies to tab characters as well, which will show as `^I&#8217;. If you want a truer representation, any embedded tabs should be expanded. The following example takes what could have been a `file&#8217; entry but employs a `pipe&#8217; instead so as to expand the embedded tabs. </p>
<pre>
  # next would have contained `	' ...
  # file ^I &lt;your_name&gt; ^I /proc/%d/status
  # but this will eliminate embedded `	' ...
  pipe ^I &lt;your_name&gt; ^I cat /proc/%d/status | expand -
</pre>
<p> <code>Note</code>: Some programs might rely on <i>SIGINT</i> to end. Therefore, if a `<code>pipe</code>&#8216; such as the following is established, one must use Ctrl-C to terminate it in order to review the results. This is the single occasion where a `^C&#8217; will not also terminate top. </p>
<pre>
  pipe ^I Trace ^I /usr/bin/strace -p %d 2&gt;&amp;1
</pre>
<p> Lastly, while `<code>pipe</code>&#8216; type entries have been discussed in terms of pipelines and commands, there is nothing to prevent you from including <i> shell scripts</i> as well. Perhaps even newly created scripts designed specifically for the `Y&#8217; interactive command. </p>
<p> For example, as the number of your Inspect entries grows over time, the `Options:&#8217; row will be truncated when screen width is exceeded. That does not affect operation other than to make some selections invisible. However, if some choices are lost to truncation but you want to see more options, there is an easy solution hinted at below. </p>
<pre>
  Inspection Pause at pid ...
  Use:  left/right then &lt;Enter&gt; ...
  Options:  help  1  2  3  4  5  6  7  8  9  10  11 ...
</pre>
<p> The entries in the top rcfile would have a number for the `.name&#8217; element and the `help&#8217; entry would identify a shell script you&#8217;ve written explaining what those numbered selections actually mean. In that way, many more choices can be made visible. </p>
<h3>6c. SYSTEM Configuration File</h3>
<p> This configuration file represents defaults for users who have not saved their own configuration file. The format mirrors exactly the personal configuration file and can also include `inspect&#8217; entries as explained above. </p>
<p> Creating it is a simple process. </p>
<p> 1. Configure top appropriately for your installation and preserve that configuration with the `W&#8217; interactive command. </p>
<p> 2. Add and test any desired `inspect&#8217; entries. </p>
<p> 3. Copy that configuration file to the <i>/etc/</i> directory as `<code>topdefaultrc</code>&#8216;. </p>
<h3>6d. SYSTEM Restrictions File</h3>
<p> The presence of this file will influence which version of the help screen is shown to an ordinary user. </p>
<p> More importantly, it will limit what ordinary users are allowed to do when top is running. They will not be able to issue the following commands. </p>
<pre>
    k        Kill a task
    r        Renice a task
    d or s   Change delay/sleep interval
</pre>
<p> This configuration file is not created by top. Rather, it is created manually and placed it in the <i>/etc/</i> directory as `<code>toprc</code>&#8216;. </p>
<p> It should have exactly two lines, as shown in this example: </p>
<pre>
    s        # line 1: secure mode switch
    5.0      # line 2: delay interval in seconds
</pre>
<h2>7. STUPID TRICKS Sampler</h2>
<p> Many of these tricks work best when you give top a scheduling boost. So plan on starting him with a nice value of -10, assuming you&#8217;ve got the authority. </p>
<h3>7a. Kernel Magic</h3>
<p> For these stupid tricks, top needs full-screen mode. </p>
<dl>
<dt>&bull;</p>
<dd> The user interface, through prompts and help, intentionally implies that the delay interval is limited to tenths of a second. However, you&#8217;re free to set any desired delay. If you want to see Linux at his scheduling best, try a delay of .09 seconds or less. </p>
<p> For this experiment, under x-windows open an xterm and maximize it. Then do the following: </p>
<pre>
  . provide a scheduling boost and tiny delay via:
      nice -n -10 top -d.09
  . keep sorted column highlighting <i>Off</i> so as to
    minimize path length
  . turn <i>On</i> reverse row highlighting for emphasis
  . try various sort columns (TIME/MEM work well),
    and normal or reverse sorts to bring the most
    active processes into view
</pre>
<p> What you&#8217;ll see is a very busy Linux doing what he&#8217;s always done for you, but there was no program available to illustrate this. </p>
<dt>&bull;</p>
<dd> Under an xterm using `white-on-black&#8217; colors, on top&#8217;s Color Mapping screen set the task color to black and be sure that task highlighting is set to bold, not reverse. Then set the delay interval to around .3 seconds. </p>
<p> After bringing the most active processes into view, what you&#8217;ll see are the ghostly images of just the currently running tasks. </p>
<dt>&bull;</p>
<dd> Delete the existing rcfile, or create a new symlink. Start this new version then type `T&#8217; (a secret key, see topic 4c. Task Area Commands, SORTING) followed by `W&#8217; and `q&#8217;. Finally, restart the program with -d0 (zero delay). </p>
<p> Your display will be refreshed at three times the rate of the former top, a 300% speed advantage. As top climbs the TIME ladder, be as patient as you can while speculating on whether or not top will ever reach the top. </p>
</dl>
<h3>7b. Bouncing Windows</h3>
<p> For these stupid tricks, top needs alternate-display mode. </p>
<dl>
<dt>&bull;</p>
<dd> With 3 or 4 task displays visible, pick any window other than the last and turn idle processes <i>Off</i> using the `i&#8217; command toggle. Depending on where you applied `i&#8217;, sometimes several task displays are bouncing and sometimes it&#8217;s like an accordion, as top tries his best to allocate space. </p>
<dt>&bull;</p>
<dd> Set each window&#8217;s summary lines differently: one with no memory (`m&#8217;); another with no states (`t&#8217;); maybe one with nothing at all, just the message line. Then hold down `a&#8217; or `w&#8217; and watch a variation on bouncing windows &nbsp;&#8212;&nbsp; hopping windows. </p>
<dt>&bull;</p>
<dd> Display all 4 windows and for each, in turn, set idle processes to <i>Off</i> using the `i&#8217; command toggle. You&#8217;ve just entered the &quot;extreme bounce&quot; zone. </p>
</dl>
<h3>7c. The Big Bird Window</h3>
<p> This stupid trick also requires alternate-display mode. </p>
<dl>
<dt>&bull;</p>
<dd> Display all 4 windows and make sure that 1:Def is the `current&#8217; window. Then, keep increasing window size with the `n&#8217; interactive command until all the other task displays are &quot;pushed out of the nest&quot;. </p>
<p> When they&#8217;ve all been displaced, toggle between all visible/invisible windows using the `_&#8217; command toggle. Then ponder this: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;is top fibbing or telling honestly your imposed truth? </p>
</dl>
<h3>7d. The Ol&#8217; Switcheroo</h3>
<p> This stupid trick works best without alternate-display mode, since justification is active on a per window basis. </p>
<dl>
<dt>&bull;</p>
<dd> Start top and make COMMAND the last (rightmost) column displayed. If necessary, use the `c&#8217; command toggle to display command lines and ensure that forest view mode is active with the `V&#8217; command toggle. </p>
<p> Then use the up/down arrow keys to position the display so that some truncated command lines are shown (`+&#8217; in last position). You may have to resize your xterm to produce truncation. </p>
<p> Lastly, use the `j&#8217; command toggle to make the COMMAND column right justified. </p>
<p> Now use the right arrow key to reach the COMMAND column. Continuing with the right arrow key, watch closely the direction of travel for the command lines being shown. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;some lines travel left, while others travel right </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;eventually all lines will Switcheroo, and move right </p>
</dl>
<h2>8. BUGS</h2>
<p> Please send bug reports to </p>
<p>&nbsp;</p>
<h2>9. SEE Also</h2>
<p> <code><a href="/docs/linux/man/1-free/">free</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-uptime/">uptime</a></code>(1), <code><a href="/docs/linux/man/1-atop/">atop</a></code>(1), <code><a href="/docs/linux/man/1-slabtop/">slabtop</a></code>(1), <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8), <code><a href="/docs/linux/man/1-w/">w</a></code>(1) </p>
<h2>Index</h2>
<dt><a href="#lbAI">1. COMMAND-LINE Options</a></p>
<dd>
<dt><a href="#lbAJ">2. SUMMARY Display</a></p>
<dd>
<dt><a href="#lbAN">3. FIELDS / Columns</a></p>
<dd>
<dt><a href="#lbAQ">4. INTERACTIVE Commands</a></p>
<dd>
<dt><a href="#lbAV">5. ALTERNATE-DISPLAY Provisions</a></p>
<dd>
<dt><a href="#lbBB">6. FILES</a></p>
<dd>
<dt><a href="#lbBG">7. STUPID TRICKS Sampler</a></p>
<dd>
<dt><a href="#lbBL">8. BUGS</a></p>
<dd>
<dt><a href="#lbBM">9. SEE Also</a></p>
<dd></dl>
