---
title: "namespace(5)"
name: "namespace"
section: "5"
letter: "n"
url: "/docs/linux/man/5-namespace/"
description: "namespace.conf – the namespace configuration file"
---

<p>namespace.conf &#8211; the namespace configuration file</p>
<h2>Description</h2>
<p>The <i>pam_namespace.so</i> module allows setup of private namespaces with polyinstantiated directories. Directories can be polyinstantiated based on user name or, in the case of SELinux, user name, sensitivity level or complete security context. If an executable script /etc/security/namespace.init exists, it is used to initialize the namespace every time an instance directory is set up and mounted. The script receives the polyinstantiated directory path and the instance directory path as its arguments. </p>
<p> The /etc/security/namespace.conf file specifies which directories are polyinstantiated, how they are polyinstantiated, how instance directories would be named, and any users for whom polyinstantiation would not be performed. </p>
<p> When someone logs in, the file namespace.conf is scanned. Comments are marked by <i>#</i> characters. Each non comment line represents one polyinstantiated directory. The fields are separated by spaces but can be quoted by <i>&quot;</i> characters also escape sequences <i></i>, <i>
</i>, and <i>	</i> are recognized. The fields are as follows: </p>
<p> <i>polydir</i><i>instance_prefix</i><i>method</i><i>list_of_uids</i> </p>
<p> The first field, <i>polydir</i>, is the absolute pathname of the directory to polyinstantiate. The special string <i>$HOME</i> is replaced with the user&#8217;s home directory, and <i>$USER</i> with the username. This field cannot be blank. </p>
<p> The second field, <i>instance_prefix</i> is the string prefix used to build the pathname for the instantiation of &lt;polydir&gt;. Depending on the polyinstantiation <i>method</i> it is then appended with &quot;instance differentiation string&quot; to generate the final instance directory path. This directory is created if it did not exist already, and is then bind mounted on the &lt;polydir&gt; to provide an instance of &lt;polydir&gt; based on the &lt;method&gt; column. The special string <i>$HOME</i> is replaced with the user&#8217;s home directory, and <i>$USER</i> with the username. This field cannot be blank. </p>
<p> The third field, <i>method</i>, is the method used for polyinstantiation. It can take these values; &quot;user&quot; for polyinstantiation based on user name, &quot;level&quot; for polyinstantiation based on process MLS level and user name, &quot;context&quot; for polyinstantiation based on process security context and user name, &quot;tmpfs&quot; for mounting tmpfs filesystem as an instance dir, and &quot;tmpdir&quot; for creating temporary directory as an instance dir which is removed when the user&#8217;s session is closed. Methods &quot;context&quot; and &quot;level&quot; are only available with SELinux. This field cannot be blank. </p>
<p> The fourth field, <i>list_of_uids</i>, is a comma separated list of user names for whom the polyinstantiation is not performed. If left blank, polyinstantiation will be performed for all users. If the list is preceded with a single &quot;~&quot; character, polyinstantiation is performed only for users in the list. </p>
<p> The <i>method</i> field can contain also following optional flags separated by <i>:</i> characters. </p>
<p> <i>create</i>=<i>mode</i>,<i>owner</i>,<i>group</i> &#8211; create the polyinstantiated directory. The mode, owner and group parameters are optional. The default for mode is determined by umask, the default owner is the user whose session is opened, the default group is the primary group of the user. </p>
<p> <i>iscript</i>=<i>path</i> &#8211; path to the instance directory init script. The base directory for relative paths is /etc/security/namespace.d. </p>
<p> <i>noinit</i> &#8211; instance directory init script will not be executed. </p>
<p> <i>shared</i> &#8211; the instance directories for &quot;context&quot; and &quot;level&quot; methods will not contain the user name and will be shared among all users. </p>
<p> <i>mntopts</i>=<i>value</i> &#8211; value of this flag is passed to the mount call when the tmpfs mount is done. It allows for example the specification of the maximum size of the tmpfs instance that is created by the mount call. See <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) for details. </p>
<p> The directory where polyinstantiated instances are to be created, must exist and must have, by default, the mode of 0000. The requirement that the instance parent be of mode 0000 can be overridden with the command line option <i>ignore_instance_parent_mode</i> </p>
<p> In case of context or level polyinstantiation the SELinux context which is used for polyinstantiation is the context used for executing a new process as obtained by getexeccon. This context must be set by the calling application or pam_selinux.so module. If this context is not set the polyinstatiation will be based just on user name. </p>
<p> The &quot;instance differentiation string&quot; is &lt;user name&gt; for &quot;user&quot; method and &lt;user name&gt;_&lt;raw directory context&gt; for &quot;context&quot; and &quot;level&quot; methods. If the whole string is too long the end of it is replaced with md5sum of itself. Also when command line option <i>gen_hash</i> is used the whole string is replaced with md5sum of itself.</p>
<h2>Examples</h2>
<p>These are some example lines which might be specified in /etc/security/namespace.conf. </p>
<dl>
<dd>
<pre> # The following three lines will polyinstantiate /tmp,
 # /var/tmp and user's home directories. /tmp and /var/tmp
 # will be polyinstantiated based on the security level
 # as well as user name, whereas home directory will be
 # polyinstantiated based on the full security context and user name.
 # Polyinstantiation will not be performed for user root
 # and adm for directories /tmp and /var/tmp, whereas home
 # directories will be polyinstantiated for all users.
 #
 # Note that instance directories do not have to reside inside
 # the polyinstantiated directory. In the examples below,
 # instances of /tmp will be created in /tmp-inst directory,
 # where as instances of /var/tmp and users home directories
 # will reside within the directories that are being
 # polyinstantiated.
 #
 /tmp /tmp-inst/ level root,adm
 /var/tmp /var/tmp/tmp-inst/ level root,adm
 $HOME $HOME/$USER.inst/inst- context</pre>
</dl>
<p> For the &lt;service&gt;s you need polyinstantiation (login for example) put the following line in /etc/pam.d/&lt;service&gt; as the last line for session group: </p>
<p> session required pam_namespace.so [arguments] </p>
<p> This module also depends on pam_selinux.so setting the context.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_namespace/">pam_namespace</a></code>(8), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Authors</h2>
<p>The namespace.conf manual page was written by Janak Desai &lt;janak [at] us.ibm.com&gt;. More features added by Tomas Mraz &lt;tmraz [at] redhat.com&gt;.</p>
