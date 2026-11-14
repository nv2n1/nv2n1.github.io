---
title: "cgconfig-conf(5)"
name: "cgconfig-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cgconfig-conf/"
description: "cgconfig.conf – libcgroup configuration file"
---

<p>cgconfig.conf &#8211; libcgroup configuration file</p>
<h2>Description</h2>
<p><code>cgconfig.conf</code> is a configuration file used by <code>libcgroup</code> to define control groups, their parameters and their mount points. The file consists of <i>mount</i> , <i>group</i> and <i>default</i> sections. These sections can be in arbitrary order and all of them are optional. Any line starting with &#8216;#&#8217; is considered a comment line and is ignored. </p>
<pre><code>mount

section has this form:


mount {
    &lt;controller&gt; = &lt;path&gt;;
    ...

}</code></pre>
<dl>
<dt><code>controller</code></p>
<dd>Name of the kernel subsystem. The list of subsystems supported by the kernel can be found in <i>/proc/cgroups</i> file. Named hierarchy can be specified as controller <code>&quot;name=&lt;somename&gt;&quot;</code>. Do not forget to use double quotes around this controller name (see examples below). <code>Libcgroup</code> merges all subsystems mounted to the same directory (see Example 1) and the directory is mounted only once.</p>
<dt><code>path</code></p>
<dd>The directory path where the group hierarchy associated to a given controller shall be mounted. The directory is created automatically on cgconfig service startup if it does not exist and is deleted on service shutdown.</dl>
<p> If no <i>mount</i> section is specified, no controllers are mounted. group</p>
<p>section has this form:</p>
<p>group &lt;name&gt; {<br />
    [permissions]<br />
    &lt;controller&gt; {<br />
        &lt;param name&gt; = &lt;param value&gt;;<br />
        &#8230;</p>
<p>    }<br />
    &#8230;</p>
<p>}</p>
<dl>
<dt><code>name</code></p>
<dd>Name of the control group. It can contain only characters, which are allowed for directory names. The groups form a tree, i.e. a control group can contain zero or more subgroups. Subgroups can be specified using &#8216;/&#8217; delimiter. The root control group is always created automatically in all hierarchies and it is the base of the group hierarchy. It can be explicitly specified in <code>cgconfig.conf</code> by using &#8216;.&#8217; as group name. This can be used e.g. to set its permissions, as shown in Example 6. When the parent control group of a subgroup is not specified it is created automatically. permissions</p>
<p>Permissions of the given control group on mounted filesystem.<br />
root</p>
<p>has always permission to do anything with the control group.<br />
Permissions have the following syntax:</p>
<p>perm {<br />
    task {<br />
        uid = &lt;task user&gt;;<br />
        gid = &lt;task group&gt;;<br />
        fperm = &lt;file permissions&gt;</p>
<p>    }<br />
    admin {<br />
        uid = &lt;admin name&gt;;<br />
        gid = &lt;admin group&gt;;<br />
        dperm = &lt;directory permissions&gt;<br />
        fperm = &lt;file permissions&gt;</p>
<p>    }</p>
<p>}</p>
<dl>
<dd>
<dl>
<dt><code>task user/group</code></p>
<dd>Name of the user and the group, which own the <i>tasks</i> file of the control group. Given fperm then specify the file permissions. Please note that the given value is not used as was specified. Instead, current file owner permissions are used as a &quot;umask&quot; for group and others permissions. For example if fperm = 777 then both group and others will get the same permissions as the file owner.</p>
<dt><code>admin user/group</code></p>
<dd>Name of the user and the group which own the rest of control group&#8217;s files. Given fperm and dperm control file and directory permissions. Again, the given value is masked by the file/directory owner permissions.</dl>
<p> Permissions are only apply to the enclosing control group and are not inherited by subgroups. If there is no <code>perm</code> section in the control group definition, <i>root:root</i> is the owner of all files and default file permissions are preserved if fperm resp. dperm are not specified.</dl>
<dt><code>controller</code></p>
<dd>Name of the kernel subsystem. The section can be empty, default kernel parameters will be used in this case. By specifying <code>controller</code> the control group and all its parents are controlled by the specific subsystem. One control group can be controlled by multiple subsystems, even if the subsystems are mounted on different directories. Each control group must be controlled by at least one subsystem, so that <code>libcgroup</code> knows in which hierarchies the control group should be created. The parameters of the given controller can be modified in the following section enclosed in brackets.</p>
<dl>
<dd>
<dl>
<dt><code>param name</code></p>
<dd>Name of the file to set. Each controller can have zero or more parameters.</p>
<dt><code>param value</code></p>
<dd>Value which should be written to the file when the control group is created. If it is enclosed in double quotes `&quot;&#8217;, it can contain spaces and other special characters.</dl>
</dl>
<p> If no <i>group</i> section is specified, no groups are created. default</p>
<p>section has this form:</p>
<p>default {<br />
    perm {<br />
        task {<br />
            uid = &lt;task user&gt;;<br />
            gid = &lt;task group&gt;;<br />
            fperm = &lt;file permissions&gt;</p>
<p>        }<br />
        admin {<br />
            uid = &lt;admin name&gt;;<br />
            gid = &lt;admin group&gt;;<br />
            dperm = &lt;directory permissions&gt;<br />
            fperm = &lt;file permissions&gt;</p>
<p>        }</p>
<p>    }</p>
<p>} Content of the <code>perm</code> section has the same form as in <i>group</i> section. The permissions defined here specify owner and permissions of groups and files of all groups, which do not have explicitly specified their permissions in their <i>group</i> section. <i>template</i> section has the same structure as <code>group</code> section. Template name uses the same templates string as <code>cgrules.conf</code> destination tag (see (<code>cgrules.conf</code> (5)). Template definition is used as a control group definition for rules in <code>cgrules.conf</code> (5) with the same destination name. Templates does not use <code>default</code> section settings. <i>/etc/cgconfig.d/</i> directory can be used for additional configuration files. cgrulesengd searches this directory for additional templates. </p>
<h2>Examples</h2>
<h3>Example 1</h3>
<p>The configuration file: </p>
<pre><code>mount {
    cpu = /mnt/cgroups/cpu;
    cpuacct = /mnt/cgroups/cpu;

}</code></pre>
<p> creates the hierarchy controlled by two subsystems with no groups inside. It corresponds to the following operations:</p>
<dl>
<dd>
<pre>mkdir /mnt/cgroups/cpu
mount -t cgroup -o cpu,cpuacct cpu /mnt/cgroups/cpu</pre>
</dl>
<h3>Example 2</h3>
<p>The configuration file:</p>
<dl>
<dd>
<pre>mount {
<dl><dt><dd>cpu = /mnt/cgroups/cpu;
&quot;name=scheduler&quot; = /mnt/cgroups/cpu;
&quot;name=noctrl&quot; = /mnt/cgroups/noctrl;
</dl>
}
group daemons {
<dl><dt><dd>cpu {
<dl><dt><dd>cpu.shares = &quot;1000&quot;;
</dl>
}
</dl>
}
group test {
<dl><dt><dd>&quot;name=noctrl&quot; {
}
</dl>
}
</dl></pre>
<p>creates two hierarchies. One hierarchy named <code>scheduler</code> controlled by cpu subsystem, with group <code>daemons</code> inside. Second hierarchy is named <code>noctrl</code> without any controller, with group <code>test</code>. It corresponds to following operations:</p>
<dl>
<dd>
<pre>mkdir /mnt/cgroups/cpu
mount -t cgroup -o cpu,name=scheduler cpu /mnt/cgroups/cpu
mount -t cgroup -o none,name=noctrl none /mnt/cgroups/noctrl
mkdir /mnt/cgroups/cpu/daemons
echo 1000 &gt; /mnt/cgroups/cpu/daemons/www/cpu.shares
mkdir /mnt/cgroups/noctrl/tests</pre>
</dl>
<p> The <i>daemons</i> group is created automatically when its first subgroup is created. All its parameters have the default value and only root can access group&#8217;s files. Since both <i>cpuacct</i> and <i>cpu</i> subsystems are mounted to the same directory, all groups are implicitly controlled also by <i>cpuacct</i> subsystem, even if there is no <i>cpuacct</i> section in any of the groups.</p>
<h3>Example 3</h3>
<p>The configuration file:</p>
<dl>
<dd>
<pre>mount {
<dl><dt><dd>cpu = /mnt/cgroups/cpu;
cpuacct = /mnt/cgroups/cpu;
</dl>
}
group daemons/www {
<dl><dt><dd>perm {
<dl><dt><dd>task {
<dl><dt><dd>uid = root;
gid = webmaster;
fperm = 770;
</dl>
}
admin {
<dl><dt><dd>uid = root;
gid = root;
dperm = 775;
fperm = 744;
</dl>
}
</dl>
}
cpu {
<dl><dt><dd>cpu.shares = &quot;1000&quot;;
</dl>
}
</dl>
}
group daemons/ftp {
<dl><dt><dd>perm {
<dl><dt><dd>task {
<dl><dt><dd>uid = root;
gid = ftpmaster;
fperm = 774;
</dl>
}
admin {
<dl><dt><dd>uid = root;
gid = root;
dperm = 755;
fperm = 700;
</dl>
}
</dl>
}
cpu {
<dl><dt><dd>cpu.shares = &quot;500&quot;;
</dl>
}
</dl>
}
</dl></pre>
<p>creates the hierarchy controlled by two subsystems with one group and two subgroups inside, setting one parameter. It corresponds to the following operations (except for file permissions which are little bit trickier to emulate via chmod):</p>
<dl>
<dd>
<pre>mkdir /mnt/cgroups/cpu
mount -t cgroup -o cpu,cpuacct cpu /mnt/cgroups/cpu
mkdir /mnt/cgroups/cpu/daemons
mkdir /mnt/cgroups/cpu/daemons/www
chown root:root /mnt/cgroups/cpu/daemons/www/*
chown root:webmaster /mnt/cgroups/cpu/daemons/www/tasks
echo 1000 &gt; /mnt/cgroups/cpu/daemons/www/cpu.shares
 # + chmod the files so the result looks like:
 # ls -la /mnt/cgroups/cpu/daemons/www/
 # admin.dperm = 755:
 # drwxr-xr-x. 2 root webmaster 0 Jun 16 11:51 .
 #
 # admin.fperm = 744:
 # --w-------. 1 root webmaster 0 Jun 16 11:51 cgroup.event_control
 # -r--r--r--. 1 root webmaster 0 Jun 16 11:51 cgroup.procs
 # -r--r--r--. 1 root webmaster 0 Jun 16 11:51 cpuacct.stat
 # -rw-r--r--. 1 root webmaster 0 Jun 16 11:51 cpuacct.usage
 # -r--r--r--. 1 root webmaster 0 Jun 16 11:51 cpuacct.usage_percpu
 # -rw-r--r--. 1 root webmaster 0 Jun 16 11:51 cpu.rt_period_us
 # -rw-r--r--. 1 root webmaster 0 Jun 16 11:51 cpu.rt_runtime_us
 # -rw-r--r--. 1 root webmaster 0 Jun 16 11:51 cpu.shares
 # -rw-r--r--. 1 root webmaster 0 Jun 16 11:51 notify_on_release
 #
 # tasks.fperm = 770
 # -rw-rw----. 1 root webmaster 0 Jun 16 11:51 tasks
mkdir /mnt/cgroups/cpu/daemons/ftp
chown root:root /mnt/cgroups/cpu/daemons/ftp/*
chown root:ftpmaster /mnt/cgroups/cpu/daemons/ftp/tasks
echo 500 &gt; /mnt/cgroups/cpu/daemons/ftp/cpu.shares
 # + chmod the files so the result looks like:
 # ls -la /mnt/cgroups/cpu/daemons/ftp/
 # admin.dperm = 755:
 # drwxr-xr-x. 2 root ftpmaster 0 Jun 16 11:51 .
 #
 # admin.fperm = 700:
 # --w-------. 1 root ftpmaster 0 Jun 16 11:51 cgroup.event_control
 # -r--------. 1 root ftpmaster 0 Jun 16 11:51 cgroup.procs
 # -r--------. 1 root ftpmaster 0 Jun 16 11:51 cpuacct.stat
 # -rw-------. 1 root ftpmaster 0 Jun 16 11:51 cpuacct.usage
 # -r--------. 1 root ftpmaster 0 Jun 16 11:51 cpuacct.usage_percpu
 # -rw-------. 1 root ftpmaster 0 Jun 16 11:51 cpu.rt_period_us
 # -rw-------. 1 root ftpmaster 0 Jun 16 11:51 cpu.rt_runtime_us
 # -rw-------. 1 root ftpmaster 0 Jun 16 11:51 cpu.shares
 # -rw-------. 1 root ftpmaster 0 Jun 16 11:51 notify_on_release
 #
 # tasks.fperm = 774:
 # -rw-rw-r--. 1 root ftpmaster 0 Jun 16 11:51 tasks</pre>
</dl>
<p> The <i>daemons</i> group is created automatically when its first subgroup is created. All its parameters have the default value and only root can access the group&#8217;s files. Since both <i>cpuacct</i> and <i>cpu</i> subsystems are mounted to the same directory, all groups are implicitly also controlled by the <i>cpuacct</i> subsystem, even if there is no <i>cpuacct</i> section in any of the groups.</p>
<h3>Example 4</h3>
<p>The configuration file:</p>
<dl>
<dd>
<pre>mount {
<dl><dt><dd>cpu = /mnt/cgroups/cpu;
cpuacct = /mnt/cgroups/cpuacct;
</dl>
}
group daemons {
<dl><dt><dd>cpuacct{
}
cpu {
}
</dl>
}</pre>
</dl>
<p> creates two hierarchies and one common group in both of them. It corresponds to the following operations:</p>
<dl>
<dd>
<pre>mkdir /mnt/cgroups/cpu
mkdir /mnt/cgroups/cpuacct
mount -t cgroup -o cpu cpu /mnt/cgroups/cpu
mount -t cgroup -o cpuacct cpuacct /mnt/cgroups/cpuacct
mkdir /mnt/cgroups/cpu/daemons
mkdir /mnt/cgroups/cpuacct/daemons</pre>
</dl>
<p> In fact there are two groups created. One in the <i>cpuacct</i> hierarchy, the second in the <i>cpu</i> hierarchy. These two groups have nothing in common and can contain different subgroups and different tasks.</p>
<h3>Example 5</h3>
<p>The configuration file:</p>
<dl>
<dd>
<pre>mount {
<dl><dt><dd>cpu = /mnt/cgroups/cpu;
cpuacct = /mnt/cgroups/cpuacct;
</dl>
}
group daemons {
<dl><dt><dd>cpuacct{
}
</dl>
}
group daemons/www {
<dl><dt><dd>cpu {
<dl><dt><dd>cpu.shares = &quot;1000&quot;;
</dl>
}
</dl>
}
group daemons/ftp {
<dl><dt><dd>cpu {
<dl><dt><dd>cpu.shares = &quot;500&quot;;
</dl>
}
</dl>
}</pre>
</dl>
<p> creates two hierarchies with few groups inside. One of the groups is created in both hierarchies. It corresponds to the following operations:</p>
<dl>
<dd>
<pre>mkdir /mnt/cgroups/cpu
mkdir /mnt/cgroups/cpuacct
mount -t cgroup -o cpu cpu /mnt/cgroups/cpu
mount -t cgroup -o cpuacct cpuacct /mnt/cgroups/cpuacct
mkdir /mnt/cgroups/cpuacct/daemons
mkdir /mnt/cgroups/cpu/daemons
mkdir /mnt/cgroups/cpu/daemons/www
echo 1000 &gt; /mnt/cgroups/cpu/daemons/www/cpu.shares
mkdir /mnt/cgroups/cpu/daemons/ftp
echo 500 &gt; /mnt/cgroups/cpu/daemons/ftp/cpu.shares</pre>
</dl>
<p> Group <i>daemons</i> is created in both hierarchies. In the <i>cpuacct</i> hierarchy the group is explicitly mentioned in the configuration file. In the <i>cpu</i> hierarchy the group is created implicitly when <i>www</i> is created there. These two groups have nothing in common, for example they do not share processes and subgroups. Groups <i>www</i> and <i>ftp</i> are created only in the <i>cpu</i> hierarchy and are not controlled by the <i>cpuacct</i> subsystem.</p>
<h3>Example 6</h3>
<p>The configuration file:</p>
<dl>
<dd>
<pre>mount {
<dl><dt><dd>cpu = /mnt/cgroups/cpu;
cpuacct = /mnt/cgroups/cpu;
</dl>
}
group . {
<dl><dt><dd>perm {
<dl><dt><dd>task {
<dl><dt><dd>uid = root;
gid = operator;
</dl>
}
admin {
<dl><dt><dd>uid = root;
gid = operator;
</dl>
}
</dl>
}
cpu {
}
</dl>
}
group daemons {
<dl><dt><dd>perm {
<dl><dt><dd>task {
<dl><dt><dd>uid = root;
gid = daemonmaster;
</dl>
}
admin {
<dl><dt><dd>uid = root;
gid = operator;
</dl>
}
</dl>
}
cpu {
}
</dl>
}
</dl></pre>
<p>creates the hierarchy controlled by two subsystems with one group having some special permissions. It corresponds to the following operations:</p>
<dl>
<dd>
<pre>mkdir /mnt/cgroups/cpu
mount -t cgroup -o cpu,cpuacct cpu /mnt/cgroups/cpu
chown root:operator /mnt/cgroups/cpu/*
chown root:operator /mnt/cgroups/cpu/tasks
mkdir /mnt/cgroups/cpu/daemons
chown root:operator /mnt/cgroups/cpu/daemons/*
chown root:daemonmaster /mnt/cgroups/cpu/daemons/tasks</pre>
</dl>
<p> Users which are members of the <i>operator</i> group are allowed to administer the control groups, i.e. create new control groups and move processes between these groups without having root privileges. Members of the <i>daemonmaster</i> group can move processes to the <i>daemons</i> control group, but they can not move the process out of the group. Only the <i>operator</i> or root can do that.</p>
<h3>Example 7</h3>
<p>The configuration file:</p>
<dl>
<dd>
<pre>mount {
<dl><dt><dd>cpu = /mnt/cgroups/cpu;
cpuacct = /mnt/cgroups/cpuacct;
</dl>
}
group students {
<dl><dt><dd>cpuacct{
}
cpu {
}
</dl>
}
template students/%u {
<dl><dt><dd>cpuacct{
}
cpu {
}
</dl>
}
mkdir /mnt/cgroups/cpu/daemons
mkdir /mnt/cgroups/cpuacct/daemons</pre>
</dl>
<p> The situation is the similar as in Example 4. The only difference is template, which is used if some rule uses &quot;/students/%u&quot; as a destination. </p>
<h2>Recommendations</h2>
<h3>Keep hierarchies separated</h3>
<p>Having multiple hierarchies is perfectly valid and can be useful in various scenarios. To keeps things clean, do not create one group in multiple hierarchies. Examples 4 and 5 show how unreadable and confusing it can be, especially when reading somebody elses configuration file.</p>
<h3>Explicit is better than implicit</h3>
<p><code>libcgroup</code> can implicitly create groups which are needed for the creation of configured subgroups. This may be useful and save some typing in simple scenarios. When it comes to multiple hierarchies, it&#8217;s better to explicitly specify all groups and all controllers related to them.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/cgconfig.conf</code></p>
<dd>default libcgroup configuration file</p>
<dt><code>/etc/cgconfig.d/</code></p>
<dd>default libcgroup configuration files directory </p>
</dl>
<h2>See Also</h2>
<p>cgconfigparser (8) </p>
<h2>Bugs</h2>
<p>Parameter values must be single strings without spaces. Parsing of quoted strings is not implemented. </p>
