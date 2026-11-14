---
title: "bournal(1)"
name: "bournal"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bournal/"
description: "bournal – When nobody else cares what you have to say!"
---

<h2>NAME</h2>
<p> bournal &#8211; When nobody else cares what you have to say!</p>
<h2>SYNOPSIS</h2>
<p> <code>bournal</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>bournal</code> is a program that allows you to write personal, password-protected journal entries, as well as search through and edit old entries. Bournal has no internet capabilities, so if you&#8217;re looking for a blogging app, boy, did you install the wrong package.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options</p>
<dt><code>-i</code></p>
<dd> Interactive mode&#8211;Open a bournal shell to run several operations without having to reenter your password. Readline editing options are supported.</p>
<dt><code>-lst</code></p>
<dd> List and edit entries made today. You will be prompted to choose a subject.</p>
<dt><code>-ls [MONTH] [YEAR]</code></p>
<dd> List and edit archived entries. Month and year arguments filter out superfluous entries, which will prompt you first with a list of days within the given timeframe, then a list of subjects made on the chosen day. If no month or year arguments are given, all days containing entries are listed, followed by a list of entries made on the chosen day.</p>
<dt><code>-d [MONTH] [YEAR]</code></p>
<dd> List and delete archived entries. Month and year arguments filter out superfluous entries, which will prompt you first with a list of days within the given time frame, then a list of subjects made on the chosen day. If no month or year arguments are given, all days containing entries are listed, followed by a list of entries made on the chosen day, then a prompt to confirm deletion.</p>
<dt><code>-f [PATTERN] [MONTH]</code></p>
<dd> Find text within entries. Protect space-separated search terms with quotes. Regular expression searches are accepted, using egrep syntax.</p>
<dt><code>-fi [PatTerN] [MONTH]</code></p>
<dd> Find case-insensitive text within entries. Protect space-separated search terms with quotes. Regular expression searches are accepted, using egrep syntax.</p>
<dt><code>-r </code></p>
<dd> Read all entries at once</p>
<dt><code>-p </code></p>
<dd> Change the encryption password</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show version information</p>
<dt><code>&#8211;hack_the_gibson</code></p>
<dd> Hack the planet (for updates)</dl>
<h2>SYSTEM REQUIREMENTS</h2>
<dl>
<dt><code>ccrypt</code></p>
<dd> a utility for encrypting and decrypting files and streams</p>
<dt><code>Linux</code></p>
<dd> or something similar with basic *NIX utils</p>
<dt><code>Vim </code></p>
<dd> or <code>Nano</code> or <code>Jed</code> , or some other editor that is not as awesome as Vim.</dl>
<h2>NOTES</h2>
<p> Files encrypted with ccrypt WILL work between computers (assuming it&#8217;s installed), so taking Bournal and all its entries with you on a flash drive will work just peachy. You can have entries automatically saved to the flash drive by changing the DIR variable to the path of your flashdrive, (e.g. ` <i>DIR=/media/USB_VOL_NAME</i> `). However, if you run Bournal from a USB drive, you will need to predeed it with a shell (e.g. ` <i>bash bournal</i> `)</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.bournal/</code></p>
<dd> Default directory where entries are stored.</p>
<dt><code>~/.bournal/.passwd.cpt</code></p>
<dd> Default password file.</p>
<dt><code>~/.bournalrc</code></p>
<dd> Default configuration file.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grep/">grep</a>(1), <a href="/docs/linux/man/7-regex/">regex</a>(7), <a href="/docs/linux/man/3-readline/">readline</a>(3), <a href="/docs/linux/man/1-vim/">vim</a>(1), <a href="/docs/linux/man/1-nano/">nano</a>(1), <a href="/docs/linux/man/1-nanorc/">nanorc</a>(1), <a href="/docs/linux/man/1-jed/">jed</a>(1)</code> </p>
<dl>
<dt><code>Bournal web page</code></p>
<dd> <i><a rel="nofollow" href="http://freshmeat.net/projects/bournal">http://freshmeat.net/projects/bournal</a></i></dl>
<h2>AUTHOR</h2>
<p> bournal was written by Professor Fapsanders &lt;frankpena [at] gmail.com&gt;. </p>
<p> This manual page was written by Kevin Wallace &lt;kevjava [at] gmail.com&gt;, for the Ubuntu project (but may be used by others). </p>
<h2>Index</h2>
