---
title: "smokeping_probes_webproxyfilter(3)"
name: "smokeping_probes_webproxyfilter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_webproxyfilter/"
---

Smokeping::probes::WebProxyFilter - tests webproxy filter performance and function. 

<h2>Overview</h2>This probe tests if your filtering webproxy is working properly. Drawing from a list of forbidden websites, it tries to establish a connection to each one of them and registers a 'loss' when it suceeeds. 

 If you want to test availability of a website, use the EchoPingHttp probe.
<h2>Synopsis</h2><pre> *** Probes ***
 +WebProxyFilter
 forks = 5
 maxsize = 2000
 min_interval = 0.1
 offset = 50%
 step = 300
 timeout = 15
 useragent = SmokePing/2.x (WebProxyFilter Probe)
 # The following variables can be overridden in each target section
 deny_re = Access Prohibited
 more_hosts = <a rel="nofollow" HREF="http://www.playboy.com">www.playboy.com</a>, <a HREF="http://www.our-competition.com">www.our-competition.com</a>
 pings = 5
 timeout = 2
 # [...]
 *** Targets ***
 probe = WebProxyFilter # if this should be the default probe
 # [...]
 + mytarget
 # probe = WebProxyFilter # if the default probe is something else
 host = my.host
 deny_re = Access Prohibited
 more_hosts = <a rel="nofollow" HREF="http://www.playboy.com">www.playboy.com</a>, <a HREF="http://www.our-competition.com">www.our-competition.com</a>
 pings = 5
 timeout = 2</pre><h2>Description</h2>The probe uses the LWP::UserAgent module to retreive a series of wepages. It expects to get the firewalls 'site-prohibited' page. Any other response (or a real loss) gets logged as a loss and can be used to trigger an alarm. 

 The probe tries to be nice to the firewall and waits at least X seconds between starting filetransfers, where X is the value of the probe specific `min_interval' variable (1 by default). 

 Many variables can be specified either in the probe or in the target definition, the target-specific variable will override the prove-specific variable.
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>forks
<dd>Run this many concurrent processes at maximum 

 Example value: 5 

 Default value: 5
<dt>maxsize
<dd>How much of the webpage should be retreived. 

 Default value: 2000
<dt>min_interval
<dd>The minimum interval between each starting GETs in seconds. 

 Example value: 0.1 

 Default value: 1
<dt>offset
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 50%
<dt>step
<dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 300
<dt>timeout
<dd>How long a single 'ping' takes at maximum 

 Example value: 15 

 Default value: 5
<dt>useragent
<dd>The web browser we claim to be, just in case the <font SIZE="-1">FW</font> is interested 

 Default value: SmokePing/2.x (WebProxyFilter Probe)</dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>deny_re
<dd>Regular expression, matching the 'deny' response from the firewall 

 Example value: Access Prohibited
<dt>more_hosts
<dd>A comma separated list of banned websites to test in addition to the one specified in the <i>host</i> variable. The websites will be tested one after the other in one round, this means that while normal probes do run the same test serveral times in a row, this one will alter the webpage with each round. The reason for this is, that eventhough we try to retreive remote webpages, the answer will come from the firewall everytime, so we kill two birds in one go. First we test the firewalls latency and second we make sure its filter works properly. 

 Example value: <a rel="nofollow" HREF="http://www.playboy.com">www.playboy.com</a>, <a HREF="http://www.our-competition.com">www.our-competition.com</a>
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5
<dt>timeout
<dd>Timeout in seconds for the test complete. 

 Example value: 2 

 Default value: 2</dl><h2>Authors</h2>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; sponsored by Virtela
<h2>Bugs</h2>This probe is somewhat unortodox, since it regards the sucessful retrieval of a banned webpage as a loss.
