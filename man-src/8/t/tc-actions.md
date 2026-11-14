---
title: "tc-actions(8)"
name: "tc-actions"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-actions/"
description: "actions – independently defined actions in tc"
---

<p>actions &#8211; independently defined actions in tc</p>
<h2>Synopsis</h2>
<p><code>tc</code> [ <i>TC_OPTIONS</i> ] <code>actions</code> <code>add</code> | <code>change</code> | <code>replace</code> <i>ACTSPEC</i> <code>tc</code> [ <i>TC_OPTIONS</i> ] <code>actions</code> <code>get</code> | <code>delete</code> <i>ACTISPEC</i> <code>tc</code> [ <i>TC_OPTIONS</i> ] <code>actions flush</code> <i>ACTNAMESPEC</i> <code>tc</code> [ <i>TC_OPTIONS</i> ] <code>actions</code> <code>ls</code> | <code>list</code> <i>ACTNAMESPEC</i> [ <i>ACTFILTER</i> ] <i>ACTSPEC</i> := <code>action</code> <i>ACTDETAIL</i> [ <i>INDEXSPEC</i> ] [ <i>COOKIESPEC</i> ] [ <i>FLAGS</i> ] [ <i>HWSTATSSPEC</i> ] [ <i>CONTROL</i> ] <i>ACTISPEC</i> := <i>ACTNAMESPEC INDEXSPEC</i> <i>ACTNAMESPEC</i> := <code>action</code> ACTNAME <i>INDEXSPEC</i> := <code>index</code><i> INDEX</i> <i>ACTFILTER</i> := <code>since</code><i> MSTIME</i> <i>COOKIESPEC</i> := <code>cookie</code><i> COOKIE</i> <i>FLAGS</i> := <i>no_percpu</i> </p>
<pre><code>HWSTATSSPEC

:=
hw_stats {

    immediate | delayed | disabled }</code></pre>
<p> <i>ACTDETAIL</i> := <i>ACTNAME ACTPARAMS</i> <i>ACTNAME</i> may be any valid action type: gact, mirred, bpf, connmark, csum, police, etc. <i>MSTIME</i> Time since last update. </p>
<pre><code>CONTROL

