---
title: "mimesend(1)"
name: "mimesend"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mimesend/"
---

<h2 class="name">NAME</h2>
 

 mimesend - send files via MIME mail, from the command line 

<h2>USAGE</h2>

 Pretty basic: 

 <pre><code>
    mimesend [-n] [-t to] [-s subj] (-f file [-m type])+
        -n        Don't actually send it; just print it to stdout.
        -t to     The "to" address.
        -s subj   The subject of the message.
        -f file   Path to attached file, or - for STDIN.
        -m type   MIME type of previous -f;
    therefore - m must follow - f.
</code></pre> 

 For example: 

 <pre>
    mimesend -t you [at] yourhost.com -s &quot;Hello, nurse!&quot; 
          -f greetings.htm -f foo.gif
</pre>

<h2>AUTHOR</h2>

 Eryq, eryq [at] zeegee.com 

 8 Jan 1997 

<h2>Index</h2>


