---
title: "fwb_ipf(1)"
name: "fwb_ipf"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fwb_ipf/"
description: "fwb_ipf – Policy compiler for ipfilter"
---

<h2>NAME</h2>
<p> fwb_ipf &#8211; Policy compiler for ipfilter</p>
<h2>SYNOPSIS</h2>
<p> <code>fwb_ipf</code> <code>[-vVx]</code> <code>[-d wdir]</code> <code>[-o output.fw]</code> <code>[-i]</code> <code>-f data_file.xml</code> object_name </p>
<h2>DESCRIPTION</h2>
<p> <code>fwb_ipf</code> is a firewall policy compiler component of Firewall Builder (see <a href="/docs/linux/man/1-fwbuilder/">fwbuilder</a>(1)). This compiler generates code for ipfilter. Compiler reads objects definitions and firewall description from the data file specified with &quot;-f&quot; option and generates ipfilter configuration files and firewall activation script. </p>
<p> All generated files have names that start with the name of the firewall object. Firewall activation script has extension &quot;.fw&quot; and is simple shell script that flushes current policy, loads new filter and nat rules and then activates ipfilter. IPFilter configuration file name starts with the name of the firewall object, plus &quot;-ipf.conf&quot;. NAT configuration file name also starts with the name of the firewall object, plus &quot;-nat.conf&quot;. For example, if firewall object has name &quot;myfirewall&quot;, then compiler will create three files: &quot;myfirewall.fw&quot;, &quot;myfirewall-pf.conf&quot;, &quot;myfirewall-nat.conf&quot;. </p>
<p> The data file and the name of the firewall objects must be specified on the command line. Other command line parameters are optional. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-f FILE</p>
<dd> Specify the name of the data file to be processed. </p>
<dt>-o output.fw</p>
<dd> Specify output file name </p>
<dt>-d wdir</p>
<dd> Specify working directory. Compiler creates firewall activation script and ipfilter configuration files in this directory. If this parameter is missing, then all files will be placed in the current working directory. </p>
<dt>-v</p>
<dd> Be verbose: compiler prints diagnostic messages when it works. </p>
<dt>-V</p>
<dd> Print version number and quit. </p>
<dt>-i</p>
<dd> When this option is present, the last argument on the command line is supposed to be firewall object ID rather than its name </p>
<dt>-x</p>
<dd> Generate debugging information while working. This option is intended for debugging only and may produce lots of cryptic messages. </p>
</dl>
<h2>NOTES</h2>
<p> Support for ipf returned in version 1.0.1 of Firewall Builder </p>
<p> Supported features: </p>
<dl>
<dt>o</p>
<dd> both ipf.conf and nat.conf files are generated </p>
<dt>o</p>
<dd> negation in policy rules </p>
<dt>o</p>
<dd> stateful inspection in individual rule can be turned off in rule options dialog. By default compiler adds &quot;keep state&quot; or &quot;modulate state&quot; to each rule with action &#8216;pass&#8217; </p>
<dt>o</p>
<dd> rule options dialog provides a choice of icmp or tcp rst replies for rules with action &quot;Reject&quot; </p>
<dt>o</p>
<dd> compiler adds flag &quot;allow-opts&quot; if match on ip options is needed </p>
<dt>o</p>
<dd> compiler can generate rules matching on TCP flags </p>
<dt>o</p>
<dd> compiler can generate script adding ip aliases for NAT rules using addresses that do not belong to any interface of the firewall </p>
<dt>o</p>
<dd> compiler always adds rule &quot;block quick all&quot; at the very bottom of the script to ensure &quot;block all by default&quot; policy even if the policy is empty. </p>
<dt>o</p>
<dd> Address ranges in both policy and NAT </p>
</dl>
<p> Features that are not supported (yet) </p>
<dl>
<dt>o</p>
<dd> negation in NAT </p>
<dt>o</p>
<dd> custom services </p>
</dl>
<p> Features that won&#8217;t be supported (at least not anytime soon) </p>
<dl>
<dt>o</p>
<dd> policy routing </p>
</dl>
<h2>URL</h2>
<p> Firewall Builder home page is located at the following URL: <code><a rel="nofollow" href="http://www.fwbuilder.org/">http://www.fwbuilder.org/</a></code> </p>
<h2>BUGS</h2>
<p> Please report bugs using bug tracking system on SourceForge: </p>
<p> <code><a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=5314">http://sourceforge.net/tracker/?group_id=5314</a>&amp;atid=105314</code> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fwbuilder/">fwbuilder</a>(1),</code> <code><a href="/docs/linux/man/1-fwb_ipt/">fwb_ipt</a>(1),</code> <code><a href="/docs/linux/man/1-fwb_pf/">fwb_pf</a>(1)</code> </p>
<h2>Index</h2>
