---
title: "arc-vomsac-check(8)"
name: "arc-vomsac-check"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arc-vomsac-check/"
description: "arc-vomsac-check – ARC VOMS AC-based queue policy enforcing plugin"
---

<p>arc-vomsac-check &#8211; ARC VOMS AC-based queue policy enforcing plugin </p>
<h2>Description</h2>
<p><code>ARC VOMS AC-based queue policy enforcing plugin</code> perfors per-queue authorization based on information stored in <code>VOMS AC.</code> </p>
<h2>Synopsis</h2>
<p>arc-vomsac-check [-N] -P &lt;user proxy&gt; -L &lt;A-REX local&gt; [-c &lt;configfile&gt;] [-d &lt;loglevel&gt;] </p>
<h2>Options</h2>
<dl>
<dt><code>-N</code></p>
<dd>treat absence of VOMS AC as allowed access (deny by default)</p>
<dt><code>-P</code> <i>user proxy</i></p>
<dd>path to user proxy certificate file to get VOMS AC from</p>
<dt><code>-L</code> <i>A-REX local</i></p>
<dd>A-REX jobstatus .local file (used to determine submission queue)</p>
<dt><code>-c</code> <i>configfile</i></p>
<dd>plugin configuration file (/etc/arc.conf will be used by default)</p>
<dt><code>-d</code> <i>loglevel</i></p>
<dd>logging level from 0(ERROR) to 5(DEBUG) </p>
</dl>
<h2>Getting A-Rex To Work With Plugin</h2>
<p>You must attach plugin as handler for ACCEPTED state: </p>
<p> <code>authplugin=ACCEPTED 60 /opt/arc/libexec/arc/arc-vomsac-check -L %C/job.%I.local -P %C/job.%I.proxy</code></p>
<h2>Configuration</h2>
<p>Queue policies need to be written into plain text configuration file of the same format as arc.conf. The plugin expects several configuration blocks for every queue identified by [queue] or [queue/name] section. </p>
<p> The attribute value pairs identified by &#8216;ac_policy&#8217; keyword within a queue configuration block represent rules for allowing or denying users to utilize queue. These rules are processed in order of specification. </p>
<p> The first rule that matches the VOMS AC presented by a user stops further processing of remaining rules in the block. If no one rule mathes VOMS AC, access is denied. If no &#8216;ac_policy&#8217; rules supplied in the queue block, access is granted. </p>
<p> Matching rules has the following format: </p>
<p>&nbsp;<wbr>ac_policy=&quot;[+/-]VOMS:&nbsp;<wbr>&lt;mathing FQAN&gt;&quot; </p>
<p> Prepending &#8216;+&#8217; indicate positive match (users with FQAN match are allowed). Prepending &#8216;-&#8216; or &#8216;!&#8217; indicate negative match (users with FQAN match are prohibited). Without any prefix character, rule is treated as positive match. </p>
<p> FQAN format can be specified either in ARC format or general VOMS format: &#8216;/VO=students/Group=physics/Role=production&#8217; is the same as &#8216;/students/physics/Role=production&#8217; or &#8216;/students/Group=physics/Role=production/Capability=NULL&#8217; or any other combinations. Regalar expressions syntax can be used in FQAN specification.</p>
<h2>Example Configuration</h2>
<p>&nbsp;<wbr>[queue/general]<br />
&nbsp;<wbr>ac_policy=&quot;-VOMS:&nbsp;<wbr>/students/Role=production&quot;<br />
&nbsp;<wbr>ac_policy=&quot;-VOMS:&nbsp;<wbr>/students/Group=nosubmission&quot;<br />
&nbsp;<wbr>ac_policy=&quot;VOMS:&nbsp;<wbr>/VO=students&quot;<br />
&nbsp;<wbr><br />
&nbsp;<wbr>[queue]<br />
&nbsp;<wbr>name=&quot;production&quot;<br />
&nbsp;<wbr>ac_policy=&quot;VOMS:&nbsp;<wbr>/students/Role=production&quot;<br />
&nbsp;<wbr>ac_policy=&quot;-VOMS:&nbsp;<wbr>/badvo&quot;<br />
&nbsp;<wbr>ac_policy=&quot;VOMS:&nbsp;<wbr>/.*/Role=production&quot;<br />
&nbsp;<wbr> In the example configuration, queue &quot;general&quot; can NOT be used by VO &quot;students&quot; users with Role &quot;production&quot; and VO &quot;students&quot; &quot;nosubmission&quot; Group. It CAN be used by any other members of VO &quot;students&quot;. </p>
<p> Queue &quot;production&quot; allow access to VO &quot;students&quot; users with Role &quot;production&quot;, prohibit some VO &quot;badvo&quot; and allow any VO users with Role &quot;production&quot;. First rule may be omitted due to common regex.</p>
<h2>Author</h2>
<p>Andrii Salnikov &lt;manf at grid dot org dot ua&gt;</p>
