---
title: "mysql_install_db(1)"
name: "mysql_install_db"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_install_db/"
description: "mysql_install_db – initialize MySQL data directory"
---

<h2 class="name">NAME</h2>
<p> mysql_install_db &#8211; initialize MySQL data directory </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql_install_db [</code><i>options</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd>
<dd> <font SIZE="+1"> <code>Note</code> </font></p>
<dd>
<p> <code>mysql_install_db</code></p>
<dd>is deprecated as of MySQL 5.7.6 because its functionality has been integrated into <code>mysqld</code>, the MySQL server. To initialize a MySQL installation, invoke <code>mysqld</code> with the <code>&#8211;initialize</code> or <code>&#8211;initialize-insecure</code> option. For more information, see Section 2.10.1, &#8220;Initializing the Data Directory&#8221;. <code>mysql_install_db</code> will be removed in a future MySQL release. </p>
</dl>
<p> <code>mysql_install_db</code> handles initialization tasks that must be performed before the MySQL server, <code>mysqld</code>, is ready to use: </p>
<dl>
<dt>
<dd> &bull; It initializes the MySQL data directory and creates the system tables that it contains.</dl>
<dl>
<dt>
<dd> &bull; It initializes the system tablespace and related data structures needed to manage InnoDB tables.</dl>
<dl>
<dt>
<dd> &bull; It loads the server-side help tables.</dl>
<dl>
<dt>
<dd> &bull; It installs the sys schema.</dl>
<dl>
<dt>
<dd> &bull; It creates an administrative account. Older versions of <code>mysql_install_db</code> may create anonymous-user accounts.</dl>
<p> Before MySQL 5.7.5, <code>mysql_install_db</code> is a Perl script and requires that Perl be installed. As of 5.7.5, <code>mysql_install_db</code> is written in C++ and supplied in binary distributions as an executable binary. In addition, a number of new options were added and old options removed. If you find that an option does not work as you expect, be sure to check which options apply in your version of <code>mysql_install_db</code> (invoke it with the <code>&#8211;help</code> option). Secure-by-Default Deployment.PP Current versions of <code>mysql_install_db</code> produce a MySQL deployment that is secure by default. It is recommended that you use <code>mysql_install_db</code> from MySQL 5.7.5 or up for best security, but version-dependent information about security characteristics is included here for completeness (secure-by-default deployment was introduced in stages in MySQL 5.7). </p>
<p> MySQL 5.7.5 and up is secure by default, with these characteristics: </p>
<dl>
<dt>
<dd> &bull; A single administrative account named &#8216;root&#8217;@&#8217;localhost&#8217; is created with a randomly generated password, which is marked expired.</dl>
<dl>
<dt>
<dd> &bull; No anonymous-user accounts are created.</dl>
<dl>
<dt>
<dd> &bull; No test database accessible by all users is created.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;admin-</code><i>xxx</i> options are available to control characteristics of the administrative account.</dl>
<dl>
<dt>
<dd> &bull; The <code>&#8211;random-password-file</code> option is available to control where the random password is written.</dl>
<dl>
<dt>
<dd> &bull; The <code>&#8211;insecure</code> option is available to suppress random password generation.</dl>
<p> MySQL 5.7.4 is secure by default, with these characteristics: </p>
<dl>
<dt>
<dd> &bull; A single administrative account named &#8216;root&#8217;@&#8217;localhost&#8217; is created with a randomly generated password, which is marked expired.</dl>
<dl>
<dt>
<dd> &bull; No anonymous-user accounts are created.</dl>
<dl>
<dt>
<dd> &bull; No test database accessible by all users is created.</dl>
<dl>
<dt>
<dd> &bull; The <code>&#8211;skip-random-passwords</code> option is available to suppress random password generation, and to create a test database.</dl>
<p> MySQL 5.7.3 and earlier are not secure by default, with these characteristics: </p>
<dl>
<dt>
<dd> &bull; Multiple administrative root accounts are created with no password.</dl>
<dl>
<dt>
<dd> &bull; Anonymous-user accounts are created.</dl>
<dl>
<dt>
<dd> &bull; A test database accessible by all users is created.</dl>
<dl>
<dt>
<dd> &bull; The <code>&#8211;random-passwords</code> option is available to generate random passwords for administrative accounts and mark them expired, and to not create anonymous-user accounts.</dl>
<p> If <code>mysql_install_db</code> generates a random administative password, it writes the password to a file and displays the file name. The password entry includes a timestamp to indicate when it was written. By default, the file is .mysql_secret in the home directory of the effective user running the script. .mysql_secret is created with mode 600 to be accessible only to the operating system user for whom it is created. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font> </p>
<p> When <code>mysql_install_db</code> generates a random password for the administrative account, it is necessary after <code>mysql_install_db</code> has been run to start the server, connect using the administrative account with the password written to the .mysql_secret file, and specify a new administrative password. Until this is done, the administrative account cannot be used for anything else. To change the password, you can use the SET PASSWORD statement (for example, with the <code>mysql</code> or <code>mysqladmin</code> client). After resetting the password, remove the .mysql_secret file; otherwise, if you run <code>mysql_secure_installation</code>, that command may see the file and expire the root password again as part of ensuring secure deployment. </p>
</dl>
<p> Invocation Syntax.PP Several changes to <code>mysql_install_db</code> were made in MySQL 5.7.5 that affect the invocation syntax. Change location to the MySQL installation directory and use the command appropriate to your version of MySQL: </p>
<dl>
<dt>
<dd> &bull; Invocation syntax for MySQL 5.7.5 and up: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>bin/mysql_install_db --datadir=</code><i>path/to/datadir</i><code> [</code><i>other_options</i><code>]</code>
</pre>
</dl>
<p> The <code>&#8211;datadir</code> option is mandatory. <code>mysql_install_db</code> creates the data directory, which must not already exist: </p>
<dl>
<dt>
<dd> &bull; If the data directory does already exist, you are performing an upgrade operation (not an install operation) and should run <code>mysql_upgrade</code>, not <code>mysql_install_db</code>. See <code><a href="/docs/linux/man/1-mysql_upgrade/">mysql_upgrade</a></code>(1).</dl>
<dl>
<dt>
<dd> &bull; If the data directory does not exist but <code>mysql_install_db</code> fails, you must remove any partially created data directory before running <code>mysql_install_db</code> again.</dl>
</dl>
<dl>
<dt>
<dd> &bull; Invocation syntax before MySQL 5.7.5: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>scripts/mysql_install_db [</code><i>options</i><code>]</code>
</pre>
</dl>
</dl>
<p> Because the MySQL server, <code>mysqld</code>, must access the data directory when it runs later, you should either run <code>mysql_install_db</code> from the same system account that will be used for running <code>mysqld</code>, or run it as root and specify the <code>&#8211;user</code> option to indicate the user name that <code>mysqld</code> will run as. It might be necessary to specify other options such as <code>&#8211;basedir</code> if <code>mysql_install_db</code> does not use the correct location for the installation directory. For example: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>bin/mysql_install_db --user=mysql \</code>
         <code>--basedir=/opt/mysql/mysql \</code>
         <code>--datadir=/opt/mysql/mysql/data</code>
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> After <code>mysql_install_db</code> sets up the InnoDB system tablespace, changes to some tablespace characteristics require setting up a whole new instance. This includes the file name of the first file in the system tablespace and the number of undo logs. If you do not want to use the default values, make sure that the settings for the innodb_data_file_path and innodb_log_file_size configuration parameters are in place in the MySQL configuration file before running <code>mysql_install_db</code>. Also make sure to specify as necessary other parameters that affect the creation and location of InnoDB files, such as innodb_data_home_dir and innodb_log_group_home_dir. </p>
<p> If those options are in your configuration file but that file is not in a location that MySQL reads by default, specify the file location using the <code>&#8211;defaults-extra-file</code> option when you run <code>mysql_install_db</code>. </p>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> If you have set a custom TMPDIR environment variable when performing the installation, and the specified directory is not accessible, <code>mysql_install_db</code> may fail. If so, unset TMPDIR or set TMPDIR to point to the system temporary directory (usually /tmp). </p>
</dl>
<p> Administrative Account Creation.PP <code>mysql_install_db</code> creates an administrative account named &#8216;root&#8217;@&#8217;localhost&#8217; by default. (Before MySQL 5.7.4, <code>mysql_install_db</code> creates additional root accounts, such as &#8216;root&#8217;@&#8217;127.0.0.1&#8217;. This is no longer done.) </p>
<p> As of MySQL 5.7.5, <code>mysql_install_db</code> provides options that enable you to control several aspects of the administrative account: </p>
<dl>
<dt>
<dd> &bull; To change the user or host parts of the account name, use <code>&#8211;login-path</code>, or <code>&#8211;admin-user</code> and <code>&#8211;admin-host</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;insecure</code> suppresses generation of a random password.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;admin-auth-plugin</code> specifies the authentication plugin.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;admin-require-ssl</code> specifies whether the account must use SSL connections.</dl>
<p> For more information, see the descriptions of those options. </p>
<p> <code>mysql_install_db</code> assigns mysql.user system table rows a nonempty plugin column value to set the authentication plugin. The default value is mysql_native_password. The value can be changed using the <code>&#8211;admin-auth-plugin</code> option in MySQL 5.7.5 and up (as noted previously), or by setting the default_authentication_plugin system variable in MySQL 5.7.2 to 5.7.4. Default my.cnf File.PP As of MySQL 5.7.5, <code>mysql_install_db</code> creates no default my.cnf file. </p>
<p> Before MySQL 5.7.5, <code>mysql_install_db</code> creates a default option file named my.cnf in the base installation directory. This file is created from a template included in the distribution package named my-default.cnf. You can find the template in or under the base installation directory. When started using <code>mysqld_safe</code>, the server uses my.cnf file by default. If my.cnf already exists, <code>mysql_install_db</code> assumes it to be in use and writes a new file named my-new.cnf instead. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> As of MySQL 5.7.18, my-default.cnf is no longer included in or installed by distribution packages. </p>
</dl>
<p> With one exception, the settings in the default option file are commented and have no effect. The exception is that the file sets the sql_mode system variable to NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES. This setting produces a server configuration that results in errors rather than warnings for bad data in operations that modify transactional tables. See Section 5.1.10, &#8220;Server SQL Modes&#8221;. Command Options.PP <code>mysql_install_db</code> supports the following options, which can be specified on the command line or in the [mysql_install_db] group of an option file. For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. </p>
<p> Before MySQL 5.7.5, <code>mysql_install_db</code> passes unrecognized options to <code>mysqld</code>. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;admin-auth-plugin=</code><i>plugin_name</i> </p>
<p> The authentication plugin to use for the administrative account. The default is mysql_native_password.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;admin-host=</code><i>host_name</i> </p>
<p> The host part to use for the adminstrative account name. The default is localhost. This option is ignored if <code>&#8211;login-path</code> is also specified.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;admin-require-ssl</code> </p>
<p> Whether to require SSL for the administrative account. The default is not to require it. With this option enabled, the statement that <code>mysql_install_db</code> uses to create the account includes a REQUIRE SSL clause. As a result, the administrative account must use secure connections when connecting to the server.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;admin-user=</code><i>user_name</i> </p>
<p> The user part to use for the adminstrative account name. The default is root. This option is ignored if <code>&#8211;login-path</code> is also specified.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;basedir=</code><i>dir_name</i> </p>
<p> The path to the MySQL installation directory.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;builddir=</code><i>dir_name</i> </p>
<p> For use with <code>&#8211;srcdir</code> and out-of-source builds. Set this to the location of the directory where the built files reside.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;cross-bootstrap</code> </p>
<p> For internal use. This option is used for building system tables on one host intended for another. </p>
<p> This option was removed in MySQL 5.7.5.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;datadir=</code><i>dir_name</i> </p>
<p> The path to the MySQL data directory. Only the last component of the path name is created if it does not exist; the parent directory must already exist or an error occurs. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 As of MySQL 5.7.5, the <code>&#8211;datadir</code> option is mandatory and the data directory must not already exist. (It remains true that the parent directory must exist.) </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults</code> </p>
<p> This option causes <code>mysql_install_db</code> to invoke <code>mysqld</code> in such a way that it reads option files from the default locations. If given as <code>&#8211;no-defaults</code>, and <code>&#8211;defaults-file</code> or <code>&#8211;defaults-extra-file</code> is not also specified, <code>mysql_install_db</code> passes <code>&#8211;no-defaults</code> to <code>mysqld</code>, to prevent option files from being read. This may help if program startup fails due to reading unknown options from an option file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-extra-file=</code><i>file_name</i> </p>
<p> Read this option file after the global option file but (on Unix) before the user option file. If the file does not exist or is otherwise inaccessible, an error occurs. <i>file_name</i> is interpreted relative to the current directory if given as a relative path name rather than a full path name. </p>
<p> This option is passed by <code>mysql_install_db</code> to <code>mysqld</code>. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-file=</code><i>file_name</i> </p>
<p> Use only the given option file. If the file does not exist or is otherwise inaccessible, an error occurs. <i>file_name</i> is interpreted relative to the current directory if given as a relative path name rather than a full path name. </p>
<p> This option is passed by <code>mysql_install_db</code> to <code>mysqld</code>. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;extra-sql-file=</code><i>file_name</i>, <code>-f </code><i>file_name</i> </p>
<p> This option names a file containing additional SQL statements to be executed after the standard bootstrapping statements. Accepted statement syntax in the file is like that of the <code>mysql</code> command-line client, including support for multiple-line C-style comments and delimiter handling to enable definition of stored programs.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;force</code> </p>
<p> Cause <code>mysql_install_db</code> to run even if DNS does not work. Grant table entries normally created using host names will use IP addresses instead. </p>
<p> This option was removed in MySQL 5.7.5.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;insecure</code> </p>
<p> Do not generate a random password for the adminstrative account. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 The <code>&#8211;insecure</code> option was added in MySQL 5.7.5, replacing the <code>&#8211;skip-random-passwords</code> option. </p>
</dl>
<p> If <code>&#8211;insecure</code> is <i>not</i> given, it is necessary after <code>mysql_install_db</code> has been run to start the server, connect using the administrative account with the password written to the .mysql_secret file, and specify a new administrative password. Until this is done, the administrative account cannot be used for anything else. To change the password, you can use the SET PASSWORD statement (for example, with the <code>mysql</code> or <code>mysqladmin</code> client). After resetting the password, remove the .mysql_secret file; otherwise, if you run <code>mysql_secure_installation</code>, that command may see the file and expire the root password again as part of ensuring secure deployment.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;keep-my-cnf</code> </p>
<p> Tell <code>mysql_install_db</code> to preserve any existing my.cnf file and not create a new default my.cnf file. </p>
<p> This option was added in MySQL 5.7.4 and removed in 5.7.5. As of 5.7.5, <code>mysql_install_db</code> does not create a default my.cnf file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;lc-messages=name</code> </p>
<p> The locale to use for error messages. The default is en_US. The argument is converted to a language name and combined with the value of <code>&#8211;lc-messages-dir</code> to produce the location for the error message file. See Section 10.12, &#8220;Setting the Error Message Language&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;lc-messages-dir=</code><i>dir_name</i> </p>
<p> The directory where error messages are located. The value is used together with the value of <code>&#8211;lc-messages</code> to produce the location for the error message file. See Section 10.12, &#8220;Setting the Error Message Language&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ldata=</code><i>dir_name</i> </p>
<p> A synonym for <code>&#8211;datadir</code>. </p>
<p> This option was removed in MySQL 5.7.5.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;login-file=</code><i>file_name</i> </p>
<p> The file from which to read the login path if the <code>&#8211;login-path=</code><i>file_name</i> option is specified. The default file is .mylogin.cnf.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;login-path=</code><i>name</i> </p>
<p> Read options from the named login path in the .mylogin.cnf login path file. The default login path is client. (To read a different file, use the <code>&#8211;login-file=</code><i>name</i> option.) A &#8220;login path&#8221; is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the <code>mysql_config_editor</code> utility. See <code><a href="/docs/linux/man/1-mysql_config_editor/">mysql_config_editor</a></code>(1). </p>
<p> If the <code>&#8211;login-path</code> option is specified, the user, host, and password values are taken from the login path and used to create the administrative account. The password must be defined in the login path or an error occurs, unless the <code>&#8211;insecure</code> option is also specified. In addition, with <code>&#8211;login-path</code>, any <code>&#8211;admin-host</code> and <code>&#8211;admin-user</code> options are ignored. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;mysqld-file=</code><i>file_name</i> </p>
<p> The path name of the <code>mysqld</code> binary to execute. The option value must be an absolute path name or an error occurs. </p>
<p> If this option is not given, <code>mysql_install_db</code> searches for <code>mysqld</code> in these locations: </p>
<dl>
<dt>
<dd> &bull; In the bin directory under the <code>&#8211;basedir</code> option value, if that option was given.</dl>
<dl>
<dt>
<dd> &bull; In the bin directory under the <code>&#8211;srcdir</code> option value, if that option was given.</dl>
<dl>
<dt>
<dd> &bull; In the bin directory under the <code>&#8211;builddir</code> option value, if that option was given.</dl>
<dl>
<dt>
<dd> &bull; In the local directory and in the bin and sbin directories under the local directory.</dl>
<dl>
<dt>
<dd> &bull; In /usr/bin, /usr/sbin, /usr/local/bin, /usr/local/sbin, /opt/local/bin, /opt/local/sbin.</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code> </p>
<p> Before MySQL 5.7.5, do not read any option files. If program startup fails due to reading unknown options from an option file, <code>&#8211;no-defaults</code> can be used to prevent them from being read. For behavior of this option as of MySQL 5.7.5, see the description of <code>&#8211;defaults</code>. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;random-password-file=</code><i>file_name</i> </p>
<p> The path name of the file in which to write the randomly generated password for the administrative account. The option value must be an absolute path name or an error occurs. The default is $HOME/.mysql_secret.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;random-passwords</code> </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 This option was removed in MySQL 5.7.4 and replaced with <code>&#8211;skip-random-passwords</code>, which was in turn removed in MySQL 5.7.5 and replaced with <code>&#8211;insecure</code>. </p>
</dl>
<p> On Unix platforms, this option provides for more secure MySQL installation. Invoking <code>mysql_install_db</code> with <code>&#8211;random-passwords</code> causes it to perform the following actions in addition to its normal operation: </p>
<dl>
<dt>
<dd> &bull; The installation process creates a random password, assigns it to the initial MySQL root accounts, and marks the password expired for those accounts.</dl>
<dl>
<dt>
<dd> &bull; The initial random root password is written to the .mysql_secret file in the directory named by the HOME environment variable. Depending on operating system, using a command such as <code>sudo</code> may cause the value of HOME to refer to the home directory of the root system user. .mysql_secret is created with mode 600 to be accessible only to the operating system user for whom it is created. </p>
<p> If .mysql_secret already exists, the new password information is appended to it. Each password entry includes a timestamp to indicate when it was written.</dl>
<dl>
<dt>
<dd> &bull; No anonymous-user MySQL accounts are created.</dl>
<p> As a result of these actions, it is necessary after installation to start the server, connect as root using the password written to the .mysql_secret file, and specify a new root password. Until this is done, root cannot do anything else. This must be done for each root account you intend to use. To change the password, you can use the SET PASSWORD statement (for example, with the <code>mysql</code> client). You can also use <code>mysqladmin</code> or <code>mysql_secure_installation</code>. </p>
<p> New install operations (not upgrades) using RPM packages and Solaris PKG packages invoke <code>mysql_install_db</code> with the <code>&#8211;random-passwords</code> option. (Install operations using RPMs for Unbreakable Linux Network are unaffected because they do not use <code>mysql_install_db</code>.) </p>
<p> For install operations using a binary .tar.gz distribution or a source distribution, you can invoke <code>mysql_install_db</code> with the <code>&#8211;random-passwords</code> option manually to make your MySQL installation more secure. This is recommended, particularly for sites with sensitive data.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;rpm</code> </p>
<p> For internal use. This option is used during the MySQL installation process for install operations performed using RPM packages. </p>
<p> This option was removed in MySQL 5.7.5.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-name-resolve</code> </p>
<p> Use IP addresses rather than host names when creating grant table entries. This option can be useful if your DNS does not work. </p>
<p> This option was removed in MySQL 5.7.5.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-random-passwords</code> </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 The <code>&#8211;skip-random-passwords</code> option was added in MySQL 5.7.4, replacing the <code>&#8211;random-passwords</code> option. <code>&#8211;skip-random-passwords</code> was in turn removed in MySQL 5.7.5 and replaced with <code>&#8211;insecure</code>. </p>
</dl>
<p> As of MySQL 5.7.4, MySQL deployments produced using <code>mysql_install_db</code> are secure by default. When invoked <i>without</i> the <code>&#8211;skip-random-passwords</code> option, <code>mysql_install_db</code> uses these default deployment characteristics: </p>
<dl>
<dt>
<dd> &bull; The installation process creates a single root account, &#8216;root&#8217;@&#8217;localhost&#8217;, automatically generates a random password for this account, and marks the password expired.</dl>
<dl>
<dt>
<dd> &bull; The initial random root password is written to the .mysql_secret file in the home directory of the effective user running the script. .mysql_secret is created with mode 600 to be accessible only to the operating system user for whom it is created. </p>
<p> If .mysql_secret already exists, the new password information is appended to it. Each password entry includes a timestamp to indicate when it was written.</dl>
<dl>
<dt>
<dd> &bull; No anonymous-user MySQL accounts are created.</dl>
<dl>
<dt>
<dd> &bull; No test database is created.</dl>
<p> As a result of these actions, it is necessary after installation to start the server, connect as root using the password written to the .mysql_secret file, and specify a new root password. Until this is done, the administrative account cannot be used for anything else. To change the password, you can use the SET PASSWORD statement (for example, with the <code>mysql</code> client). You can also use <code>mysqladmin</code> or <code>mysql_secure_installation</code>. </p>
<p> To produce a MySQL deployment that is not secure by default, you must explicitly specify the <code>&#8211;skip-random-passwords</code> option when you invoke <code>mysql_install_db</code>. With this option, <code>mysql_install_db</code> performs the following actions: </p>
<dl>
<dt>
<dd> &bull; No random password is generated for the &#8216;root&#8217;@&#8217;localhost&#8217; account.</dl>
<dl>
<dt>
<dd> &bull; A test database is created that is accessible by any user.</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-sys-schema</code> </p>
<p> As of MySQL 5.7.7, <code>mysql_install_db</code> installs the sys schema. The <code>&#8211;skip-sys-schema</code> option suppresses this behavior. This option was added in MySQL 5.7.7.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;srcdir=</code><i>dir_name</i> </p>
<p> For internal use. This option specifies the directory under which <code>mysql_install_db</code> looks for support files such as the error message file and the file for populating the help tables.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user=</code><i>user_name</i>, <code>-u </code><i>user_name</i> </p>
<p> The system (login) user name to use for running <code>mysqld</code>. Files and directories created by <code>mysqld</code> will be owned by this user. You must be the system root user to use this option. By default, <code>mysqld</code> runs using your current login name and files and directories that it creates will be owned by you.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;verbose</code>, <code>-v</code> </p>
<p> Verbose mode. Print more information about what the program does. You can use this option to see the <code>mysqld</code> command that <code>mysql_install_db</code> invokes to start the server in bootstrap mode.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;version</code>, <code>-V</code> </p>
<p> Display version information and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;windows</code> </p>
<p> For internal use. This option is used for creating Windows distributions. It is a deprecated alias for <code>&#8211;cross-bootstrap</code> </p>
<p> This option was removed in MySQL 5.7.5.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 2019, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
