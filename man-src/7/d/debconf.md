---
title: "debconf(7)"
name: "debconf"
section: "7"
letter: "d"
url: "/docs/linux/man/7-debconf/"
description: "debconf – Debian package configuration system"
---

<p>debconf &#8211; Debian package configuration system</p>
<h2>Description</h2>
<p>Debconf is a configuration system for Debian packages. There is a rarely-used command named debconf, documented in <code><a href="/docs/linux/man/1-debconf/">debconf</a></code>(1) </p>
<p> Debconf provides a consistent interface for configuring packages, allowing you to choose from several user interface frontends. It supports preconfiguring packages before they are installed, which allows large installs and upgrades to ask you for all the necessary information up front, and then go do the work while you do something else. It lets you, if you&#8217;re in a hurry, skip over less important questions and information while installing a package (and revisit it later).</p>
<h2>Preconfiguring packages</h2>
<p>Debconf can configure packages before they are even installed onto your system. This is useful because it lets all the questions the packages are going to ask be asked at the beginning of an install, so the rest of the install can proceed while you are away getting a cup of coffee. </p>
<p> If you use apt (version 0.5 or above), and you have apt-utils installed, each package apt installs will be automatically preconfigured. This is controlled via <i>/etc/apt/apt.conf.d/70debconf</i> </p>
<p> Sometimes you might want to preconfigure a package by hand, when you&#8217;re not installing it with apt. You can use <code><a href="/docs/linux/man/8-dpkg-preconfigure/">dpkg-preconfigure</a></code>(8) to do that, just pass it the filenames of the packages you want to preconfigure. You will need apt-utils installed for that to work.</p>
<h2>Reconfiguring packages</h2>
<p>Suppose you installed the package, and answered debconf&#8217;s questions, but now that you&#8217;ve used it awhile, you realize you want to go back and change some of your answers. In the past, reinstalling a package was often the thing to do when you got in this situation, but when you reinstall the package, debconf seems to remember you have answered the questions, and doesn&#8217;t ask them again (this is a feature). </p>
<p> Luckily, debconf makes it easy to reconfigure any package that uses it. Suppose you want to reconfigure debconf itself. Just run, as root:<br />
&nbsp;<wbr>&nbsp;<wbr>dpkg-reconfigure debconf </p>
<p> This will ask all the questions you saw when debconf was first installed. It may ask you other questions as well, since it asks even low priority questions that may have been skipped when the package was installed. You can use it on any other package that uses debconf, as well.</p>
<h2>Frontends</h2>
<p>One of debconf&#8217;s unique features is that the interface it presents to you is only one of many, that can be swapped in at will. There are many debconf frontends available:</p>
<dl>
<dt><code>dialog</code></p>
<dd>The default frontend, this uses the <code><a href="/docs/linux/man/1-whiptail/">whiptail</a></code>(1) or <code><a href="/docs/linux/man/1-dialog/">dialog</a></code>(1) programs to display questions to you. It works in text mode.</p>
<dt><code>readline</code></p>
<dd>
<dl>
<dd>The most traditional frontend, this looks quite similar to how Debian configuration always has been: a series of questions, printed out at the console using plain text, and prompts done using the readline library. It even supports tab completion. The libterm-readline-gnu-perl package is strongly recommended if you chose to use this frontend; the default readline module does not support prompting with default values. At the minimum, you&#8217;ll need the perl-modules package installed to use this frontend. </p>
<p> This frontend has some special hotkeys. Pageup (or ctrl-u) will go back to the previous question (if that is supported by the package that is using debconf), and pagedown (or ctrl-v) will skip forward to the next question. </p>
<p> This is the best frontend for remote admin work over a slow connection, or for those who are comfortable with unix.</dl>
<dt><code>noninteractive</code></p>
<dd>This is the anti-frontend. It never interacts with you at all, and makes the default answers be used for all questions. It might mail error messages to root, but that&#8217;s it; otherwise it is completely silent and unobtrusive, a perfect frontend for automatic installs. If you are using this front-end, and require non-default answers to questions, you will need to preseed the debconf database; see the section below on Unattended Package Installation for more details.</p>
<dt><code>gnome</code></p>
<dd>This is a modern X GUI using the gtk and gnome libraries. Of course, it requires a valid DISPLAY to work; debconf will fall back to other frontends if it can&#8217;t work. Note that this frontend requires you have the libgnome2-perl package installed.</p>
<dt><code>kde</code></p>
<dd>This frontend provides a simple X GUI written with the Qt library. It fits well the KDE desktop. You of course need a DISPLAY to use this frontend and must install libqt-perl. The frontend will fall back to dialog if some of the prerequisites are not met.</p>
<dt><code>editor</code></p>
<dd>This is for those fanatics who have to do everything in a text editor. It runs your editor on a file that looks something like a typical unix config file, and you edit the file to communicate with debconf. Debconf&#8217;s author prefers to not comment regarding the circumstances that led to this frontend being written.</p>
<dt><code>web</code></p>
<dd>
<dl>
<dd>This frontend acts as a web server, that you connect to with your web browser, to browse the questions and answer them. It has a lot of promise, but is a little rough so far. When this frontend starts up, it will print out the location you should point your web browser to. You have to run the web browser on the same machine you are configuring, for security reasons. </p>
<p> Do keep in mind that this is not a very secure frontend. Anyone who has access to the computer being configured can currently access the web server and configure things while this frontend is running. So this is more of a proof of concept than anything.</dl>
</dl>
<p> You can change the default frontend debconf uses by reconfiguring debconf. On the other hand, if you just want to change the frontend for a minute, you can set the DEBIAN_FRONTEND environment variable to the name of the frontend to use. For example:<br />
&nbsp;<wbr>&nbsp;<wbr>DEBIAN_FRONTEND=readline apt-get install slrn </p>
<p> The <code><a href="/docs/linux/man/8-dpkg-reconfigure/">dpkg-reconfigure</a></code>(8) and <code><a href="/docs/linux/man/8-dpkg-preconfigure/">dpkg-preconfigure</a></code>(8) commands also let you pass <i>&#8211;frontend=</i> to them, followed by the frontend you want them to use. </p>
<p> Note that not all frontends will work in all circumstances. If a frontend fails to start up for some reason, debconf will print out a message explaining why, and fall back to the next-most similar frontend.</p>
<h2>Priorities</h2>
<p>Another nice feature of debconf is that the questions it asks you are prioritized. If you don&#8217;t want to be bothered about every little thing, you can set up debconf to only ask you the most important questions. On the other hand, if you are a control freak, you can make it show you all questions. Each question has a priority. In increasing order of importance:</p>
<dl>
<dt><code>low</code></p>
<dd>Very trivial questions that have defaults that will work in the vast majority of cases.</p>
<dt><code>medium</code></p>
<dd>Normal questions that have reasonable defaults.</p>
<dt><code>high</code></p>
<dd>Questions that don&#8217;t have a reasonable default.</p>
<dt><code>critical</code></p>
<dd>Questions that you really, really need to see (or else).</dl>
<p> Only questions with a priority equal to or greater than the priority you choose will be shown to you. You can set the priority value by reconfiguring debconf, or temporarily by passing <i>&#8211;priority=</i> followed by the value to the <code><a href="/docs/linux/man/8-dpkg-reconfigure/">dpkg-reconfigure</a></code>(8) and <code><a href="/docs/linux/man/8-dpkg-preconfigure/">dpkg-preconfigure</a></code>(8) commands, or by setting the DEBIAN_PRIORITY environment variable.</p>
<h2>Backend Database</h2>
<p>Debconf uses a rather flexible and potentially complicated backend database for storing data such as the answers to questions. The file <code>/etc/debconf.conf</code> is used to configure this database. If you need to set up something complicated, like make debconf read a remote database to get defaults, with local overrides, read the <code><a href="/docs/linux/man/5-debconf-conf/">debconf.conf</a></code>(5) man page for all the gory details. Generally, the backend database is located in <code>/var/cache/debconf/</code><br />
&nbsp;<wbr>.</p>
<h2>Unattended Package Installation</h2>
<p>If you have many machines to manage you will sometimes find yourself in the position of needing to perform an unattended installation or upgrade of packages on many systems, when the default answers to some configuration questions are not acceptable. There are many ways to approach this; all involve setting up a database and making debconf use it to get the answers you want. </p>
<p> You should really read <code><a href="/docs/linux/man/5-debconf-conf/">debconf.conf</a></code>(5) before this section, as you need to understand how debconf&#8217;s databases work. </p>
<p> The easiest way to set up the database is to install the packages on one machine and answer their questions as usual. Or you might just use <code><a href="/docs/linux/man/8-dpkg-preconfigure/">dpkg-preconfigure</a></code>(8) to configure a set of packages without actually installing them. Or you might even decide to write a plain text debconf database by hand or something. </p>
<p> Once you have the database, you need to figure out how to make the remote systems use it. This depends of course on the configuration of those systems and what database types they are set up to use. </p>
<p> If you are using the LDAP debconf database, an entire network of debian machines can also have any or all package installation questions answered automatically by a single LDAP server. </p>
<p> But perhaps you&#8217;re using something a little bit easier to set up like, say, the default debconf database configuration, or you just don&#8217;t want your remote systems to use LDAP all the time. In this case the best approach is to temporarily configure the remote systems to stack your database underneath their own existing databases, so they pull default values out of it. Debconf offers two environment variables, DEBCONF_DB_FALLBACK and DEBCONF_DB_OVERRIDE, to make it easy to do this on the fly. Here is a sample use: </p>
<p>cat&nbsp;<wbr>/var/cache/debconf/config.dat |&nbsp;<wbr>\<br />
ssh root [at] target&nbsp;<wbr>&quot;DEBIAN_FRONTEND=noninteractive&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DEBCONF_DB_FALLBACK=Pipe apt-get upgrade&quot; </p>
<p> This makes the debconf on the remote host read in the data that is piped across the ssh connection and interpret it as a plain text format debconf database. It then uses that database as a fallback database &#8212; a read-only database that is queried for answers to questions if the system&#8217;s main debconf database lacks answers. </p>
<p> Here&#8217;s another way to use the DEBCONF_DB_FALLBACK environment variable: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ssh -R 389:ldap:389 root [at] target&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&quot;DEBCONF_DB_FALLBACK=&#8217;LDAP{host:localhost}&#8217;&nbsp;<wbr>apt-get upgrade&quot;</p>
<p> Here ssh is used to set up a tunneled LDAP connection and run debconf. Debconf is told to use the LDAP server as the fallback database. Note the use of &quot;{host:localhost}&quot; to configure how debconf accesses the LDAP database by providing the &quot;host&quot; field with a value of &quot;localhost&quot;. </p>
<p> Here&#8217;s another method: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>scp config.dat root [at] target:<br />
&nbsp;<wbr>&nbsp;<wbr>ssh root [at] target&nbsp;<wbr>&quot;DEBCONF_DB_FALLBACK=&#8217;File{/root/config.dat}&#8217;&nbsp;<wbr>apt-get upgrade </p>
<p> Here you copy the database over with scp, and then ssh over and make debconf use the file you copied over. This illustrates a shorthand you can use in the DEBCONF_DB_FALLBACK parameters &#8212; if a field name is left off, it defaults to &quot;filename&quot;. </p>
<p> There is only one problem with these uses of the DEBCONF_DB_FALLBACK parameter: While the fallback database can provide answers to questions the other debconf databases have never seen, it is only queried as a fallback; after the other databases. If you need to instead temporarily override an existing value on the remote host, you should instead use the DEBCONF_DB_OVERRIDE variable. Like DEBCONF_DB_FALLBACK, it sets up a temporary database, but this database is consulted before any others, and can be used to override existing values.</p>
<h2>Developing for Debconf</h2>
<p>Package developers and others who want to develop packages that use debconf should read <code><a href="/docs/linux/man/7-debconf-devel/">debconf-devel</a></code>(7)<br />
&nbsp;<wbr>. </p>
<p> Briefly, debconf communicates with maintainer scripts or other programs via standard input and output, using a simple line-oriented command language similar to that used by common internet protocols such as SMTP. Programs use this protocol to ask debconf to display questions to the user, and retrieve the user&#8217;s answers. The questions themselves are defined in a separate file, called the &quot;templates file&quot;, which has a format not unlike a debian control file. </p>
<p> Debian packages which use debconf typically provide both a templates file and a &quot;config&quot; script (run to preconfigure the package) in the control metadata section of the package.</p>
<h2>Environment</h2>
<dl>
<dt><code>DEBIAN_FRONTEND</code></p>
<dd>Used to temporarily change the frontend debconf uses. See above.</p>
<dt><code>DEBIAN_PRIORITY</code></p>
<dd>Used to temporarily change the minimum priority of question debconf will display. See above.</p>
<dt><code>DEBCONF_DEBUG</code></p>
<dd>
<dl>
<dd>Turns on debugging output on standard error. May be set to a facility name or a regular expression which matches a facility name (such as &#8216;.*&#8217; to output all debug info). The facility names include:</p>
<dl>
<dt><code>user</code></p>
<dd>Debugging info of interest to a debconf user.</p>
<dt><code>developer</code></p>
<dd>Debugging info of interest to a package developer.</p>
<dt><code>db</code></p>
<dd>Debugging info about the backend database.</dl>
</dl>
<dt><code>DEBCONF_NOWARNINGS</code></p>
<dd>Set to &quot;yes&quot; to disable some warnings that debconf may display. Does not suppress display of fatal errors.</p>
<dt><code>DEBCONF_TERSE</code></p>
<dd>Set to &quot;yes&quot; to enable terse mode, in which debconf frontends cut down on the verbiage as much as possible.</p>
<dt><code>DEBCONF_DB_FALLBACK</code></p>
<dd>Stack a database after the normally used databases, so that it is used as a fallback to get configuration information from. See &quot;Unattended Package Installation&quot; above. If the value of the variable is the name of an existing database in debconf.conf, then that database will be used. Otherwise, the environment variable can be used to configure a database on the fly, by telling the type of database, and optionally passing field:value settings, inside curly braces after the type. Spaces are used to separate fields, so you cannot specify a field value containing whitespace.</dl>
<p> Thus, this uses the fallbackdb in debconf.conf:<br />
&nbsp;<wbr>&nbsp;<wbr>DEBCONF_DB_FALLBACK=fallbackdb </p>
<p> While this sets up a new database of type File, and tells it a filename to use and turns off backups:<br />
&nbsp;<wbr>&nbsp;<wbr>DEBCONF_DB_FALLBACK=File{Filename:/root/config.dat Backup:no} </p>
<p> And as a shorthand, this sets up a database of type File with a filename:<br />
&nbsp;<wbr>&nbsp;<wbr>DEBCONF_DB_FALLBACK=File{/root/config.dat} </p>
<p> Note that if a fallback database is set up on the fly, it will be read-only by default.</p>
<dl>
<dt><code>DEBCONF_DB_OVERRIDE</code></p>
<dd>Stack a database before the normally used databases, so that it can override values from them. The value of the variable works the same as does the value of DEBCONF_DB_FALLBACK.</p>
<dt><code>DEBCONF_DB_REPLACE</code></p>
<dd>Use a given database instead of the normally used databases. This may be useful for testing with a separate database without having to create a separate debconf.conf, or to avoid locking the normal databases.</p>
<dt><code>DEBCONF_SYSTEMRC</code></p>
<dd>If this environment variable is set, debconf will ignore a user&#8217;s ~/.debconfrc file, and use the system one instead. If it is set to the name of a regular file, debconf will use that file in preference to the system configuration files.</p>
<dt><code>DEBCONF_FORCE_DIALOG</code></p>
<dd>If this environment variable is set, debconf will use dialog in preference to whiptail for the dialog frontend.</p>
<dt><code>DEBCONF_FORCE_XDIALOG</code></p>
<dd>If this environment variable is set, debconf will use Xdialog in preference to whiptail for the dialog frontend.</p>
<dt><code>DEBCONF_NONINTERACTIVE_SEEN</code></p>
<dd>Set to &quot;true&quot; to cause the seen flag to be set for questions asked in the noninteractive frontend.</dl>
<h2>Bugs</h2>
<p>Probably quite a few, there&#8217;s a lot of code here. </p>
<p> If you do file a bug report, be sure to include the following information:</p>
<dl>
<dt><code>*</code></p>
<dd>The debconf frontend you were using when the problem occurred</p>
<dt><code>*</code></p>
<dd>What you did to trigger the problem.</p>
<dt><code>*</code></p>
<dd>The full text of any error messages. If you can reproduce the bug, do so with DEBCONF_DEBUG=&#8217;.*&#8217; set and exported. This speeds up debugging a lot.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-debconf-conf/">debconf.conf</a></code>(5), <code><a href="/docs/linux/man/7-debconf-devel/">debconf-devel</a></code>(7), <code><a href="/docs/linux/man/8-dpkg-preconfigure/">dpkg-preconfigure</a></code>(8), <code><a href="/docs/linux/man/8-dpkg-reconfigure/">dpkg-reconfigure</a></code>(8), <code><a href="/docs/linux/man/1-debconf/">debconf</a></code>(1),</p>
<h2>Author</h2>
<p>Joey Hess &lt;joeyh [at] debian.org&gt;</p>
