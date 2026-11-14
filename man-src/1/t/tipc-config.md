---
title: "tipc-config(1)"
name: "tipc-config"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tipc-config/"
---

<h2>NAME</h2>

 tipc-config - tipc configuration

<h2>SYNOPSIS</h2>

 tipc-config command [command ...] 

<h2>DESCRIPTION</h2>

 The tipc-config tool provides numerous commands for configuring and monitoring a TIPC network. Certain commands are only available to users having network administrator privileges (eg. root) to prevent unauthorized users from reconfiguring the network. 

 Users can pass multiple commands to tipc-config in a single invocation. Commands are normally processed serially, from left to right; exceptions are the &quot;-v&quot;, &quot;-i&quot;, and &quot;-dest&quot; commands, which have an immediate effect on all commands in a command set. If tipc-config detects a failure while executing a set of commands, it exits without attempting any unprocessed commands. 

<h3>Options</h3>

<dl>
<dt>-help
<dd> This usage list 

<dt>-i
<dd> Interactive set operations 

<dt>-l [=&lt;domain&gt;|&lt;linkpat&gt;]
<dd> Get links to domain 

<dt>-log [=&lt;size&gt;]
<dd> Dump/resize log 

<dt>-lp =&lt;linkpat&gt;|&lt;bearer&gt;|&lt;media&gt;/&lt;value&gt;
<dd> Set link priority 

<dt>-ls [=&lt;linkpat&gt;]
<dd> Get link statistics 

<dt>-lsr =&lt;linkpat&gt;
<dd> Reset link statistics 

<dt>-lt =&lt;linkpat&gt;|&lt;bearer&gt;|&lt;media&gt;/&lt;value&gt;
<dd> Set link tolerance 

<dt>-lw =&lt;linkpat&gt;|&lt;bearer&gt;|&lt;media&gt;/&lt;value&gt;
<dd> Set link window 

<dt>-m
<dd> Get media 

<dt>-max_ports [=&lt;value&gt;]
<dd> Get/set max number of ports 

<dt>-max_publ [=&lt;value&gt;]
<dd> Get/set max publications 

<dt>-max_subscr [=&lt;value&gt;]
<dd> Get/set max subscriptions 

<dt>-mng [=enable|disable]
<dd> Get/set remote management 

<dt>-n [=&lt;domain&gt;]
<dd> Get nodes in domain 

<dt>-netid[=&lt;value&gt;]
<dd> Get/set network id 

<dt>-nt [=[&lt;depth&gt;,]&lt;type&gt;[,&lt;low&gt;[,&lt;up&gt;]]]
<dd> Get name table where &lt;depth&gt; = types|names|ports|all 

<dt>-p
<dd> Get port info 

<dt>-s
<dd> Get TIPC status info 

<dt>-v
<dd> Verbose output 

<dt>-V
<dd> Get tipc-config version info 

</dl>

<h2>EXMAPLES</h2>

 

 Set up TIPC with network id 1234 and address 1.1.8 on eth0 
&nbsp;<wbr>tipc-config -netid=1234 -a=1.1.8 -be=eth:eth0 

 Display the name table 
&nbsp;<wbr>tipc-config -nt 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-tipc-pipe/">tipc-pipe</a>(1) 

<h2>AUTHORS</h2>

 Written by <i>erik.hugne [at] ericsson.com</i> 

<h2>REPORTING BUGS</h2>

 Report ls bugs to <i>tipc-discussion [at] lists.sourceforge.net</i> 

<h2>Index</h2>


