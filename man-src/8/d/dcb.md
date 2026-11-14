---
title: "dcb(8)"
name: "dcb"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dcb/"
description: "dcb – show / manipulate DCB (Data Center Bridging) settings"
---

<p>dcb &#8211; show / manipulate DCB (Data Center Bridging) settings</p>
<h2>Synopsis</h2>
<pre><code>dcb

[ OPTIONS ]

{ app | buffer | ets | maxrate | pfc }

{ COMMAND | help }
</code></pre>
<p> <code>dcb</code> [ <code>-force</code> ] <code>-batch </code><i>filename</i><br />
 <code>dcb</code> [ <i>OPTIONS</i> ] <code>help</code> </p>
<h2>Options</h2>
<dl>
<dt><code>-n</code>,<code> &#8211;netns </code>&lt;NETNS&gt;</p>
<dd>switches <code>dcb</code> to the specified network namespace <i>NETNS</i>. </p>
<dt><code>-V</code>,<code> &#8211;Version</code></p>
<dd>Print the version of the <code>dcb</code> utility and exit. </p>
<dt><code>-b,</code> &#8211;batch <code>&lt;FILENAME&gt;</code></p>
<dd>Read commands from provided file or standard input and invoke them. First failure will cause termination of dcb. </p>
<dt><code>-f,</code> &#8211;force</p>
<dd>Don&#8217;t terminate dcb on errors in batch mode. If there were any errors during execution of the commands, the application return code will be non zero. </p>
<dt><code>-i</code>,<code> &#8211;iec</code></p>
<dd>When showing rates, use ISO/IEC 1024-based prefixes (Ki, Mi, Bi) instead of the 1000-based ones (K, M, B). </p>
<dt><code>-j</code>,<code> &#8211;json</code></p>
<dd>Generate JSON output. </p>
<dt><code>-N</code>,<code> &#8211;Numeric</code></p>
<dd>If the subtool in question translates numbers to symbolic names in some way, suppress this translation. </p>
<dt><code>-p</code>,<code> &#8211;pretty</code></p>
<dd>When combined with -j generate a pretty JSON output. </p>
<dt><code>-s</code>,<code> &#8211;statistics</code></p>
<dd>If the object in question contains any statistical counters, shown them as part of the &quot;show&quot; output. </p>
</dl>
<h2>Objects</h2>
<dl>
<dt><code>app</code></p>
<dd>&#8211; Configuration of application priority table </p>
<dt><code>buffer</code></p>
<dd>&#8211; Configuration of port buffers </p>
<dt><code>ets</code></p>
<dd>&#8211; Configuration of ETS (Enhanced Transmission Selection) </p>
<dt><code>maxrate</code></p>
<dd>&#8211; Configuration of per-TC maximum transmit rate </p>
<dt><code>pfc</code></p>
<dd>&#8211; Configuration of PFC (Priority-based Flow Control) </p>
</dl>
<h2>Commands</h2>
<p>A <i>COMMAND</i> specifies the action to perform on the object. The set of possible actions depends on the object type. As a rule, it is possible to <code>show</code> objects and to invoke topical <code>help,</code> which prints a list of available commands and argument syntax conventions.</p>
<h2>Array Parameters</h2>
<p>Like commands, specification of parameters is in the domain of individual objects (and their commands) as well. However, much of the DCB interface revolves around arrays of fixed size that specify one value per some key, such as per traffic class or per priority. There is therefore a single syntax for adjusting elements of these arrays. It consists of a series of <i>KEY</i><code>:</code><i>VALUE</i> pairs, where the meaning of the individual keys and values depends on the parameter. </p>
<p> The elements are evaluated in order from left to right, and the latter ones override the earlier ones. The elements that are not specified on the command line are queried from the kernel and their current value is retained. </p>
<p> As an example, take a made-up parameter tc-juju, which can be set to charm traffic in a given TC with either good luck or bad luck. <i>KEY</i> can therefore be 0..7 (as is usual for TC numbers in DCB), and <i>VALUE</i> either of <code>none</code>, <code>good</code>, and <code>bad</code>. An example of changing a juju value of TCs 0 and 7, while leaving all other intact, would then be: </p>
<p> # dcb foo set dev eth0 tc-juju 0:good 7:bad </p>
<p> A special key, <code>all</code>, is recognized which sets the same value to all array elements. This can be combined with the usual single-element syntax. E.g. in the following, the juju of all keys is set to <code>none</code>, except 0 and 7, which have other values: </p>
<p> # dcb foo set dev eth0 tc-juju all:none 0:good 7:bad</p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dcb-app/">dcb-app</a></code>(8), <code><a href="/docs/linux/man/8-dcb-buffer/">dcb-buffer</a></code>(8), <code><a href="/docs/linux/man/8-dcb-ets/">dcb-ets</a></code>(8), <code><a href="/docs/linux/man/8-dcb-maxrate/">dcb-maxrate</a></code>(8), <code><a href="/docs/linux/man/8-dcb-pfc/">dcb-pfc</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Petr Machata &lt;me [at] pmachata.org&gt;</p>
