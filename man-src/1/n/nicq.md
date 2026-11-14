---
title: "nicq(1)"
name: "nicq"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nicq/"
description: "naim – console mode chat client"
---

<h2>NAME</h2>
<p> naim &#8211; console mode chat client</p>
<h2>SYNOPSIS</h2>
<p> naim<br />
 nicq<br />
 nirc [<i>nickname</i> [<i>server</i>]]<br />
 nlily</p>
<h2>DESCRIPTION</h2>
<p> naim is the original ncurses AIM client. It uses the TOC protocol, and features many commonly-requested features found nowhere else, while still providing an intuitive chat interface. </p>
<h2>OPTIONS</h2>
<p> If a `<code>.naimrc</code>&#8216; file exists in your home directory, naim executes that and ignores all command line options. Otherwise&#8230; </p>
<p> When invoked as `<code>naim</code>&#8216;, naim will create a connection of type AIM/TOC and will display some helpful information to the screen (but won&#8217;t actually try to sign you on). </p>
<p> When invoked as `<code>nicq</code>&#8216;, naim will create a connection of type ICQ/TOC and will display some helpful information to the screen (but won&#8217;t actually try to sign you on). </p>
<p> When invoked as `<code>nirc</code>&#8216;, naim will create a connection of type IRC and will attempt to sign you on using the <i>nickname</i> and <i>server</i>, if provided. </p>
<p> When invoked as `<code>nlily</code>&#8216;, naim will create a connection of type Lily/SLCP and will display some helpful information to the screen (but won&#8217;t actually try to sign you on). </p>
<h2>ADDITIONAL CONNECTIONS</h2>
<p> Once you have naim started, you can easily create additional connections by using the /newconn command. For example, to visit me on the EFnet IRC network, you might type:<br />
 /newconn EFnet IRC<br />
 /connect naimuser irc.servercentral.net<br />
 /join #naim<br />
 (note that if you start naim as `<code>nirc</code>&#8216; it will run the previous commands automatically) </p>
<p> If you wanted to sign on to AIM more than once, you might type:<br />
 /newconn AIM2 AIM<br />
 /connect othername </p>
<p> If you start naim as `<code>naim</code>&#8216; it will issue `<code>/newconn AIM TOC</code>&#8216; automatically. If you start naim as `<code>nicq</code>&#8216; it will issue `<code>/newconn ICQ TOC</code>&#8216; automatically. If you start naim as `<code>nlily</code>&#8216; it will issue `<code>/newconn Lily SLCP</code>&#8216; automatically. The first argument to /newconn is the connection &quot;name&quot;, which can be anything you dream up (it might make sense to use your screen name if you are going to be connecting to the same service more than once), and the second argument is the connection type. AIM and ICQ both use the same connection type (TOC). </p>
<p> By default, the Ins and Del keys will switch between connections. See `<code>/help keys</code>&#8216; for additional information, including how to change your key bindings. </p>
<h2>SETTINGS</h2>
<p> Once you have setup naim the way you like it (see `<code>/help settings</code>&#8216; and `<code>/help keys</code>&#8216;), use the `<code>/save</code>&#8216; command to have naim create a .naimrc file in your home directory. From then on, naim will always start up configured the way it is currently configured, including all of your current settings (<code>/set</code>), key bindings (<code>/bind</code>), and open connections (<code>/newconn</code>). Feel free to load the generated .naimrc file in a text editor for further tweaking. </p>
<h2>ONLINE HELP</h2>
<p> Online help is available by typing <code>/help</code> at the console. </p>
<h2>EXITING</h2>
<p> Use the <code>/quit</code> command. </p>
<h2>AUTHOR</h2>
<p> Daniel Reed &lt;n@ml.org&gt;, with notable contributions from Ian Gulliver &lt;ian [at] penguinhosting.net&gt; and Joshua Wise &lt;joshua [at] joshuawise.com&gt;. </p>
<h2>UPDATES</h2>
<p> The latest version of naim will always be available from <code><a rel="nofollow" href="http://naim.n.ml.org/">http://naim.n.ml.org/</a></code> . If you ever use naim, you are strongly encouraged to subscribe to the naim-announce mailing list. This is a low-volume mailing list used exclusively to announce new releases of naim or changes in the AIM service that affects naim users. To subscribe, simply send a blank email to &lt;naim-announce-subscribe [at] n.ml.org&gt; and reply to the confirmation message you will receive. </p>
<h2>BUG REPORTS</h2>
<p> Before reporting any bugs, please review Simon Tatham (of PuTTY)&#8217;s wonderful essay, <i>How to Report Bugs Effectively</i> at <code><a rel="nofollow" href="http://www.chiark.greenend.org.uk/~sgtatham/bugs.html">http://www.chiark.greenend.org.uk/~sgtatham/bugs.html</a></code>. </p>
<p> To report issues with the front end (things having to do with buddy windows, colors, .naimrc, and anything else &quot;user oriented&quot;) contact the naim maintainer, Daniel Reed &lt;n@ml.org&gt;. </p>
<p> To report issues with the protocol library (problems connecting, error messages while connected, and anything else not a part of the front end) contact the FireTalk maintainer, now also Daniel Reed &lt;n@ml.org&gt;. </p>
<p> To report issues with the FreeBSD port, contact Ryan T. Dean &lt;rtdean [at] cytherianage.net&gt;. </p>
<h2>FEATURE REQUESTS</h2>
<p> If you would like to suggest new features or significant behavior changes, subscribe to the naim-users mailing list and suggest it there. I get a lot of mail every day, and non-bug reports get a fairly low priority. The best way to make sure something you want is implemented is to post it to naim-users whenever I ask for them on the list. To subscribe, send a blank email to &lt;naim-users-subscribe [at] n.ml.org&gt; and reply to the confirmation message you will receive. </p>
<h2>PATCHES</h2>
<p> If you would like to participate to naim&#8217;s development in a more active role, feel free to submit patches either to myself or to the naim-users mailing list. Patches in context output format are prefered. In order to work on naim, you may wish to extract naim twice, and perform your builds in a third directory, as in:<br />
 <i> tar -jxvf naim-0.11.8.tar.bz2</i><br />
 <i> mv naim-0.11.8 naim-0.11.8,original</i><br />
 <i> tar -jxvf naim-0.11.8.tar.bz2</i><br />
 <i> mkdir naim-0.11.8-objdir</i><br />
 <i> cd naim-0.11.8-objdir</i><br />
 <i> ../naim-0.11.8/configure &#8211;prefix=/usr</i> </p>
<p> Then you may modify the files in ../naim-0.11.8, compile, test, modify again, recompile, test, etc. until your are satisfied, then:<br />
 <i> cd ..</i><br />
 <i> diff -rcN naim-0.11.8,original naim-0.11.8 &gt; \</i><br />
 <i> naim-0.11.8.feature1.patch</i> </p>
<p> And submit `<code>naim-0.11.8.feature1.patch</code>&#8216;. Do not gzip or otherwise encode patches, so they may be reviewed from within a mail client. </p>
<h2>Index</h2>
