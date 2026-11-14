---
title: "tarantoolctl(1)"
name: "tarantoolctl"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tarantoolctl/"
---

<h2 class="name">NAME</h2>
 

 tarantoolctl - an utility to control tarantool instances 

<h2>SYNOPSIS</h2>

 <pre>
    vim /etc/tarantool/instances.enabled/my_instance.lua
    tarantoolctl start my_instance
    tarantoolctl stop  my_instance
    tarantoolctl logrotate my_instance
</pre>

<h2>DESCRIPTION</h2>

 The script is read <tt>&quot;/etc/sysconfig/tarantool&quot;</tt> or <tt>&quot;/etc/default/tarantool&quot;</tt>. The file contains common default instances options: 

 <pre><code>
    $ cat /etc/default/tarantool
    -- Options for Tarantool
    default_cfg = {
        -- will become pid_file .. instance .. '.pid'
        pid_file    =   "/var/run/tarantool",
        -- will become wal_dir/instance/
        wal_dir     =   "/var/lib/tarantool",
        -- snap_dir/instance/
        snap_dir    =   "/var/lib/tarantool",
        -- sophia_dir/instance/
        sophia_dir  =   "/var/lib/tarantool/sophia",
        -- logger/instance .. '.log'
        logger      =   "/var/log/tarantool",
        username    =   "tarantool",
    }
    instance_dir = "/etc/tarantool/instances.enabled"
</code></pre> 

 The file defines <tt>&quot;instance_dir&quot;</tt> where user can place his applications (instances). 

 Each instance can be controlled by <tt>&quot;tarantoolctl&quot;</tt>:

<h3>Starting instance</h3>

 <pre>
    tarantoolctl start instance_name
</pre>

<h3>Stopping instance</h3>

 <pre>
    tarantoolctl stop instance_name
</pre>

<h3>Logrotate instance's log</h3>

 <pre>
    tarantoolctl logrotate instance_name
</pre>

<h3>Enter instance admin console</h3>

 <pre>
    tarantoolctl enter instance_name
</pre>

<h3>status</h3>

 <pre>
    tarantoolctl status instance_name
</pre> 

 Check if instance is up. 

 If pid file exists and control socket exists and control socket is alive returns code <tt>0</tt>. 

 Return code != 0 in other cases. Can complain in log (stderr) if pid file exists and socket doesn't, etc.

<h3>separate instances control</h3>

 If You use SysV init, You can use symlink from <tt>&quot;tarantoolctl&quot;</tt> to <tt>&quot;/etc/init.d/instance_name[.lua]&quot;</tt>. <tt>&quot;tarantoolctl&quot;</tt> detects if it is started by symlink and uses instance_name as <tt>&quot;`basename $0 .lua`&quot;</tt>.

<h2>COPYRIGHT</h2>

 Copyright (C) 2010-2013 Tarantool <font SIZE="-1">AUTHORS:</font> please see <font SIZE="-1">AUTHORS</font> file. 

<h2>Index</h2>


