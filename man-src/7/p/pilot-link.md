---
title: "pilot-link(7)"
name: "pilot-link"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pilot-link/"
description: "pilot-link – A suite of tools for communicating with Palm handhelds, such as those made by Palm, Handspring, Handera, TRGPro, Sony or other Palm Compatible Handheld PDA device."
---

<p>pilot-link &#8211; A suite of tools for communicating with Palm handhelds, such as those made by Palm, Handspring, Handera, TRGPro, Sony or other Palm Compatible Handheld PDA device.</p>
<h2>Section</h2>
<p>Pilot-link: Overview</p>
<h2>Description</h2>
<p>The pilot-link suite of tools contains a series of conduits, libraries, and language bindings for moving information to and from your Palm device and your desktop or server/workstation system, as well as across the network. </p>
<h2>Target Device</h2>
<p>The /dev/pilot fallback has been removed in v0.12. The environment variable <code>$PILOTPORT</code> can be set in your shell, to save specifying the port each time. A serial device specified on the command-line will be used regardless of any <code>$PILOTPORT</code> setting. If <code>$PILOTPORT</code> is not set, and <code>-p</code> is not supplied, all conduits in <i>pilot-link</i> will print the usage information. The default connection rate is 9600 baud. You are welcome to try higher baud rates (19200, 38400, 57600 or higher) by setting the <code>$PILOTRATE</code> environment variable, but various machines have various limitations. (Be careful about values higher than 115200 on older Linux boxes if you&#8217;ve been using setserial to change the multiplier).</p>
<h2>Conduits</h2>
<p>A complete list of conduits available from within the <i>pilot-link</i> package as of the date of this manpage. If you invoke any of the conduits from <i>pilot-link</i> with no command-line arguments at all, the usage summary will be printed. </p>
<p> Note that there are widespread changes in this release &#8211; some conduits have been merged, a lot have had new options added and some options have been renamed or removed.</p>
<h3>addresses</h3>
<p>DEPRECATED: Use pilot-addresses &#8211;write|&#8211;human-readable instead.</p>
<h3>pilot-hinotes</h3>
<p>Syncronize your Hi-Notes database with your desktop machine.</p>
<h3>install-datebook</h3>
<p>installs a new datebook entry onto your Palm handheld.</p>
<h3>pilot-install-expenses</h3>
<p>Install an expense record from various parameters and arguments passed at connection time.</p>
<h3>install-hinote</h3>
<p>Install local files into your Hi-Note database on your Palm handheld.</p>
<h3>install-memo</h3>
<p>Installs a new Memo Pad entry onto your Palm handheld.</p>
<h3>pilot-install-netsync</h3>
<p>reads or sets the Network Preferences information on a Palm Device. Modifies the &quot;Network Preference&quot; settings and reports additional intormation about the Palm, such as the IP, hostname, and other information as they are set on the Palm.</p>
<h3>install-todo</h3>
<p>Updates the Palm ToDo list with one new entry.</p>
<h3>install-todos</h3>
<p>Updates the Palm ToDo list with entries from a local file.</p>
<h3>install-user</h3>
<p>Reads or sets a Palm User and UserID on a Palm Device. Modifies the &quot;User Preference&quot; settings and reports additional intormation about the Palm, such as the Username and UserID as they are set on the Palm</p>
<h3>pilot-memos</h3>
<p>Manipulate Memo entries from a file or your Palm device.</p>
<h3>pilot-addresses</h3>
<p>Read and write address book databases to and from a Palm handheld. </p>
<p> Changes in 0.12: Incorporates functionality from the now deprecated <i>addresses</i> conduit.</p>
<h3>pilot-archive</h3>
<p>DEPRECATED: Use pilot-read-todos -w &#8211;archived instead.</p>
<h3>pilot-clip</h3>
<p>Get or Set the Palm Clipboard contents from STDOUT/STDIN.</p>
<h3>pilot-dedupe</h3>
<p>Removes duplicate records from any Palm database.</p>
<h3>pilot-file</h3>
<p>Dump application and header information from your local PRC/PDB files.</p>
<h3>pilot-foto</h3>
<p>Palm &#8216;Foto&#8217; Image Installer/Remover/Fetcher/Converter</p>
<h3>pilot-read-screenshot</h3>
<p>Read screenshots from Palm (ScreenShotDB).</p>
<h3>pilot-schlep</h3>
<p>Package up any arbitrary file and sync it to your Palm device.</p>
<h3>pilot-foto-treo600</h3>
<p>Copies Treo 600 foto databases to current directory and extracts .jpg files from them.</p>
<h3>pilot-foto-treo650</h3>
<p>Copies Treo 600 images and videos to the current directory</p>
<h3>pilot-wav</h3>
<p>Decodes Palm Voice Memo files to wav files you can read</p>
<h3>pilot-xfer</h3>
<p>Backup, sync, and restore databases from a Palm handheld device.</p>
<h3>pilot-read-expenses</h3>
<p>Export Palm Expense application data in a text format.</p>
<h3>pilot-read-ical</h3>
<p>Exports the DatebookDB and/or ToDo applications (DatebookDB.pdb and ToDoDB.pdb respectively) to Ical format. (The ical application must be installed and working on your system first. This is NOT the same thing as the iCal Calendar format, however).</p>
<h3>pilot-read-notepad</h3>
<p>List the record information found in the Palm Notepad (Palm OS4 and later) application.</p>
<h3>pilot-read-palmpix</h3>
<p>Convert all pictures in the files given or found on a Palm handheld.</p>
<h3>pilot-read-todos</h3>
<p>Syncronize your Palm ToDo application&#8217;s database with your desktop machine.</p>
<h3>pilot-read-veo</h3>
<p>Synchronize your Veo Traveler databases</p>
<h3>pilot-reminders</h3>
<p>Exports your Palm Datebook database into a &#8216;remind&#8217; data file format.</p>
<h2>Tools</h2>
<h3>pilot-debugsh</h3>
<p>Simple debugging console for a Palm Handheld device (deprecated).</p>
<h3>pilot-dlpsh</h3>
<p>An interactive Desktop Link Protocol (DLP) Shell for your Palm device. This is very useful for debugging potential problems with your serial port. Query the RAM/ROM, list databases, change your UserID or Username, and many other useful functions. This is the &quot;Swiss Army Knife&quot; of any of pilot-link&#8217;s tools.</p>
<h3>pilot-csd</h3>
<p>Connection Service Daemon for Palm Devices</p>
<h3>pilot-getram</h3>
<p>Retrieves the RAM image from your Palm device for use in debugging.</p>
<h3>pilot-getrom</h3>
<p>Retrieves the ROM image from your Palm device for use in debugging.</p>
<h3>pilot-getromtoken</h3>
<p>Reads a ROM token from a Palm Handheld device.</p>
<h3>pilot-nredir</h3>
<p>Accept connection and redirect via Network Hotsync Protocol.</p>
<h2>Perl Scripts</h2>
<p>(Available from the source code, not always installed from packages).</p>
<h3>pilot-ietf2datebook.pl</h3>
<p>Converts IETF agenda format to install-datebook format</p>
<h3>pilot-undelete.pl</h3>
<p>Turn previously archived records into normal (non-archived) records by resetting the &quot;dirty&quot; bit.</p>
<h3>pilot-sync-plan.pl</h3>
<p>completely synchronize the Palm datebook with the &quot;plan&quot; calendar via netplan, including authenticating to the netplan server itself.</p>
<h2>Advanced Programs</h2>
<p>Some of these programs are not intended for general end-users. More detailed documentation on their usage can be obtained by reading the source of the application itself.</p>
<h3>ccexample</h3>
<p>test program demonstrating C++ interface.</p>
<h3>iambicexample</h3>
<p>test program demonstrating C++ interface.</p>
<h3>validate</h3>
<p>experimental program to test C++ features.</p>
<h2>Obtaining</h2>
<p>The most current version of the pilot-link suite of tools can be found at the pilot link homepage: <a rel="nofollow" href="http://www.pilot-link.org/">http://www.pilot-link.org/</a></p>
<h2>Mailing List</h2>
<p>The original pilot-unix mailing list has been taken offline, and is now being hosted and maintained by David A. Desrosiers &lt;desrod [at] gnu-designs.com&gt;. The original pilot-unix mailing list was maintained by Matthew Cravit. Its mandate was: </p>
<p> The pilot-unix mailing list is for discussion and &quot;idea-sharing&quot; for those interested in using your Palm handheld with UNIX systems. This includes people who are interested in helping to develop tools to allow the Palm to operate with UNIX and other POSIX systems, and possibly to develop an SDK (Software Develop- ment Kit) for the Palm for Unix. </p>
<p> For more information, including how to subscribe to the pilot-link mailing lists, please visit the pilot-link mailing list subscription page: </p>
<p> <a rel="nofollow" href="http://lists.pilot-link.org/">http://lists.pilot-link.org/</a> </p>
<p> pilot-link specific mailing lists are also available for Development, General, and Announce topics, at the following: </p>
<p> <a rel="nofollow" href="http://lists.pilot-link.org/mailman/listinfo/pilot-link-devel">http://lists.pilot-link.org/mailman/listinfo/pilot-link-devel</a> </p>
<p> <a rel="nofollow" href="http://lists.pilot-link.org/mailman/listinfo/pilot-link-general">http://lists.pilot-link.org/mailman/listinfo/pilot-link-general</a> </p>
<p> <a rel="nofollow" href="http://lists.pilot-link.org/mailman/listinfo/pilot-link-announce">http://lists.pilot-link.org/mailman/listinfo/pilot-link-announce</a></p>
<h2>Author</h2>
<p>Most of the pilot-link tools were written by Kenneth Albanowski. This manual page was written by David H. Silber &lt;pilot [at] orbits.com&gt;, and updated for version 0.12 of pilot-link by Neil Williams &lt; linux [at] codehelp.co.uk &gt; . </p>
<p> Current maintainer of pilot-link as of the authoring of this manpage is David A. Desrosiers &lt;desrod [at] gnu-designs.com&gt;. </p>
<p> Any questions or problems with <i>pilot-link</i> should be directed at the various <i> pilot-link </i> mailing lists or to the irc channel dedicated to supporting <i>pilot-link</i> at <i> irc.pilot-link.org </i> in your irc application (not a web browser).</p>
<h2>Patches</h2>
<p>All patches you wish to submit should be sent to &lt;patches [at] pilot-link.org&gt; directly, with a brief explanation of what the patch adds or fixes. Please make sure to send your patched in unified diff format (diff -u).</p>
<h2>See Also</h2>
<p>&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-addresses/">pilot-addresses</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-dlpsh/">pilot-dlpsh</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-hinotes/">pilot-hinotes</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-ietf2datebook/">pilot-ietf2datebook</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-install-datebook/">pilot-install-datebook</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-install-expenses/">pilot-install-expenses</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-install-hinote/">pilot-install-hinote</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-install-memo/">pilot-install-memo</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-install-netsync/">pilot-install-netsync</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-install-user/">pilot-install-user</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-getrom/">pilot-getrom</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-getram/">pilot-getram</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-addresses/">pilot-addresses</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-xfer/">pilot-xfer</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-read-ical/">pilot-read-ical</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-read-notepad/">pilot-read-notepad</a></i>(1),&nbsp;<wbr><i><a href="/docs/linux/man/1-pilot-read-palmpix/">pilot-read-palmpix</a></i>(1) David Silber &lt;pilot [at] orbits.com&gt; has written a Pilot HOWTO, which you can find at <a rel="nofollow" href="http://www.sgmltools.org/HOWTO/Pilot-HOWTO/t1.html">http://www.sgmltools.org/HOWTO/Pilot-HOWTO/t1.html</a> </p>
