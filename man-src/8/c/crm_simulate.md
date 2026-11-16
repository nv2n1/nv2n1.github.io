---
title: "crm_simulate(8)"
name: "crm_simulate"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_simulate/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_simulate</code> <i>datasource operation </i>[<i>additional options</i>]</p>
<h2>Description</h2>
<p>crm_simulate &#8211; Tool for simulating the cluster&#8217;s response to events</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></dt>
<dd>This text</dd>
<dt>-$, <code>&#8211;version</code></dt>
<dd>Version information</dd>
<dt><code>-Q</code>, <code>&#8211;quiet</code></dt>
<dd>Display only essentialoutput</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd>Increase debug output</dd></dl>
<h3>Operations:</h3>
<dl>
<dt><code>-R</code>, <code>&#8211;run</code></dt>
<dd>Determine the cluster&#8217;s response to the given configuration and status</dd>
<dt> <code>-S</code>, <code>&#8211;simulate</code> Simulate the transition&#8217;s execution and display the resulting cluster status</dt>
<dt> <code>-X</code>, <code>&#8211;in-place</code> Simulate the transition&#8217;s execution and store the result back to the input file</dt>
<dt><code>-s</code>, <code>&#8211;show-scores</code></dt>
<dd>
</dd><dd>Show allocation scores</dd>
<dt> <code>-U</code>, <code>&#8211;show-utilization</code> Show utilization information</dt>
<dt><code>-P</code>, <code>&#8211;profile</code>=<i>value</i></dt>
<dd>
</dd><dd>Run all tests in the named directory to create profiling data</dd>
<dt><code>-j</code>, <code>&#8211;pending</code></dt>
<dd>Display pending state if &#8216;record-pending&#8217; is enabled</dd></dl>
<h3>Synthetic Cluster Events:</h3>
<dl>
<dt><code>-u</code>, <code>&#8211;node-up</code>=<i>value</i></dt>
<dd>Bring a node online</dd>
<dt><code>-d</code>, <code>&#8211;node-down</code>=<i>value</i></dt>
<dd>Take a node offline</dd>
<dt><code>-f</code>, <code>&#8211;node-fail</code>=<i>value</i></dt>
<dd>Mark a node as failed</dd>
<dt><code>-i</code>, <code>&#8211;op-inject</code>=<i>value</i></dt>
<dd>Generate a failure for the cluster to react to in the simulation</dd>
<dd>Value is of the form ${resource}_${task}_${interval}@${node}=${rc}. Eg. memcached_monitor_20000 [at] bart.example.com=7 For more information on OCF return codes, refer to: <a rel="nofollow" href="http://www.clusterlabs.org/doc/en-US/Pacemaker/1.1/html/Pacemaker_Explained/s-ocf-return-codes.html">http://www.clusterlabs.org/doc/en-US/Pacemaker/1.1/html/Pacemaker_Explained/s-ocf-return-codes.html</a></dd>
<dt><code>-F</code>, <code>&#8211;op-fail</code>=<i>value</i></dt>
<dd>If the specified task occurs during the simulation, have it fail with return code ${rc}</dd>
<dd>Value is of the form ${resource}_${task}_${interval}@${node}=${rc}. Eg. memcached_stop_0 [at] bart.example.com=1</dd>
<dt>The transition will normally stop at the failed action.</dt>
<dd>Save the result with <code>&#8211;save-output</code> and re-run with <code>&#8211;xml-file</code></dd>
<dt><code>-t</code>, <code>&#8211;set-datetime</code>=<i>value</i></dt>
<dd>Set date/time</dd>
<dt><code>-q</code>, <code>&#8211;quorum</code>=<i>value</i></dt>
<dd>Specify a value for quorum</dd>
<dt><code>-w</code>, <code>&#8211;watchdog</code>=<i>value</i></dt>
<dd>Assume a watchdog device is active</dd>
<dt><code>-g</code>, <code>&#8211;ticket-grant</code>=<i>value</i></dt>
<dd>Grant a ticket</dd>
<dt><code>-r</code>, <code>&#8211;ticket-revoke</code>=<i>value</i></dt>
<dd>Revoke a ticket</dd>
<dt><code>-b</code>, <code>&#8211;ticket-standby</code>=<i>value</i></dt>
<dd>Make a ticket standby</dd>
<dt><code>-e</code>, <code>&#8211;ticket-activate</code>=<i>value</i></dt>
<dd>Activate a ticket</dd></dl>
<h3>Output Options:</h3>
<dl>
<dt><code>-I</code>, <code>&#8211;save-input</code>=<i>value</i></dt>
<dd>Save the input configuration to the named file</dd>
<dt><code>-O</code>, <code>&#8211;save-output</code>=<i>value</i></dt>
<dd>Save the output configuration to the named file</dd>
<dt><code>-G</code>, <code>&#8211;save-graph</code>=<i>value</i></dt>
<dd>Save the transition graph (XML format) to the named file</dd>
<dt><code>-D</code>, <code>&#8211;save-dotfile</code>=<i>value</i></dt>
<dd>Save the transition graph (DOT format) to the named file</dd>
<dt><code>-a</code>, <code>&#8211;all-actions</code></dt>
<dd>Display all possible actions in the DOT graph &#8211; even ones not part of the transition</dd></dl>
<h3>Data Source:</h3>
<dl>
<dt><code>-L</code>, <code>&#8211;live-check</code></dt>
<dd>Connect to the CIB and use the current contents as input</dd>
<dt><code>-x</code>, <code>&#8211;xml-file</code>=<i>value</i></dt>
<dd>Retrieve XML from the named file</dd>
<dt><code>-p</code>, <code>&#8211;xml-pipe</code></dt>
<dd>Retrieve XML from stdin</dd></dl>
<h2>Examples</h2>
<p>Pretend a recurring monitor action found memcached stopped on node fred.example.com and, during recovery, that the memcached stop action failed</p>
<dl>
<dd># crm_simulate -LS &#8211;op-inject memcached:0_monitor_20000 [at] bart.example.com=7 &#8211;op-fail memcached:0_stop_0 [at] fred.example.com=1 &#8211;save-output /tmp/memcached-test.xml</dd></dl>
<p> Now see what the reaction to the stop failure would be</p>
<dl>
<dd># crm_simulate -S &#8211;xml-file /tmp/memcached-test.xml</dd></dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
