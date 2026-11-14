---
title: "mech-dump(1)"
name: "mech-dump"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mech-dump/"
---

<h2 class="name">NAME</h2>
 

 mech-dump - Dumps information about a web page 

<h2>SYNOPSIS</h2>

 mech-dump [options] [file|url] 

 Options: 

 <pre><code>
    --headers              Dump HTTP response headers
    --forms                Dump table of forms (default action)
    --links                Dump table of links
    --images               Dump table of images
    --all                  Dump all four of the above, in that order
    --text                 Dumps the textual part of the web page
    --user=user            Set the username
    --password=pass        Set the password
    --cookie-file=filename Set the filename to use for persistent cookies
    --agent=agent          Specify the UserAgent to pass
    --agent-alias=alias
                           Specify the alias for the UserAgent to pass.
                           Pick one of:
                               * Windows IE 6
                               * Windows Mozilla
                               * Mac Safari
                               * Mac Mozilla
                               * Linux Mozilla
                               * Linux Konqueror
    --absolute             Show URLs as absolute, even if relative in the page
    --help                 Show this message
</code></pre> 

 The order of the options specified is relevant. Repeated options get repeated dumps.

<h2>SEE ALSO</h2>

 WWW::Mechanize 

<h2>Index</h2>


