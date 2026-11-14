---
title: "simplevisor-control(1)"
name: "simplevisor-control"
section: "1"
letter: "s"
url: "/docs/linux/man/1-simplevisor-control/"
description: "simplevisor-control – run simplevisor as a service"
---

<h2 class="name">NAME</h2>
<p> simplevisor-control &#8211; run simplevisor as a service </p>
<h2>SYNOPSIS</h2>
<p> <code>simplevisor-control</code> command [path]</p>
<h2>DESCRIPTION</h2>
<p> The <code>simplevisor-control</code> script can be used to run simplevisor as a service. </p>
<p> If this script is used the pidfile value specified in the simplevisor configuration file will be ignored.</p>
<h2>OPTIONS</h2>
<p> <code>command</code> run &#8220;simplevisor-control help&#8221; to list the available commands </p>
<p> <code>path</code> look at simplevisor man page for path behavior.</p>
<h2>EXAMPLES</h2>
<p> On Linux you can look at the script shipped in the examples folder which is called simplevisor-new-instance, it creates folders and the configuration to run a simplevisor instance. </p>
<pre>
    mkdir -p /var/lib/myinstance/bin
    mkdir -p /var/lib/myinstance/data
    mkdir -p /var/lib/myinstance/etc
</pre>
<p> Create a file /var/lib/myinstance/bin/service with content and make it executable: </p>
<pre>
    #!/bin/sh
    #
    # init script that can be symlinked from /etc/init.d
    #
    
    # chkconfig: - 90 15
    # description: my simplevisor instance
    
    . &quot;/var/lib/myinstance/etc/simplevisor.profile&quot;
    exec &quot;/usr/bin/simplevisor-control&quot; ${1+&quot;$@&quot;}
</pre>
<p> /var/lib/myinstance/etc/simplevisor.profile could look like: </p>
<pre><code>
#main
export SIMPLEVISOR_NAME = myinstance
#if you want to run it as another user:
#export SIMPLEVISOR_USER = games
    export SIMPLEVISOR_CONF = / var / lib / myinstance / etc / simplevisor.conf export SIMPLEVISOR_PIDFILE = / var / lib / myinstance / data / simplevisor.pid export SIMPLEVISOR_LOCKFILE = / var / lib / myinstance / data / simplevisor.lock
</code></pre>
<p> Create /var/lib/myinstance/etc/simplevisor.conf according to simplevisor documentation. </p>
<p> For Red Hat or Fedora you can symlink service script: </p>
<pre>
    ln -s /var/lib/myinstance/bin/service /etc/init.d/myinstance
</pre>
<p> And use it as a normal service: </p>
<pre>
    /sbin/service myinstance start|stop|status|restart|check
</pre>
<h2>AUTHOR</h2>
<p> Massimo Paladin &lt;massimo.paladin [at] gmail.com&gt; </p>
<p> Copyright (C) <font SIZE="-1">CERN 2013-2016</font> </p>
<h2>Index</h2>
