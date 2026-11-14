---
title: "abrt-plugins(7)"
name: "abrt-plugins"
section: "7"
letter: "a"
url: "/docs/linux/man/7-abrt-plugins/"
---

abrt-plugins - plugins for the abrt crash reporter program

<h2>Description</h2>

<i>abrt</i> is a daemon that watches for application crashes. When a crash occurs, it collects the crash data (core file, application's command line etc.) and takes action according to the type of application that crashed and according to the configuration specified in the <i>abrt.conf</i> configuration file. Plugins allow abrt to perform various actions: for example, to report the crash to Bugzilla, to mail the report, to transfer the report via FTP or SCP, or to run a program that you specify. This manual page provides a list of all the manual pages for these plugins. If you want to create your own plugin, refer to the PLUGINS-HOWTO file in the documentation directory.

<h2>Invocation</h2>

Each plugin is invoked in the <i>abrt.conf</i> configuration file, in the section that is appropriate to what you want abrt to do.

<h2>Configuration</h2>

Almost every plugin has its configuration file, stored in the <i>/etc/abrt/plugins</i> directory.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-abrt/">abrt</a></i>(8), <i><a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a></i>(5), <i><a HREF="/docs/linux/man/7-abrt-bugzilla/">abrt-Bugzilla</a></i>(7), <i><a HREF="/docs/linux/man/7-abrt-filetransfer/">abrt-FileTransfer</a></i>(7), <i><a HREF="/docs/linux/man/7-abrt-kerneloopsreporter/">abrt-KerneloopsReporter</a></i>(7), <i><a HREF="/docs/linux/man/7-abrt-kerneloopsscanner/">abrt-KerneloopsScanner</a></i>(7), <i><a HREF="/docs/linux/man/7-abrt-logger/">abrt-Logger</a></i>(7), <i><a HREF="/docs/linux/man/7-abrt-mailx/">abrt-Mailx</a></i>(7), <i><a HREF="/docs/linux/man/7-abrt-runapp/">abrt-RunApp</a></i>(7), <i><a HREF="/docs/linux/man/7-abrt-sqlite3/">abrt-SQLite3</a></i>(7)

<h2>Author</h2>

<i>abrt</i> written by Zdeněk Přikryl &lt;zprikryl [at] redhat.com&gt; and Jiří Moskovčák &lt;jmoskovc [at] redhat.com&gt;. Manual page written by Daniel Novotný &lt;dnovotny [at] redhat.com&gt;.
