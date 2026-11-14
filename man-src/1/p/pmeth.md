---
title: "pmeth(1)"
name: "pmeth"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmeth/"
---

<h2 class="name">NAME</h2>
 

 pmeth - show a Perl class's methods 

<h2>DESCRIPTION</h2>

 Given a class name, print out all methods available to that class. It does this by loading in the class module, and walking its symbol table and those of its ancestor classes. A regular method call shows up simply: 

 <pre>
    $ pmeth IO::Socket | grep '^con'
    confess
    configure
    connect
    connected
</pre> 

 But one that came from else where is noted with one or more ``via'' notations: 

 <pre>
    DESTROY via IO::Handle
    export via Exporter via IO::Handle
</pre> 

 A base-class method that is unavailable due to being hidden by a close derived-class method by the same name (but accessible via <font SIZE="-1">SUPER::</font>) is indicated by a leading ``[overridden]'' before it: 

 <pre>
    [overridden] new via IO::Handle
</pre> 

 Constants declared via constant have a leading ``[constant]'' added to the output, but <font SIZE="-1">XS </font><tt>&quot;define&quot;</tt>'s are not yet so flagged.

<h2>EXAMPLES</h2>

 <pre><code>
$ pmeth IO::Socket
    AF_INET
        AF_UNIX
            INADDR_ANY
                INADDR_BROADCAST
                    INADDR_LOOPBACK
                        INADDR_NONE
                            SOCK_DGRAM
                                SOCK_RAW
                                    SOCK_STREAM
                                        accept
                                            bind
                                                carp
                                                    confess
                                                        configure
                                                            connect
                                                                connected
                                                                    croak
                                                                        getsockopt
                                                                            import
                                                                                inet_aton
                                                                                    inet_ntoa
                                                                                        listen new pack_sockaddr_in
                                                                                            pack_sockaddr_un
                                                                                                peername
                                                                                                    protocol
                                                                                                        recv
                                                                                                            register_domain
                                                                                                                send
                                                                                                                    setsockopt
                                                                                                                        shutdown
                                                                                                                            sockaddr_in
                                                                                                                                sockaddr_un
                                                                                                                                    sockdomain
                                                                                                                                        socket
                                                                                                                                            socketpair
                                                                                                                                                sockname
                                                                                                                                                    sockopt
                                                                                                                                                        socktype
                                                                                                                                                            timeout
                                                                                                                                                                unpack_sockaddr_in
                                                                                                                                                                    unpack_sockaddr_un
                                                                                                                                                                        DESTROY via IO::Handle
                                                                                                                                                                            SEEK_CUR via IO::Handle
                                                                                                                                                                                SEEK_END via IO::Handle
                                                                                                                                                                                    SEEK_SET via IO::Handle
                                                                                                                                                                                        _IOFBF via IO::Handle
                                                                                                                                                                                            _IOLBF via IO::Handle
                                                                                                                                                                                                _IONBF via IO::Handle
                                                                                                                                                                                                    _open_mode_string via IO::Handle
                                                                                                                                                                                                        autoflush via IO::Handle
                                                                                                                                                                                                            blocking via IO::Handle
                                                                                                                                                                                                                [overridden] carp via IO::Handle
                                                                                                                                                                                                                    clearerr via IO::Handle
                                                                                                                                                                                                                        close via IO::Handle
                                                                                                                                                                                                                            [overridden] confess via IO::Handle
                                                                                                                                                                                                                                constant via IO::Handle
                                                                                                                                                                                                                                    [overridden] croak via IO::Handle
                                                                                                                                                                                                                                        eof via IO::Handle
                                                                                                                                                                                                                                            error via IO::Handle
                                                                                                                                                                                                                                                fcntl via IO::Handle
                                                                                                                                                                                                                                                    fdopen via IO::Handle
                                                                                                                                                                                                                                                        fileno via IO::Handle
                                                                                                                                                                                                                                                            flush via IO::Handle
                                                                                                                                                                                                                                                                format_formfeed via IO::Handle
                                                                                                                                                                                                                                                                    format_line_break_characters via IO::Handle
                                                                                                                                                                                                                                                                        format_lines_left via IO::Handle
                                                                                                                                                                                                                                                                            format_lines_per_page via IO::Handle
                                                                                                                                                                                                                                                                                format_name via IO::Handle
                                                                                                                                                                                                                                                                                    format_page_number via IO::Handle
                                                                                                                                                                                                                                                                                        format_top_name via IO::Handle
                                                                                                                                                                                                                                                                                            format_write via IO::Handle
                                                                                                                                                                                                                                                                                                formline via IO::Handle
                                                                                                                                                                                                                                                                                                    gensym via IO::Handle
                                                                                                                                                                                                                                                                                                        getc via IO::Handle
                                                                                                                                                                                                                                                                                                            getline via IO::Handle
                                                                                                                                                                                                                                                                                                                getlines via IO::Handle
                                                                                                                                                                                                                                                                                                                    gets via IO::Handle
                                                                                                                                                                                                                                                                                                                        input_line_number via IO::Handle
                                                                                                                                                                                                                                                                                                                            input_record_separator via IO::Handle
                                                                                                                                                                                                                                                                                                                                ioctl via IO::Handle
                                                                                                                                                                                                                                                                                                                                    [overridden] new via IO::Handle
                                                                                                                                                                                                                                                                                                                                        new_from_fd via IO::Handle
                                                                                                                                                                                                                                                                                                                                            opened via IO::Handle
                                                                                                                                                                                                                                                                                                                                                output_field_separator via IO::Handle
                                                                                                                                                                                                                                                                                                                                                    output_record_separator via IO::Handle
                                                                                                                                                                                                                                                                                                                                                        print via IO::Handle
                                                                                                                                                                                                                                                                                                                                                            printf via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                printflush via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                    qualify via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                        qualify_to_ref via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                            read via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                setbuf via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                    setvbuf via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                        stat via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                            sync via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                sysread via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                    syswrite via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                        truncate via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                            ungensym via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                                ungetc via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                                    untaint via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                                        write via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                                            _push_tags via Exporter via IO::Handle export via Exporter via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                                                export_fail via Exporter via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                                                    export_ok_tags via Exporter via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                                                        export_tags via Exporter via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                                                            export_to_level via Exporter via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                                                                [overridden] import via Exporter via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                                                                    require_version via Exporter via IO::Handle
                                                                                                                                                                                                                                                                                                                                                                                                                                                        VERSION via UNIVERSAL
                                                                                                                                                                                                                                                                                                                                                                                                                                                            can via UNIVERSAL
                                                                                                                                                                                                                                                                                                                                                                                                                                                                [overridden] import via UNIVERSAL
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    isa via UNIVERSAL
</code></pre>

<h2>NOTE</h2>

 Perl makes no distinction between functions, procedures, and methods, nor whether they are public or nominally private, nor whether a method is nominally a class method, an object method, or both. They all show up as subs in the package namespace. So if your class says <tt>&quot;use Carp&quot;</tt>, you just polluted your namespace with things like <i>croak()</i> and <i>confess()</i>, which will appear to be available as method calls on objects of your class.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-perltoot/">perltoot</a></i>(1), <i><a HREF="/docs/linux/man/1-perlobj/">perlobj</a></i>(1)

<h2>AUTHORS and COPYRIGHTS</h2>

 Copyright (C) 1999 Tom Christiansen. 

 Copyright (C) 2006-2014 Mark Leighton Fisher.

<h2>LICENSE</h2>

 This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl ``Artistic License''. (This is the Perl 5 licensing scheme.) 

 Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl ``Artistic License''. 

<h2>Index</h2>


