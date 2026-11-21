---

title: "nx_server_selinux(8)"
name: "nx_server_selinux"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nx_server_selinux/"
---

 </p>
<h2>NAME</h2>
<p> nx_server_r &#8211; <code>nx_server user role</code> &#8211; Security Enhanced Linux Policy </p>
<p> SELinux supports Roles Based Access Control (RBAC), some Linux roles are login roles, while other roles need to be transition into. </p>
<p> <i>Note:</i> Examples in this man page will use the <code>staff_u</code> SELinux user. </p>
<p> Non login roles are usually used for administrative tasks. For example, tasks that require root privileges. Roles control which types a user can run processes with. Roles often have default types assigned to them. </p>
<p> The default type for the nx_server_r role is nx_server_t. </p>
<p> The <code>newrole</code> program to transition directly to this role. </p>
<p> <code>newrole -r nx_server_r -t nx_server_t</code> </p>
<p> <code>sudo</code> is the preferred method to do transition from one role to another. You setup sudo to transition to nx_server_r by adding a similar line to the /etc/sudoers file. </p>
<p> USERNAME ALL=(ALL) ROLE=nx_server_r TYPE=nx_server_t COMMAND </p>
<p> <br />
 sudo will run COMMAND as staff_u:nx_server_r:nx_server_t:LEVEL </p>
<p> When using a a non login role, you need to setup SELinux so that your SELinux user can reach nx_server_r role. </p>
<p> Execute the following to see all of the assigned SELinux roles: </p>
<p> <code>semanage user -l</code> </p>
<p> You need to add nx_server_r to the staff_u user. You could setup the staff_u user to be able to use the nx_server_r role with a command like: </p>
<p> <code>$ semanage user -m -R &#8216;staff_r system_r nx_server_r&#8217; staff_u</code> </p>
<h2>BOOLEANS</h2>
<p> SELinux policy is customizable based on least access required. nx_server policy is extremely flexible and has several booleans that allow you to manipulate the policy and run nx_server with the tightest access possible. </p>
<p> If you want to deny any process from ptracing or debugging any other processes, you must turn on the deny_ptrace boolean. Enabled by default. </p>
<p> <code>setsebool -P deny_ptrace 1</code> </p>
<p> If you want to allow all domains to use other domains file descriptors, you must turn on the domain_fd_use boolean. Enabled by default. </p>
<p> <code>setsebool -P domain_fd_use 1</code> </p>
<p> If you want to allow all domains to have the kernel load modules, you must turn on the domain_kernel_load_modules boolean. Disabled by default. </p>
<p> <code>setsebool -P domain_kernel_load_modules 1</code> </p>
<p> If you want to allow all domains to execute in fips_mode, you must turn on the fips_mode boolean. Enabled by default. </p>
<p> <code>setsebool -P fips_mode 1</code> </p>
<p> If you want to enable reading of urandom for all domains, you must turn on the global_ssp boolean. Disabled by default. </p>
<p> <code>setsebool -P global_ssp 1</code> </p>
<h2>MANAGED FILES</h2>
<p> The SELinux process type nx_server_t can manage files labeled with the following file types. The paths listed are the default paths for these file types. Note the processes UID still need to have DAC permissions. </p>
<p> <br />
 <code>nx_server_home_ssh_t</code> </p>
<p> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/opt/NX/home/nx/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/usr/NX/home/nx/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/nxserver/home/.ssh(/.*)?<br />
 <br />
 </p>
<p> <br />
 <code>nx_server_tmp_t</code> </p>
<p> <br />
 <code>nx_server_var_lib_t</code> </p>
<p> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/opt/NX/home(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/usr/NX/home(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/nxserver(/.*)?<br />
 <br />
 </p>
<p> <br />
 <code>nx_server_var_run_t</code> </p>
<p> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/opt/NX/var(/.*)?<br />
 <br />
 </p>
<p> <br />
 <code>ssh_home_t</code> </p>
<p> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/[^/]+/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/root/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/one/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/pgsql/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/openshift/[^/]+/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/amanda/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/stickshift/[^/]+/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/gitolite/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/nocpulse/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/gitolite3/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/var/lib/openshift/gear/[^/]+/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/root/.shosts<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/home/[^/]+/.ssh(/.*)?<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/home/[^/]+/.ansible/cp/.*<br />
 <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>/home/[^/]+/.shosts<br />
 <br />
 </p>
<h2>COMMANDS</h2>
<p> <code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>semanage boolean</code> can also be used to manipulate the booleans </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings. </p>
<h2>AUTHOR</h2>
<p> This manual page was auto-generated using <code>sepolicy manpage.</code> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-nx_server/">nx_server</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) , <a href="/docs/linux/man/8-setsebool/">setsebool</a>(8), <a href="/docs/linux/man/8-nx_server_ssh_selinux/">nx_server_ssh_selinux</a>(8), <a href="/docs/linux/man/8-nx_server_ssh_selinux/">nx_server_ssh_selinux</a>(8) </p>
