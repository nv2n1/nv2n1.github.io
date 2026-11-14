---
title: "crm_mon(8)"
name: "crm_mon"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_mon/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_mon</code> <i>mode </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>crm_mon &#8211; Provides a summary of cluster&#8217;s current state. </p>
<p> Outputs varying levels of detail in a number of different formats.</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</p>
<dt><code>-Q</code>, <code>&#8211;quiet</code></p>
<dd>Display only essential output</dl>
<h3>Modes:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;as-html</code>=<i>value</i></p>
<dd>Write cluster status to the named html file</p>
<dt><code>-X</code>, <code>&#8211;as-xml</code></p>
<dd>Write cluster status as xml to stdout. This will enable one-shot mode.</p>
<dt><code>-w</code>, <code>&#8211;web-cgi</code></p>
<dd>Web mode with output suitable for cgi</p>
<dt><code>-s</code>, <code>&#8211;simple-status</code></p>
<dd>Display the cluster status once as a simple one line output (suitable for nagios)</dl>
<h3>Display Options:</h3>
<dl>
<dt><code>-n</code>, <code>&#8211;group-by-node</code></p>
<dd>Group resources by node</p>
<dt><code>-r</code>, <code>&#8211;inactive</code></p>
<dd>Display inactive resources</p>
<dt><code>-f</code>, <code>&#8211;failcounts</code></p>
<dd>Display resource fail counts</p>
<dt><code>-o</code>, <code>&#8211;operations</code></p>
<dd>Display resource operation history</p>
<dt><code>-t</code>, <code>&#8211;timing-details</code></p>
<dd>Display resource operation history with timing details</p>
<dt><code>-c</code>, <code>&#8211;tickets</code></p>
<dd>Display cluster tickets</p>
<dt><code>-W</code>, <code>&#8211;watch-fencing</code></p>
<dd>Listen for fencing events. For use with <code>&#8211;external-agent</code>, <code>&#8211;mail-to</code> and/or <code>&#8211;snmp-traps</code> where supported</p>
<dt><code>-L</code>, <code>&#8211;neg-locations</code>[=<i>value</i>]</p>
<dd>Display negative location constraints [optionally filtered by id prefix]</p>
<dt><code>-A</code>, <code>&#8211;show-node-attributes</code></p>
<dd>Display node attributes</p>
<dt><code>-D</code>, <code>&#8211;hide-headers</code></p>
<dd>Hide all headers</p>
<dt><code>-R</code>, <code>&#8211;show-detail</code></p>
<dd>Show more details (node IDs, individual clone instances)</p>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>Brief output</p>
<dt><code>-j</code>, <code>&#8211;pending</code></p>
<dd>Display pending state if &#8216;record-pending&#8217; is enabled</dl>
<h3>Additional Options:</h3>
<dl>
<dt><code>-i</code>, <code>&#8211;interval</code>=<i>value</i></p>
<dd>Update frequency in seconds</p>
<dt><code>-1</code>, <code>&#8211;one-shot</code></p>
<dd>Display the cluster status once on the console and exit</p>
<dt><code>-N</code>, <code>&#8211;disable-ncurses</code></p>
<dd>Disable the use of ncurses</p>
<dt><code>-d</code>, <code>&#8211;daemonize</code></p>
<dd>Run in the background as a daemon</p>
<dt><code>-p</code>, <code>&#8211;pid-file</code>=<i>value</i></p>
<dd>(Advanced) Daemon pid file location</p>
<dt><code>-E</code>, <code>&#8211;external-agent</code>=<i>value</i></p>
<dd>A program to run when resource operations take place.</p>
<dt> <code>-e</code>, <code>&#8211;external-recipient</code>=<i>value</i> A recipient for your program (assuming you want the program to send something to someone).</dl>
<h2>Examples</h2>
<dd>Display the cluster status on the console with updates as they occur:</p>
<dl>
<dd># crm_mon</dl>
<p> Display the cluster status on the console just once then exit:</p>
<dl>
<dd># crm_mon -1</dl>
<p> Display your cluster status, group resources by node, and include inactive resources in the list:</p>
<dl>
<dd># crm_mon &#8211;group-by-node &#8211;inactive</dl>
<p> Start crm_mon as a background daemon and have it write the cluster status to an HTML file:</p>
<dl>
<dd># crm_mon &#8211;daemonize &#8211;as-html /path/to/docroot/filename.html</dl>
<p> Start crm_mon and export the current cluster status as xml to stdout, then exit.:</p>
<dl>
<dd># crm_mon &#8211;as-xml</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
