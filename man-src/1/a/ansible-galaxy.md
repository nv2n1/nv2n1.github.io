---
title: "ansible-galaxy(1)"
name: "ansible-galaxy"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ansible-galaxy/"
description: "ansible-galaxy – manage roles using galaxy.ansible.com"
---

<h2 class="name">NAME</h2>
<p> ansible-galaxy &#8211; manage roles using galaxy.ansible.com </p>
<h2>SYNOPSIS</h2>
<p> ansible-galaxy [delete|import|info|init|install|list|login|remove|search|setup] [&#8211;help] [options] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>Ansible Galaxy</code> is a shared repository for Ansible roles. The ansible-galaxy command can be used to manage these roles, or for creating a skeleton framework for roles you&#8217;d like to upload to Galaxy.</p>
<h2>COMMON OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show a help message related to the given sub-command.</dl>
<h2>INSTALL</h2>
<p> The <code>install</code> sub-command is used to install roles.</p>
<h3>USAGE</h3>
<p> $ ansible-galaxy install [options] [-r FILE | role_name(s)[,version] | tar_file(s)] </p>
<p> Roles can be installed in several different ways: </p>
<dl>
<dt>
<dd> &bull; A username.rolename[,version] &#8211; this will install a single role. The Galaxy API will be contacted to provide the information about the role, and the corresponding .tar.gz will be downloaded from <code>github.com</code>. If the version is omitted, the most recent version available will be installed.</dl>
<dl>
<dt>
<dd> &bull; A file name, using <code>-r</code> &#8211; this will install multiple roles listed one per line. The format of each line is the same as above: username.rolename[,version]</dl>
<dl>
<dt>
<dd> &bull; A .tar.gz of a valid role you&#8217;ve downloaded directly from <code>github.com</code>. This is mainly useful when the system running Ansible does not have access to the Galaxy API, for instance when behind a firewall or proxy.</dl>
<h3>OPTIONS</h3>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Force overwriting an existing role.</dl>
<p> <code>-i</code>, <code>&#8211;ignore-errors</code></p>
<dl>
<dt>
<dd> Ignore errors and continue with the next specified role.</dl>
<p> <code>-n</code>, <code>&#8211;no-deps</code></p>
<dl>
<dt>
<dd> Don&#8217;t download roles listed as dependencies.</dl>
<p> <code>-p</code> <i>ROLES_PATH</i>, <code>&#8211;roles-path=</code><i>ROLES_PATH</i></p>
<dl>
<dt>
<dd> The path to the directory containing your roles. The default is the <code>roles_path</code> configured in your <code>ansible.cfg</code> file (/etc/ansible/roles if not configured)</dl>
<p> <code>-r</code> <i>ROLE_FILE</i>, <code>&#8211;role-file=</code><i>ROLE_FILE</i></p>
<dl>
<dt>
<dd> A file containing a list of roles to be imported, as specified above. This option cannot be used if a rolename or .tar.gz have been specified.</dl>
<h2>REMOVE</h2>
<p> The <code>remove</code> sub-command is used to remove one or more roles.</p>
<h3>USAGE</h3>
<p> $ ansible-galaxy remove role1 role2 &#8230;</p>
<h3>OPTIONS</h3>
<p> <code>-p</code> <i>ROLES_PATH</i>, <code>&#8211;roles-path=</code><i>ROLES_PATH</i></p>
<dl>
<dt>
<dd> The path to the directory containing your roles. The default is the <code>roles_path</code> configured in your <code>ansible.cfg</code> file (/etc/ansible/roles if not configured)</dl>
<h2>INIT</h2>
<p> The <code>init</code> command is used to create an empty role suitable for uploading to <a rel="nofollow" href="https://galaxy.ansible.com">https://galaxy.ansible.com</a> (or for roles in general).</p>
<h3>USAGE</h3>
<p> $ ansible-galaxy init [options] role_name</p>
<h3>OPTIONS</h3>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Force overwriting an existing role.</dl>
<p> <code>-p</code> <i>INIT_PATH</i>, <code>&#8211;init-path=</code><i>INIT_PATH</i></p>
<dl>
<dt>
<dd> The path in which the skeleton role will be created.The default is the current working directory.</dl>
<p> <code>&#8211;offline</code></p>
<dl>
<dt>
<dd> Don&#8217;t query the galaxy API when creating roles</dl>
<h2>LIST</h2>
<p> The <code>list</code> sub-command is used to show what roles are currently installed. You can specify a role name, and if installed only that role will be shown.</p>
<h3>USAGE</h3>
<p> $ ansible-galaxy list [role_name]</p>
<h3>OPTIONS</h3>
<p> <code>-p</code> <i>ROLES_PATH</i>, <code>&#8211;roles-path=</code><i>ROLES_PATH</i></p>
<dl>
<dt>
<dd> The path to the directory containing your roles. The default is the <code>roles_path</code> configured in your <code>ansible.cfg</code> file (/etc/ansible/roles if not configured)</dl>
<h2>SEARCH</h2>
<p> The <code>search</code> sub-command returns a filtered list of roles found on the remote server.</p>
<h3>USAGE</h3>
<p> $ ansible-galaxy search [options] [searchterm1 searchterm2]</p>
<h3>OPTIONS</h3>
<p> <code>&#8211;galaxy-tags</code></p>
<dl>
<dt>
<dd> Provide a comma separated list of Galaxy Tags on which to filter.</dl>
<p> <code>&#8211;platforms</code></p>
<dl>
<dt>
<dd> Provide a comma separated list of Platforms on which to filter.</dl>
<p> <code>&#8211;author</code></p>
<dl>
<dt>
<dd> Specify the username of a Galaxy contributor on which to filter.</dl>
<p> <code>-c</code>, <code>&#8211;ignore-certs</code></p>
<dl>
<dt>
<dd> Ignore TLS certificate errors.</dl>
<p> <code>-s</code>, <code>&#8211;server</code></p>
<dl>
<dt>
<dd> Override the default server <a rel="nofollow" href="https://galaxy.ansible.com.">https://galaxy.ansible.com.</a></dl>
<h2>INFO</h2>
<p> The <code>info</code> sub-command shows detailed information for a specific role. Details returned about the role included information from the local copy as well as information from galaxy.ansible.com.</p>
<h3>USAGE</h3>
<p> $ ansible-galaxy info [options] role_name[, version]</p>
<h3>OPTIONS</h3>
<p> <code>-p</code> <i>ROLES_PATH</i>, <code>&#8211;roles-path=</code><i>ROLES_PATH</i></p>
<dl>
<dt>
<dd> The path to the directory containing your roles. The default is the <code>roles_path</code> configured in your <code>ansible.cfg</code> file (/etc/ansible/roles if not configured)</dl>
<p> <code>-c</code>, <code>&#8211;ignore-certs</code></p>
<dl>
<dt>
<dd> Ignore TLS certificate errors.</dl>
<p> <code>-s</code>, <code>&#8211;server</code></p>
<dl>
<dt>
<dd> Override the default server <a rel="nofollow" href="https://galaxy.ansible.com.">https://galaxy.ansible.com.</a></dl>
<h2>LOGIN</h2>
<p> The <code>login</code> sub-command is used to authenticate with galaxy.ansible.com. Authentication is required to use the import, delete and setup commands. It will authenticate the user, retrieve a token from Galaxy, and store it in the user&#8217;s home directory.</p>
<h3>USAGE</h3>
<p> $ ansible-galaxy login [options] </p>
<p> The <code>login</code> sub-command prompts for a <code>GitHub</code> username and password. It does NOT send your password to Galaxy. It actually authenticates with GitHub and creates a personal access token. It then sends the personal access token to Galaxy, which in turn verifies that you are you and returns a Galaxy access token. After authentication completes the <code>GitHub</code> personal access token is destroyed. </p>
<p> If you do not wish to use your GitHub password, or if you have two-factor authentication enabled with GitHub, use the <code>&#8211;github-token</code> option to pass a personal access token that you create. Log into GitHub, go to Settings and click on Personal Access Token to create a token.</p>
<h3>OPTIONS</h3>
<p> <code>-c</code>, <code>&#8211;ignore-certs</code></p>
<dl>
<dt>
<dd> Ignore TLS certificate errors.</dl>
<p> <code>-s</code>, <code>&#8211;server</code></p>
<dl>
<dt>
<dd> Override the default server <a rel="nofollow" href="https://galaxy.ansible.com.">https://galaxy.ansible.com.</a></dl>
<p> <code>&#8211;github-token</code></p>
<dl>
<dt>
<dd> Authenticate using a <code>GitHub</code> personal access token rather than a password.</dl>
<h2>IMPORT</h2>
<p> Import a role from <code>GitHub</code> to galaxy.ansible.com. Requires the user first authenticate with galaxy.ansible.com using the <code>login</code> subcommand.</p>
<h3>USAGE</h3>
<p> $ ansible-galaxy import [options] github_user github_repo</p>
<h3>OPTIONS</h3>
<p> <code>-c</code>, <code>&#8211;ignore-certs</code></p>
<dl>
<dt>
<dd> Ignore TLS certificate errors.</dl>
<p> <code>-s</code>, <code>&#8211;server</code></p>
<dl>
<dt>
<dd> Override the default server <a rel="nofollow" href="https://galaxy.ansible.com.">https://galaxy.ansible.com.</a></dl>
<p> <code>&#8211;branch</code></p>
<dl>
<dt>
<dd> Provide a specific branch to import. When a branch is not specified the branch found in meta/main.yml is used. If no branch is specified in meta/main.yml, the repo&#8217;s default branch (usually master) is used.</dl>
<h2>DELETE</h2>
<p> The <code>delete</code> sub-command will delete a role from galaxy.ansible.com. Requires the user first authenticate with galaxy.ansible.com using the <code>login</code> subcommand.</p>
<h3>USAGE</h3>
<p> $ ansible-galaxy delete [options] github_user github_repo</p>
<h3>OPTIONS</h3>
<p> <code>-c</code>, <code>&#8211;ignore-certs</code></p>
<dl>
<dt>
<dd> Ignore TLS certificate errors.</dl>
<p> <code>-s</code>, <code>&#8211;server</code></p>
<dl>
<dt>
<dd> Override the default server <a rel="nofollow" href="https://galaxy.ansible.com.">https://galaxy.ansible.com.</a></dl>
<h2>SETUP</h2>
<p> The <code>setup</code> sub-command creates an integration point for <code>Travis CI</code>, enabling galaxy.ansible.com to receive notifications from <code>Travis</code> on build completion. Requires the user first authenticate with galaxy.ansible.com using the <code>login</code> subcommand.</p>
<h3>USAGE</h3>
<p> $ ansible-galaxy setup [options] source github_user github_repo secret </p>
<dl>
<dt>
<dd> &bull; Use <code>travis</code> as the source value. In the future additional source values may be added.</dl>
<dl>
<dt>
<dd> &bull; Provide your <code>Travis</code> user token as the secret. The token is not stored by galaxy.ansible.com. A hash is created using github_user, github_repo and your token. The hash value is what actually gets stored.</dl>
<h3>OPTIONS</h3>
<p> <code>-c</code>, <code>&#8211;ignore-certs</code></p>
<dl>
<dt>
<dd> Ignore TLS certificate errors.</dl>
<p> <code>-s</code>, <code>&#8211;server</code></p>
<dl>
<dt>
<dd> Override the default server <a rel="nofollow" href="https://galaxy.ansible.com.">https://galaxy.ansible.com.</a></dl>
<p> &#8211;list</p>
<dl>
<dt>
<dd> Show your configured integrations. Provides the ID of each integration which can be used with the remove option.</dl>
<p> &#8211;remove</p>
<dl>
<dt>
<dd> Remove a specific integration. Provide the ID of the integration to be removed.</dl>
<h2>AUTHOR</h2>
<p> Ansible was originally written by Michael DeHaan. See the AUTHORS file for a complete list of contributors.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2014, Michael DeHaan </p>
<p> Ansible is released under the terms of the GPLv3 License.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ansible/">ansible</a></code>(1), <code><a href="/docs/linux/man/1-ansible-pull/">ansible-pull</a></code>(1), <code><a href="/docs/linux/man/1-ansible-doc/">ansible-doc</a></code>(1), <code><a href="/docs/linux/man/1-ansible-playbook/">ansible-playbook</a></code>(1), <code><a href="/docs/linux/man/1-ansible-vault/">ansible-vault</a></code>(1) </p>
<p> Extensive documentation is available in the documentation site: <a rel="nofollow" href="http://docs.ansible.com.">http://docs.ansible.com.</a> IRC and mailing list info can be found in file CONTRIBUTING.md, available in: <a href="https://github.com/ansible/ansible">https://github.com/ansible/ansible</a> </p>
<h2>Index</h2>
