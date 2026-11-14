---
title: "smokeping_probes_sendemail(3)"
name: "smokeping_probes_sendemail"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_sendemail/"
---

Smokeping::probes::SendEmail - a Smokeping probe that measure time neeed to send an mail 

<h2>Synopsis</h2><pre> *** Probes ***
 +SendEmail
 bodysize = 0
 forks = 5
 from = test [at] test.com # mandatory
 offset = 50%
 step = 300
 subject = Test
 timeout = 15
 to = # mandatory
 # The following variables can be overridden in each target section
 pings = 5
 port = 25
 # [...]
 *** Targets ***
 probe = SendEmail # if this should be the default probe
 # [...]
 + mytarget
 # probe = SendEmail # if the default probe is something else
 host = my.host
 pings = 5
 port = 25</pre><h2>Description</h2>This probe actually send a mail to a <font SIZE="-1">MX</font> server and measure time it took. You can choose the sender and recipient adress as well as the size of the mail.
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>bodysize
<dd>Size of the mail to send in bytes. If set to 0, a default mail content will be set. Note that mail always contain From, To and Subject headers. 

 Default value: 0
<dt>forks
<dd>Run this many concurrent processes at maximum 

 Example value: 5 

 Default value: 5
<dt>from
<dd>Mail from address 

 Example value: test [at] test.com 

 This setting is mandatory.
<dt>offset
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 50%
<dt>step
<dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 300
<dt>subject
<dd>Subject of the mail 

 Default value: Test
<dt>timeout
<dd>How long a single 'ping' takes at maximum 

 Example value: 15 

 Default value: 5
<dt>to
<dd>Rcpt to address 

 This setting is mandatory.</dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5
<dt>port
<dd>Port of the <font SIZE="-1">SMTP</font> server to reach 

 Default value: 25</dl><h2>Authors</h2><pre> Florian Coulmier &lt;florian [at] coulmier.fr&gt;,</pre><h2>See Also</h2>smokeping_extend
