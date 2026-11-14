---
title: "ansible-vault(1)"
name: "ansible-vault"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ansible-vault/"
description: "ansible-vault – manage encrypted ansible vars files (YAML)."
---

<h2 class="name">NAME</h2>
<p> ansible-vault &#8211; manage encrypted ansible vars files (YAML). </p>
<h2>SYNOPSIS</h2>
<p> ansible-vault [create|decrypt|edit|encrypt|rekey] [&#8211;help] [options] file_name</p>
<h2>DESCRIPTION</h2>
<p> <code>ansible-vault</code> can encrypt any structured data file used by Ansible. This can include <code>group_vars/</code> or <code>host_vars/</code> inventory variables, variables loaded by <code>include_vars</code> or <code>vars_files</code>, or variable files passed on the ansible-playbook command line with <code>-e @file.yml</code> or <code>-e @file.json</code>. Role variables and defaults are also included! </p>
<p> Because Ansible tasks, handlers, and so on are also data, these can also be encrypted with vault. If you&#8217;d like to not betray what variables you are even using, you can go as far to keep an individual task file entirely encrypted. </p>
<p> The password used with vault currently must be the same for all files you wish to use together at the same time.</p>
<h2>COMMON OPTIONS</h2>
<p> The following options are available to all sub-commands: </p>
<p> <code>&#8211;vault-password-file=</code><i>FILE</i></p>
<dl>
<dt>
<dd> A file containing the vault password to be used during the encryption/decryption steps. Be sure to keep this file secured if it is used. If the file is executable, it will be run and its standard output will be used as the password.</dl>
<p> <code>&#8211;new-vault-password-file=</code><i>FILE</i></p>
<dl>
<dt>
<dd> A file containing the new vault password to be used when rekeying a file. Be sure to keep this file secured if it is used. If the file is executable, it will be run and its standard output will be used as the password.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show a help message related to the given sub-command.</dl>
<p> If <i>&#8211;vault-password-file</i> is not supplied ansible-vault will automatically prompt for passwords as required.</p>
<h2>CREATE</h2>
<p> <code>$ ansible-vault create [options] FILE</code> </p>
<p> The <code>create</code> sub-command is used to initialize a new encrypted file. </p>
<p> After providing a password, the tool will launch whatever editor you have defined with $EDITOR, and defaults to vi. Once you are done with the editor session, the file will be saved as encrypted data. </p>
<p> The default cipher is AES (which is shared-secret based).</p>
<h2>EDIT</h2>
<p> <code>$ ansible-vault edit [options] FILE</code> </p>
<p> The <code>edit</code> sub-command is used to modify a file which was previously encrypted using ansible-vault. </p>
<p> This command will decrypt the file to a temporary file and allow you to edit the file, saving it back when done and removing the temporary file.</p>
<h2>REKEY</h2>
<p> <code>$ ansible-vault rekey [options] FILE_1 [FILE_2, &#8230;, FILE_N]</code> </p>
<p> The <code>rekey</code> command is used to change the password on a vault-encrypted files. This command can update multiple files at once.</p>
<h2>ENCRYPT</h2>
<p> <code>$ ansible-vault encrypt [options] FILE_1 [FILE_2, &#8230;, FILE_N]</code> </p>
<p> The <code>encrypt</code> sub-command is used to encrypt pre-existing data files. As with the <code>rekey</code> command, you can specify multiple files in one command. </p>
<p> The <code>encrypt</code> command accepts an <code>&#8211;output FILENAME</code> option to determine where encrypted output is stored. With this option, input is read from the (at most one) filename given on the command line; if no input file is given, input is read from stdin. Either the input or the output file may be given as <i>&#8211;</i> for stdin and stdout respectively. If neither input nor output file is given, the command acts as a filter, reading plaintext from stdin and writing it to stdout. </p>
<p> Thus any of the following invocations can be used: </p>
<p> <code>$ ansible-vault encrypt</code> </p>
<p> <code>$ ansible-vault encrypt &#8211;output OUTFILE</code> </p>
<p> <code>$ ansible-vault encrypt INFILE &#8211;output OUTFILE</code> </p>
<p> <code>$ echo secret|ansible-vault encrypt &#8211;output OUTFILE</code> </p>
<p> Reading from stdin and writing only encrypted output is a good way to prevent sensitive data from ever hitting disk (either interactively or from a script).</p>
<h2>DECRYPT</h2>
<p> <code>$ ansible-vault decrypt [options] FILE_1 [FILE_2, &#8230;, FILE_N]</code> </p>
<p> The <code>decrypt</code> sub-command is used to remove all encryption from data files. The files will be stored as plain-text YAML once again, so be sure that you do not run this command on data files with active passwords or other sensitive data. In most cases, users will want to use the <code>edit</code> sub-command to modify the files securely. </p>
<p> As with <code>encrypt</code>, the <code>decrypt</code> subcommand also accepts the <code>&#8211;output FILENAME</code> option to specify where plaintext output is stored, and stdin/stdout is handled as described above.</p>
<h2>AUTHOR</h2>
<p> Ansible was originally written by Michael DeHaan. See the AUTHORS file for a complete list of contributors.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2014, Michael DeHaan </p>
<p> Ansible is released under the terms of the GPLv3 License.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ansible/">ansible</a></code>(1), <code><a href="/docs/linux/man/1-ansible-pull/">ansible-pull</a></code>(1), <code><a href="/docs/linux/man/1-ansible-doc/">ansible-doc</a></code>(1), <code><a href="/docs/linux/man/1-ansible-playbook/">ansible-playbook</a></code>(1), <code><a href="/docs/linux/man/1-ansible-galaxy/">ansible-galaxy</a></code>(1) </p>
<p> Extensive documentation is available in the documentation site: <a rel="nofollow" href="http://docs.ansible.com.">http://docs.ansible.com.</a> IRC and mailing list info can be found in file CONTRIBUTING.md, available in: <a href="https://github.com/ansible/ansible">https://github.com/ansible/ansible</a> </p>
<h2>Index</h2>