:= {
    reclassify | pipe | drop | continue | ok

}</code></pre>
<p> <i>TC_OPTIONS</i> These are the options that are specific to <code>tc</code> and not only the options. Refer to <code><a href="/docs/linux/man/8-tc/">tc</a>(8)</code> for more information. </p>
<h2>Description</h2>
<p>The <code>actions</code> object in <code>tc</code> allows a user to define actions independently of a classifier (filter). These actions can then be assigned to one or more filters, with any packets matching the classifier&#8217;s criteria having that action performed on them. Each action type (mirred, police, etc.) will have its own table to store all created actions. </p>
<h2>Operations</h2>
<dl>
<dt><code>add</code></p>
<dd>Create a new action in that action&#8217;s table. </p>
<dt><code>change</code></p>
<dd><code>replace</code> Make modifications to an existing action.</p>
<dt><code>get</code></p>
<dd>Display the action with the specified index value. When combined with the <code>-s</code> option for <code>tc</code>, display the statistics for that action.</p>
<dt><code>delete</code></p>
<dd>Delete the action with the specified index value. If the action is already associated with a classifier, it does not delete the classifier.</p>
<dt><code>ls</code></p>
<dd><code>list</code> List all the actions in the specified table. When combined with the <code>-s</code> option for <code>tc</code>, display the statistics for all actions in the specified table. When combined with the option <code>since</code> allows doing a millisecond time-filter since the last time an action was used in the datapath.</p>
<dt><code>flush</code></p>
<dd>Delete all actions stored in the specified table. </p>
</dl>
<h2>Action Options</h2>
<p>Note that these options are available to all action types.</p>
<dl>
<dt><code>index</code><i> INDEX</i></p>
<dd>Specify the table index value of an action. <i>INDEX</i> is a 32-bit value that is unique to the specific type of action referenced. </p>
<dl>
<dd>For <code>add</code>, <code>change</code>, and <code>replace</code> operations, the index is <code>optional.</code> When adding a new action, specifying an index value will assign the action to that index unless that index value has already been assigned. Omitting the index value for an add operation will cause the kernel to assign a value to the new action.</dl>
<dl>
<dd>For <code>get</code> and <code>delete</code> operations, the index is <code>required</code> to identify the specific action to be displayed or deleted.</dl>
<dt><code>cookie</code><i> COOKIE</i></p>
<dd>In addition to the specific action, mark the matching packet with the value specified by <i>COOKIE</i>. The <i>COOKIE</i> is a 128-bit value that will not be interpreted by the kernel whatsoever. As such, it can be used as a correlating value for maintaining user state. The value to be stored is completely arbitrary and does not require a specific format. It is stored inside the action structure itself. </p>
<dt><i>FLAGS</i></p>
<dd>Action-specific flags. Currently, the only supported flag is <i>no_percpu</i> which indicates that action is expected to have minimal software data-path traffic and doesn&#8217;t need to allocate stat counters with percpu allocator. This option is intended to be used by hardware-offloaded actions. </p>
<dt><code>hw_stats</code><i> HW_STATS</i></p>
<dd>Specifies the type of HW stats of new action. If omitted, any stats counter type is going to be used, according to driver and its resources. The <i>HW_STATS</i> indicates the type. Any of the following are valid:</p>
<dl>
<dd>
<dl>
<dt><code>immediate</code></p>
<dd>Means that in dump, user gets the current HW stats state from the device queried at the dump time.</p>
<dt><code>delayed</code></p>
<dd>Means that in dump, user gets HW stats that might be out of date for some time, maybe couple of seconds. This is the case when driver polls stats updates periodically or when it gets async stats update from the device.</p>
<dt><code>disabled</code></p>
<dd>No HW stats are going to be available in dump.</dl>
</dl>
<dt><code>since</code><i> MSTIME</i></p>
<dd>When dumping large number of actions, a millisecond time-filter can be specified <i>MSTIME</i>. The <i>MSTIME</i> is a millisecond count since last time a packet hit the action. As an example specifying &quot;since 20000&quot; implies to dump all actions that have seen packets in the last 20 seconds. This option is useful when the kernel has a large number of actions and you are only interested in recently used actions. </p>
<dt><i>CONTROL</i></p>
<dd>The <i>CONTROL</i> indicates how <code>tc</code> should proceed after executing the action. Any of the following are valid:</p>
<dl>
<dd>
<dl>
<dt><code>reclassify</code></p>
<dd>Restart the classifiction by jumping back to the first filter attached to the action&#8217;s parent.</p>
<dt><code>pipe</code></p>
<dd>Continue with the next action. This is the default control.</p>
<dt><code>drop</code></p>
<dd>Drop the packed without running any further actions.</p>
<dt><code>continue</code></p>
<dd>Continue the classification with the next filter.</p>
<dt><code>pass</code></p>
<dd>Return to the calling qdisc for packet processing, and end classification of this packet.</dl>
</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-bpf/">tc-bpf</a></code>(8), <code><a href="/docs/linux/man/8-tc-connmark/">tc-connmark</a></code>(8), <code><a href="/docs/linux/man/8-tc-csum/">tc-csum</a></code>(8), <code><a href="/docs/linux/man/8-tc-ife/">tc-ife</a></code>(8), <code><a href="/docs/linux/man/8-tc-mirred/">tc-mirred</a></code>(8), <code><a href="/docs/linux/man/8-tc-nat/">tc-nat</a></code>(8), <code><a href="/docs/linux/man/8-tc-pedit/">tc-pedit</a></code>(8), <code><a href="/docs/linux/man/8-tc-police/">tc-police</a></code>(8), <code><a href="/docs/linux/man/8-tc-simple/">tc-simple</a></code>(8), <code><a href="/docs/linux/man/8-tc-skbedit/">tc-skbedit</a></code>(8), <code><a href="/docs/linux/man/8-tc-skbmod/">tc-skbmod</a></code>(8), <code><a href="/docs/linux/man/8-tc-tunnel_key/">tc-tunnel_key</a></code>(8), <code><a href="/docs/linux/man/8-tc-vlan/">tc-vlan</a></code>(8), <code><a href="/docs/linux/man/8-tc-xt/">tc-xt</a></code>(8) </p>
