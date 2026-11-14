---
title: "git_selinux(8)"
name: "git_selinux"
section: "8"
letter: "g"
url: "/docs/linux/man/8-git_selinux/"
---

git_selinux - Security Enhanced Linux Policy for the Git daemon.

<h2>Description</h2>

Security-Enhanced Linux secures the Git server via flexible mandatory access control.

<h2>File_Contexts</h2>

SELinux requires files to have an extended attribute to define the file type. Policy governs the access daemons have to these files. SELinux Git policy is very flexible allowing users to setup their web services in as secure a method as possible. 

 The following file contexts types are by default defined for Git: <pre>git_system_content_t </pre>- Set files with git_system_content_t if you want the Git system daemon to read the file, and if you want the file to be modifiable and executable by all &quot;Git shell&quot; users. <pre>git_session_content_t </pre>- Set files with git_session_content_t if you want the Git session and system daemon to read the file, and if you want the file to be modifiable and executable by all users. Note that &quot;Git shell&quot; users may not interact with this type.

<h2>Booleans</h2>

SELinux policy is customizable based on least access required. Git policy is extremely flexible and has several booleans that allow you to manipulate the policy and run Git with the tightest access possible. 

 Allow the Git system daemon to search user home directories so that it can find git session content. This is useful if you want the Git system daemon to host users personal repositories. <pre>sudo setsebool -P git_system_enable_homedirs 1</pre>Allow the Git system daemon to read system shared repositories on NFS shares. <pre>sudo setsebool -P git_system_use_nfs 1</pre>Allow the Git system daemon to read system shared repositories on Samba shares. <pre>sudo setsebool -P git_system_use_cifs 1</pre>Allow the Git session daemon to read users personal repositories on NFS mounted home directories. <pre>sudo setsebool -P use_nfs_home_dirs 1</pre>Allow the Git session daemon to read users personal repositories on Samba mounted home directories. <pre>sudo setsebool -P use_samba_home_dirs 1</pre>To also allow Git system daemon to read users personal repositories on NFS and Samba mounted home directories you must also allow the Git system daemon to search home directories so that it can find the repositories. <pre>sudo setsebool -P git_system_enable_homedirs 1</pre>To allow the Git System daemon mass hosting of users personal repositories you can allow the Git daemon to listen to any unreserved ports. <pre>sudo setsebool -P git_session_bind_all_unreserved_ports 1</pre>

<h2>Git_Shell</h2>

The Git policy by default provides a restricted user environment to be used with &quot;Git shell&quot;. This default git_shell_u SELinux user can modify and execute generic Git system content (generic system shared respositories with type git_system_content_t). 

 To add a new Linux user and map him to this Git shell user domain automatically: <pre>sudo useradd -Z git_shell_u joe</pre>

<h2>Advanced_System_Shared_Repository_And Git_Shell_Restrictions</h2>

Alternatively Git SELinux policy can be used to restrict &quot;Git shell&quot; users to git system shared repositories. The policy allows for the creation of new types of Git system content and Git shell user environment. The policy allows for delegation of types of &quot;Git shell&quot; environments to types of Git system content. 

 To add a new Git system repository type, for example &quot;project1&quot; create a file named project1.te and add to it: <pre>policy_module(project1, 1.0.0)
git_content_template(project1)</pre>Next create a file named project1.fc and add a file context specification for the new repository type to it: <pre>/srv/git/project1.git(/.*)? gen_context(system_u:object_r:git_project1_content_t,s0)</pre>Build a binary representation of this source policy module, load it into the policy store and restore the context of the repository: <pre>make -f /usr/share/selinux/devel/Makefile project.pp
sudo semodule -i project1.pp
sudo restorecon -R -v /srv/git/project1</pre>To create a &quot;Git shell&quot; domain that can interact with this repository create a file named project1user.te in the same directory as where the source policy for the Git systemm content type is and add the following: <pre>policy_module(project1user, 1.0.0) 
git_role_template(project1user)
git_content_delegation(project1user_t, git_project1_content_t)
gen_user(project1user_u, user, project1user_r, s0, s0)</pre>Build a binary representation of this source policy module, load it into the policy store and map Linux users to the new project1user_u SELinux user: <pre>make -f /usr/share/selinux/devel/Makefile project1user.pp
sudo semodule -i project1user.pp
sudo useradd -Z project1user_u jane</pre>system-config-selinux is a GUI tool available to customize SELinux policy settings.

<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>

This manual page was written by Dominick Grift &lt;domg472 [at] gmail.com&gt;.

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-selinux/">selinux</a>(8), <a HREF="/docs/linux/man/8-git/">git</a>(8), <a HREF="/docs/linux/man/1-chcon/">chcon</a>(1), <a HREF="/docs/linux/man/8-semodule/">semodule</a>(8), <a HREF="/docs/linux/man/8-setsebool/">setsebool</a>(8) 
