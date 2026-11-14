---
title: "smokeping_probes_curl(3)"
name: "smokeping_probes_curl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_curl/"
---

Smokeping::probes::Curl - a 

<a HREF="/docs/linux/man/1-curl/">curl</a>(1) probe for SmokePing
<h2>Overview</h2>Fetches an <font SIZE="-1">HTTP</font> or <font SIZE="-1">HTTPS URL</font> using <i><a HREF="/docs/linux/man/1-curl/">curl</a></i>(1).
<h2>Synopsis</h2><pre> *** Probes ***
 +Curl
 binary = /usr/bin/curl
 forks = 5
 offset = 50%
 step = 300
 # The following variables can be overridden in each target section
 agent = User-Agent: Lynx/2.8.4rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.6c
 expect = Status: green
 extraargs = -6 --head --user user:password
 extrare = / /
 follow_redirects = yes
 include_redirects = yes
 insecure_ssl = 1
 interface = eth0
 pings = 5
 ssl2 = 1
 timeout = 20
 urlformat = <a rel="nofollow" HREF="http://%host%/">http://%host%/</a> # mandatory
 # [...]
 *** Targets ***
 probe = Curl # if this should be the default probe
 # [...]
 + mytarget
 # probe = Curl # if the default probe is something else
 host = my.host
 agent = User-Agent: Lynx/2.8.4rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.6c
 expect = Status: green
 extraargs = -6 --head --user user:password
 extrare = / /
 follow_redirects = yes
 include_redirects = yes
 insecure_ssl = 1
 interface = eth0
 pings = 5
 ssl2 = 1
 timeout = 20
 urlformat = <a rel="nofollow" HREF="http://%host%/">http://%host%/</a> # mandatory</pre><h2>Description</h2>(see <i><a HREF="/docs/linux/man/1-curl/">curl</a></i>(1) for details of the options below)
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>binary
<dd>The location of your curl binary. 

 Default value: /usr/bin/curl
<dt>forks
<dd>Run this many concurrent processes at maximum 

 Example value: 5 

 Default value: 5
<dt>offset
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 50%
<dt>step
<dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 300</dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>agent
<dd>The ``-A'' <i><a HREF="/docs/linux/man/1-curl/">curl</a></i>(1) option. This is a full <font SIZE="-1">HTTP</font> User-Agent header including the words ``User-Agent:''. Note that it does not need any quotes around it. 

 Example value: User-Agent: Lynx/2.8.4rel.1 libwww-FM/2.14 <font SIZE="-1">SSL-MM/1.4.1</font> OpenSSL/0.9.6c
<dt>expect
<dd>Require the given text to appear somewhere in the response, otherwise probe is treated as a failure 

 Example value: Status: green 

 Default value:
<dt>extraargs
<dd>Any extra arguments you might want to hand to <i><a HREF="/docs/linux/man/1-curl/">curl</a></i>(1). The arguments should be separated by the regexp specified in ``extrare'', which contains just the space character (`` '') by default. 

 Note that curl will be called with the resulting list of arguments without any shell expansion. If you need to specify any arguments containing spaces, you should set ``extrare'' to something else. 

 As a complicated example, to explicitly set the ``Host:'' header in Curl requests, you need to set ``extrare'' to something else, eg. ``/;/'', and then specify <tt>&quot;extraargs = --header;Host: <a rel="nofollow" HREF="http://www.example.com">www.example.com</a>&quot;</tt>. 

 Example value: -6 --head --user user:password
<dt>extrare
<dd>The regexp used to split the extraargs string into an argument list, in the ``/regexp/'' notation. This contains just the space character (`` '') by default, but if you need to specify any arguments containing spaces, you can set this variable to a different value. 

 Example value: / / 

 Default value: / /
<dt>follow_redirects
<dd>If this variable is set to 'yes', curl will follow any <font SIZE="-1">HTTP</font> redirection steps (the '-L' option). If set to 'no', <font SIZE="-1">HTTP</font> Location: headers will not be followed. See also 'include_redirects'. 

 Example value: yes 

 Default value: no
<dt>include_redirects
<dd>If this variable is set to 'yes', the measurement result will include the time spent on following any <font SIZE="-1">HTTP</font> redirection steps. If set to 'no', only the last step is measured. See also 'follow_redirects'. 

 Example value: yes 

 Default value: no
<dt>insecure_ssl
<dd>The ``-k'' <i><a HREF="/docs/linux/man/1-curl/">curl</a></i>(1) option. Accept <font SIZE="-1">SSL</font> connections that don't have a secure certificate chain to a trusted <font SIZE="-1">CA.</font> Note that if you are going to monitor https targets, you'll probably have to either enable this option or specify the <font SIZE="-1">CA</font> path to curl through extraargs below. For more info, see the <i><a HREF="/docs/linux/man/1-curl/">curl</a></i>(1) manual page. 

 Example value: 1
<dt>interface
<dd>The ``--interface'' <i><a HREF="/docs/linux/man/1-curl/">curl</a></i>(1) option. Bind to a specific interface, <font SIZE="-1">IP</font> address or host name. 

 Example value: eth0
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5
<dt>ssl2
<dd>The ``-2'' <i><a HREF="/docs/linux/man/1-curl/">curl</a></i>(1) option. Force <font SIZE="-1">SSL2.</font> 

 Example value: 1
<dt>timeout
<dd>The ``-m'' <i><a HREF="/docs/linux/man/1-curl/">curl</a></i>(1) option. Maximum timeout in seconds. 

 Example value: 20 

 Default value: 10
<dt>urlformat
<dd>The template of the <font SIZE="-1">URL</font> to fetch. Can be any one that curl supports. Any occurrence of the string '%host%' will be replaced with the host to be probed. 

 Example value: <a rel="nofollow" HREF="http://%host%/">http://%host%/</a> 

 This setting is mandatory.</dl><h2>Authors</h2><pre> Gerald Combs &lt;gerald [AT] ethereal.com&gt;
 Niko Tyni &lt;ntyni [at] iki.fi&gt;</pre><h2>Notes</h2>You should consider setting a lower value for the <tt>&quot;pings&quot;</tt> variable than the default 20, as repetitive <font SIZE="-1">URL</font> fetching may be quite heavy on the server. 

 The <font SIZE="-1">URL</font> to be tested used to be specified by the variable 'url' in earlier versions of Smokeping, and the 'host' setting did not influence it in any way. The variable name has now been changed to 'urlformat', and it can (and in most cases should) contain a placeholder for the 'host' variable.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-curl/">curl</a></i>(1), &lt;<a rel="nofollow" HREF="http://curl.haxx.se/">http://curl.haxx.se/</a>&gt;
