---
title: "fence_na(8)"
name: "fence_na"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_na/"
description: "fence_na"
---

<p><code>fence_na</code> </p>
<p> This is the fence agent for the Node Assassin fence device.</p>
<h2>Synopsis</h2>
<pre> fence_na -a motoko.alteeve.com -n 2 -l motoko -p secret -o off</pre>
<h2>Description</h2>
<p>This fence agent takes argument from the command line or from the &#8216;fenced&#8217; program and interprets them into calls to send to the Node Assassin fence device. It analyzes the returned information and exits with an appropriate exit code as dictated by the FenceAgentAPI.</p>
<h2>Usage</h2>
<p>Arguments are read from <font SIZE="-1">STDIN</font> as &#8216;variable=value&#8217; pairs, one pair per new line. This is the method used by &#8216;fenced&#8217;. </p>
<p> For testing or manual control, arguments may be passed as command line arguments.</p>
<h2>Overview</h2>
<p>This takes arguments that defined which Node Assassin to call, what node to work on and what action should be taken. These arguments are defined by the FenceAgentAPI. These actions are then translated into a set of Node Assassin states which then get passed to the device.</p>
<h2>Node Assassin Ports</h2>
<p>The FenceAgentAPI refers to &#8220;ports&#8221; while the Node Assassin refers to &#8220;nodes&#8221;. These two terms are thus used interchangably. The reason for the difference is that, internally, Node Assassin maps each node to three &#8220;ports&#8221;; The node&#8217;s power and reset buttons plus the node&#8217;s power feed. </p>
<p> Each node in the Node Assassin can be set to one of four states described in the next section.</p>
<h2>Node Assassin States</h2>
<p>Each Node Assassin port can be set to one of four states. They are:</p>
<h2>0</h2>
<p>This will release the fence on the specified <font SIZE="-1">NA</font> node&#8217;s power and reset ports.</p>
<h2>1</h2>
<p>This state will fence the node specified by the &#8220;port&#8221; argument. The fence will remain active until released. Further, the fence will &#8220;lock out&#8221; the node&#8217;s front-panel buttons until the fence is released.</p>
<h2>2</h2>
<p>This will fence the node for one second. This is meant to provide a mechanism to boot or initiate a clean shut down of a node.</p>
<h2>3</h2>
<p>This state will fence the node for five seconds to 30 seconds, depending on how long it takes for the power feed to drop low. This is meant to provide a way to force crashed nodes to power off without the front-panel lock.</p>
<h2>Options</h2>
<p>Which options are valid depends on how the arguments are passed in. The &#8220;main&#8221; method of passing arguments is via <font SIZE="-1">STDIN</font> as a series of &#8216;varible=value&#8217; pairs, one per line. All arguments accepted this way have command-line arguments passed in via single-dashes switches. Each option below shows either calling method&#8217;s arguments, where available.</p>
<h2>-h</h2>
<p>Prints this help message.</p>
<h2>-v</tt>, <tt>-V</h2>
<p>Prints the version of this fence agent and then the version of any configured, reachable Node Assassins. </tt></p>
<h2>-q</h2>
<p>Tells this fence agent to only print critical messages.</p>
<h2>-d</h2>
<p>Tells this fence agent to print debug messages.</p>
<h2>-a address</tt>, <tt>ipaddr=address</h2>
<p>Tells the fence agent which Node Assassin to use. </p>
<p> </tt><i></i><font SIZE="-1"><i>NOTE</i></font><i>!</i> The name or <font SIZE="-1">IP</font> addresses *MUST* match a name or <font SIZE="-1">IP</font> address defined in <tt>&quot;/etc/cluster/fence_na.conf&quot;</tt>! Specifically, it must match one of the <tt>&quot;node::X::ipaddr&quot;</tt> entries where <tt>&quot;X&quot;</tt> is the <font SIZE="-1">ID</font> of the Node Assassin.</p>
<h2>-l name</tt>, <tt>login=name</h2>
<p>This is the login name used to connect to this fence agent. It must match the value &quot;system::username&quot;</tt> in <tt>&quot;/etc/cluster/fence_na.conf&quot;</tt>.</p>
<h2>-p secret</tt>, <tt>passwd=secret</h2>
<p>This is the login password used to connect to this fence agent. It must match the value &quot;system::password&quot;</tt> in <tt>&quot;/etc/cluster/fence_na.conf&quot;</tt>.</p>
<h2>-n #</tt>, <tt>port=#</h2>
<p>This tells the fence agent which node to act on. </p>
<p> </tt><i></i><font SIZE="-1"><i>NOTE</i></font><i>!</i> Please do not confuse this with the Node Assassin&#8217;s internal concept of a port.</p>
<h2>-o val</tt>, <tt>action=val</h2>
<p>This is the &quot;action&quot;</tt> (formerly <tt>&quot;option&quot;</tt>) to perform on the selected node. Valid actions and how Node Assassin implements them are: </p>
<p> <i></i>&quot;off&quot;<i></i> </p>
<p> This set&#8217;s the node to state 1; Fenced. Internally, it will hit the reset switch for one second to immediately disable the node. Then it will release the reset switch for another second before pressing and holding the power switch. After five seconds, Node Assassin will check the node&#8217;s power feed. If it is still on, it will wait another 25 seconds and check again. If the node is still on, an error will be generated. If the node turns off successfully, the fence is declared a success. reboot </p>
<p> <i></i>&quot;on&quot;<i></i> </p>
<p> This sets the node to state &#8216;0&#8217;; Unfenced. Both the power and reset switches are opened, the Node Assassin will pause for one second and then the power switch will be closed for one second to boot the node (that is, the node is set to &#8220;state 2&#8221;). </p>
<p> <i></i>&quot;reboot&quot;<i></i> </p>
<p> <i>Note</i>: This will do a hard reboot! Do not use when a normal restart would suffice. </p>
<p> This essetially just calls an <tt>&quot;off&quot;</tt> and then an <tt>&quot;on&quot;</tt>. However, the <code>fence_na</code> agent will return a success (exit <tt>0</tt>) even if the <tt>&quot;on&quot;</tt> stage succeeded. As per the FenceAgentAPI, a reboot does not need to successfully boot the node to be concidered a success, it only needs to shut it down. </p>
<p> <i></i>&quot;status&quot;<i></i> </p>
<p> This checks the power feed for the requested node is checked. If the node is on, the agent will exit with code <tt>0</tt>. If the node is off (or disconnected), it will exit with code <tt>1</tt>. If an error occurred calling the Node Assassin, this will exit with code <tt>2</tt>. </p>
<p> Note that this argument is designed to be used by the fence agent and will not print any output to <tt>&quot;STDOUT&quot;</tt>. </p>
<p> <i></i>&quot;monitor&quot;<i>, </i>&quot;list&quot;<i></i></p>
<h2>Node Assassin Specific Actions</h2>
<p><i></i><font SIZE="-1"><i>NOTE</i></font><i></i>: The following states are supported by Node Assassin only. These states are not used by the <tt>&quot;fenced&quot;</tt> daemon and are provided here as a convenience for the user. </p>
<p> Any commands named <tt>*_all</tt> ignore the node value, if set.</p>
<h2>release</h2>
<p>If the node is fenced, the fence will be released. The difference from <tt>&quot;on&quot;</tt> being that this will not boot the node after the fence is released.</p>
<h2>release_all</h2>
<p>This does a <tt>&quot;release&quot;</tt> on all fenced nodes.</p>
<h2>fence_all</h2>
<p>All nodes are fenced. See the <tt>&quot;off&quot;</tt> state above.</p>
<h2>boot</h2>
<p>The power feed of the specific node on the Node Assassin is checked. If it is found to be off, it will be set to state <tt>2</tt> to initiate boot.</p>
<h2>boot_all</h2>
<p>The power feeds of all nodes on the Node Assassin are checked. Any found to be off are set to state <tt>2</tt> to initiate boot.</p>
<h2>shutdown</h2>
<p>The power feed of the specific node on the Node Assassin is checked. If it is found to be on, it will be set to state <tt>2</tt> to initiate an ACPI-induced soft shutdown.</p>
<h2>shutdown_all</h2>
<p>The power feeds of all nodes on the Node Assassin are checked. Any found to be on are set to state <tt>2</tt> to initiate an ACPI-induced soft shutdown.</p>
<h2>forcedown_all</h2>
<p>The power feeds of all nodes on the Node Assassin are checked. Any found to be on are set to state <tt>3</tt>. This state is similar to state <tt>1</tt> (see &quot;<tt>&quot;off&quot;</tt>&quot; above), except that the node&#8217;s front-panel switches are not disabled after the fence completes.</p>
<h2>Examples</h2>
<p>To simulate how &#8216;fenced&#8217; calls the script, create a text file called <tt>&quot;args.txt&quot;</tt> containing: </p>
<pre> # Test file used as input for the NA fence agent.
 ipaddr=ariel.alteeve.com
 port=02
 login=motoko
 passwd=secret
 action=off</pre>
<p>Now use <tt>&quot;cat&quot;</tt> to pipe the contents into the fence agent: </p>
<pre> cat args.txt | fence_na</pre>
<p>This will call the <tt>&quot;off&quot;</tt> function against node #02 connected to the Node Assassin at <tt>&quot;motoko.alteeve.com&quot;</tt>, fencing it. Change the <tt>&quot;action&quot;</tt> line to <tt>&quot;action=on&quot;</tt> and re-run the script to release the fence and boot the node. </p>
<p> To duplicate the same call using command line arguments: </p>
<pre> fence_na -a motoko.alteeve.com -n 2 -l motoko -p secret -o off</pre>
<h2>See Also</h2>
<p><a rel="nofollow" href="http://nodeassassin.org">http://nodeassassin.org</a></p>
<h2>Updated</h2>
<p>Jun. 26, 2010 </p>
<p> Digimer (digimer [at] alteeve.com)</p>
