---
title: "srp_daemon(1)"
name: "srp_daemon"
section: "1"
letter: "s"
url: "/docs/linux/man/1-srp_daemon/"
description: "srp_daemon – Discovers SRP targets in an InfiniBand Fabric"
---

<h2 class="name">NAME</h2>
<p> srp_daemon &#8211; Discovers SRP targets in an InfiniBand Fabric</p>
<h2>SYNOPSIS</h2>
<p> <code>srp_daemon [-vVcaeon] [-d </code><i>umad-device</i> | -i <i>infiniband-device</i> [-p <i>port-num</i>]] [-t <i>timeout(ms)</i>] [-r <i>retries</i>] [-R <i>Rescan-time</i>] [-f <i>rules-File</i>] </p>
<h2>DESCRIPTION</h2>
<p> Discovers and connects to InfiniBand SCSI RDMA Protocol (SRP) targets in an IB fabric. </p>
<p> Each srp_daemon instance operates on one local port. Upon boot it performs a full rescan of the fabric then waits for an srp_daemon event. An srp_daemon event can be a join of a new machine to the fabric, a change in the capabilities of a machine, an SA change, or an expiration of a predefined timeout. </p>
<p> When a new machine joins the fabric, srp_daemon checks if it is a target. When there is a change of capabilities, srp_daemon checks if the machine has turned into a target. When there is an SA change or a timeout expiration, srp_daemon performs a full rescan of the fabric. </p>
<p> For each target srp_daemon finds, it checks if it should connect to this target according to its rules (default rules file is /etc/srp_daemon.conf) and if it is already connected to the local port. If it should connect to this target and if it is not connected yet, srp_daemon can either print the target details or connect to it. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></dt>
<dd> Print more verbose output</dd>
<dt><code>-V</code></dt>
<dd> Print even more verbose output (debug mode)</dd>
<dt><code>-i</code> <i>infiniband-device</i></dt>
<dd> Work on <i>infiniband-device</i>. This option should not be used with -d.</dd>
<dt><code>-p</code> <i>port-num</i></dt>
<dd> Work on port <i>port-num</i> (default 1). This option must be used with -i and should not be used with -d.</dd>
<dt><code>-d</code> <i>umad-device</i></dt>
<dd> Use device file <i>umad-device</i> (default /dev/infiniband/umad0) This option should not be used with -i or -p.</dd>
<dt><code>-c</code></dt>
<dd> Generate output suitable for piping directly to a /sys/class/infiniband_srp/srp-&lt;device&gt;-&lt;port&gt;/add_target file.</dd>
<dt><code>-a</code></dt>
<dd> Prints all the targets in the fabric, not only targets that are not connected through the local port. (The same as ibsrpdm.)</dd>
<dt><code>-e</code></dt>
<dd> Execute the connection command, i.e., make the connection to the target.</dd>
<dt><code>-o</code></dt>
<dd> Perform only one rescan and exit. (The same as ibsrpdm.)</dd>
<dt><code>-R</code> <i>Rescan-time</i></dt>
<dd> Force a complete rescan every <i>Rescan-time</i> seconds. If -R is not specified, no timeout rescans will be performed.</dd>
<dt><code>-T</code> <i>retry-Timeout</i></dt>
<dd> Retries to connect to existing target after <i>retry-Timeout</i> seconds. If -R is not specified, uses 5 Seconds timeout. if retry-Timeout is 0, will not try to reconnect. The reason srp_daemon retries to connect to the target is because there may be a rare scnerio in which srp_daemon will try to connect to add a target when the target is about to be removed, but is not removed yet.</dd>
<dt><code>-f</code> <i>rules-File</i></dt>
<dd> Decide to which targets to connect according to the rules in <i>rules-File</i>. If <code>-f</code> is not specified, uses the default rules file /etc/srp_daemon.conf. Each line in the <i>rules-File</i> is a rule which can be either an allow connection or a disallow connection according to the first character in the line (a or d accordingly). The rest of the line is values for id_ext, ioc_guid, dgid, service_id. Please take a look at the example section for an example of the file. srp_daemon decide whether to allow or disallow each target according to first rule that match the target. If no rule matches the target, the target is allowed and will be connected. In an allow rule it is possible to set attributes for the connection to the target. Supported attributes are max_cmd_per_lun and max_sect.</dd>
<dt><code>-t</code> <i>timeout</i></dt>
<dd> Use timeout of <i>timeout</i> msec for MAD responses (default: 5 sec).</dd>
<dt><code>-r</code> <i>retries</i></dt>
<dd> Perform <i>retries</i> retries on each send to MAD (default: 3 retries).</dd>
<dt><code>-n</code></dt>
<dd> New format &#8211; use also initiator_ext in the connection command. </dd>
</dl>
<h2>FILES</h2>
<p> /etc/srp_daemon.conf &#8211; Default rules configuration file that indicates to which targets to connect. Can be overridden using the <code>-f</code> <i>rules-File</i> option. Each line in this file is a rule which can be either an allow connection or a disallow connection according to the first character in the line (a or d accordingly). The rest of the line is values for id_ext, ioc_guid, dgid, service_id. Please take a look at the example section for an example of the file. srp_daemon decide whether to allow or disallow each target according to first rule that match the target. If no rule matches the target, the target is allowed and will be connected. In an allow rule it is possible to set attributes for the connection to the target. Supported attributes are max_cmd_per_lun and max_sect. </p>
<h2>EXAMPLES</h2>
<p> srp_daemon -e -i mthca0 -p 1 -R 60 (Connects to the targets accessible through port 1 of mthca0. Performs a complete rescan every minute) </p>
<p> srp_daemon -o -c -a<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> (Prints the connection commands for the targets in the fabric and exits &#8211; similar to ibsrpdm)</p>
<p> srp_daemon -e -f rules.txt<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> (Connects to the targets allowed in the rules file rules.txt)</p>
<pre><code>
An example for a rules configuration file (such as /etc/srp_daemon.conf)
------------------------------------------------------------------------
#Rules file example
#This is a comment
#disallow the following dgid
d       dgid=fe800000000000000002c90200402bd5
#allow target with the following ioc_guid
a       ioc_guid=00a0b80200402bd7
#allow target with the following id_ext and ioc_guid.And setting max_cmd_per_lun to 31.
a       id_ext=200500A0B81146A1,ioc_guid=00a0b80200402bef,max_cmd_per_lun=31
#disallow all the rest
d
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ibsrpdm/">ibsrpdm</a></code>(1) </p>
<h2>AUTHORS</h2>
<dl>
<dt>Roland Dreier</dt>
<dd> &lt;<i>rolandd [at] cisco.com</i>&gt;</dd>
<dt>Ishai Rabinovitz</dt>
<dd> &lt;<i>ishai [at] mellanox.co.il</i>&gt; </dd>
</dl>
<h2>Index</h2>
