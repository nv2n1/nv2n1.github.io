---
title: "nss_wrapper(1)"
name: "nss_wrapper"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nss_wrapper/"
description: "nss_wrapper – A wrapper for the user, group and hosts NSS API"
---

<h2 class="name">NAME</h2>
<p> nss_wrapper &#8211; A wrapper for the user, group and hosts NSS API </p>
<h2>SYNOPSIS</h2>
<p> LD_PRELOAD=libnss_wrapper.so NSS_WRAPPER_PASSWD=/path/to/passwd NSS_WRAPPER_GROUP=/path/to/group NSS_WRAPPER_HOSTS=/path/to/host <code>./myapplication</code></p>
<h2>DESCRIPTION</h2>
<p> There are projects which provide daemons needing to be able to create, modify and delete Unix users. Or just switch user ids to interact with the system e.g. a user space file server. To be able to test that you need the privilege to modify the passwd and groups file. With nss_wrapper it is possible to define your own passwd and groups file which will be used by software to act correctly while under test. </p>
<p> If you have a client and server under test they normally use functions to resolve network names to addresses (dns) or vice versa. The nss_wrappers allow you to create a hosts file to setup name resolution for the addresses you use with socket_wrapper. </p>
<dl>
<dt>
<dd> &bull; Provides information for user and group accounts.</dl>
<dl>
<dt>
<dd> &bull; Network name resolution using a hosts file.</dl>
<dl>
<dt>
<dd> &bull; Loading and testing of NSS modules.</dl>
<h2>LIMITATIONS</h2>
<p> Some calls in nss_wrapper will only work if uid_wrapper is loaded and active. One of this functions is initgroups() which needs to run setgroups() to set the groups for the user. setgroups() is wrapped by uid_wrapper.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>NSS_WRAPPER_PASSWD</code>, <code>NSS_WRAPPER_GROUP</code></p>
<dl>
<dt>
<dd> For user and group accounts you need to create two files: <i>passwd</i> and <i>group</i>. The format of the passwd file is described in <i>man 5 passwd</i> and the group file in <i>man 5 group</i>. So you can fill these files with made up accounts. You point nss_wrapper to them using the two variables NSS_WRAPPER_PASSWD=/path/to/your/passwd and NSS_WRAPPER_GROUP=/path/to/your/group.</dl>
<p> <code>NSS_WRAPPER_HOSTS</code></p>
<dl>
<dt>
<dd> If you also need to emulate network name resolution in your enviornment, especially with socket_wrapper, you can write a hosts file. The format is described in <i>man 5 hosts</i>. Then you can point nss_wrapper to your hosts file using: NSS_WRAPPER_HOSTS=/path/to/your/hosts</dl>
<p> <code>NSS_WRAPPER_HOSTNAME</code></p>
<dl>
<dt>
<dd> If you need to return a hostname which is different from the one of your machine is using you can use: NSS_WRAPPER_HOSTNAME=test.example.org</dl>
<p> <code>NSS_WRAPPER_MODULE_SO_PATH</code>, <code>NSS_WRAPPER_MODULE_FN_PREFIX</code></p>
<dl>
<dt>
<dd> If you have a project which also provides user and group information out of a database, you normally write your own nss modules. nss_wrapper is able to load nss modules and ask them first before looking into the faked passwd and group file. To point nss_wrapper to the module you can do that using NSS_WRAPPER_MODULE_SO_PATH=/path/to/libnss_yourmodule.so. As each nss module has a special prefix like _nss_winbind_getpwnam() you need to set the prefix too so nss_wrapper can load the functions with NSS_WRAPPER_MODULE_FN_PREFIX=&lt;prefix&gt;.</dl>
<p> For _nss_winbind_getpwnam() this would be: </p>
<dl>
<dt>
<dd>
<pre>
NSS_WRAPPER_MODULE_FN_PREFIX=winbind
</pre>
</dl>
<p> <code>NSS_WRAPPER_DEBUGLEVEL</code></p>
<dl>
<dt>
<dd> If you need to see what is going on in nss_wrapper itself or try to find a bug, you can enable logging support in nss_wrapper if you built it with debug symbols. </p>
<dl>
<dt>
<dd> &bull; 0 = ERROR</dl>
<dl>
<dt>
<dd> &bull; 1 = WARNING</dl>
<dl>
<dt>
<dd> &bull; 2 = DEBUG</dl>
<dl>
<dt>
<dd> &bull; 3 = TRACE</dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
$ echo &quot;bob:x:1000:1000:bob gecos:/home/test/bob:/bin/false&quot; &gt; passwd
$ echo &quot;root:x:65534:65532:root gecos:/home/test/root:/bin/false&quot; &gt;&gt; passwd
$ echo &quot;users:x:1000:&quot; &gt; group
$ echo &quot;root:x:65532:&quot; &gt;&gt; group
$ LD_PRELOAD=libnss_wrapper.so NSS_WRAPPER_PASSWD=passwd \
  NSS_WRAPPER_GROUP=group getent passwd bob
bob:x:1000:1000:bob gecos:/home/test/bob:/bin/false
$ LD_PRELOAD=libnss_wrapper.so NSS_WRAPPER_HOSTNAME=test.example.org hostname
test.example.org
</pre>
</dl>
<h2>Index</h2>
