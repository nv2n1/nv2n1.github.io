---
title: "ksu(1)"
name: "ksu"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ksu/"
description: "ksu – Kerberized super-user"
---

<h2>NAME</h2>
<p> ksu &#8211; Kerberized super-user</p>
<h2>SYNOPSIS</h2>
<p> <code>ksu</code> [ <i>target_user</i> ] [ <code>-n</code> <i>target_principal_name</i> ] [ <code>-c</code> <i>source_cache_name</i> ] [ <code>-k</code> ] [ <code>-r</code> time ] [ <code>-pf</code> ] [ <code>-l</code> <i>lifetime</i> ] [ <code>-z | Z</code> ] [ <code>-q</code> ] [ <code>-e</code> <i>command</i> [ args &#8230; ] ] [ <code>-a</code> [ args &#8230; ] ]</p>
<h2>REQUIREMENTS</h2>
<p> Must have Kerberos version 5 installed to compile ksu. Must have a Kerberos version 5 server running to use ksu.</p>
<h2>DESCRIPTION</h2>
<p> ksu is a Kerberized version of the su program that has two missions: one is to securely change the real and effective user ID to that of the target user, and the other is to create a new security context. </p>
<p> <code>NOTE:</code> For the sake of clarity, all references to and attributes of the user invoking the program will start with &quot;source&quot; (e.g., &quot;source user&quot;, &quot;source cache&quot;, etc.). </p>
<p> Likewise, all references to and attributes of the target account will start with &quot;target&quot;.</p>
<h2>AUTHENTICATION</h2>
<p> To fulfill the first mission, ksu operates in two phases: authentication and authorization. Resolving the target principal name is the first step in authentication. The user can either specify his principal name with the <code>-n</code> option (e.g., <code>-n jqpublic [at] USC.EDU</code>) or a default principal name will be assigned using a heuristic described in the OPTIONS section (see <code>-n</code> option). The target user name must be the first argument to ksu; if not specified root is the default. If <code>.</code> is specified then the target user will be the source user (e.g., <code>ksu .</code>). If the source user is root or the target user is the source user, no authentication or authorization takes place. Otherwise, ksu looks for an appropriate Kerberos ticket in the source cache. </p>
<p> The ticket can either be for the end-server or a ticket granting ticket (TGT) for the target principal&#8217;s realm. If the ticket for the end-server is already in the cache, it&#8217;s decrypted and verified. If it&#8217;s not in the cache but the TGT is, the TGT is used to obtain the ticket for the end-server. The end-server ticket is then verified. If neither ticket is in the cache, but ksu is compiled with the <code>GET_TGT_VIA_PASSWD</code> define, the user will be prompted for a Kerberos password which will then be used to get a TGT. If the user is logged in remotely and does not have a secure channel, the password may be exposed. If neither ticket is in the cache and <code>GET_TGT_VIA_PASSWD</code> is not defined, authentication fails.</p>
<h2>AUTHORIZATION</h2>
<p> This section describes authorization of the source user when ksu is invoked without the <code>-e</code> option. For a description of the <code>-e</code> option, see the OPTIONS section. </p>
<p> Upon successful authentication, ksu checks whether the target principal is authorized to access the target account. In the target user&#8217;s home directory, ksu attempts to access two authorization files: <i><a href="/docs/linux/man/5--k5login/">.k5login</a>(5)</i> and .k5users. In the .k5login file each line contains the name of a principal that is authorized to access the account. </p>
<p> For example: </p>
<pre><code>
jqpublic[at] USC.EDU
        jqpublic /
    secure[at] USC.EDU
        jqpublic /
    admin[at] USC.EDU
</code></pre>
<p> The format of .k5users is the same, except the principal name may be followed by a list of commands that the principal is authorized to execute (see the <code>-e</code> option in the OPTIONS section for details). </p>
<p> Thus if the target principal name is found in the .k5login file the source user is authorized to access the target account. Otherwise ksu looks in the .k5users file. If the target principal name is found without any trailing commands or followed only by <code>*</code> then the source user is authorized. If either .k5login or .k5users exist but an appropriate entry for the target principal does not exist then access is denied. If neither file exists then the principal will be granted access to the account according to the aname-&gt;lname mapping rules. Otherwise, authorization fails.</p>
<h2>EXECUTION OF THE TARGET SHELL</h2>
<p> Upon successful authentication and authorization, ksu proceeds in a similar fashion to su. The environment is unmodified with the exception of USER, HOME and SHELL variables. If the target user is not root, USER gets set to the target user name. Otherwise USER remains unchanged. Both HOME and SHELL are set to the target login&#8217;s default values. In addition, the environment variable <code>KRB5CCNAME</code> gets set to the name of the target cache. The real and effective user ID are changed to that of the target user. The target user&#8217;s shell is then invoked (the shell name is specified in the password file). Upon termination of the shell, ksu deletes the target cache (unless ksu is invoked with the <code>-k</code> option). This is implemented by first doing a fork and then an exec, instead of just exec, as done by su.</p>
<h2>CREATING A NEW SECURITY CONTEXT</h2>
<p> ksu can be used to create a new security context for the target program (either the target shell, or command specified via the <code>-e</code> option). The target program inherits a set of credentials from the source user. By default, this set includes all of the credentials in the source cache plus any additional credentials obtained during authentication. The source user is able to limit the credentials in this set by using <code>-z</code> or <code>-Z</code> option. <code>-z</code> restricts the copy of tickets from the source cache to the target cache to only the tickets where client == the target principal name. The <code>-Z</code> option provides the target user with a fresh target cache (no creds in the cache). Note that for security reasons, when the source user is root and target user is non-root, <code>-z</code> option is the default mode of operation. </p>
<p> While no authentication takes place if the source user is root or is the same as the target user, additional tickets can still be obtained for the target cache. If <code>-n</code> is specified and no credentials can be copied to the target cache, the source user is prompted for a Kerberos password (unless <code>-Z</code> specified or <code>GET_TGT_VIA_PASSWD</code> is undefined). If successful, a TGT is obtained from the Kerberos server and stored in the target cache. Otherwise, if a password is not provided (user hit return) ksu continues in a normal mode of operation (the target cache will not contain the desired TGT). If the wrong password is typed in, ksu fails. </p>
<p> <code>NOTE:</code> During authentication, only the tickets that could be obtained without providing a password are cached in in the source cache.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code> <i>target_principal_name</i></p>
<dd> Specify a Kerberos target principal name. Used in authentication and authorization phases of ksu. </p>
<p> If ksu is invoked without <code>-n</code>, a default principal name is assigned via the following heuristic:</p>
<dt>&bull;</p>
<dd> Case 1: source user is non-root. </p>
<p> If the target user is the source user the default principal name is set to the default principal of the source cache. If the cache does not exist then the default principal name is set to <code>target_user [at] local_realm</code>. If the source and target users are different and neither <code>~target_user/.k5users</code> nor <code>~target_user/.k5login</code> exist then the default principal name is <code>target_user_login_name [at] local_realm</code>. Otherwise, starting with the first principal listed below, ksu checks if the principal is authorized to access the target account and whether there is a legitimate ticket for that principal in the source cache. If both conditions are met that principal becomes the default target principal, otherwise go to the next principal.</p>
<dt>a.</p>
<dd> default principal of the source cache</p>
<dt>b.</p>
<dd> target_user [at] local_realm</p>
<dt>c.</p>
<dd> source_user [at] local_realm </p>
<p> If a-c fails try any principal for which there is a ticket in the source cache and that is authorized to access the target account. If that fails select the first principal that is authorized to access the target account from the above list. If none are authorized and ksu is configured with <code>PRINC_LOOK_AHEAD</code> turned on, select the default principal as follows: </p>
<p> For each candidate in the above list, select an authorized principal that has the same realm name and first part of the principal name equal to the prefix of the candidate. For example if candidate a) is <code>jqpublic [at] ISI.EDU</code> and <code>jqpublic/secure [at] ISI.EDU</code> is authorized to access the target account then the default principal is set to <code>jqpublic/secure [at] ISI.EDU</code>.</p>
<dt>&bull;</p>
<dd> Case 2: source user is root. </p>
<p> If the target user is non-root then the default principal name is <code>target_user [at] local_realm</code>. Else, if the source cache exists the default principal name is set to the default principal of the source cache. If the source cache does not exist, default principal name is set to <code>root\@local_realm</code>. </p>
<p> <code>-c</code> <i>source_cache_name</i> Specify source cache name (e.g., <code>-c FILE:/tmp/my_cache</code>). If <code>-c</code> option is not used then the name is obtained from <code>KRB5CCNAME</code> environment variable. If <code>KRB5CCNAME</code> is not defined the source cache name is set to <code>krb5cc_&lt;source uid&gt;</code>. The target cache name is automatically set to <code>krb5cc_&lt;target uid&gt;.(gen_sym())</code>, where gen_sym generates a new number such that the resulting cache does not already exist. For example: </p>
<pre>
krb5cc_1984.2
</pre>
<dt><code>-k</code></p>
<dd> Do not delete the target cache upon termination of the target shell or a command (<code>-e</code> command). Without <code>-k</code>, ksu deletes the target cache.</p>
<dt><code>-z</code></p>
<dd> Restrict the copy of tickets from the source cache to the target cache to only the tickets where client == the target principal name. Use the <code>-n</code> option if you want the tickets for other then the default principal. Note that the <code>-z</code> option is mutually exclusive with the <code>-Z</code> option.</p>
<dt><code>-Z</code></p>
<dd> Don&#8217;t copy any tickets from the source cache to the target cache. Just create a fresh target cache, where the default principal name of the cache is initialized to the target principal name. Note that the <code>-Z</code> option is mutually exclusive with the <code>-z</code> option.</p>
<dt><code>-q</code></p>
<dd> Suppress the printing of status messages. </p>
<p> Ticket granting ticket options:</p>
<dt><code>-l</code> <i>lifetime</i> <code>-r</code> <i>time</i> <code>-pf</code></p>
<dd> The ticket granting ticket options only apply to the case where there are no appropriate tickets in the cache to authenticate the source user. In this case if ksu is configured to prompt users for a Kerberos password (<code>GET_TGT_VIA_PASSWD</code> is defined), the ticket granting ticket options that are specified will be used when getting a ticket granting ticket from the Kerberos server.</p>
<dt><code>-l</code> <i>lifetime</i></p>
<dd> (<i>duration</i> string.) Specifies the lifetime to be requested for the ticket; if this option is not specified, the default ticket lifetime (12 hours) is used instead.</p>
<dt><code>-r</code> <i>time</i></p>
<dd> (<i>duration</i> string.) Specifies that the <code>renewable</code> option should be requested for the ticket, and specifies the desired total lifetime of the ticket.</p>
<dt><code>-p</code></p>
<dd> specifies that the <code>proxiable</code> option should be requested for the ticket.</p>
<dt><code>-f</code></p>
<dd> option specifies that the <code>forwardable</code> option should be requested for the ticket.</p>
<dt><code>-e</code> <i>command</i> [<i>args</i> &#8230;]</p>
<dd> ksu proceeds exactly the same as if it was invoked without the <code>-e</code> option, except instead of executing the target shell, ksu executes the specified command. Example of usage: </p>
<pre>
ksu bob -e ls -lag
</pre>
<p> The authorization algorithm for <code>-e</code> is as follows: </p>
<p> If the source user is root or source user == target user, no authorization takes place and the command is executed. If source user id != 0, and <code>~target_user/.k5users</code> file does not exist, authorization fails. Otherwise, <code>~target_user/.k5users</code> file must have an appropriate entry for target principal to get authorized. </p>
<p> The .k5users file format: </p>
<p> A single principal entry on each line that may be followed by a list of commands that the principal is authorized to execute. A principal name followed by a <code>*</code> means that the user is authorized to execute any command. Thus, in the following example: </p>
<p>jqpublic[at] USC.EDU ls mail / local / kerberos / klist jqpublic / secure[at] USC.EDU *jqpublic / admin[at] USC.EDU</p>
<p> <code>jqpublic [at] USC.EDU</code> is only authorized to execute <code>ls</code>, <code>mail</code> and <code>klist</code> commands. <code>jqpublic/secure [at] USC.EDU</code> is authorized to execute any command. <code>jqpublic/admin [at] USC.EDU</code> is not authorized to execute any command. Note, that <code>jqpublic/admin [at] USC.EDU</code> is authorized to execute the target shell (regular ksu, without the <code>-e</code> option) but <code>jqpublic [at] USC.EDU</code> is not. </p>
<p> The commands listed after the principal name must be either a full path names or just the program name. In the second case, <code>CMD_PATH</code> specifying the location of authorized programs must be defined at the compilation time of ksu. Which command gets executed? </p>
<p> If the source user is root or the target user is the source user or the user is authorized to execute any command (<code>*</code> entry) then command can be either a full or a relative path leading to the target program. Otherwise, the user must specify either a full path or just the program name.</p>
<dt><code>-a</code> <i>args</i></p>
<dd> Specify arguments to be passed to the target shell. Note that all flags and parameters following -a will be passed to the shell, thus all options intended for ksu must precede <code>-a</code>. </p>
<p> The <code>-a</code> option can be used to simulate the <code>-e</code> option if used as follows: </p>
<pre><code>
- a - c[command[arguments]].
</code></pre>
<p> <code>-c</code> is interpreted by the c-shell to execute the command.</dl>
<h2>INSTALLATION INSTRUCTIONS</h2>
<p> ksu can be compiled with the following four flags:</p>
<dl>
<dt><code>GET_TGT_VIA_PASSWD</code></p>
<dd> In case no appropriate tickets are found in the source cache, the user will be prompted for a Kerberos password. The password is then used to get a ticket granting ticket from the Kerberos server. The danger of configuring ksu with this macro is if the source user is logged in remotely and does not have a secure channel, the password may get exposed.</p>
<dt><code>PRINC_LOOK_AHEAD</code></p>
<dd> During the resolution of the default principal name, <code>PRINC_LOOK_AHEAD</code> enables ksu to find principal names in the .k5users file as described in the OPTIONS section (see <code>-n</code> option).</p>
<dt><code>CMD_PATH</code></p>
<dd> Specifies a list of directories containing programs that users are authorized to execute (via .k5users file).</p>
<dt><code>HAVE_GETUSERSHELL</code></p>
<dd> If the source user is non-root, ksu insists that the target user&#8217;s shell to be invoked is a &quot;legal shell&quot;. <i><a href="/docs/linux/man/3-getusershell/">getusershell</a>(3)</i> is called to obtain the names of &quot;legal shells&quot;. Note that the target user&#8217;s shell is obtained from the passwd file. </p>
<p> Sample configuration: </p>
<pre>
KSU_OPTS = -DGET_TGT_VIA_PASSWD -DPRINC_LOOK_AHEAD -DCMD_PATH='&quot;/bin /usr/ucb /local/bin&quot;
</pre>
<p> ksu should be owned by root and have the set user id bit turned on. </p>
<p> ksu attempts to get a ticket for the end server just as Kerberized telnet and rlogin. Thus, there must be an entry for the server in the Kerberos database (e.g., <code>host/nii.isi.edu [at] ISI.EDU</code>). The keytab file must be in an appropriate location.</dl>
<h2>SIDE EFFECTS</h2>
<p> ksu deletes all expired tickets from the source cache.</p>
<h2>AUTHOR OF KSU</h2>
<p> GENNADY (ARI) MEDVINSKY</p>
<h2>AUTHOR</h2>
<p> MIT</p>
<h2>COPYRIGHT</h2>
<p> 1985-2017, MIT </p>
<h2>Index</h2>
