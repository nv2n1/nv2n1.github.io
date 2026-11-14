---
title: "irsim(1)"
name: "irsim"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irsim/"
description: "irsim – An event-driven logic-level simulator for MOS circuits"
---

<h2 class="name">NAME</h2>
<p> irsim &#8211; An event-driven logic-level simulator for MOS circuits </p>
<h2>SYNOPSIS</h2>
<p> <code>irsim </code><i>[-s] prm_file sim_file &#8230; [+hist_file] [-cmd_file &#8230;] </i></p>
<h2>DESCRIPTION</h2>
<p> IRSIM is an event-driven logic-level simulator for MOS (both N and P) transistor circuits. Two simulation models are available:</p>
<dl>
<dt><code>switch</code></p>
<dd> Each transistor is modeled as a voltage-controlled switch. Useful for initializing or determining the functionality of the network.</p>
<dt><code>linear</code></p>
<dd> Each transistor is modeled as a resistor in series with a voltage-controlled switch; each node has a capacitance. Node values and transition times are computed from the resulting RC network, using Chorng-Yeoung Chu&#8217;s model. Chris Terman&#8217;s original model is not supported any more.</dl>
<p> If the <code>-s</code> switch is specified, 2 or more transistors of the same type connected in series, with no other connections to their common source/drain will be <i>stacked</i> into a compound transistor with multiple gates. </p>
<p> The <code>prm_file</code> is the electrical parameters file that configure the devices to be simulated. It defines the capacitance of the various layers, transistor resistances, threshold voltages, etc&#8230; (see <a href="/docs/linux/man/1-presim/">presim</a>(1)). </p>
<p> If <i>prm_file</i> does not specify an absolute path then IRSIM will search for the <i>prm_file</i> as follows (in that order): </p>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1) <i>./&lt;prm_file&gt;</i> (in the current directory).</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2) <code>${CAD_ROOT}/irsim/</code><i>&lt;prm_file&gt;</i></p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>3) <code>${CAD_ROOT}/irsim/</code><i>&lt;prm_file&gt;</i><code>.prm</code>
</dl>
<dd>The default search directory (nominally /usr/local/lib) can be overriden by setting the environment variable CAD_ROOT to the appropriate directory prior to running IRSIM (i.e. setenv CAD_ROOT /cad/lib). </p>
<p> IRSIM first processes the files named on the command line, then (assuming the exit command has not been processed) accepts commands from the user, executing each command before reading the next. </p>
<p> File names NOT beginning with a &#8216;-&#8216; are assumed to be sim files (see <a href="/docs/linux/man/5-sim/">sim</a>(5)), note that this version does not require to run the sim files through presim. These files are read and added to the network database. There is only a single name space for nodes, so references to node &quot;A&quot; in different network files all refer to the same node. While this feature allows one to modularize a large circuit into several network files, care must be taken to ensure that no unwanted node merges happen due to an unfortunate clash in names. </p>
<p> File names prefaced with a &#8216;-&#8216; are assumed to be command files: text files which contain command lines to be processed in the normal fashion. These files are processed line by line; when an end-of-file is encountered, processing continues with the next file. After all the command files have been processed, and if an &quot;exit&quot; command has not terminated the simulation run, IRSIM will accept further commands from the user, prompting for each one like so:</p>
<dl>
<dt><code>irsim&gt;</code></p>
<dd></dl>
<p> The <code>hist_file</code> is the name of a file created with the <i>dumph</i> command (see below). If it is present, IRSIM will initilize the network to the state saved in that file. This file is different from the ones created with the &quot;&gt;&quot; command since it saves the state of every node for all times, including any pending events. </p>
<p> This version supports changes to the network through the <code>update</code> command. Also, the capability to incrementally re-simulate the network up to the current time is provided by the <code>isim</code> command. </p>
<h2>COMMAND SUMMARY</h2>
<dl>
<dt>
<dd>
<dl>
<dt><code>@ </code><i>filename</i></p>
<dd> take commands from command file</p>
<dt><code>? </code><i>wnode&#8230;</i></p>
<dd> print info about node&#8217;s source/drain connections</p>
<dt><code>! </code><i>wnode&#8230;</i></p>
<dd> print info about node&#8217;s gate connections</p>
<dt><code>&lt; </code><i>filename</i></p>
<dd> restore network state from file</p>
<dt><code>&gt; </code><i>filename</i></p>
<dd> write current network state to file</p>
<dt><code>&lt;&lt; </code><i>filename</i></p>
<dd> same as &quot;&lt;&quot; but restores inputs too</p>
<dt><code>| </code><i>comment&#8230;</i></p>
<dd> comment line</p>
<dt><code>activity </code><i>from [to]</i></p>
<dd> graph circuit activity in time interval</p>
<dt><code>ana </code><i>wnode&#8230;</i></p>
<dd> display nodes in analyzer window</p>
<dt><code>analyzer </code><i>wnode&#8230;</i></p>
<dd> display nodes in analyzer window</p>
<dt><code>assert </code><i>wnode [m] val</i></p>
<dd> assert that <i>wnode</i> equals <i>value</i></p>
<dt><code>assertWhen nodeT valT node val</code></p>
<dd> assert when a condition is met</p>
<dt><code>back </code><i>[time]</i></p>
<dd> move back to <i>time</i></p>
<dt><code>c </code><i>[n]</i></p>
<dd> simulate for <i>n</i> clock cycles (default:1)</p>
<dt><code>changes </code><i>from [to]</i></p>
<dd> print nodes that changed in time interval</p>
<dt><code>clock </code><i>[node [val]]</i></p>
<dd> define value sequence for clock node</p>
<dt><code>clear</code></p>
<dd> clear analyzer window (remove signals)</p>
<dt><code>d </code><i>[wnode]&#8230;</i></p>
<dd> print display list or specified node(s)</p>
<dt><code>debug </code><i>[debug_level&#8230;]</i></p>
<dd> set debug level (default: off)</p>
<dt><code>decay </code><i>[n]</i></p>
<dd> set charge decay time (0 =&gt; no decay)</p>
<dt><code>display </code><i>[arg]&#8230;</i></p>
<dd> control what gets displayed when</p>
<dt><code>dumph </code><i>filename&#8230;</i></p>
<dd> write net history to file</p>
<dt><code>hist [on|off]</code></p>
<dd> turn history on or off</p>
<dt><code>exit </code><i>[status]</i></p>
<dd> return to system</p>
<dt><code>flush</code> <i>[time]</i></p>
<dd> flush out history up to <i>time</i> (default: now)</p>
<dt><code>h </code><i>wnode&#8230;</i></p>
<dd> make node logic high (1) input</p>
<dt><code>has_coords</code></p>
<dd> print YES if transistor coordinates are available</p>
<dt><code>inputs</code></p>
<dd> print current list of input nodes</p>
<dt><code>ires </code><i>[n]</i></p>
<dd> set incremental resolution to <i>n</i> ns</p>
<dt><code>isim </code><i>[filename]</i></p>
<dd> incrementally resimulate changes form <i>filename</i></p>
<dt><code>l </code><i>wnode&#8230;</i></p>
<dd> make node logic low (0) input</p>
<dt><code>logfile </code><i>[filename]</i></p>
<dd> start/stop log file</p>
<dt><code>model </code><i>[name]</i></p>
<dd> set simulation model to <i>name</i></p>
<dt><code>p</code></p>
<dd> step clock one simulation step (phase)</p>
<dt><code>path </code><i>wnode&#8230;</i></p>
<dd> display critical path for last transition of a node</p>
<dt><code>powlogfile </code><i>[filename]</i></p>
<dd> start/stop power logfile</p>
<dt><code>powtrace </code><i>-[node]&#8230;</i></p>
<dd> start/stop power tracing of specified node(s)/vector(s)</p>
<dt><code>powstep</code></p>
<dd> toggle the display of power estimate for each timestep</p>
<dt><code>print </code><i>comment&#8230;</i></p>
<dd> print specified text</p>
<dt><code>printp</code></p>
<dd> print a list of all pending events</p>
<dt><code>printx</code></p>
<dd> print all undefined (X) nodes</p>
<dt><code>q</code></p>
<dd> terminate input from current stream</p>
<dt><code>R </code><i>[n]</i></p>
<dd> simulate for <i>n</i> cycles (default:longest sequence)</p>
<dt><code>readh </code><i>filename</i></p>
<dd> read history from <i>filename</i></p>
<dt><code>report</code><i>[level]</i></p>
<dd> set/reset reporting of decay events</p>
<dt><code>s </code><i>[n]</i></p>
<dd> simulate for <i>n</i> ns. (default: stepsize)</p>
<dt><code>stepsize </code><i>[n]</i></p>
<dd> set simulation step size to <i>n</i> ns.</p>
<dt><code>set </code><i>vector value</i></p>
<dd> assign <i>value</i> to <i>vector</i></p>
<dt><code>setlog</code><i>[file|off]</i></p>
<dd> log net changes to file (<i>off</i> -&gt; no log)</p>
<dt><code>setpath</p>
<dd> set search path for cmd files</p>
<dt>stats</code></p>
<dd> print event statistics</p>
<dt><code>sumcap</code></p>
<dd> print out the sum of the capacitance of all nodes</p>
<dt><code>t </code><i>[-]wnode&#8230;</i></p>
<dd> start/stop tracing of specified nodes</p>
<dt><code>tcap</code></p>
<dd> print list of shorted transistors</p>
<dt><code>time </code><i>[command]</i></p>
<dd> print resource utilization summary</p>
<dt><code>until wnode [mask] value count</code></p>
<dd> delayed assert based on the clock count.</p>
<dt><code>u </code><i>wnode&#8230;</i></p>
<dd> make node undefined (X) input</p>
<dt><code>unitdelay </code><i>[n]</i></p>
<dd> force transitions to take <i>n</i> ns. (0 disables)</p>
<dt><code>update </code><i>filename</i></p>
<dd> read net changes from file</p>
<dt><code>V </code><i>[node [value&#8230;]]</i></p>
<dd> define sequence of inputs for a node</p>
<dt><code>vector </code><i>label node&#8230;</i></p>
<dd> define bit vector</p>
<dt><code>vsupply </code><i>voltage</i></p>
<dd> set supply voltage for calculating power (default 5V)</p>
<dt><code>w </code><i>[-]wnode&#8230;</i></p>
<dd> add/delete nodes from display list</p>
<dt><code>wnet </code><i>[filename]</i></p>
<dd> write network to file</p>
<dt><code>x </code><i>wnode&#8230;</i></p>
<dd> remove node from input lists</p>
<dt><code>Xdisplay </code><i>[host:n]</i></p>
<dd> set/show X display (for analyzer) </p>
</dl>
</dl>
<dl>
<dt>COMMAND DESCRIPTIONS</p>
<dd></dl>
<p> Commands have the following simple syntax:</p>
<dl>
<dt><code>cmd </code><i>arg1 arg2 &#8230; argn</i><code> &lt;newline&gt;</code></p>
<dd></dl>
<p> where <code>cmd</code> specifies the command to be performed and the <i>argi</i> are arguments to that command. The arguments are separated by spaces (or tabs) and the command is terminated by a <code>&lt;newline&gt;.</code> </p>
<p> If <code>cmd</code> is not one of the built-in commands documented below, IRSIM appends &quot;.cmd&quot; to the command name and tries to open that file as a command file (see &quot;<code>@</code>&quot; command). Thus the command &quot;foo&quot; has the same effect as &quot;<code>@</code> foo.cmd&quot;. </p>
<p> Notation: </p>
<dl>
<dt><code>&#8230;</code></p>
<dd> indicates zero or more repetitions</p>
<dt><code>[ ]</code></p>
<dd> enclosed arguments are optional</p>
<dt><code>node</code></p>
<dd> name of node or vector in network</p>
<dt><code>wnode</code></p>
<dd> name of node or vector in network, can include <code>&#8216;*&#8217;</code> wildcard which matches any sequence of zero or more characters. The pair of characters <code>&#8216;{&#8216;</code> and <code>&#8216;}&#8217;</code> denote iteration over the limits enclosed by it, for example: <code>name{1:10}</code> will expand into <i>name1, name2 &#8230; name10.</i> A 3rd optional argument sets the stride, for example: <code>name{1:10:2}</code> will expand into <i>name1, name3, &#8230; name7, name9.</i></p>
<dt><code>| comment&#8230;</code></p>
<dd> Lines beginning with vertical bar are treated as comments and ignored &#8212; useful for comments or temporarily disabling certain commands in a command file.</dl>
<p> Most commands take one or more node names as arguments. Whenever a node name is acceptible in a command line, one can also use the name of a bit vector. In this case, the command will be applied to each node of the vector (the &quot;<code>t</code>&quot; and &quot;<code>d</code>&quot; treat vectors specially, see below).</p>
<dl>
<dt><code>vector </code><i>label node&#8230;</i></p>
<dd> Define a bit vector named &quot;label&quot; which includes the specified nodes. If you redefine a bit vector, any special attributes of the old vector (e.g., being on the display or trace list) are lost. Wild cards are not accepted in the list of node names since you would have no control over the order in which matching nodes would appear in the vector.</dl>
<p> The simulator performs most commands silently. To find out what&#8217;s happened you can use one of the following commands to examine the state of the network and/or the simulator.</p>
<dl>
<dt><code>set </code><i>vector value</i></p>
<dd> Assign <i>value</i> to <i>vector.</i> For example, the following sequence of commands:</p>
<dl>
<dt>
<dd>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>vector </code>BUS bit.1 bit.2 bit.3</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>set </code>BUS 01x
</dl>
<dt>
<dd> The first command will define <i>BUS</i> to be a vector composed of nodes <i>bit.1, bit.2,</i> and <i>bit.3.</i> The second command will assign the following values:</dl>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>bit.1 = 0</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>bit.2 = 1</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>bit.3 = X</p>
<dt>
<dd>
<dd>Value can be any sequence of [0,1,h,H,l,L,x,X], and must be of the same length as the bit vector itself.</p>
<dt><code>d </code><i>[wnode]&#8230;</i></p>
<dd> Display. Without arguments displays the values all nodes and bit vectors currently on the display list (see <code>w</code> command). With arguments, only displays the nodes or bit vectors specified. See also the &quot;display&quot; command if you wish to have the display list printed out automatically at the end of certain simulation commands.</p>
<dt><code>w </code><i>[-]wnode&#8230;</i></p>
<dd> Watch/unwatch one or more nodes. Whenever a &quot;<code>d</code>&quot; command is given, each watched node will displayed like so:</p>
<dt>
<dd> <code>node1=0 node2=X &#8230;</code></dl>
<dl>
<dt>
<dd> To remove a node from the watched list, preface its name with a &#8216;-&#8216;. If <i>wnode</i> is the name of a bit vector, the values of the nodes which make up the vector will be displayed as follows:</dl>
<dl>
<dt>
<dd> <code>label=010100</code></dl>
<dl>
<dt>
<dd> where the first 0 is the value of first node in the list, the first 1 the value of the second node, etc.</dl>
<dl>
<dt><code>assert </code><i>wnode [mask] value</i></p>
<dd> Assert that the boolean value of the node or vector <i>wnode</i> is <i>value</i>. If the comparison fails, an error message is printed. If <i>mask</i> is given then only those bits corresponding to zero bits in <i>mask</i> take part in the comparison, any character other than 0 will skip that bit. The format of the error message is the following:</dl>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(tty, 3): assertion failed on &#8216;name&#8217; 10X10 (1010X)</p>
<dt>
<dd>
<dd>Where <i>name</i> is the name of the vector, followed by the actual value and the expected value enclosed in parenthesis. If a <i>mask</i> is specified, then bits that were not compared are printed as &#8216;-&#8216;.</p>
<dt><code>until wnode [mask] value count</code></p>
<dd> Acts just like the assert command except it requires an additional argument &lt;count&gt; which is the max number of clock cycles to run. Instead of just testing the current state, like assert, until tests for true and if false it runs clock cycles until condition becomes true or count runs out.</p>
<dt><code>ana </code><i>wnode&#8230;</i></p>
<dd> This is a shorthand for the <code>analyzer</code> command (described below).</p>
<dt><code>analyzer </code><i>wnode&#8230;</i></p>
<dd> Add the specified node(s)/vector(s) to the analyzer display list (see <a href="/docs/linux/man/3-irsim-analyzer/">irsim-analyzer</a>(3) for a detailed explanation). If the analyzer window does not exist, it will be created. If no arguments are given and the analyzer window already exists, nothing happens.</p>
<dt><code>Xdisplay </code><i>[host:display]</i></p>
<dd> You must be able to connect to an X-server to start the analyzer. If you haven&#8217;t set up the <code>DISPLAY</code> environment variable properly, the analyzer command may fail. If this is the case you can use the <code>Xdisplay</code> command to set it from within the simulator. With no arguments, the name of the current X-server will be printed.</p>
<dt><code>clear</code></p>
<dd> Removes all nodes and vectors from the analyzer window. This command is most useful in command scripts for switching between different signals being displayed on the analyzer.</dl>
<p> &quot;<code>?</code>&quot; and &quot;<code>!</code>&quot; allow the user to go both backwards and forwards through the network. This is a useful debugging aid.</p>
<dl>
<dt><code>? </code><i>wnode&#8230;</i></p>
<dd> Prints a synopsis of the named nodes including their current values and the state of all transistors that affect the value of these nodes. This is the most common way of wandering through the network in search of what went wrong. </p>
<p> The output from the command <i>? out</i> looks like</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>out=0 (vl=0.3 vh=0.8) (0.100 pf) is computed from:</p>
<dt>
<dd>n-channel phi2=0 out=0 in=0 [1.0e+04, 1.3e+04, 8.7e+03]</p>
<dt>
<dd>pulled down by (a=1 b=1) [1.0e+04, 1.3e+04, 8.8e+03]</p>
<dt>
<dd>pulled up [4.0e+04, 7.4e+04, 4.0e+04]</dl>
<p> The first line gives the node&#8217;s name and current value, its low and high logic thresholds, user-specifed low-to-high and high-to-low propagation delays if present, and its capacitance if nonzero. Succeeding lines list the transistor whose sources or drains connect to this node: the transistor type (&quot;pulled down&quot; is an n-channel transistor connected to gnd, &quot;pulled up&quot; is a depletion pullup or p-channel transistor connected to vdd), the values of the gate, source, and drain nodes, and the modeling resistances. Simple chains of transistors with the same implant type are collapsed by the <i>-s</i> option into a single transistor with a &quot;compound&quot; gate; compound gates appear as a parenthesized list of nodes (e.g., the pulldown shown above). The three resistance values &#8212; static, dynamic high, dynamic low &#8212; are given in Kilo-ohms. </p>
<p> Finally, any pending events for a node are listed after the electrical information.</dl>
<dt><code>! </code><i>wnode&#8230;</i></p>
<dd> For each node in the argument list, print a list of transistors controlled by that node.</p>
<dt><code>tcap</code></p>
<dd>
<p> Prints a list of all transistors with their source/drain shorted together or whose source/drain are connected to the power supplies. These transistors will have no effect on the simulation other than their gate capacitance load. Although transistors connected across the power supplies are real design errors, the simulator does not complain about them.</dl>
<p> Any node can be made an input &#8212; the simulator will not change an input node&#8217;s value until it is released. Usually on specific nodes &#8212; inputs to the circuit &#8212; are manipulated using the commands below, but you can fool with a subcircuit by forcing values on internal nodes just as easily.</p>
<dl>
<dt><code>h </code><i>wnode&#8230;</i></p>
<dd> Force each node on the argument list to be a high (1) input. Overrides previous input commands if necessary.</p>
<dt><code>l </code><i>wnode&#8230;</i></p>
<dd> Like &quot;<code>h</code>&quot; except forces nodes to be a low (0) input.</p>
<dt><code>u </code><i>wnode&#8230;</i></p>
<dd> Like &quot;<code>h</code>&quot; except forces nodes to be a undefined (X) input.</p>
<dt><code>x </code><i>wnode&#8230;</i></p>
<dd> Removes nodes from whatever input list they happen to be on. The next simulation step will determine the correct node value from the surrounding circuit. This is the default state of most nodes. Note that this does not force nodes to have an &quot;X&quot; value &#8212; it simply removes them from the input lists.</p>
<dt><code>inputs</code></p>
<dd> prints the high, low, and undefined input lists. </p>
</dl>
<p> It is possible to define a sequence of values for a node, and then cycle the circuit as many times as necessary to input each value and simulate the network. A similar mechanism is used to define the sequence of values each clock node goes through during a single cycle. </p>
<p> Each value is a list of characters (with no intervening blanks) chosen from the following: </p>
<dl>
<dt>
<dd>
<dl>
<dt>1, h, H</p>
<dd> logic high (1)</p>
<dt>0, l, L</p>
<dd> logic low (0)</p>
<dt>u, U</p>
<dd> undefined (X)</p>
<dt>x, X</p>
<dd> remove node from input lists</dl>
</dl>
<p> Presumably the length of the character list is the same as the size of the node/vector to which it will be assigned. Blanks (spaces and tabs) are used to separate values in a sequence. The sequence is used one value at a time, left to right. If more values are needed than supplied by the sequence, IRSIM just restarts the sequence again.</p>
<dl>
<dt><code>V </code><i>[node [value&#8230;]]</i></p>
<dd> Define a vector of inputs for a node. After each cycle of an &quot;R&quot; command, the node is set to the next value specified in the sequence.</dl>
<dl>
<dt>
<dd> With no arguments, clears all input sequences (does not affect clock sequences however). With one argument, &quot;node&quot;, clears any input sequences for that node/vector.</dl>
<dl>
<dt><code>clock </code><i>[node [value&#8230;]]</i></p>
<dd> Define a phase of the clock. Each cycle, each node specified by a clock command must run through its respective values. For example,</dl>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>clock phi1 1 0 0 0</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>clock phi2 0 0 1 0</p>
<dl>
<dt>
<dd>
<dd>defines a simple 4-phase clock using nodes <i>phi1</i> and <i>phi2.</i> Alternatively one could have issued the following commands: </p>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>vector clk phi1 phi2</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>clock clk 10 00 01 00
</dl>
<dd>With no arguments, clears all clock sequences. With one argument, &quot;node&quot;, clears any clock sequences for that node/vector.</dl>
</dl>
<p> After input values have been established, their effect can be propagated through the network with the following commands. The basic simulated time unit is 0.1ns; all event times are quantized into basic time units. A simulation step continues until <i>stepsize</i> ns. have elapsed, and any events scheduled for that interval are processed. It is possible to build circuits which oscillate &#8212; if the period of oscillation is zero, the simulation command will not return. If this seems to be the case, you can hit <code>&lt;ctrl-C&gt;</code> to return to the command interpreter. Note that if you do this while input is being taken from a file, the simulator will bring you to the top level interpreter, aborting all pending input from any command files. </p>
<p> When using the linear model (see the &quot;<code>model</code>&quot; command) transition times are estimated using an RC time constant calculated from the surrounding circuit. When using the switch model, transitions are scheduled with unit delay. These calculations can be overridden for a node by setting its tplh and tphl parameters which will then be used to determine the time for a transition.</p>
<dl>
<dt><code>s </code><i>[n]</i></p>
<dd> Simulation step. Propogates new values for the inputs through the network, returns when <i>n</i> (default: <i>stepsize</i>) ns. have passed. If <i>n</i> is specified, it will temporarily override the <i>stepsize</i> value. Unlike previous versions, this value is NOT remembered as the default value for the <i>stepsize</i> parameter. If the display mode is &quot;automatic&quot;, the current display list is printed out on the completion of this command (see &quot;display&quot; command).</p>
<dt><code>c </code><i>[n]</i></p>
<dd> Cycle <i>n</i> times (default: 1) through the clock, as defined by the &quot;<code>clock</code>&quot; command. Each phase of the clock lasts <i>stepsize</i> ns. If the display mode is &quot;<i>automatic</i>&quot;, the current display list is printed out on the completion of this command (see &quot;<code>display</code>&quot; command).</p>
<dt><code>p</code></p>
<dd> Step the clock through one phase (or simulation step). For example, if the clock is defined as above</dl>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>clock phi1 1 0 0 0</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>clock phi2 0 0 1 0</p>
<dl>
<dt>
<dd>
<dd>then &quot;<code>p</code>&quot; will set phi1 to 1 and phi2 to 0, and then propagate the effects for one simulation step. The next time &quot;<code>p</code>&quot; is issued, phi1 and phi2 will both be set to 0, and the effects propagated, and so on. If the &quot;<code>c</code>&quot; command is issued after &quot;<code>p</code>&quot; has been used, the effect will be to step through the next 4 phases from where the &quot;<code>p</code>&quot; command left off.</dl>
<dt><code>R </code><i>[n]</i></p>
<dd> Run the simulator through <i>n</i> cycles (see the &quot;<code>c</code>&quot; command). If <i>n</i> is not present make the run as long as the longest sequence. If display mode is automatic (see &quot;<code>display</code>&quot; command) the display is printed at the end of each cycle. Each &quot;<code>R</code>&quot; command starts over at the beginning of the sequence defined for each node.</p>
<dt><code>back </code><i>time</i></p>
<dd> Move back to the specified time. This command restores circuit state as of <i>time</i>, effectively undoing any changes in between. Note that you can not move past any previously flushed out history (see <code>flush</code> command below) as the history mechanism is used to restore the network state. This command can be useful to undo a mistake in the input vectors or to re-simulate the circuit with a different debug level.</p>
<dt><code>path </code><i>wnode&#8230;</i></p>
<dd> display critical path(s) for last transition of the specified node(s). The critical path transistions are reported using the following format:</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>node</i><code> -&gt; </code><i>value</i><code> @ </code><i>time</i><code> (</code><i>delta</i><code>)</code></p>
<dt>
<dd>
<dd>where <i>node</i> is the name of the node, <i>value</i> is the value to which the node transitioned, <i>time</i> is the time at which the transistion occurred, and <i>delta</i> is the delay through the node since the last transition. For example:</dl>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>critical path for last transition of Hit_v1:</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>phi1-&gt; 1 @ 2900.0ns , node was an input</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>PC_driver-&gt; 0 @ 2900.4ns (0.4ns)</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>PC_b_q1-&gt; 1 @ 2904.0ns (3.6ns)</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tagDone_b_v1-&gt; 0 @ 2912.8ns (8.8ns)</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tagDone1_v1-&gt; 1 @ 2915.3ns (2.5ns)</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tagDone1_b_v1-&gt; 0 @ 2916.0ns (0.7ns)</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tagDone_v1-&gt; 1 @ 2918.4ns (2.4ns)</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tagCmp_b_v1-&gt; 0 @ 2922.1ns (3.7ns)</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tagCmp_v1-&gt; 1 @ 2923.0ns (0.9ns)</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Vbit_b_v1-&gt; 0 @ 2923.2ns (0.2ns)</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Hit_v1-&gt; 1 @ 2923.5ns (0.3ns)</p>
<dt><code>activity </code><i>from_time [to_time]</i></p>
<dd>
<dd>print histogram showing amount of circuit activity in the specified time inteval. Actually only shows number of nodes which had their most recent transition in the interval.</p>
<dt><code>changes </code><i>from_time [to_time]</i></p>
<dd> print list of nodes which last changed value in the specified time interval.</p>
<dt><code>printp</code></p>
<dd> print list of all pending events sorted in time. The node associated with each event and the scheduled time is printed.</p>
<dt><code>printx</code></p>
<dd> print a list of all nodes with undefined (X) values.</dl>
<p> Using the trace command, it is possible to get more detail about what&#8217;s happening to a particular node. Much of what is said below is described in much more detail in &quot;Logic-level Simulation for VLSI Circuits&quot; by Chris Terman, available from Kluwer Academic Press. When a node is traced, the simulator reports each change in the node&#8217;s value:</p>
<dl>
<dt>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[event #100] node out.1: 0 -&gt; 1 @ 407.6ns
</dl>
<p> The event index is incremented for each event that is processed. The transition is reported as</p>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>old value</i><code> -&gt; </code><i>new value</i><code> @ </code><i>report time</i>
</dl>
<dd>Note that since the time the event is processed may differ from the event&#8217;s report time, the report time for successive events may not be strictly increasing. </p>
<p> Depending on the debug level (see the &quot;<code>debug</code>&quot; command) each calculation of a traced node&#8217;s value is reported: </p>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[event #99] node clk: 0 -&gt; 1 @ 400.2ns</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>final_value( Load ) V=[0.00, 0.04] =&gt; 0</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>..compute_tau( Load )</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>{Rmin=2.2K Rdom=2.2K Rmax=2.2K} {Ca=0.06 Cd=0.17}</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tauA=0.1 tauD=0.4 ns</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[event #99: clk-&gt;1] transition for Load: 1 -&gt; 0 (tau=0.5ns, delay=0.6ns)
</dl>
<dd>In this example, a calculation for node <i>Load</i> is reported. The calculation was caused by event 99 in which node clk went to 1. When using the linear model (as in this example) the report shows</p>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>current value</i><code> -&gt; </code><i>final value</i>
</dl>
<dd>The second line displays information regarding the final value (or dc) analysis for node &quot;Load&quot;; the minimun and maximum voltages as well as the final logical value (0 in this case). </p>
<p> The next three lines display timing analysis information used to estimate the delays. The meaning of the variables displayed can be found Chu&#8217;s thesis: &quot;Improved Models for Switch-Level Simulation&quot;. </p>
<p> When the <i>final value</i> is reported as &quot;D&quot;, the node is not connected to an input and may be scheduled to decay from its current value to X at some later time (see the &quot;<code>decay</code><i>&quot; command). </p>
<p> &quot;tau&quot; is the calculated transition time constant, &quot;delta&quot; is when any consequences of the event will be computed; the difference in the two times is how IRSIM accounts for the shape of the transition waveform on subsequent stages (see reference given above for more details). The middle lines of the report indicate the Thevenin and capacitance parameters of the surrounding networks, i.e., the parameters on which the transition calculations are based.</p>
<dl>
<dt></i><code>debug </code><i>[ev dc tau taup tw spk][off][all]</i></p>
<dd> Set debugging level. Useful for debugging simulator and/or circuit at various levels of the computation. The meaning of the various debug levels is as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ev</code></p>
<dd> display event enqueueing and dequeueing.</p>
<dt><code>dc</code></p>
<dd> display dc calculation information.</p>
<dt><code>tau</code></p>
<dd> display time constant (timing) calculation.</p>
<dt><code>taup</code></p>
<dd> display second time constant (timing) calculation.</p>
<dt><code>tw</code></p>
<dd> display network parameters for each stage of the tree walk, this applies to <code>dc, tau</code>, and <code>taup</code>. This level of debugging detail is usually needed only when debugging the simulator.</p>
<dt><code>spk</code></p>
<dd> displays spike analysis information.</p>
<dt><code>all</code></p>
<dd> This is a shorthand for specifying all of the above.</p>
<dt><code>off</code></p>
<dd> This turns off all debugging information.</dl>
</dl>
<dt>
<dd> If a debug switch is on then during a simulation step, each time a watched node is encounted in some event, that fact is indicated to the user along with some event info. If a node keeps appearing in this prinout, chances are that its value is oscillating. Vice versa, if your circuit never settles (ie., it oscillates) , you can use the &quot;<code>debug</code>&quot; and &quot;<code>t</code>&quot; commands to find the node(s) that are causing the problem. </p>
<p> Without any arguments, the debug command prints the current debug level.</p>
<dt><code>t </code><i>[-]wnode&#8230;</i></p>
<dd> set trace flag for node. Enables the various printouts described above. Prefacing the node name with &#8216;-&#8216; clear its trace flag. If &quot;wnode&quot; is the name of a vector, whenever any node of that vector changes value, the current time and the values of all traced vectors is printed. This feature is useful for watching the relative arrival times of values at nodes in an output vector.</dl>
<p> System interface commands:</p>
<dl>
<dt><code>&gt; </code><i>filename</i></p>
<dd> Write current state of each node into specified file. Useful for making a breakpoint in your simulation run. Only stores values so isn&#8217;t really useful to &quot;dump&quot; a run for later use, i.e., the current input lists, pending events, etc. are NOT saved in the state file.</p>
<dt><code>&lt; </code><i>filename</i></p>
<dd> Read from specified file, reinitializing the value of each node as directed. Note that network must already exist and be identical to the network used to create the dump file with the &quot;&gt;&quot; command. These state saving commands are really provided so that complicated initializing sequences need only be simulated once.</p>
<dt><code>&lt;&lt; </code><i>filename</i></p>
<dd> Same as &quot;<code>&lt;</code>&quot; command, except that this command will restore the <i>input</i> status of the nodes as well. It does not, however, restore pending events.</p>
<dt><code>dumph </code><i>[filename]</i></p>
<dd> Write the history of the simulation to the specified file, that is; all transistions since time = 0. The resulting file is a machine-independent binary file, and contains all the required information to continue simulation at the time the dump takes place. If the filename isn&#8217;t specified, it will be constructed by taking the name of the sim_file (from the command line) and appending &quot;.hist&quot; to it.</p>
<dt><code>readh </code><i>filename</i></p>
<dd> Read the specified history-dump file into the current network. This command will restore the state of the circuit to that of the dump file, overwriting the current state.</p>
<dt><code>flush </code><i>[time]</i></p>
<dd> If memory consumption due to history maintanance becomes prohibitive, this command can be used to free the memory consumed by the history up to the time specified. With no arguments, all history up to the current point in the simulation is freed. Flushing out the history may invalidate an incremental simulation and the portions flushed will no longer appear in the analyzer window.</p>
<dt><code>setpath </code><i>[path&#8230;]</i></p>
<dd> Set the search-path for command files. <i>Path</i> should be a sequence of directories to be searched for &quot;.cmd&quot; files, &quot;.&quot; meaning the current directory. For eaxmple:</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>setpath </code>. /usr/me/rsim/cmds /cad/lib/cmds</p>
<dt>
<dd>
<dd>With no arguments, it will print the current search-path. Initially this is just &quot;.&quot;.</p>
<dt><code>print </code><i>text&#8230;</i></p>
<dd> Simply prints the text on the user&#8217;s console. Useful for keeping user posted of progress through a long command file.</p>
<dt><code>logfile </code><i>[filename]</i></p>
<dd> Create a logfile with the specified name, closing current log file if any; if no argument, just close current logfile. All output which appears on user&#8217;s console will also be placed in the logfile. Output to the logfile is cleverly formatted so that logfiles themselves can serve as command files.</p>
<dt><code>setlog </code><i>[filename | off]</i></p>
<dd> Record all net changes, as well as resulting error messages, to the specified file (see &quot;<code>update</code>&quot; command). Net changes are always appended to the log-file, preceding each sequence of changes by the current date. If the argument is <i>off</i> then net-changes will not be logged. With no arguments, the name of the current log-file is printed. </p>
<p> The default is to always record net changes; if no filename is specified (using the &quot;<code>setlog</code>&quot; command) the default filename <i>irsim_changes.log</i> will be used. The log-files are formatted so that log-files may themselves be used as net-change files.</p>
<dt><code>wnet </code><i>[filename]</i></p>
<dd> Write the current network to the specified file. If the filename isn&#8217;t specified, it will be constructed by taking the name of the sim_file (from the command line) and appending &quot;.inet&quot; to it. The resulting file can be used in a future simulation run, as if it were a sim file. The file produced is a machine independent binary file, which is typically about 1/3 the size of the sim file and about 8 times faster to load.</p>
<dt><code>time </code><i>[command]</i></p>
<dd> With no argument, a summary of time used by the simulator is printed. If arguments are given the specified command is timed and a time summary is printed when the command completes. The format of the time summary is <i>U</i><code>u </code><i>S</i><code>s </code><i>E P</i><code>%</code><i> M</i>, where:</dl>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>U</i> =&gt; User time in seconds</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>S</i> =&gt; System time in seconds</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>E</i> =&gt; Elapsed time, minutes:seconds</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>P</i> =&gt; Percentage of CPU time (((U + S)/E) * 100)</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>M</i> =&gt; Median text, data, and stack size use</p>
<dt><code>q</code></p>
<dd>
<dd>Terminate current input stream. If this is typed at top level, the simulator will exit back to the system; otherwise, input reverts to the previous input stream.</p>
<dt><code>exit </code><i>[n]</i></p>
<dd> Exit to system, <i>n</i> is the reported status (default: 0).</dl>
<p> Simulator parameters are set with the following commands. With no arguments, each of the commands simply prints the current value of the parameter.</p>
<dl>
<dt><code>decay </code><i>[n]</i></p>
<dd> Set decay parameter to <i>n</i> ns. (default: 0). If non-zero, it tells the number of ns. it takes for charge on a node to decay to X. A value of 0 implies no decay at all. You cannot specify this parameters separately for each node, but this turns out not to be a problem. See &quot;<code>report</code>&quot; command.</p>
<dt><code>display </code><i>[-][cmdfile][automatic]</i></p>
<dd> set/reset the display modes, which are</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cmdfile</code></p>
<dd> commands executed from command files are displayed to user before executing. The default is <i>cmdfile = OFF.</i></p>
<dt><code>automatic</code></p>
<dd> print out current display list (see &quot;<code>d</code>&quot; command) after completion of &quot;<code>s</code>&quot; or &quot;<code>c</code>&quot; command. The default is <i>automatic = ON.</i></dl>
</dl>
<dt>
<dd> Prefacing the previous commands with a &quot;-&quot; turns off that display option.</p>
<dt><code>model </code><i>[name]</i></p>
<dd> Set simulation model to one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>switch</code></p>
<dd> Model transistors as voltage controlled switches. This model uses interval logic levels, without accounting for transistor resistances, so circuits with fighting transistors may not be accuratelly modelled. Delays may not reflect the <i>true</i> speed of the circuit as well.</p>
<dt><code>linear</code></p>
<dd> Model transistors as a resistor in series with a voltage controlled switch. This model uses a single-time-constant computed from the resulting RC network and uses a two-time-constant model to analyze charge sharing and spikes.</dl>
</dl>
<dt>
<dd> The default is the <code>linear</code> model. You can change the simulation model at any time &#8212; even with events pending &#8212; as only new calculations are affected. Without arguments, this command prints the current model name.</p>
<dt><code>report </code><i>[level]</i></p>
<dd> When level is nonzero, report all nodes which are set to X because of charge decay, regardless on whether they are being traced. Setting level to zero disables reporting, but not the decay itself (see &quot;<code>decay</code>&quot; command).</p>
<dt><code>stepsize </code><i>[n]</i></p>
<dd> Specify duration of simulation step or clock phase. <i>n is specified</i> in ns. (nanoseconds). Floating point numbers with up to 1 digit past the decimal point are allowed. Further decimals are trucated (i.e. 10.299 == 10.2).</p>
<dt><code>unitdelay </code><i>[n]</i></p>
<dd> When nonzero, force all transitions to take <i>n</i> ns. Setting the parameter to zero disables this feature. The resolution is the same as for the &quot;<code>stepsize</code>&quot; command.</p>
<dt><code>stats</code></p>
<dd> Print event statitistics, as follows:</dl>
<dl>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>changes = 26077</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>punts (cns) = 208 (34)</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>punts = 0.79%, cons_punted = 16.35%</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>nevents = 28012; evaluations = 27972</p>
<dt>
<dd>
<dd>Where <i>changes</i> is the total number of transistions recorded, <i>punts</i> is the number of punted events, <i>(cns)</i> is the number of consecutive punted events (a punted event that punted another event). The penultimate line shows the percentage of punted events with respect to the total number of events, and the percentage of consecutive punted events with respect to the number of punted events. The last line shows the total number of events (nevents) and the number of net evaluations.</dl>
<p> Incremental simulation commands: </p>
<p> <code>Irsim</code> supports incremental changes to the network and resimulation of the resulting network. This is done incrementally so that only the nodes affected by the changes, either directly or indirectly, are re-evaluated. </p>
<dl>
<dt><code>update </code><i>filename</i></p>
<dd> Read net-change tokens from the specified file. The following net-change commands are available: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>a</code>dd</p>
<dd> type gate source drain length width [area]</p>
<dt><code>d</code>elete</p>
<dd> type gate source drain length width [area]</p>
<dt><code>m</code>ove</p>
<dd> type gate source drain length width [area] g s d</p>
<dt><code>c</code>ap</p>
<dd> node value</p>
<dt><code>N</code></p>
<dd> node metal-area poly-area diff-area diff-perim</p>
<dt><code>M</code></p>
<dd> node M2A M2P MA MP PA PP DA DP PDA PDP</p>
<dt><code>t</code>hresh</p>
<dd> node low high</p>
<dt><code>D</code>elay</p>
<dd> node tplh tphl</dl>
</dl>
<dt>
<dd> For a detailed dscription of this file see <a href="/docs/linux/man/5-netchange/">netchange</a>(5). Note that this is an experimental interface and is likely to change in the future.</p>
<dt>
<dd> Note that this command doesn&#8217;t resimulate the circuit so that it may leave the network in an inconsistent state. Usually this command will be followed by an <code>isim</code> command (see below), if that is not the case then it&#8217;s up to the user to initilize the state of the circuit. This command exists only for historical reasons and will probably disappear in the future. It&#8217;s use is discouraged.</p>
<dt><code>isim </code><i>[filename]</i></p>
<dd> Read net-change tokens from the specified file (see <a href="/docs/linux/man/5-netchange/">netchange</a>(5)) and incrementally resimulate the circuit up to the current simulation time (not supported yet).</p>
<dt><code>ires </code><i>n</i></p>
<dd> The incremental algorithm keeps track of nodes deviating from their past behavior as recorded in the network history. During resimulation, a node is considered to deviate from its history if it&#8217;s new state is found to be different within <i>n</i> ns of its previous state. This command allows for changing the incremental resolution. With no arguments, it will print the current resolution. The default resolution is 0 ns.</p>
<dt><code>powlogfile </code><i>[filename]</i></p>
<dd> Opens <i>filename</i> for writting nodal transition reports. The format of the report is the same you get when you trace a node normaly. With no arguments powlogfile just closes the opened logfile and prints out a power dissipation summary. Nodal transitions in inputs are <code>not </code> included in the transition count.</p>
<dt><code>powtrace </code><i>[[-]node&#8230;]</i></p>
<dd> The syntax of this command is the same as the normal <code>t </code> (trace) command. If you want to trace and report power dissipation for all the nodes just use powtrace *. Use powtrace <code>-node </code> if you want to exclude some nodes.</p>
<dt><code>powstep</code></p>
<dd> Toggles whether dynamic power estimation is displayed after each timestep. The ynamic power displayed will only be for the nodes that have been selected using the <code>powtrace </code> command.</p>
<dt><code>vsupply </code><i>voltage</i></p>
<dd> Sets the <code>V </code> variable for use in the <code>P=CV^2/(2t) </code> expression where <code>C </code> is capacitance switched, and <code>t </code> is the timestep. The default value for vsupply is 5.0 Volts.</p>
<dt><code>sumcap</code></p>
<dd> Gives a sum of <code>all </code> nodal capcitances, <code>not </code> just those selected with the <code>powtrace</code> command. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-presim/">presim</a>(1) (now obsolete) </p>
<p> <a href="/docs/linux/man/1-rsim/">rsim</a>(1) </p>
<p> <a href="/docs/linux/man/3-irsim-analyzer/">irsim-analyzer</a>(3) </p>
<p> <a href="/docs/linux/man/5-sim/">sim</a>(5) </p>
<p> <a href="/docs/linux/man/5-netchange/">netchange</a>(5) </p>
<h2>Index</h2>
