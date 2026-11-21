---

title: "tipc-config(1)"
name: "tipc-config"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tipc-config/"
---

<h2>NAME</h2>

 tipc-config - tipc configuration

tipc-config command [command ...] 

The tipc-config tool provides numerous commands for configuring and monitoring a TIPC network. Certain commands are only available to users having network administrator privileges (eg. root) to prevent unauthorized users from reconfiguring the network. 

 Users can pass multiple commands to tipc-config in a single invocation. Commands are normally processed serially, from left to right; exceptions are the &quot;-v&quot;, &quot;-i&quot;, and &quot;-dest&quot; commands, which have an immediate effect on all commands in a command set. If tipc-config detects a failure while executing a set of commands, it exits without attempting any unprocessed commands. 

<h3>Options</h3>

<dl>
<dt>-help
</dt><dd> This usage list 
</dd><dt>-i
</dt><dd> Interactive set operations 
</dd><dt>-l [=&lt;domain&gt;|&lt;linkpat&gt;]
</dt><dd> Get links to domain 
</dd><dt>-log [=&lt;size&gt;]
</dt><dd> Dump/resize log 
</dd><dt>-lp =&lt;linkpat&gt;|&lt;bearer&gt;|&lt;media&gt;/&lt;value&gt;
</dt><dd> Set link priority 
</dd><dt>-ls [=&lt;linkpat&gt;]
</dt><dd> Get link statistics 
</dd><dt>-lsr =&lt;linkpat&gt;
</dt><dd> Reset link statistics 
</dd><dt>-lt =&lt;linkpat&gt;|&lt;bearer&gt;|&lt;media&gt;/&lt;value&gt;
</dt><dd> Set link tolerance 
</dd><dt>-lw =&lt;linkpat&gt;|&lt;bearer&gt;|&lt;media&gt;/&lt;value&gt;
</dt><dd> Set link window 
</dd><dt>-m
</dt><dd> Get media 
</dd><dt>-max_ports [=&lt;value&gt;]
</dt><dd> Get/set max number of ports 
</dd><dt>-max_publ [=&lt;value&gt;]
</dt><dd> Get/set max publications 
</dd><dt>-max_subscr [=&lt;value&gt;]
</dt><dd> Get/set max subscriptions 
</dd><dt>-mng [=enable|disable]
</dt><dd> Get/set remote management 
</dd><dt>-n [=&lt;domain&gt;]
</dt><dd> Get nodes in domain 
</dd><dt>-netid[=&lt;value&gt;]
</dt><dd> Get/set network id 
</dd><dt>-nt [=[&lt;depth&gt;,]&lt;type&gt;[,&lt;low&gt;[,&lt;up&gt;]]]
</dt><dd> Get name table where &lt;depth&gt; = types|names|ports|all 
</dd><dt>-p
</dt><dd> Get port info 
</dd><dt>-s
</dt><dd> Get TIPC status info 
</dd><dt>-v
</dt><dd> Verbose output 
</dd><dt>-V
</dt><dd> Get tipc-config version info 
</dd></dl>

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
