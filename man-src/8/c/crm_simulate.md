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
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-Q</code>, <code>&#8211;quiet</code></p>
<dd>Display only essentialoutput</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</dl>
<h3>Operations:</h3>
<dl>
<dt><code>-R</code>, <code>&#8211;run</code></p>
<dd>Determine the cluster&#8217;s response to the given configuration and status</p>
<dt> <code>-S</code>, <code>&#8211;simulate</code> Simulate the transition&#8217;s execution and display the resulting cluster status</p>
<dt> <code>-X</code>, <code>&#8211;in-place</code> Simulate the transition&#8217;s execution and store the result back to the input file</p>
<dt><code>-s</code>, <code>&#8211;show-scores</code></p>
<dd>
<dd>Show allocation scores</p>
<dt> <code>-U</code>, <code>&#8211;show-utilization</code> Show utilization information</p>
<dt><code>-P</code>, <code>&#8211;profile</code>=<i>value</i></p>
<dd>
<dd>Run all tests in the named directory to create profiling data</p>
<dt><code>-j</code>, <code>&#8211;pending</code></p>
<dd>Display pending state if &#8216;record-pending&#8217; is enabled</dl>
<h3>Synthetic Cluster Events:</h3>
<dl>
<dt><code>-u</code>, <code>&#8211;node-up</code>=<i>value</i></p>
<dd>Bring a node online</p>
<dt><code>-d</code>, <code>&#8211;node-down</code>=<i>value</i></p>
<dd>Take a node offline</p>
<dt><code>-f</code>, <code>&#8211;node-fail</code>=<i>value</i></p>
<dd>Mark a node as failed</p>
<dt><code>-i</code>, <code>&#8211;op-inject</code>=<i>value</i></p>
<dd>Generate a failure for the cluster to react to in the simulation</p>
<dd>Value is of the form ${resource}_${task}_${interval}@${node}=${rc}. Eg. memcached_monitor_20000 [at] bart.example.com=7 For more information on OCF return codes, refer to: <a rel="nofollow" href="http://www.clusterlabs.org/doc/en-US/Pacemaker/1.1/html/Pacemaker_Explained/s-ocf-return-codes.html">http://www.clusterlabs.org/doc/en-US/Pacemaker/1.1/html/Pacemaker_Explained/s-ocf-return-codes.html</a></p>
<dt><code>-F</code>, <code>&#8211;op-fail</code>=<i>value</i></p>
<dd>If the specified task occurs during the simulation, have it fail with return code ${rc}</p>
<dd>Value is of the form ${resource}_${task}_${interval}@${node}=${rc}. Eg. memcached_stop_0 [at] bart.example.com=1</p>
<dt>The transition will normally stop at the failed action.</p>
<dd>Save the result with <code>&#8211;save-output</code> and re-run with <code>&#8211;xml-file</code></p>
<dt><code>-t</code>, <code>&#8211;set-datetime</code>=<i>value</i></p>
<dd>Set date/time</p>
<dt><code>-q</code>, <code>&#8211;quorum</code>=<i>value</i></p>
<dd>Specify a value for quorum</p>
<dt><code>-w</code>, <code>&#8211;watchdog</code>=<i>value</i></p>
<dd>Assume a watchdog device is active</p>
<dt><code>-g</code>, <code>&#8211;ticket-grant</code>=<i>value</i></p>
<dd>Grant a ticket</p>
<dt><code>-r</code>, <code>&#8211;ticket-revoke</code>=<i>value</i></p>
<dd>Revoke a ticket</p>
<dt><code>-b</code>, <code>&#8211;ticket-standby</code>=<i>value</i></p>
<dd>Make a ticket standby</p>
<dt><code>-e</code>, <code>&#8211;ticket-activate</code>=<i>value</i></p>
<dd>Activate a ticket</dl>
<h3>Output Options:</h3>
<dl>
<dt><code>-I</code>, <code>&#8211;save-input</code>=<i>value</i></p>
<dd>Save the input configuration to the named file</p>
<dt><code>-O</code>, <code>&#8211;save-output</code>=<i>value</i></p>
<dd>Save the output configuration to the named file</p>
<dt><code>-G</code>, <code>&#8211;save-graph</code>=<i>value</i></p>
<dd>Save the transition graph (XML format) to the named file</p>
<dt><code>-D</code>, <code>&#8211;save-dotfile</code>=<i>value</i></p>
<dd>Save the transition graph (DOT format) to the named file</p>
<dt><code>-a</code>, <code>&#8211;all-actions</code></p>
<dd>Display all possible actions in the DOT graph &#8211; even ones not part of the transition</dl>
<h3>Data Source:</h3>
<dl>
<dt><code>-L</code>, <code>&#8211;live-check</code></p>
<dd>Connect to the CIB and use the current contents as input</p>
<dt><code>-x</code>, <code>&#8211;xml-file</code>=<i>value</i></p>
<dd>Retrieve XML from the named file</p>
<dt><code>-p</code>, <code>&#8211;xml-pipe</code></p>
<dd>Retrieve XML from stdin</dl>
<h2>Examples</h2>
<p>Pretend a recurring monitor action found memcached stopped on node fred.example.com and, during recovery, that the memcached stop action failed</p>
<dl>
<dd># crm_simulate -LS &#8211;op-inject memcached:0_monitor_20000 [at] bart.example.com=7 &#8211;op-fail memcached:0_stop_0 [at] fred.example.com=1 &#8211;save-output /tmp/memcached-test.xml</dl>
<p> Now see what the reaction to the stop failure would be</p>
<dl>
<dd># crm_simulate -S &#8211;xml-file /tmp/memcached-test.xml</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
