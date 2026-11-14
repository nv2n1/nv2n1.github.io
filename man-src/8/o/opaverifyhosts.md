---
title: "opaverifyhosts(8)"
name: "opaverifyhosts"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaverifyhosts/"
description: "opaverifyhosts Verifies basic node configuration and performance by running FF_HOSTVERIFY_DIR/hostverify.sh on all specified hosts. NOTE: Prior to using opaverifyhosts, copy the sample file /usr/li..."
---

<p>opaverifyhosts Verifies basic node configuration and performance by running FF_HOSTVERIFY_DIR/hostverify.sh on all specified hosts. <code>NOTE:</code> Prior to using opaverifyhosts, copy the sample file /usr/lib/opa-ff/samples/hostverify.sh to FF_HOSTVERIFY_DIR and edit it to appropriate configuration and performance expectations and select which tests to run by default. On the first run for a given node, use the -c option so that hostverify.sh gets copied to each node. FF_HOSTVERIFY_DIR defines both the location of hostverify.sh and the destination of the hostverify.res output file. FF_HOSTVERIFY_DIR is configured in the /etc/sysconfig/opa/opafastfabric.conf file. A summary of results is appended to the FF_RESULT_DIR/verifyhosts.res file. A punchlist of failures is also appended to the FF_RESULT_DIR/punchlist.csv file. Only failures are shown on stdout. </p>
<h2>Syntax</h2>
<p>opaverifyhosts [-kc] [-f <i>hostfile</i>] [-u <i>upload_file</i>] [-d <i>upload_dir</i>]<br />
 [-h <i>hosts</i>] [-T <i>timelimit</i>] [ <i>test</i>&#8230;]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-k</p>
<dd>At start and end of verification, kills any existing hostverify or xhpl jobs on the hosts. </p>
<dt>-c</p>
<dd>Copies hostverify.sh to hosts first, useful if you have edited it. </p>
<dt>-f <i>hostfile</i></p>
<dd>File with hosts in cluster. Default is /etc/sysconfig/opa/hosts. </p>
<dt>-h <i>hosts</i></p>
<dd>List of hosts to ping. </p>
<dt>-u <i>upload_file</i></p>
<dd>Filename to upload hostverify.res to after verification to allow backup and review of the detailed results for each node. The default upload destination file is hostverify.res. If -u &#8221; is specified, no upload occurs. </p>
<dt>-d <i>upload_dir</i></p>
<dd>Directory to upload result from each host to. Default is uploads. </p>
<dt>-T <i>timelimit</i></p>
<dd>Time limit in seconds for host to complete tests. Default is 300 seconds (5 minutes). </p>
<dt>
&nbsp;<wbr><i>test</i>&nbsp;<wbr></p>
<dd>One or more specific tests to run. See /usr/lib/opa-ff/samples/hostverify.sh for a list of available tests. </p>
</dl>
<h2>Examples</h2>
<p>opaverifyhosts -c<br />
 opaverifyhosts -h &#8216;arwen elrond&#8217;<br />
 HOSTS=&#8217;arwen elrond&#8217; opaverifyhosts</p>
<h2>Environment Variables</h2>
<dl>
<dt><code>HOSTS</code></p>
<dd>List of hosts, used if -h option not supplied. </p>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing list of hosts, used in absence of -f and -h. </p>
<dt><code>UPLOADS_DIR</code></p>
<dd>Directory to upload to, used in absence of -d. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>Maximum concurrent operations. </p>
</dl>
